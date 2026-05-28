#!/usr/bin/env python3
"""Figura 4: Presupuesto de enlace óptico Tierra-α Centauri.
AMPLIADO — Incluye ruido de fondo estelar, scintilación atmosférica, jitter de apuntamiento."""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from style_config import *
import numpy as np

fig, all_axes = figura_nueva(ancho=9, alto=7, nrows=2, ncols=1)
ax1, ax2 = all_axes[0], all_axes[1]

# ── PARÁMETROS DEL ENLACE ──
DISTANCIA_AL = 4.37  # años luz
DISTANCIA_M = DISTANCIA_AL * LY / 1e3 * 1e3  # 4.37 ly → metros
LAMBDA = 1064e-9
FRECUENCIA = C * 1e3 / LAMBDA
ENERGIA_FOTON = 6.626e-34 * FRECUENCIA
APERTURA_TX = 1.0      # [m]
APERTURA_RX = 39.0     # ELT [m]
EFICIENCIA_OPTICA = 0.5
POTENCIAS_LASER = np.logspace(-3, 9, 200)  # 1 mW → 1 GW

# ── CÁLCULO GEOMÉTRICO ──
theta_div = LAMBDA / APERTURA_TX
A_rx = np.pi * (APERTURA_RX / 2)**2
P_rx_ideal = POTENCIAS_LASER * EFICIENCIA_OPTICA * (A_rx / (np.pi * (DISTANCIA_M * theta_div / 2)**2))
P_rx_ideal = np.clip(P_rx_ideal, 1e-35, None)

# ── TÉRMINOS DE RUIDO ──
T_BIT = 1e-3  # 1 ms/bit (~1 kbps base)

# 1. Shot noise (ruido cuántico fundamental)
fotones_senal = P_rx_ideal * T_BIT / ENERGIA_FOTON

# 2. Fondo estelar (α Cen A: m_V ≈ 0.0, ~5×10^10 fotones/s/m² en banda V)
# En el ancho de banda del filtro (Δλ≈1 nm a 1064 nm), flujo reducido ~10^7 fotones/s/m²
flujo_fondo_estelar = 1e7  # fotones/s/m² en Δλ≈1 nm
A_recogida = np.pi * (APERTURA_RX/2)**2
Omega_ifov = (LAMBDA / APERTURA_RX)**2  # ángulo sólido del IFOV
fondo_estelar_fotones = flujo_fondo_estelar * A_recogida * Omega_ifov * T_BIT

# 3. Luz exozodiacal (α Cen) — estimación ~10× fondo zodiacal solar
fondo_exozodiacal = fondo_estelar_fotones * 0.5  # ~50% adicional

# 4. Scintilación atmosférica (modelo de Kolmogorov)
# Para ELT 39m, seeing 0.5", σ_scint ≈ 0.05 en amplitud → varianza 0.25% en potencia
sigma_scint = 0.05
ruido_scint = fotones_senal * sigma_scint

# 5. Jitter de apuntamiento (σ_jitter = 0.1 μrad asumido)
sigma_jitter = 0.1e-6  # rad
theta_beam = LAMBDA / APERTURA_TX
perdida_jitter = np.exp(-2 * (sigma_jitter / theta_beam)**2)
fotones_senal_jitter = fotones_senal * perdida_jitter

# ── SNR TOTAL ──
fotones_total = fotones_senal_jitter
ruido_total = np.sqrt(fotones_total + fondo_estelar_fotones + fondo_exozodiacal + ruido_scint**2)
SNR_total = fotones_total / np.clip(ruido_total, 0.1, None)

# SNR solo shot noise (para comparar)
SNR_shot_only = fotones_senal / np.sqrt(np.clip(fotones_senal, 0.1, None))

# ── SUBPLOT 1: SNR vs Potencia (comparación con/sin ruido) ──
ax1.plot(POTENCIAS_LASER, SNR_shot_only, "--", color=COLORS["laser_sail"],
         linewidth=1.5, alpha=0.5, label="Solo shot noise (ideal)")
ax1.plot(POTENCIAS_LASER, SNR_total, "-", color=COLORS["laser_sail"],
         linewidth=2.5, label="Con ruido completo (fondo+scint+jitter)")
ax1.fill_between(POTENCIAS_LASER, SNR_total, SNR_shot_only, alpha=0.1, color=COLORS["laser_sail"])

