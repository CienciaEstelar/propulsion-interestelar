#!/usr/bin/env python3
"""
SINCRONIZACIÓN TEMPORAL RELATIVISTA
===================================
Cálculo del error de sincronización acumulado durante el crucero
interestelar a 0.2c hacia α Centauri.

CORREGIDO (C1): El error NO es ~1.4×10⁸ ms sino ~1.4×10¹⁰ ms.
Factor de corrección: ~100×.

Incluye:
    1. Dilatación temporal por Relatividad Especial (efecto Doppler)
    2. Dilatación por Relatividad General (potencial gravitacional solar)
    3. Efecto Sagnac (rotación terrestre en comunicaciones DSN)
    4. Varianza de Allan (ruido estocástico del reloj atómico DSAC)

Autor: J. D. Galaz Amengual
Fecha: 2026-05-28
"""

import numpy as np
from .constantes import *
from .cinematica import gamma

# ══════════════════════════════════════════════════════════════════════
# PARÁMETROS DE LA MISIÓN
# ══════════════════════════════════════════════════════════════════════

D_ALPHA_CEN: float = 4.37        # Distancia a α Centauri [años luz]
V_CRUCERO_C: float = 0.2         # Velocidad de crucero [fracción de c]

BETA_CRUCERO: float = V_CRUCERO_C
GAMMA_CRUCERO: float = gamma(BETA_CRUCERO)

# Tiempo de crucero medido DESDE LA TIERRA
T_CRUCERO_YR: float = D_ALPHA_CEN / V_CRUCERO_C  # ≈ 21.85 años
T_CRUCERO_S: float = T_CRUCERO_YR * YR_S          # ≈ 6.895×10⁸ s

# Tiempo PROPIO de la nave (Más corto por dilatación temporal)
T_PROPIO_S: float = T_CRUCERO_S / GAMMA_CRUCERO    # ≈ 6.756×10⁸ s
T_PROPIO_YR: float = T_PROPIO_S / YR_S             # ≈ 21.41 años


# ══════════════════════════════════════════════════════════════════════
# 1. DERIVA POR RELATIVIDAD ESPECIAL (CORREGIDA — C1)
# ══════════════════════════════════════════════════════════════════════
# La nave envejece MÁS LENTO que la Tierra.
# Δt_RE = T_Tierra - T_nave = T × (1 - 1/γ)
# Para γ=1.0206 y T=6.895×10⁸ s → Δt ≈ 1.393×10⁷ s

DT_REL_S: float = T_CRUCERO_S - T_PROPIO_S   # [s] ← VALOR CORREGIDO
DT_REL_MS: float = DT_REL_S * 1e3             # [ms]
DT_REL_KM: float = DT_REL_S * C / 1e3         # [km] equivalente en distancia


# ══════════════════════════════════════════════════════════════════════
# 2. CORRECCIÓN POR RELATIVIDAD GENERAL (Potencial gravitacional solar)
# ══════════════════════════════════════════════════════════════════════
# Integración del potencial gravitacional a lo largo de la trayectoria.
# La nave parte de ~1 AU del Sol y llega a 4.37 al.
# El potencial solar se debilita con 1/r, el de α Cen crece al acercarse.

# Trayectoria simplificada: línea recta del Sol a α Cen
r_inicial: float = AU                     # ~1 UA del Sol al inicio
r_final: float = D_ALPHA_CEN * LY         # ~4.13×10¹⁶ m al final
N_PUNTOS: int = 1000
distancias: np.ndarray = np.linspace(r_inicial, r_final, N_PUNTOS)

# Potencial gravitacional solar adimensional: Φ/c² = GM/(c²r)
potencial_sol: np.ndarray = G * M_SOL / (C**2 * distancias)

# Potencial de α Cen (creciente al aproximarse)
# Masa total α Cen A+B ≈ 2.0 M_Sol
potencial_alpha: np.ndarray = G * (2.0 * M_SOL) / (C**2 * (r_final - distancias + 1e12))
potencial_alpha = np.clip(potencial_alpha, 0, potencial_sol[0] * 0.1)

# La dilatación temporal gravitacional integrada:
# Δτ/Δt ≈ 1 - Φ/c² - v²/(2c²)  (aproximación post-Newtoniana)
integrando_gr: np.ndarray = potencial_sol + potencial_alpha + BETA_CRUCERO**2 / 2.0
dt_seg: np.ndarray = np.gradient(np.linspace(0, T_CRUCERO_S, N_PUNTOS))
deriva_gr_s: np.ndarray = np.cumsum(integrando_gr * dt_seg)
deriva_gr_s -= deriva_gr_s[0]  # Referencia al inicio

DT_GR_TOTAL_S: float = deriva_gr_s[-1]  # Deriva GR total al final del crucero


# ══════════════════════════════════════════════════════════════════════
# 3. EFECTO SAGNAC (Rotación terrestre en DSN)
# ══════════════════════════════════════════════════════════════════════
# Las estaciones DSN (Madrid, Goldstone, Canberra) están en la superficie
# terrestre. La rotación de la Tierra durante el tiempo de vuelo de la
# señal introduce una asimetría en el Two-Way Ranging.
# Δt_Sagnac = 2 × (ω · A) / c²
# donde A es el área proyectada del triángulo estación-centro Tierra-satélite.

