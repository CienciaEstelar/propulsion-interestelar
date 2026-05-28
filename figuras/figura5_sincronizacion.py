#!/usr/bin/env python3
"""Figura 5: Sincronización temporal relativista para crucero interestelar.
CORREGIDO — El error acumulado es ~1.4×10^10 ms, no ~1.4×10^8 ms.
Incluye: Doppler, dilatación GR, efecto Sagnac, varianza de Allan (DSAC)."""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from style_config import *
import numpy as np

fig, all_axes = figura_nueva(ancho=8, alto=7, nrows=2, ncols=2)
(ax1, ax2), (ax3, ax4) = all_axes

# ── Parámetros de la misión (VERIFICADOS) ──
DISTANCIA_AL = 4.37
VELOCIDAD_C = 0.2
BETA = VELOCIDAD_C
GAMMA = 1.0 / np.sqrt(1.0 - BETA**2)  # = 1.02062...
TIEMPO_CRUCERO_YR = DISTANCIA_AL / VELOCIDAD_C  # = 21.85 años
TIEMPO_CRUCERO_S = TIEMPO_CRUCERO_YR * 365.25 * 86400  # = 6.894×10^8 s

print(f"  γ = {GAMMA:.6f}")
print(f"  T_crucero = {TIEMPO_CRUCERO_YR:.2f} años = {TIEMPO_CRUCERO_S:.3e} s")

DIAS_MISION = int(TIEMPO_CRUCERO_YR * 365.25)
TIEMPO_DIAS = np.linspace(0, DIAS_MISION, 1000)
TIEMPO_SEGUNDOS = TIEMPO_DIAS * 86400

# ── 1. Corrección Relatividad Especial (dilatación temporal) ──
tiempo_propio_seg = TIEMPO_SEGUNDOS / GAMMA
deriva_re_seg = TIEMPO_SEGUNDOS - tiempo_propio_seg  # [s]

# Verificación analítica:
deriva_re_final_s = TIEMPO_CRUCERO_S * (1.0 - 1.0/GAMMA)
deriva_re_final_ms = deriva_re_final_s * 1e3
print(f"  Deriva RE final = {deriva_re_final_s:.3e} s = {deriva_re_final_ms:.3e} ms")
print(f"  Equivalente en distancia = {deriva_re_final_s * C:.3e} km")

# ── 2. Corrección Relatividad General (potencial gravitacional) ──
r_inicial = AU
r_final = DISTANCIA_AL * LY
distancias = np.linspace(r_inicial, r_final, 1000)
potencial_sol = G * M_SOL / (C**2 * distancias)
potencial_alpha_cen = G * (2.0 * M_SOL) / (C**2 * (r_final - distancias + 1e12))
potencial_alpha_cen = np.clip(potencial_alpha_cen, 0, potencial_sol[0] * 0.1)
# Término cinemático + potencial integrado
integrando_gr = potencial_sol + potencial_alpha_cen + BETA**2 / 2.0
dt_seg = np.gradient(TIEMPO_SEGUNDOS)
deriva_gr_seg = np.cumsum(integrando_gr * dt_seg)
deriva_gr_seg -= deriva_gr_seg[0]

# ── 3. Efecto Sagnac (banda de error) ──
omega_tierra = 7.2921e-5  # rad/s
area_dsn = np.pi * (6371e3)**2 / 4
sagnac_por_paso_s = 2 * omega_tierra * area_dsn / (C * 1e3)**2
banda_sagnac_s = sagnac_por_paso_s * np.sqrt(TIEMPO_DIAS) * 2

# ── 4. Varianza de Allan (DSAC, σ=1×10^-15) ──
sigma_allan = 1e-15
ruido_allan_s = sigma_allan * np.sqrt(TIEMPO_SEGUNDOS)

# ── Subplot 1: Deriva temporal relativista ──
ax1.fill_between(TIEMPO_DIAS / 365.25, 0, deriva_re_seg * 1e3,
                 alpha=0.15, color=COLORS["laser_sail"],
                 label="Relatividad Especial (dilatacion temporal)")
ax1.plot(TIEMPO_DIAS / 365.25, deriva_re_seg * 1e3, "-",
         color=COLORS["laser_sail"], linewidth=2)
ax1.plot(TIEMPO_DIAS / 365.25, deriva_gr_seg * 1e3, "--",
         color=COLORS["warp"], linewidth=1.5, alpha=0.7,
         label="Relatividad General (potencial grav.)")
ax1.set_ylabel("Deriva acumulada [ms]", fontweight="bold")
ax1.set_title("(a) Correccion relativista integrada", fontweight="bold", fontsize=10)
ax1.legend(fontsize=7, loc="upper left")
ax1.set_xlabel("Tiempo de crucero [anos]", fontweight="bold")
ax1.text(0.98, 0.05, f"Final RE: {deriva_re_final_ms:.2e} ms",
         transform=ax1.transAxes, fontsize=7, ha="right",
         bbox=dict(boxstyle="round,pad=0.1", facecolor="white", alpha=0.8))

# ── Subplot 2: Banda de error Sagnac ──
banda_sagnac_us = banda_sagnac_s * 1e6
ax2.fill_between(TIEMPO_DIAS / 365.25, -banda_sagnac_us, banda_sagnac_us,
                 alpha=0.2, color="#F39C12", label="Banda de error Sagnac (±2σ)")
