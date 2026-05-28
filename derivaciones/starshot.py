#!/usr/bin/env python3
"""
VELA LÁSER — BREAKTHROUGH STARSHOT
===================================
Cálculos completos para el paradigma de vela láser interestelar.
Basado en Parkin (2018), Lubin (2016), y actualizaciones 2024-2026.

CONTENIDO
---------
1. Cinemática: energía cinética, aceleración, distancia de aceleración
2. Análisis térmico: temperatura de equilibrio radiativo de la vela
3. Divergencia del haz: límite de difracción, diámetro en α Centauri
4. Eficiencia wall-plug: energía eléctrica real requerida
5. Comparación de costo del array láser

PARÁMETROS DE DISEÑO (Parkin 2018)
----------------------------------
- Masa de la carga útil (starchip): 1 gramo
- Velocidad objetivo: 0.2c (~60,000 km/s)
- Potencia láser: 100 GW
- Área de la vela: 4×4 = 16 m²
- Reflectividad requerida: >99.99%
- Tiempo de aceleración: ~10 minutos
- Distancia de aceleración: ~0.2 AU

CORRECCIONES APLICADAS
----------------------
C5: Análisis térmico añadido (temperatura de equilibrio para ε = 0.05-0.9)
A5: Eficiencia wall-plug incluida (η_total ≈ 1.8×10⁻⁴)
A2: Estimación de costo del array láser (~$150B)
B4: Comparación energética corregida

Autor: J. D. Galaz Amengual
Fecha: 2026-05-28
"""

import numpy as np
from .constantes import *
from .cinematica import gamma, E_cin_relativista


# ══════════════════════════════════════════════════════════════════════
# PARÁMETROS DE DISEÑO — Parkin (2018), Lubin (2016)
# ══════════════════════════════════════════════════════════════════════

M_PAYLOAD: float = 1e-3          # Masa de la starchip [kg] = 1 gramo
                                  # Incluye: chip computación, cámara CMOS,
                                  # giroscopio MEMS, fotodiodos, antena

V_FRAC_C: float = 0.2            # Velocidad objetivo [fracción de c]
                                  # 0.2c = 59,958 km/s — compromiso entre
                                  # tiempo de viaje (~22 años) y energía requerida

P_LASER: float = 100e9           # Potencia óptica del array láser [W] = 100 GW
                                  # Equivalente a ~30× la potencia eléctrica global

A_SAIL: float = 16.0             # Área de la vela [m²] = 4m × 4m
                                  # La vela debe ser ultraligera (<1 g/m²)

R_REFLECTIVITY: float = 0.9999   # Reflectividad requerida = 99.99%
                                  # A este nivel, solo 0.01% de 100 GW = 10 MW
                                  # son absorbidos por la vela — sigue siendo MUCHO

T_ACCEL: float = 600.0           # Tiempo de aceleración [s] = 10 minutos
                                  # Limitado por la divergencia del haz láser
                                  # (~0.2 AU antes de que el haz se ensanche demasiado)

LAMBDA_LASER: float = 1064e-9    # Longitud de onda Yb:YAG [m]
                                  # Elegida por: alta eficiencia de fibra,
                                  # buena transmisión atmosférica, detectores maduros

D_TX: float = 1.0                # Apertura del transmisor en la sonda [m]
                                  # La vela misma actúa como antena de comunicaciones

D_RX: float = 39.0               # Diámetro del receptor en Tierra [m]
                                  # European Extremely Large Telescope (E-ELT)


# ══════════════════════════════════════════════════════════════════════
# 1. CINEMÁTICA DE LA FASE DE ACELERACIÓN
# ══════════════════════════════════════════════════════════════════════

GAMMA_STARSHOT: float = gamma(V_FRAC_C)
E_CIN_STARSHOT: float = E_cin_relativista(M_PAYLOAD, V_FRAC_C)
E_REST_STARSHOT: float = M_PAYLOAD * C**2
V_FINAL_MS: float = V_FRAC_C * C

