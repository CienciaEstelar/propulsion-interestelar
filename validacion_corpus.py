#!/usr/bin/env python3
"""Validación de integridad del corpus de referencias.
Basado en bosque_oscuro/sim/validacion.py (dark-forest)."""
import json
import os
import re

CORPUS_DIR = os.path.dirname(__file__)
VERIFICATION_FILE = os.path.join(CORPUS_DIR, "datos", "doi_verification.json")
OUTPUT_REPORT = os.path.join(CORPUS_DIR, "datos", "validacion_corpus.json")


def checks_integridad():
    """Verifica la integridad del corpus de referencias."""
    issues = []
    stats = {}

    # 1. Cargar verificación de DOIs
    if os.path.exists(VERIFICATION_FILE):
        with open(VERIFICATION_FILE) as f:
            doi_data = json.load(f)
        stats["dois_totales"] = doi_data["total"]
        stats["dois_ok"] = doi_data["ok"]
        stats["dois_fail"] = doi_data["fail"]
        stats["pct_ok"] = doi_data["pct_ok"]
    else:
        stats["doi_verification"] = "no ejecutada"
        issues.append({
            "severidad": "MEDIA",
            "tipo": "verificacion_pendiente",
            "mensaje": "No se encontró doi_verification.json. Ejecutar verify_dois.py primero."
        })

    # 2. Verificar archivos del paper
    paper_files = [
        "PAPER_INTERESTELAR.md",
        "literatura_procesada.md",
        "literatura_procesada_v2.md",
        "gaps_identificados.md",
        "matriz_ingenieria.md",
        "sintesis_critica.md",
        "AUDITORIA_PAPER.md",
    ]
    for f in paper_files:
        path = os.path.join(CORPUS_DIR, f)
        if not os.path.exists(path):
            issues.append({
                "severidad": "ALTA",
                "tipo": "archivo_faltante",
                "archivo": f,
                "mensaje": f"Archivo requerido '{f}' no encontrado."
            })

    # 3. Verificar figuras generadas
    figuras_dir = os.path.join(CORPUS_DIR, "output", "figuras")
    figuras_esperadas = [
        "figura1_matriz_trl",
        "figura2_evolucion_warp",
        "figura3_arquitectura_mision",
        "figura4_link_budget",
        "figura5_sincronizacion_relativista",
        "figura6_gaps_cobertura",
    ]
    figuras_encontradas = []
    if os.path.exists(figuras_dir):
        for fname in os.listdir(figuras_dir):
            if fname.endswith(".pdf") or fname.endswith(".png"):
                figuras_encontradas.append(fname.replace(".pdf", "").replace(".png", ""))
    stats["figuras_generadas"] = len(figuras_encontradas)
    stats["figuras_esperadas"] = len(figuras_esperadas)
    for esperada in figuras_esperadas:
        if esperada not in figuras_encontradas:
            issues.append({
                "severidad": "MEDIA",
                "tipo": "figura_faltante",
                "figura": esperada,
                "mensaje": f"Figura '{esperada}' no generada. Ejecutar generar_figuras.py."
            })

    # 4. Verificar estructura de scripts
    scripts_esperados = [
        "figuras/generar_figuras.py",
        "figuras/style_config.py",
        "figuras/figura1_matriz_trl.py",
        "figuras/figura5_sincronizacion.py",
        "compile_paper.py",
        "verify_dois.py",
        "requirements.txt",
    ]
    for s in scripts_esperados:
        path = os.path.join(CORPUS_DIR, s)
        if not os.path.exists(path):
            issues.append({
                "severidad": "ALTA",
                "tipo": "script_faltante",
                "script": s,
                "mensaje": f"Script '{s}' no encontrado."
            })

    # 5. Verificar que no haya DOIs duplicados en el corpus
    doi_pattern = re.compile(r'10\.\d{4,}/[^\s"\']+')
    all_dois = []
    for md_file in ["PAPER_INTERESTELAR.md"]:
        path = os.path.join(CORPUS_DIR, md_file)
        if os.path.exists(path):
            with open(path) as f:
                content = f.read()
                found = doi_pattern.findall(content)
                all_dois.extend(found)

    unique_dois = set(all_dois)
    if len(all_dois) != len(unique_dois):
        duplicates = len(all_dois) - len(unique_dois)
        issues.append({
            "severidad": "MEDIA",
            "tipo": "dois_duplicados",
            "mensaje": f"Se encontraron {duplicates} DOIs duplicados en el paper."
        })
    stats["dois_en_paper"] = len(unique_dois)

    # 6. Verificar arXiv IDs como alternativa a DOIs faltantes
    arxiv_pattern = re.compile(r'arXiv:(\d{4}\.\d{4,5})')
    arxiv_ids = []
    for md_file in ["PAPER_INTERESTELAR.md", "literatura_procesada_v2.md"]:
        path = os.path.join(CORPUS_DIR, md_file)
        if os.path.exists(path):
            with open(path) as f:
                arxiv_ids.extend(arxiv_pattern.findall(f.read()))
    stats["arxiv_ids_encontrados"] = len(set(arxiv_ids))

    # ── Resultado final ──
    resultado = {
        "fecha": "2026-05-28",
        "stats": stats,
        "issues": issues,
        "aprobado": len([i for i in issues if i["severidad"] == "ALTA"]) == 0
    }

    os.makedirs(os.path.dirname(OUTPUT_REPORT), exist_ok=True)
    with open(OUTPUT_REPORT, "w") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)

    # ── Reporte en consola ──
    print("=" * 60)
    print("  VALIDACIÓN DE INTEGRIDAD DEL CORPUS")
    print("=" * 60)
    for k, v in stats.items():
        print(f"  {k}: {v}")
    print()
    if issues:
        print(f"  Incidencias: {len(issues)}")
        for issue in issues:
            icon = "✗" if issue["severidad"] == "ALTA" else "⚠"
            print(f"  {icon} [{issue['severidad']}] {issue['mensaje'][:100]}")
    else:
        print("  ✓ Sin incidencias.")
    print()
    print(f"  Reporte: {OUTPUT_REPORT}")
    print(f"  Aprobado: {'SI' if resultado['aprobado'] else 'NO - revisar incidencias ALTAS'}")
    print("=" * 60)

    return resultado


if __name__ == "__main__":
    checks_integridad()