ax2.plot(TIEMPO_DIAS / 365.25, np.zeros_like(TIEMPO_DIAS), "-",
         color=COLORS["text"], linewidth=0.5, alpha=0.5)
ax2.set_ylabel("Error Sagnac [μs]", fontweight="bold")
ax2.set_title("(b) Efecto Sagnac: banda de error\nde comunicacion Tierra-sonda",
              fontweight="bold", fontsize=10)
ax2.legend(fontsize=7)
ax2.set_xlabel("Tiempo de crucero [anos]", fontweight="bold")

# ── Subplot 3: Varianza de Allan ──
taus = np.logspace(0, np.log10(DIAS_MISION * 86400), 500)
sigma_wfm = 1e-15 * np.sqrt(taus)
sigma_ffm = 3e-16 * np.ones_like(taus)
sigma_rwfm = 1e-18 * taus
sigma_total = np.sqrt(sigma_wfm**2 + sigma_ffm**2 + sigma_rwfm**2)

ax3.loglog(taus / 86400, sigma_total, "-", color=COLORS["laser_sail"], linewidth=2,
           label="DSAC (σA=10⁻¹⁵, floor=3×10⁻¹⁶)")
ax3.loglog(taus / 86400, sigma_wfm, ":", color=COLORS["text"], linewidth=1, alpha=0.5, label="White FM")
ax3.loglog(taus / 86400, sigma_ffm, "--", color="#F39C12", linewidth=1, alpha=0.5, label="Flicker FM")
ax3.loglog(taus / 86400, sigma_rwfm, "-.", color=COLORS["especulativa"], linewidth=1, alpha=0.5, label="Random Walk FM")
for dias, etiq in [(1, "1 dia"), (30, "1 mes"), (365, "1 año"),
                    (365*5, "5 años"), (DIAS_MISION, "Crucero")]:
    idx = np.argmin(np.abs(taus / 86400 - dias))
    ax3.annotate(etiq, (taus[idx]/86400, sigma_total[idx]), fontsize=6, ha="center",
                bbox=dict(boxstyle="round,pad=0.1", facecolor="white", edgecolor=COLORS["grid"], alpha=0.8))
ax3.set_xlabel("Intervalo de integracion τ [días]", fontweight="bold")
ax3.set_ylabel("Desviacion de Allan σy(τ)", fontweight="bold")
ax3.set_title("(c) Estabilidad del reloj atomico (DSAC)\ndurante el crucero interestelar",
              fontweight="bold", fontsize=10)
ax3.legend(fontsize=6, loc="lower right")
ax3.set_xlim(0.5, max(taus)/86400 * 1.2)

# ── Subplot 4: Error total de sincronización ──
error_total_s = deriva_re_seg + deriva_gr_seg + banda_sagnac_s + ruido_allan_s
error_min_s = deriva_re_seg + deriva_gr_seg - banda_sagnac_s - ruido_allan_s
error_total_ms = error_total_s * 1e3
error_min_ms = error_min_s * 1e3

ax4.fill_between(TIEMPO_DIAS / 365.25, error_min_ms, error_total_ms,
                 alpha=0.2, color=COLORS["especulativa"])
ax4.plot(TIEMPO_DIAS / 365.25, error_total_ms, "-",
         color=COLORS["especulativa"], linewidth=2,
         label="Error total (RE + RG + Sagnac + Allan)")
ax4.plot(TIEMPO_DIAS / 365.25, deriva_re_seg * 1e3, "--",
         color=COLORS["laser_sail"], linewidth=1, alpha=0.6,
         label="Solo Relatividad Especial")
ax4.set_ylabel("Error de sincronizacion [ms]", fontweight="bold")
ax4.set_xlabel("Tiempo de crucero [anos]", fontweight="bold")
ax4.set_title("(d) Error total de sincronizacion acumulado\n(al final del crucero a α Centauri)",
              fontweight="bold", fontsize=10)
ax4.legend(fontsize=7, loc="upper left")

err_final_s = error_total_s[-1]
err_final_ms = err_final_s * 1e3
err_final_km = err_final_s * C
ax4.annotate(f"Error final:\n{err_final_ms:.2e} ms\n(~{err_final_km:.2e} km en distancia)\n\n"
             "Nota: este error requiere\ncorreccion continua mediante\nmodelos relativistas a bordo",
             xy=(TIEMPO_DIAS[-1]/365.25, error_total_ms[-1]),
             fontsize=7.5, fontweight="bold", color=COLORS["especulativa"],
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor=COLORS["especulativa"], alpha=0.92))

plt.suptitle("Figura 5: Sincronizacion temporal relativista para crucero interestelar Tierra–α Centauri\n"
             f"(v=0.2c, γ={GAMMA:.4f}, duracion≈{TIEMPO_CRUCERO_YR:.0f} años, reloj DSAC σ=10⁻¹⁵, DSN Madrid/Goldstone)",
             fontweight="bold", fontsize=11, y=1.02)
plt.tight_layout()

guardar_figura(fig, "figura5_sincronizacion_relativista")
print(f"✓ Figura 5 generada: Sincronizacion temporal relativista")
print(f"  Error total al final del crucero: {err_final_ms:.3e} ms")
print(f"  Equivalente en distancia: {err_final_km:.3e} km")
print(f"  CORREGIDO — factor ~100 respecto a versión anterior")