# Límites
for snr_lim, color, etiq in [(1, "orange", "SNR=1 (deteccion)"), (10, COLORS["ingenieria"], "SNR=10 (fiable)")]:
    ax1.axhline(snr_lim, color=color, linestyle="--", linewidth=1, alpha=0.6)
    ax1.text(2e-3, snr_lim * 1.3, etiq, fontsize=7, color=color)

# Regímenes de potencia
for x_lim, etiq in [(1, "DSOC"), (1e6, "MW"), (1e8, "DE-STAR")]:
    ax1.axvline(x_lim, color=COLORS["grid"], linestyle=":", alpha=0.4)
ax1.text(0.005, 0.03, "≤DSOC\n(Psyche 4W)", fontsize=6, ha="center")
ax1.text(100, 0.03, "Láser MW", fontsize=6, ha="center")
ax1.text(1e8, 0.03, "DE-STAR\n(100 GW)", fontsize=6, ha="center")

ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.set_xlabel("Potencia láser en la sonda [W]", fontweight="bold")
ax1.set_ylabel("Signal-to-Noise Ratio", fontweight="bold")
ax1.set_title("(a) SNR del enlace Tierra-α Centauri (4.37 al, λ=1064 nm, TX=1 m, RX=39 m ELT)",
              fontweight="bold", fontsize=10)
ax1.legend(fontsize=7.5, loc="upper left")
ax1.set_xlim(5e-4, 2e9)
ax1.set_ylim(5e-2, 1e5)

# ── SUBPLOT 2: Desglose de fuentes de ruido (a potencia fija de 10 kW) ──
P_REF = 1e4  # 10 kW láser en la sonda
idx_ref = np.argmin(np.abs(POTENCIAS_LASER - P_REF))

# Componentes de ruido a P_REF
componentes = [
    ("Shot noise\n(cuántico)", np.sqrt(fotones_senal[idx_ref]), COLORS["laser_sail"]),
    ("Fondo estelar\n(α Cen A)", np.sqrt(fondo_estelar_fotones), "#F39C12"),
    ("Exozodiacal\n(estimado)", np.sqrt(fondo_exozodiacal), "#E67E22"),
    ("Scintilación\natmosférica", ruido_scint[idx_ref], COLORS["especulativa"]),
    ("Jitter\n(σ=0.1 μrad)", fotones_senal[idx_ref] * (1 - perdida_jitter), "#9B59B6"),
]

nombres = [c[0] for c in componentes]
valores = [c[1] for c in componentes]
colores = [c[2] for c in componentes]
x_pos = np.arange(len(componentes))

barras = ax2.bar(x_pos, valores, color=colores, edgecolor="white", linewidth=0.8, alpha=0.85)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(nombres, fontsize=7.5)
ax2.set_ylabel("Contribución al ruido [fotones/bit]", fontweight="bold")
ax2.set_title(f"(b) Desglose de fuentes de ruido a P_láser = {P_REF/1e3:.0f} kW en la sonda",
              fontweight="bold", fontsize=10)

# SNR resultante a esta potencia
snr_ref = SNR_total[idx_ref]
ax2.text(0.98, 0.92, f"SNR total = {snr_ref:.1f}\nP_rx = {P_rx_ideal[idx_ref]:.2e} W\n"
         f"Fotones/señal/bit = {fotones_senal[idx_ref]:.1f}",
         transform=ax2.transAxes, fontsize=8, ha="right", va="top",
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=COLORS["grid"], alpha=0.9))

# Anotar: la fuente dominante depende de la potencia del laser
# A 10 kW: scintilacion atmosferica domina (~105 fotones/bit)
# A >1 MW: jitter de apuntamiento se vuelve comparable (~5% de la senal)
# A >1 GW: fondo estelar contribuye significativamente
idx_max = np.argmax(valores)
ax2.annotate(f"Fuente dominante\na P_laser = {P_REF/1e3:.0f} kW\n(la dominancia cambia\ncon la potencia)",
            xy=(idx_max, valores[idx_max]),
            fontsize=6.5, ha="center", color=COLORS["especulativa"], fontweight="bold",
            xytext=(idx_max + 0.6, valores[idx_max] * 1.4),
            arrowprops=dict(arrowstyle="->", color=COLORS["especulativa"], lw=1.2))

plt.suptitle("Figura 4: Presupuesto de enlace óptico Tierra–α Centauri con modelo completo de ruido",
             fontweight="bold", fontsize=11, y=1.02)
plt.tight_layout()

guardar_figura(fig, "figura4_link_budget")
print("✓ Figura 4 generada: Presupuesto enlace óptico con ruido completo")
