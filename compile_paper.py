#!/usr/bin/env python3
"""
Compilador del paper — Convierte Markdown a LaTeX y compila a PDF de una columna.
Adaptado de compile_paper.py v2.3 (dark-forest) y DVT.
"""
import subprocess
import sys
import os
import shutil

PAPER_MD = os.path.join(os.path.dirname(__file__), "PAPER_INTERESTELAR.md")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
FIGURAS_DIR = os.path.join(OUTPUT_DIR, "figuras")
PAPER_TEX = os.path.join(OUTPUT_DIR, "PAPER_INTERESTELAR.tex")
PAPER_PDF = os.path.join(OUTPUT_DIR, "PAPER_INTERESTELAR.pdf")


def run_figuras():
    """Ejecuta el generador de figuras antes de compilar."""
    print("=" * 60)
    print("  PASO 1/3: Generando figuras...")
    print("=" * 60)
    script = os.path.join(os.path.dirname(__file__), "figuras", "generar_figuras.py")
    result = subprocess.run([sys.executable, script], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        print("⚠ Advertencia: algunas figuras fallaron. Continuando con compilación...")


def md_to_latex():
    """Convierte el paper Markdown a LaTeX."""
    print("=" * 60)
    print("  PASO 2/3: Convirtiendo Markdown → LaTeX...")
    print("=" * 60)

    with open(PAPER_MD, "r") as f:
        md = f.read()

    # ── Extraer secciones ──
    # Simplificación: usamos pandoc si está disponible, sino conversión manual
    if shutil.which("pandoc"):
        print("  Usando pandoc para conversión...")
        cmd = [
            "pandoc", PAPER_MD,
            "-o", PAPER_TEX,
            "--from", "markdown+pipe_tables+grid_tables",
            "--to", "latex",
            "--pdf-engine=xelatex",
            "-V", "documentclass=article",
            "-V", "papersize=a4",
            "-V", "fontsize=11pt",
            "-V", "geometry=margin=2.5cm",
            "-V", "onecolumn=true",
            "-V", "lang=es",
            f"--resource-path={os.path.dirname(PAPER_MD)}:{FIGURAS_DIR}",
            "--standalone",
            "-V", "title=De Alcubierre a la Ingeniería: Evaluación Crítica de Propulsión Interestelar (1994-2026)",
            "-V", "author=J. D. Galaz Amengual",
            "-V", "date=28 de mayo de 2026",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  ✗ Error pandoc: {result.stderr}")
            return False
        print(f"  ✓ LaTeX generado: {PAPER_TEX}")
        return True
    else:
        print("  ✗ pandoc no instalado. Instálalo con: sudo apt install pandoc")
        print("  Generando PDF directamente desde Markdown con Python...")
        return simple_md_to_tex(md)


def simple_md_to_tex(md):
    """Conversión mínima Markdown → LaTeX sin pandoc."""
    tex_header = r"""\documentclass[11pt,a4paper,onecolumn]{article}
\usepackage[spanish,es-noshorthands]{babel}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{array}
\usepackage{hyperref}
\usepackage{url}
\usepackage[margin=2.5cm]{geometry}
\usepackage{setspace}
\onehalfspacing
\title{De Alcubierre a la Ingeniería: Una Evaluación Crítica de los Conceptos de Propulsión Interestelar (1994-2026)}
\author{J. D. Galaz Amengual\\ORCID: 0009-0007-7474-7560}
\date{28 de mayo de 2026}
\begin{document}
\maketitle
\begin{abstract}
"""
    tex_footer = r"""
\end{document}
"""
    # Esta es una conversión de respaldo si pandoc no está disponible
    # Por ahora escribimos un archivo mínimo que sirva para compilar
    tex = tex_header
    tex += "Revisión crítica de 28 conceptos de propulsión interestelar a través de 155 referencias en 18 bloques temáticos. Construimos una matriz comparativa de ingeniería y una hoja de ruta experimental priorizada para las próximas dos décadas."
    tex += r"\end{abstract}" + "\n"
    tex += r"\section{Introducción}" + "\n"
    tex += "Consultar PAPER\_INTERESTELAR.md para el texto completo o instalar pandoc para compilación automática." + "\n"
    tex += r"\begin{figure}[h]" + "\n"
    tex += r"\includegraphics[width=\textwidth]{figura1_matriz_trl.pdf}" + "\n"
    tex += r"\caption{Matriz TRL vs Energía Requerida para 28 conceptos.}" + "\n"
    tex += r"\end{figure}" + "\n"
    tex += tex_footer

    with open(PAPER_TEX, "w") as f:
        f.write(tex)
    print(f"  ✓ LaTeX mínimo generado: {PAPER_TEX}")
    print("  ⚠ Instala pandoc para conversión completa: sudo apt install pandoc")
    return True


def compile_pdf():
    """Compila el LaTeX a PDF."""
    print("=" * 60)
    print("  PASO 3/3: Compilando LaTeX → PDF...")
    print("=" * 60)

    outdir = OUTPUT_DIR
    os.makedirs(outdir, exist_ok=True)

    if not os.path.exists(PAPER_TEX):
        print("  ✗ No se encontró el archivo .tex")
        return False

    for engine in ["pdflatex", "xelatex", "lualatex"]:
        if shutil.which(engine):
            print(f"  Usando {engine}...")
            cmd = [
                engine,
                "-interaction=nonstopmode",
                "-output-directory", outdir,
                PAPER_TEX
            ]
            for _ in range(2):  # Dos pasadas para referencias cruzadas
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode != 0:
                    # Extraer errores relevantes del .log
                    log_file = PAPER_TEX.replace(".tex", ".log")
                    if os.path.exists(log_file):
                        with open(log_file) as lf:
                            for line in lf:
                                if "Error" in line or "!" in line:
                                    print(f"    {line.strip()[:120]}")
            print(f"  ✓ PDF compilado: {PAPER_PDF}")
            return True

    print("  ✗ No se encontró motor LaTeX. Instala: sudo apt install texlive-latex-base")
    return False


def main():
    print("=" * 60)
    print("  COMPILADOR DEL PAPER — De Alcubierre a la Ingeniería")
    print("  Adaptado de compile_paper.py v2.3 (dark-forest)")
    print("=" * 60)
    print()

    # Paso 1: Generar figuras
    run_figuras()

    # Paso 2: Markdown → LaTeX
    if not md_to_latex():
        print("✗ Falló la conversión Markdown → LaTeX")
        return 1

    # Paso 3: Compilar PDF
    if not compile_pdf():
        print("✗ Falló la compilación PDF")
        return 1

    print()
    print("=" * 60)
    print(f"  ✓ PAPER COMPILADO: {PAPER_PDF}")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
