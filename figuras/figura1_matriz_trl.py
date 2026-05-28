#!/usr/bin/env python3
"""Figura 1: Matriz TRL vs Energía Requerida para 28 conceptos de propulsión interestelar."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from style_config import *

# Datos: (nombre, TRL, energia_J, categoria, tipo_fisica)
conceptos = [
    # Categoría A: TRL ≥ 4
    ("SEXTANT\n(púlsares)", 6.5, 1e3, "Navegación", "establecida"),
    ("Interstellar\nProbe", 6.5, 1e14, "Sonda local", "establecida"),
    ("VASIMR\n(VX-200)", 4.5, 1e18, "Propulsión\neléctrica", "establecida"),
    ("UHTC\n(HfC, ZrC)", 4.5, 1e3, "Materiales", "establecida"),
    ("HTS\n(ReBCO/YBCO)", 4.5, 1e3, "Materiales", "establecida"),
    # Categoría B: TRL 2-3 (física establecida, ingeniería)
    ("Vela láser\n(Starshot 1g)", 2.5, 2e15, "Vela láser", "establecida"),
    ("Beam-riding\n(metasuperficies)", 2.5, 1e6, "Vela láser", "establecida"),
    ("DSOC\n(comunicación)", 6.5, 1e4, "Comunicación", "establecida"),
    ("RTG\n(Pu-238)", 8.5, 1e10, "Energía", "establecida"),
    ("KRUSTY\n(fisión 1kW)", 5.5, 1e12, "Energía", "establecida"),
    ("Blindaje\n(polietileno+B)", 4.5, 1e3, "Blindaje", "establecida"),
    ("Magsail\n(frenado)", 2.0, 1e18, "Frenado", "establecida"),
    ("Electric sail\n(frenado)", 3.5, 1e16, "Frenado", "establecida"),
    ("Antimateria\n(precursor ng)", 2.5, 1e16, "Antimateria", "establecida"),
    ("Orion\n(pulso nuclear)", 3.0, 1e21, "Fusión", "establecida"),
    ("Comunicación\ncuántica IS", 1.5, 1e3, "Comunicación", "establecida"),
    # Categoría C: TRL 1 (especulativa)
    ("Warp drive\n(Bobrick-Martire)", 1.0, 1e15, "Warp drive", "especulativa"),
    ("Warp drive\n(Lentz soliton)", 1.0, 1e15, "Warp drive", "especulativa"),
    ("Warp drive\n(Einstein-Cartan)", 1.0, 1e15, "Warp drive", "especulativa"),
    ("Warp drive\n(Alcubierre orig.)", 1.0, 1e52, "Warp drive", "especulativa"),
    ("Warp drive\n(Van den Broeck)", 1.0, 1e46, "Warp drive", "especulativa"),
    ("Agujeros de\ngusano", 1.0, 1e42, "Warp drive", "especulativa"),
    ("Sondas VN\n(Freitas 1980)", 1.0, 1e25, "Von Neumann", "especulativa"),
    ("Nanobots VN\n(Osmanov 2019)", 1.0, 1e5, "Von Neumann", "especulativa"),
    ("Dyson swarm\n+ beam", 1.0, 1e32, "Energía", "especulativa"),
    ("ZPE\n(energía vacío)", 1.0, 1e30, "Energía", "especulativa"),
    ("Energía oscura\n(propulsión)", 1.0, 1e40, "Energía", "especulativa"),
    ("Daedalus/Icarus\n(fusión DHe3)", 1.5, 6e21, "Fusión", "establecida"),
]

fig, axes = figura_nueva(ancho=10, alto=7)
ax = axes[0]

# Mapa de colores por tipo de física
color_map = {"establecida": COLORS["establecida"], "especulativa": COLORS["especulativa"]}
marcador_map = {
    "Navegación": "s", "Sonda local": "s", "Propulsión\neléctrica": "D",
    "Materiales": "^", "Vela láser": "o", "Comunicación": "P",
    "Energía": "X", "Blindaje": "h", "Frenado": "v",
    "Antimateria": "*", "Fusión": "p", "Warp drive": "d",
    "Von Neumann": "H",
}

for nombre, trl, energia, cat, fisica in conceptos:
    marker = marcador_map.get(cat, "o")
    color = color_map[fisica]
    edge = "black" if fisica == "establecida" else COLORS["especulativa"]
    alpha = 0.85 if fisica == "establecida" else 0.6
    size = 80 + 30 * trl  # Tamaño proporcional a TRL
    ax.scatter(trl, energia, s=size, c=color, marker=marker,
               edgecolors=edge, linewidth=0.5, alpha=alpha, zorder=3)

# Zonas de viabilidad
ax.axvspan(3, 9, alpha=0.05, color=COLORS["ingenieria"], label="TRL ≥ 3: Ingeniería")
ax.axvspan(0, 3, alpha=0.05, color=COLORS["especulativa"], label="TRL < 3: Especulativo")
ax.axhline(PRODUCCION_HUMANA_J_ANUAL, color=COLORS["text"], linestyle="--", linewidth=1, alpha=0.6)
ax.text(7.8, PRODUCCION_HUMANA_J_ANUAL * 1.3, "Producción humana\nanual (~1.8×10²⁰ J)",
        fontsize=7, color=COLORS["text"], ha="right", fontstyle="italic")

ax.set_yscale("log")
ax.set_xlabel("Technology Readiness Level (TRL)", fontweight="bold")
ax.set_ylabel("Energía requerida [J]", fontweight="bold")
ax.set_title("Figura 1: Madurez tecnológica vs. requisito energético de\nconceptos de propulsión interestelar",
             fontweight="bold", pad=12)
ax.set_xlim(0, 9.5)
ax.set_ylim(1, 1e55)

# Leyenda de tipos de física
from matplotlib.lines import Line2D
leyenda_fisica = [
    Line2D([0], [0], marker="o", color="w", markerfacecolor=COLORS["establecida"],
           markeredgecolor="black", markersize=10, label="Física establecida"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor=COLORS["especulativa"],
           markeredgecolor=COLORS["especulativa"], markersize=10, label="Especulativa"),
]
ax.legend(handles=leyenda_fisica, loc="lower left", fontsize=8,
          title="Estatus físico", title_fontsize=9)

guardar_figura(fig, "figura1_matriz_trl")
print("✓ Figura 1 generada: Matriz TRL vs Energía")
