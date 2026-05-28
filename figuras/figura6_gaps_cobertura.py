#!/usr/bin/env python3
"""Figura 6: Mapa de cobertura del corpus por bloque temático y gaps de literatura."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from style_config import *
import numpy as np

fig, ax = figura_nueva(ancho=9, alto=6)
ax = ax[0]

# Datos de cobertura por bloque
bloques = [
    "B1: Alcubierre\ny evolución", "B2: Velas\nláser", "B3: Fusión\ny conceptos",
    "B4: Sondas\nVon Neumann", "B5: Materiales\nextremos", "B6: Energía y\nescala Kardashev",
    "B7: Física\nfundamental", "B8: Detección\ny navegación", "B9: Reviews\ny roadmaps",
    "B10: Comunicación\ninterestelar", "B11: Blindaje\ny supervivencia",
    "B12: Frenado y\ndesaceleración", "B13: Fuentes\nde energía",
    "B14: Miniaturización\ny payloads", "B15: Propulsión\npor energía",
    "B16: Detectabilidad\ny SETI", "B17: Simulaciones\nnuméricas",
    "B18: Ética y\ngobernanza", "B19: Actualizaciones\n2023-2026",
]

refs_con_doi = [10, 7, 11, 5, 8, 3, 8, 6, 1, 12, 15, 8, 8, 10, 5, 7, 5, 10, 0]
refs_sin_doi = [5, 3, 3, 6, 0, 3, 1, 0, 0, 2, 3, 1, 2, 1, 3, 2, 1, 2, 11]
refs_unverified = refs_sin_doi  # Renombrar para claridad

x = np.arange(len(bloques))
width = 0.65

# Barras apiladas
bar_doi = ax.bar(x, refs_con_doi, width, color=COLORS["establecida"],
                  edgecolor="white", linewidth=0.5, label="Con DOI verificable", zorder=3)
bar_nodoi = ax.bar(x, refs_sin_doi, width, bottom=refs_con_doi,
                    color=COLORS["especulativa"], edgecolor="white", linewidth=0.5,
                    alpha=0.7, label="Sin DOI / [UNVERIFIED]", zorder=3)

# Línea de mínimo recomendado (3 refs peer-reviewed)
ax.axhline(3, color=COLORS["warp"], linestyle="--", linewidth=1, alpha=0.7, zorder=2)
ax.text(len(bloques)-0.5, 3.5, "Mínimo recomendado\n(3 refs peer-reviewed)", fontsize=7,
        color=COLORS["warp"], fontstyle="italic", ha="right")

# Anotar bloques con gaps críticos
gaps_criticos = {
    8: ("GAP CRÍTICO\npre-v2", 9),
    18: ("GAP CRÍTICO\nsin DOIs\nverificables", 11),
}
for idx, (texto, y_offset) in gaps_criticos.items():
    ax.annotate(texto, (idx, refs_con_doi[idx] + refs_sin_doi[idx] + y_offset),
                fontsize=6.5, ha="center", color=COLORS["especulativa"], fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.2", facecolor="#FFEBEE", edgecolor=COLORS["especulativa"], alpha=0.8))

# Anotar bloques más fuertes
for idx in [0, 10, 11, 13]:
    ax.annotate("✓", (idx, refs_con_doi[idx] + refs_sin_doi[idx] + 1.5),
                fontsize=14, ha="center", color=COLORS["ingenieria"], fontweight="bold")

ax.set_xticks(x)
ax.set_xticklabels(bloques, rotation=50, ha="right", fontsize=7)
ax.set_ylabel("Número de referencias", fontweight="bold")
ax.set_title("Figura 6: Cobertura del corpus por bloque temático\n"
             "Referencias con DOI verificable vs. sin DOI/[UNVERIFIED]",
             fontweight="bold", pad=12)
ax.legend(fontsize=8, loc="upper left")
ax.set_ylim(0, 22)
ax.set_xlim(-0.5, len(bloques) - 0.5)

# Totales en anotación
total_doi = sum(refs_con_doi)
total_nodoi = sum(refs_sin_doi)
ax.text(0.98, 0.95, f"Total: {total_doi + total_nodoi} refs\n"
                     f"DOI verificable: {total_doi} ({100*total_doi/(total_doi+total_nodoi):.0f}%)\n"
                     f"Sin DOI/UNVERIFIED: {total_nodoi}",
        transform=ax.transAxes, fontsize=8, ha="right", va="top",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=COLORS["grid"], alpha=0.9))

guardar_figura(fig, "figura6_gaps_cobertura")
print("✓ Figura 6 generada: Mapa de cobertura del corpus")
