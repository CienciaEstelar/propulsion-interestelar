#!/usr/bin/env python3
"""
CONSTANTES FÍSICAS Y ASTRONÓMICAS
==================================
Este módulo centraliza TODAS las constantes utilizadas en el paper.
Cada constante incluye su fuente, incertidumbre y uso en el paper.

Fuentes:
    - CODATA 2022 (scipy.constants) para constantes fundamentales
    - IAU 2015 para constantes astronómicas nominales
    - IEA World Energy Outlook 2025 para producción energética humana

Autor: J. D. Galaz Amengual
Fecha: 2026-05-28
"""

import numpy as np
from scipy import constants as _const


# ══════════════════════════════════════════════════════════════════════
# CONSTANTES FUNDAMENTALES — CODATA 2022
# ══════════════════════════════════════════════════════════════════════
# Estas constantes tienen incertidumbre CERO en el SI (son EXACTAS
# por definición de las unidades base, excepto G). Fuente: scipy.constants
# que implementa los valores recomendados por NIST/CODATA.

# Velocidad de la luz en vacío [m/s]
# EXACTA por definición del metro desde 1983: 1 m = distancia que recorre
# la luz en 1/299792458 segundos.
# USO: conversión masa-energía (E=mc²), cinemática relativista, tiempo de vuelo
C: float = _const.c  # 299792458.0 m/s

# Constante de gravitación universal [m³/(kg·s²)]
# NO es exacta. Es la constante fundamental con mayor incertidumbre relativa
# (~2.2×10⁻⁵) debido a la dificultad de medir fuerzas gravitatorias en laboratorio.
# USO: potencial gravitacional solar, longitud de Planck, fuerza de marea galáctica
G: float = _const.G  # 6.67430e-11 m³/(kg·s²)

# Constante de Planck [J·s]
# EXACTA por definición del kilogramo desde 2019.
# USO: energía de fotones (E=hν) para presupuesto de enlace óptico
H_PLANCK: float = _const.h  # 6.62607015e-34 J·s

# Constante de Planck reducida ℏ = h/2π [J·s]
# USO: longitud de Planck ℓ_P = √(ℏG/c³), principio de incertidumbre
HBAR: float = _const.hbar  # 1.054571817e-34 J·s

# Constante de Stefan-Boltzmann [W/(m²·K⁴)]
# Derivación teórica: σ = 2π⁵k_B⁴/(15h³c²)
# USO: temperatura de equilibrio radiativo de la vela láser
SIGMA_SB: float = _const.sigma  # 5.670374419e-8 W/(m²·K⁴)

# Constante de Boltzmann [J/K]
# EXACTA por definición del kelvin desde 2019.
# USO: energía térmica, velocidad del sonido en el medio interestelar
K_B: float = _const.k  # 1.380649e-23 J/K

# Carga elemental [C]
# EXACTA por definición del ampere desde 2019.
# USO: conversión J ↔ eV, sección eficaz de ionización
E_CHARGE: float = _const.e  # 1.602176634e-19 C

# Número de Avogadro [mol⁻¹]
# EXACTO por definición del mol desde 2019.
# USO: conversión entre masa molar y masa atómica, densidad numérica del ISM
N_A: float = _const.N_A  # 6.02214076e23 mol⁻¹


# ══════════════════════════════════════════════════════════════════════
# CONSTANTES ASTRONÓMICAS — IAU 2015
# ══════════════════════════════════════════════════════════════════════
# Salvo indicación, incertidumbre < 10⁻⁶.

# Masa solar nominal [kg]
# USO: referencia para energías de warp drive (Van den Broeck), órbita galáctica
M_SOL: float = 1.98847e30

# Masa de Júpiter [kg]
# USO: equivalencia energética para Alcubierre original (~1 M_Jup × c²)
M_JUPITER: float = 1.89813e27

# Masa terrestre [kg]
# USO: referencia para exoplanetas habitables (próxima b ~1.27 M_Earth)
M_EARTH: float = 5.9722e24

# Unidad Astronómica [m] — radio medio de la órbita terrestre
# USO: distancia de aceleración de Starshot (~0.2 AU), escala del sistema solar
AU: float = _const.au  # 1.495978707e11 m

# Pársec [m] — distancia a la que 1 UA subtiende 1 segundo de arco
# USO: distancias interestelares, densidad estelar en el vecindario solar
PC: float = 3.085677581e16

# Año juliano [s] — exactamente 365.25 días × 86400 s/día
# USO: conversión entre segundos y años para tiempos de misión
YR_S: float = _const.Julian_year  # 31557600 s

# Día [s] — exactamente 24 × 3600
# USO: conversión de tiempos cortos (aceleración, comunicación)
DAY_S: float = 86400.0

