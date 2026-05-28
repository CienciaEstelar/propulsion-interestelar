#!/usr/bin/env python3
"""
CINEMÁTICA RELATIVISTA
======================
Derivaciones de la cinemática relativista usadas en TODO el paper.

DEFINICIONES FUNDAMENTALES
--------------------------
Factor de Lorentz:
    γ = 1 / √(1 - β²)    donde β = v/c

Energía cinética relativista:
    E_cin = (γ - 1) × m × c²

Energía total:
    E_total = γ × m × c²

Expansión para bajas velocidades (β ≪ 1):
    E_cin ≈ ½mv² + ⅜m·v⁴/c² + O(v⁶/c⁴)

Cuando β ≪ 1, el primer término (clásico) domina.
Para β = 0.01, el segundo término es ~0.0075% del primero.
Para β = 0.20, el segundo término es ~3% del primero (no despreciable).

Autor: J. D. Galaz Amengual
Fecha: 2026-05-28
"""

import numpy as np
from .constantes import C


def gamma(beta: float) -> float:
    """
    Calcula el factor de Lorentz γ = 1/√(1-β²).

    Parámetros
    ----------
    beta : float
        Velocidad como fracción de c. Debe cumplir 0 ≤ β < 1.
        Ejemplos: beta=0.2 (Starshot), beta=0.12 (Daedalus), beta=0.5 (antimateria)

    Retorna
    -------
    float
        Factor de Lorentz γ ≥ 1.
        γ = 1.0 cuando β = 0 (reposo).
        γ → ∞ cuando β → 1 (ultra-relativista).

    Notas
    -----
    Para β = 0.2 (Starshot): γ = 1.020621 — apenas un 2% de corrección relativista.
    Para β = 0.9: γ = 2.294 — la masa efectiva más que se duplica.
    Para β = 0.999: γ = 22.37 — efectos relativistas dominan completamente.

    Verificación
    ------------
    >>> from derivaciones.cinematica import gamma
    >>> gamma(0.0)
    1.0
    >>> gamma(0.2)
    1.0206207261596576
    >>> gamma(0.9)
    2.294157338705618
    """
    if beta < 0 or beta >= 1:
        raise ValueError(f"beta = {beta} debe cumplir 0 ≤ β < 1")
    return 1.0 / np.sqrt(1.0 - beta**2)


def E_cin_relativista(masa_kg: float, beta: float) -> float:
    """
    Calcula la energía cinética relativista E_cin = (γ-1)mc².

    Parámetros
    ----------
    masa_kg : float
        Masa en reposo del objeto [kg].
        Ejemplos: 0.001 (1 gramo, Starshot), 5e7 (50000 toneladas, Daedalus)
    beta : float
        Velocidad como fracción de c [adimensional].

    Retorna
    -------
    float
        Energía cinética [J].

    Notas
    -----
    La energía cinética NO es ½mv² a velocidades relativistas.
    Para Starshot (1 g, 0.2c):
        E_clásica = ½ × 0.001 × (0.2×3×10⁸)² = 1.8×10¹² J
        E_relativista = (1.0206-1) × 0.001 × (3×10⁸)² = 1.853×10¹² J
        Diferencia: ~3% — pequeña pero no despreciable para cálculos de ingeniería.

    Verificación
    ------------
    >>> from derivaciones.cinematica import E_cin_relativista
    >>> # Para β << 1, debe recuperar la energía clásica
    >>> E_rel = E_cin_relativista(1.0, 0.001)
    >>> E_clas = 0.5 * 1.0 * (0.001 * 299792458)**2
    >>> abs(E_rel - E_clas) / E_clas < 1e-6
    True
    """
    return (gamma(beta) - 1) * masa_kg * C**2


def E_cin_clasica(masa_kg: float, velocidad_m_s: float) -> float:
    """
    Calcula la energía cinética CLÁSICA ½mv² [J].

    USO SOLO PARA COMPARACIÓN con la versión relativista.
    NO USAR para velocidades > 0.01c (error > 0.01%).

    Parámetros
    ----------
    masa_kg : float
        Masa [kg].
    velocidad_m_s : float
        Velocidad [m/s]. Debe ser ≪ C para que la aproximación sea válida.

    Retorna
    -------
    float
        Energía cinética clásica [J].
    """
    return 0.5 * masa_kg * velocidad_m_s**2


def tabla_gamma() -> None:
    """
    Imprime una tabla de γ para velocidades de interés en el paper.
    Sirve como referencia rápida para verificar cálculos manuales.
    """
    betas = [0.001, 0.01, 0.05, 0.10, 0.12, 0.20, 0.50, 0.90, 0.99, 0.999]
    print("\n" + "=" * 62)
    print("  TABLA DE FACTORES DE LORENTZ")
    print("=" * 62)
    print(f"  {'β = v/c':>10}  {'γ':>12}  {'γ-1':>12}  {'E_cin/mc²':>12}  {'Notas'}")
    print("  " + "-" * 58)
    for beta in betas:
        g = gamma(beta)
        notas = ""
        if beta == 0.001: notas = "régimen clásico"
        elif beta == 0.01: notas = "velocidad solar"
        elif beta == 0.05: notas = "Dragonfly (0.05c)"
        elif beta == 0.10: notas = "límite bajo interestelar"
        elif beta == 0.12: notas = "Daedalus (0.12c)"
        elif beta == 0.20: notas = "Starshot (0.2c)"
        elif beta == 0.50: notas = "antimateria ideal"
        elif beta == 0.90: notas = "altamente relativista"
        elif beta == 0.99: notas = "cosmológico (jet AGN)"
        elif beta == 0.999: notas = "rayos cósmicos UHE"
        print(f"  {beta:10.3f}  {g:12.6f}  {g-1:12.6f}  {g-1:12.6f}  {notas}")
    print("=" * 62)


if __name__ == "__main__":
    tabla_gamma()
