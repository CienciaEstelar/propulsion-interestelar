#!/usr/bin/env python3
"""
PAQUETE DE DERIVACIONES MATEMÁTICAS — Paper de Propulsión Interestelar
========================================================================
"De Alcubierre a la Ingeniería: Una Evaluación Crítica de los
Conceptos de Propulsión Interestelar (1994–2026)"

Autor:  J. D. Galaz Amengual
ORCID:  0009-0007-7474-7560
Fecha:  2026-05-28

PROPÓSITO
---------
Este paquete contiene TODAS las derivaciones matemáticas del paper,
reproducidas íntegramente en Python con bibliotecas científicas
estándar (numpy, scipy, sympy, astropy). Cada número que aparece
en el paper es calculado aquí desde cero, con constantes físicas
verificables y trazables a CODATA 2022.

ESTRUCTURA DEL PAQUETE
----------------------
derivaciones/
    __init__.py         <- Este archivo (índice del paquete)
    constantes.py       <- Todas las constantes físicas y astronómicas
    cinematica.py       <- Cinemática relativista (γ, E_cin, β)
    warp_drives.py      <- Energía de métricas warp (Alcubierre, Lentz, etc.)
    starshot.py         <- Vela láser: cinemática, térmico, divergencia
    fusion.py           <- Propulsión por fusión (Daedalus, Icarus)
    antimateria.py      <- Propulsión por antimateria (aniquilación, costo)
    sincronizacion.py   <- Sincronización temporal relativista
    enlace_optico.py    <- Presupuesto de enlace óptico Tierra-α Centauri
    polvo_ism.py        <- Impacto de polvo interestelar a 0.2c
    magsail.py          <- Frenado magnético con vela magnética
    colonizacion.py     <- Colonización galáctica (sondas Von Neumann)
    reproducibilidad.py <- Hash SHA-256 de verificación global

GARANTÍA DE REPRODUCIBILIDAD
----------------------------
Todos los resultados numéricos se verifican con un hash SHA-256.
Si ejecutas este paquete en cualquier máquina, con cualquier SO,
el hash DEBE ser idéntico. Si cambia, alguien modificó las
constantes, las fórmulas o el código fuente.

CORRECCIONES APLICADAS (post-revisión unificada de 5 evaluadores)
----------------------------------------------------------------
C1: Error de sincronización corregido (factor ~100 en Figura 5)
C4: Energía de Daedalus corregida (E_cin total, no solo ignición)
C5: Análisis térmico de la vela añadido
B4: Comparación con consumo humano diario corregida

USO
---
    from derivaciones import constantes as cte
    from derivaciones.cinematica import gamma, E_kin_rel
    from derivaciones.starshot import calcular_starshot
    ...

    # O para verificar TODO de una vez:
    from derivaciones.reproducibilidad import verificar_todo
    verificar_todo()
"""

__version__ = "2.0.0"
__author__ = "J. D. Galaz Amengual"
__date__ = "2026-05-28"
__all__ = [
    "constantes", "cinematica", "warp_drives", "starshot",
    "fusion", "antimateria", "sincronizacion", "enlace_optico",
    "polvo_ism", "magsail", "colonizacion", "reproducibilidad",
]