# Aceleración media durante la fase de impulso
# a = Δv/Δt — asumiendo aceleración constante (aproximación)
A_MEDIA: float = V_FINAL_MS / T_ACCEL

# Distancia recorrida durante la aceleración
# d = ½at² — MRUA (Movimiento Rectilíneo Uniformemente Acelerado)
D_ACCEL: float = 0.5 * A_MEDIA * T_ACCEL**2

# Fuerza de radiación IDEAL (reflexión perfecta, 100% acoplamiento)
# F = 2P/c — el factor 2 viene de la reflexión (momento transferido = 2× momento del fotón)
F_RAD_IDEAL: float = 2 * P_LASER / C

# Aceleración por radiación ideal
A_RAD_IDEAL: float = F_RAD_IDEAL / M_PAYLOAD


# ══════════════════════════════════════════════════════════════════════
# 2. ANÁLISIS TÉRMICO DE LA VELA (C5 — CRITICAL FIX)
# ══════════════════════════════════════════════════════════════════════
# La vela absorbe una fracción (1-R) de la potencia incidente.
# Para R=99.99% y P=100 GW, P_abs = 10 MW sobre 16 m² = 625 kW/m².
# ESTO ES UNA BARBARIDAD. La vela debe disipar este calor por radiación.

# Flujo de potencia incidente [W/m²]
P_FLUX: float = P_LASER / A_SAIL  # 6.25 GW/m² = 6,250 MW/m²!!!

# Potencia absorbida por la vela [W/m²]
P_ABSORBED: float = P_FLUX * (1 - R_REFLECTIVITY)  # 625 kW/m²

def temperatura_equilibrio(epsilon: float) -> float:
    """
    Calcula la temperatura de equilibrio radiativo de la vela.

    Balance térmico: P_absorbida = P_emitida
    P_emitida = ε × σ × A × T⁴  (ley de Stefan-Boltzmann)
    Despejando: T = (P_abs / (ε × σ))^(1/4)

    Parámetros
    ----------
    epsilon : float
        Emisividad infrarroja de la vela [0-1].
        ε = 0.05: metales pulidos (mal radiador)
        ε = 0.10: dieléctricos típicos
        ε = 0.50: materiales con alta emitancia IR
        ε = 0.90: cuerpo negro casi perfecto

    Retorna
    -------
    float
        Temperatura de equilibrio [K].
        T > 3100 K → la vela se funde (punto de fusión del SiC)
        T < 1500 K → margen de seguridad aceptable
    """
    return (P_ABSORBED / (SIGMA_SB * epsilon))**0.25

# Punto de fusión del carburo de silicio (material candidato principal)
T_MELT_SIC: float = 3100.0  # K


# ══════════════════════════════════════════════════════════════════════
# 3. DIVERGENCIA DEL HAZ LÁSER
# ══════════════════════════════════════════════════════════════════════

# Divergencia angular por límite de difracción [rad]
# θ = λ/D — criterio de Rayleigh para una apertura circular
THETA_DIV: float = LAMBDA_LASER / D_TX  # rad

# Distancia a α Centauri [m]
D_ALPHA_CEN_M: float = 4.37 * LY

# Radio del haz a la distancia de α Cen [m]
# El haz se ensancha linealmente con la distancia: r(D) = θ × D
BEAM_RADIUS_ALPHACEN: float = THETA_DIV * D_ALPHA_CEN_M

# Diámetro del haz [m]
BEAM_DIAMETER_ALPHACEN: float = 2 * BEAM_RADIUS_ALPHACEN

# Área del haz en α Cen [m²]
A_BEAM_ALPHACEN: float = np.pi * BEAM_RADIUS_ALPHACEN**2

# Área del receptor (ELT 39m) [m²]
A_RX: float = np.pi * (D_RX / 2)**2