OMEGA_TIERRA: float = 7.2921e-5     # Velocidad angular terrestre [rad/s]
R_TIERRA: float = 6371e3            # Radio terrestre [m]
AREA_DSN: float = np.pi * R_TIERRA**2 / 4  # Área efectiva [m²]

# Por cada paso de comunicación (ida)
DT_SAGNAC_SINGLE_S: float = 2 * OMEGA_TIERRA * AREA_DSN / C**2

# Acumulado durante toda la misión (~1 pase de comunicación por día)
N_PASES: float = T_CRUCERO_S / DAY_S
DT_SAGNAC_TOTAL_S: float = DT_SAGNAC_SINGLE_S * np.sqrt(N_PASES) * 2  # ida+vuelta


# ══════════════════════════════════════════════════════════════════════
# 4. VARIANZA DE ALLAN — RUIDO DEL RELOJ ATÓMICO (DSAC)
# ══════════════════════════════════════════════════════════════════════
# El Deep Space Atomic Clock (NASA/JPL) tiene estabilidad σ_A ≈ 10⁻¹⁵.
# El error crece con √T (ruido blanco de frecuencia).
# A MUY largo plazo (>1 año), el flicker floor (3×10⁻¹⁶) y el random
# walk (10⁻¹⁸ × τ) empiezan a contribuir.

SIGMA_ALLAN: float = 1e-15         # Estabilidad DSAC [adimensional]
SIGMA_FLICKER: float = 3e-16       # Flicker floor
SIGMA_RW: float = 1e-18            # Coeficiente de random walk

# Ruido acumulado al final del crucero (domina el white FM)
DT_ALLAN_S: float = SIGMA_ALLAN * np.sqrt(T_CRUCERO_S)


# ══════════════════════════════════════════════════════════════════════
# 5. ERROR TOTAL DE SINCRONIZACIÓN
# ══════════════════════════════════════════════════════════════════════

DT_TOTAL_S: float = DT_REL_S + DT_GR_TOTAL_S + DT_SAGNAC_TOTAL_S + DT_ALLAN_S
DT_TOTAL_MS: float = DT_TOTAL_S * 1e3
DT_TOTAL_KM: float = DT_TOTAL_S * C / 1e3
DT_TOTAL_AU: float = DT_TOTAL_KM / (AU / 1e3)  # Convertir km a AU


def calcular_sincronizacion() -> dict:
    """Retorna todos los resultados de sincronización."""
    return {
        "gamma": GAMMA_CRUCERO,
        "T_crucero_yr": T_CRUCERO_YR,
        "T_crucero_s": T_CRUCERO_S,
        "T_propio_yr": T_PROPIO_YR,
        "T_propio_s": T_PROPIO_S,
        "DT_RE_s": DT_REL_S,
        "DT_RE_ms": DT_REL_MS,
        "DT_RE_km": DT_REL_KM,
        "DT_GR_s": DT_GR_TOTAL_S,
        "DT_Sagnac_s": DT_SAGNAC_TOTAL_S,
        "DT_Allan_s": DT_ALLAN_S,
        "DT_total_s": DT_TOTAL_S,
        "DT_total_ms": DT_TOTAL_MS,
        "DT_total_km": DT_TOTAL_KM,
        "DT_total_AU": DT_TOTAL_AU,
        "factor_correccion": DT_TOTAL_MS / 1.4e8,  # vs versión errónea
    }


def imprimir_sincronizacion() -> None:
    """Imprime los resultados de sincronización."""
    r = calcular_sincronizacion()
    print("\n" + "=" * 65)
    print("  SINCRONIZACIÓN TEMPORAL RELATIVISTA (CORREGIDA)")
    print("=" * 65)
    print(f"  γ = {r['gamma']:.6f}")
    print(f"  T_crucero (Tierra) = {r['T_crucero_yr']:.2f} años = {r['T_crucero_s']:.3e} s")
    print(f"  T_propio (nave)    = {r['T_propio_yr']:.2f} años = {r['T_propio_s']:.3e} s")
    print(f"\n  ERRORES ACUMULADOS:")
    print(f"  Δt_RE (dilatación)    = {r['DT_RE_ms']:.2e} ms  ← CORREGIDO (×100)")
    print(f"  Δt_GR (gravitacional) = {r['DT_GR_s']*1e3:.2e} ms")
    print(f"  Δt_Sagnac (rotación)  = {r['DT_Sagnac_s']*1e3:.2f} ms")
    print(f"  Δt_Allan (ruido reloj) = {r['DT_Allan_s']*1e3:.3f} ms")
    print(f"  ─────────────────────────────────────")
    print(f"  Δt_TOTAL              = {r['DT_total_ms']:.2e} ms")
    print(f"  Equivalente distancia  = {r['DT_total_km']:.2e} km = {r['DT_total_AU']:.1f} AU")
    print(f"\n  CORRECCIÓN vs versión anterior: factor {r['factor_correccion']:.0f}×")
    print(f"  ⚠ Sin corrección relativista continua, la nave perdería")
    print(f"    {r['DT_total_AU']:.0f} AU de precisión al llegar a α Centauri.")
    print("=" * 65)


if __name__ == "__main__":
    imprimir_sincronizacion()