# Año luz [m] — distancia que recorre la luz en un año juliano
# USO: distancia a α Centauri (4.37 al), escalas de colonización galáctica
LY: float = C * YR_S  # 9.4607304725808e15 m


# ══════════════════════════════════════════════════════════════════════
# UNIDADES DE ENERGÍA — Factores de conversión
# ══════════════════════════════════════════════════════════════════════

# Megaelectronvoltio [J] — escala de reacciones nucleares
# 1 MeV = 10⁶ eV × 1.602176634×10⁻¹⁹ C = 1.602176634×10⁻¹³ J
MEV: float = 1.602176634e-13

# Gigaelectronvoltio [J] — escala de rayos cósmicos galácticos
GEV: float = 1.602176634e-10

# Megatón de TNT [J] — referencia de explosivos nucleares
# 1 Mt = 10⁶ toneladas × 4.184×10⁹ J/tonelada (definición estándar)
MT_TNT: float = 4.184e15

# 1 foe ("fifty-one ergs") [J] — energía típica de una supernova
# Acuñado por Stirling Colgate. 1 foe = 10⁵¹ erg = 10⁴⁴ J
FOE: float = 1e44


# ══════════════════════════════════════════════════════════════════════
# UNIDADES DE PLANCK — Escalas naturales del universo
# ══════════════════════════════════════════════════════════════════════
# Combinaciones de G, ħ, c que definen las escalas donde la gravedad
# cuántica se vuelve relevante.

# Longitud de Planck [m] — la escala de longitud más pequeña con sentido físico
# Fórmula: ℓ_P = √(ħG/c³)
L_PLANCK: float = np.sqrt(HBAR * G / C**3)  # ≈ 1.616×10⁻³⁵ m

# Masa de Planck [kg] — la masa de un agujero negro cuyo radio de
# Schwarzschild es comparable a su longitud de onda de Compton
# Fórmula: m_P = √(ħc/G)
M_PLANCK: float = np.sqrt(HBAR * C / G)  # ≈ 2.176×10⁻⁸ kg


# ══════════════════════════════════════════════════════════════════════
# PRODUCCIÓN ENERGÉTICA HUMANA — IEA World Energy Outlook 2025
# ══════════════════════════════════════════════════════════════════════
# Incluye TODAS las fuentes: petróleo, gas, carbón, nuclear, renovables.
# NOTA: La versión anterior del paper usaba erróneamente ~2×10¹⁷ J/día.
# El valor correcto es ~2.16×10¹⁸ J/día (un orden de magnitud mayor).

# Potencia global total [W] ≈ 25 TW
PROD_HUMANA_W: float = 2.5e13

# Energía anual [J] ≈ 7.89×10²⁰ J
PROD_HUMANA_J_ANUAL: float = PROD_HUMANA_W * YR_S

# Energía diaria [J] ≈ 2.16×10¹⁸ J
PROD_HUMANA_J_DIARIA: float = PROD_HUMANA_W * DAY_S


# ══════════════════════════════════════════════════════════════════════
# FUNCIONES AUXILIARES
# ══════════════════════════════════════════════════════════════════════

def imprimir_constantes() -> None:
    """Imprime todas las constantes en formato legible para verificación."""
    print("=" * 65)
    print("  CONSTANTES FÍSICAS Y ASTRONÓMICAS")
    print("=" * 65)
    print(f"  c      = {C:.6e} m/s        (EXACTO)")
    print(f"  G      = {G:.6e} m³/(kg·s²) (±2.2×10⁻⁵)")
    print(f"  h      = {H_PLANCK:.6e} J·s       (EXACTO)")
    print(f"  ħ      = {HBAR:.6e} J·s")
    print(f"  σ_SB   = {SIGMA_SB:.6e} W/(m²·K⁴)")
    print(f"  k_B    = {K_B:.6e} J/K")
    print(f"  ℓ_P    = {L_PLANCK:.3e} m")
    print(f"  M_P    = {M_PLANCK:.3e} kg")
    print(f"  M_Sol  = {M_SOL:.5e} kg")
    print(f"  M_Jup  = {M_JUPITER:.5e} kg")
    print(f"  1 AU   = {AU:.3e} m")
    print(f"  1 pc   = {PC:.3e} m = {PC/LY:.2f} al")
    print(f"  1 al   = {LY:.3e} m")
    print(f"  1 año  = {YR_S:.0f} s")
    print(f"  Potencia humana = {PROD_HUMANA_W/1e12:.1f} TW")
    print(f"  Energía anual   = {PROD_HUMANA_J_ANUAL:.3e} J")
    print(f"  Energía diaria  = {PROD_HUMANA_J_DIARIA:.3e} J")
    print("=" * 65)


# ── Ejecución directa ──
if __name__ == "__main__":
    imprimir_constantes()