# Fracción de la potencia transmitida que llega al receptor
# = A_receptor / A_haz — puramente geométrica (límite de difracción)
FRACCION_COLLECTADA: float = A_RX / A_BEAM_ALPHACEN


# ══════════════════════════════════════════════════════════════════════
# 4. EFICIENCIA WALL-PLUG (A5 — HIGH PRIORITY)
# ══════════════════════════════════════════════════════════════════════
# La energía cinética de la starchip NO es la energía que hay que
# generar. Hay tres pérdidas principales:
#   1. η_eléctrica: eficiencia de generación y distribución (~90%)
#   2. η_láser: conversión de electricidad a luz láser (~0.1%)
#   3. η_acoplamiento: fracción del haz que la vela intercepta (~20%)

ETA_ELECTRICA: float = 0.90
ETA_LASER: float = 0.001      # 0.1% — ESTADO DEL ARTE para fibra de alta potencia
ETA_COUPLING: float = 0.20     # 20% — la vela se aleja y el haz diverge
ETA_TOTAL: float = ETA_ELECTRICA * ETA_LASER * ETA_COUPLING

# Energía eléctrica que REALMENTE hay que generar [J]
E_ELECTRICA_REQUERIDA: float = E_CIN_STARSHOT / ETA_TOTAL

# Potencia eléctrica equivalente [W]
P_ELECTRICA_REQUERIDA: float = E_ELECTRICA_REQUERIDA / T_ACCEL


# ══════════════════════════════════════════════════════════════════════
# 5. ESTIMACIÓN DE COSTO DEL ARRAY LÁSER (A2 — HIGH PRIORITY)
# ══════════════════════════════════════════════════════════════════════

# Número de elementos láser (~10⁶ unidades de 100 kW cada una)
N_ELEMENTOS_LASER: float = 1e6
COSTO_POR_ELEMENTO: float = 100e3     # $100k por unidad de 100 kW
COSTO_LASERES: float = N_ELEMENTOS_LASER * COSTO_POR_ELEMENTO  # $100B
COSTO_ENFRIAMIENTO: float = 10e9       # $10B
COSTO_OPTICA_ADAPTATIVA: float = 5e9   # $5B
COSTO_DISTRIBUCION: float = 20e9       # $20B
COSTO_TOTAL_ARRAY: float = (COSTO_LASERES + COSTO_ENFRIAMIENTO +
                              COSTO_OPTICA_ADAPTATIVA + COSTO_DISTRIBUCION)


# ══════════════════════════════════════════════════════════════════════
# FUNCIÓN PRINCIPAL: Cálculo completo de Starshot
# ══════════════════════════════════════════════════════════════════════

def calcular_starshot() -> dict:
    """
    Ejecuta TODOS los cálculos de Starshot y retorna un diccionario
    con los resultados numéricos.

    Retorna
    -------
    dict
        Diccionario con todos los resultados: energía, temperatura,
        divergencia, eficiencia, costo.
        Las claves están documentadas en este módulo.
    """
    return {
        "gamma": GAMMA_STARSHOT,
        "E_cin_J": E_CIN_STARSHOT,
        "E_rest_J": E_REST_STARSHOT,
        "E_cin_vs_prod_diaria": E_CIN_STARSHOT / PROD_HUMANA_J_DIARIA,
        "E_cin_vs_prod_anual": E_CIN_STARSHOT / PROD_HUMANA_J_ANUAL,
        "aceleracion_m_s2": A_MEDIA,
        "aceleracion_g": A_MEDIA / 9.81,
        "distancia_aceleracion_m": D_ACCEL,
        "distancia_aceleracion_AU": D_ACCEL / AU,
        "flujo_potencia_W_m2": P_FLUX,
        "potencia_absorbida_W_m2": P_ABSORBED,
        "T_eq_eps_005": temperatura_equilibrio(0.05),
        "T_eq_eps_010": temperatura_equilibrio(0.10),
        "T_eq_eps_020": temperatura_equilibrio(0.20),
        "T_eq_eps_050": temperatura_equilibrio(0.50),
        "T_eq_eps_090": temperatura_equilibrio(0.90),
        "theta_div_rad": THETA_DIV,
        "theta_div_urad": THETA_DIV * 1e6,
        "beam_radio_alphacen_AU": BEAM_RADIUS_ALPHACEN / AU,
        "beam_diametro_alphacen_AU": BEAM_DIAMETER_ALPHACEN / AU,
        "fraccion_colectada": FRACCION_COLLECTADA,
        "eta_total": ETA_TOTAL,
        "E_electrica_requerida_J": E_ELECTRICA_REQUERIDA,
        "E_electrica_vs_prod_anual": E_ELECTRICA_REQUERIDA / PROD_HUMANA_J_ANUAL,
        "costo_array_laser_USD": COSTO_TOTAL_ARRAY,
    }


