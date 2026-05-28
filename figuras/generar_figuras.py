#!/usr/bin/env python3
"""Script maestro - Genera TODAS las figuras del paper en lote."""
import sys
import os
import time
import traceback

sys.path.insert(0, os.path.dirname(__file__))
from style_config import setup_style

setup_style()

SCRIPTS = [
    ("figura1_matriz_trl.py", "Matriz TRL vs Energía"),
    ("figura2_evolucion_warp.py", "Evolución energética warp drives"),
    ("figura3_arquitectura.py", "Arquitectura integrada de misión"),
    ("figura4_link_budget.py", "Presupuesto enlace óptico"),
    ("figura5_sincronizacion.py", "Sincronización relativista"),
    ("figura6_gaps_cobertura.py", "Mapa de cobertura del corpus"),
]

def main():
    print("=" * 60)
    print("  GENERADOR DE FIGURAS — Paper Interés Propulsión Interestelar")
    print("=" * 60)
    print(f"  Directorio: {os.path.dirname(__file__)}")
    print()

    ok = 0
    fail = 0
    t0 = time.time()

    for script, desc in SCRIPTS:
        path = os.path.join(os.path.dirname(__file__), script)
        print(f"▶ {script} — {desc}...")
        try:
            exec(open(path).read())
            ok += 1
            print(f"  ✓ OK\n")
        except Exception as e:
            fail += 1
            print(f"  ✗ ERROR: {e}")
            traceback.print_exc()
            print()

    t1 = time.time()
    print("=" * 60)
    print(f"  RESULTADO: {ok}/{len(SCRIPTS)} figuras generadas")
    print(f"  Tiempo total: {t1-t0:.1f}s")
    print(f"  Output: {os.path.join(os.path.dirname(__file__), '..', 'output', 'figuras')}")
    print("=" * 60)

    return 0 if fail == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
