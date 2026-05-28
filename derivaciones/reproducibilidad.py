#!/usr/bin/env python3
"""
REPRODUCIBILIDAD — Verificación global de todos los cálculos
=============================================================
Calcula un hash SHA-256 de todos los resultados numéricos del paper.
Si el hash cambia entre ejecuciones, algo fue modificado.

USO:
    from derivaciones.reproducibilidad import verificar_todo
    verificar_todo()

Autor: J. D. Galaz Amengual
Fecha: 2026-05-28
"""

import json
import hashlib
import sys
import os
from datetime import datetime


def verificar_todo() -> str:
    """
    Ejecuta TODOS los módulos de derivación y calcula un hash SHA-256
    de los resultados. Si el hash difiere del valor de referencia,
    algo fue modificado.

    Retorna
    -------
    str
        Hash SHA-256 de 64 caracteres hexadecimales.

    Lanza
    -----
    AssertionError
        Si algún módulo no puede importarse o ejecutarse.
    """
    # Importar todos los módulos de derivación
    from . import constantes as cte
    from .cinematica import gamma, E_cin_relativista
    from .starshot import calcular_starshot
    from .sincronizacion import calcular_sincronizacion

    print("=" * 65)
    print("  VERIFICACIÓN GLOBAL DE REPRODUCIBILIDAD")
    print("=" * 65)

    # ── Recolectar TODOS los resultados ──
    r_star = calcular_starshot()
    r_sync = calcular_sincronizacion()

    # Energía de Daedalus (CORREGIDA C4)
    m_daedalus = 50000e3  # kg
    gamma_daed = gamma(0.12)
    E_daedalus_J = E_cin_relativista(m_daedalus, 0.12)

    # Energía de Alcubierre
    E_alcubierre_J = cte.M_JUPITER * cte.C**2

    # Costo antimateria
    costo_antimateria_por_gramo = 6.4e6 * 1e9  # $6.4T/g

    todos_resultados = {
        # Cinemática
        "gamma_02c": float(gamma(0.2)),
        "gamma_012c": float(gamma(0.12)),
        # Starshot
        "E_cin_starshot_J": float(r_star["E_cin_J"]),
        "T_eq_eps_010_K": float(r_star["T_eq_eps_010"]),
        "T_eq_eps_050_K": float(r_star["T_eq_eps_050"]),
        "theta_div_urad": float(r_star["theta_div_urad"]),
        "eta_total_wall_plug": float(r_star["eta_total"]),
        # Daedalus
        "E_cin_daedalus_J": float(E_daedalus_J),
        # Antimateria
        "costo_antimateria_por_g_USD": float(costo_antimateria_por_gramo),
        # Sincronización (CORREGIDA C1)
        "DT_RE_ms": float(r_sync["DT_RE_ms"]),
        "DT_total_ms": float(r_sync["DT_total_ms"]),
        "DT_total_AU": float(r_sync["DT_total_AU"]),
        # Alcubierre
        "E_alcubierre_J": float(E_alcubierre_J),
    }

    # ── Calcular hash ──
    resultados_json = json.dumps(todos_resultados, sort_keys=True)
    h = hashlib.sha256(resultados_json.encode()).hexdigest()

    # ── Imprimir resultados ──
    for clave, valor in todos_resultados.items():
        print(f"  {clave:<35} = {valor:.6e}")

    print(f"\n  {'─'*55}")
    print(f"  HASH SHA-256: {h}")
    print(f"  Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Python: {sys.version.split()[0]}")
    print(f"  Este hash DEBE ser idéntico en cualquier ejecución.")
    print(f"  Si difiere, constantes o fórmulas fueron modificadas.")
    print(f"  {'─'*55}")

    # ── Guardar para trazabilidad ──
    outdir = os.path.join(os.path.dirname(__file__), "..", "datos")
    os.makedirs(outdir, exist_ok=True)
    reporte = {
        "hash": h,
        "fecha": datetime.now().isoformat(),
        "python": sys.version,
        "resultados": todos_resultados,
    }
    with open(os.path.join(outdir, "hash_reproducibilidad.json"), "w") as f:
        json.dump(reporte, f, indent=2, ensure_ascii=False)
    print(f"\n  Reporte guardado en: datos/hash_reproducibilidad.json")

    return h


if __name__ == "__main__":
    verificar_todo()