def imprimir_starshot() -> None:
    """Imprime todos los resultados de Starshot en formato legible."""
    r = calcular_starshot()
    print("\n" + "=" * 65)
    print("  BREAKTHROUGH STARSHOT — CÁLCULOS COMPLETOS")
    print("=" * 65)
    print(f"  γ = {r['gamma']:.6f}")
    print(f"  E_cin = {r['E_cin_J']:.3e} J = {r['E_cin_J']/MT_TNT:.2f} Mt TNT")
    print(f"  E_cin vs prod diaria = {r['E_cin_vs_prod_diaria']:.4f}×")
    print(f"  E_cin vs prod anual  = {r['E_cin_vs_prod_anual']:.2e}×")
    print(f"\n  ACELERACIÓN:")
    print(f"  a = {r['aceleracion_m_s2']:.2e} m/s² = {r['aceleracion_g']:.0f} g")
    print(f"  d = {r['distancia_aceleracion_AU']:.2f} AU = {r['distancia_aceleracion_m']/1e9:.1f} millones de km")
    print(f"\n  ANÁLISIS TÉRMICO:")
    print(f"  Flujo incidente: {r['flujo_potencia_W_m2']/1e6:.1f} MW/m²")
    print(f"  Potencia absorbida: {r['potencia_absorbida_W_m2']/1e3:.1f} kW/m²")
    # El diccionario usa keys como T_eq_eps_005, T_eq_eps_010, etc.
    eps_keys = {0.05: "005", 0.10: "010", 0.20: "020", 0.50: "050", 0.90: "090"}
    for eps, key in eps_keys.items():
        T = r[f'T_eq_eps_{key}']
        status = "FUNDIDO" if T > T_MELT_SIC else ("PELIGRO" if T > 2500 else "OK")
        print(f"  T_eq(ε={eps:.2f}) = {T:.0f} K — {status}")
    print(f"\n  DIVERGENCIA DEL HAZ:")
    print(f"  θ_div = {r['theta_div_urad']:.2f} μrad")
    print(f"  Diámetro del haz en α Cen = {r['beam_diametro_alphacen_AU']:.2f} AU")
    print(f"  Fracción colectada (ELT 39m) = {r['fraccion_colectada']:.2e}")
    print(f"\n  EFICIENCIA WALL-PLUG:")
    print(f"  η_total = {r['eta_total']:.2e}")
    print(f"  E_eléctrica = {r['E_electrica_requerida_J']:.3e} J")
    print(f"  = {r['E_electrica_vs_prod_anual']*100:.2f}% de la producción anual")
    print(f"\n  COSTO ARRAY LÁSER:")
    print(f"  Estimación: ${r['costo_array_laser_USD']/1e9:.0f}B")
    print(f"  (comparable al presupuesto acumulado de la ISS: ~$150B)")
    print("=" * 65)


if __name__ == "__main__":
    imprimir_starshot()
