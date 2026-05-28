#!/usr/bin/env python3
"""Figura 2: Evolución de requerimientos energéticos de warp drives (1994-2025)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from style_config import *
import numpy as np

fig, axes = figura_nueva(ancho=8, alto=5.5)
ax = axes[0]

# Hitos históricos con energía requerida [J] equivalente a kg de materia
hitos = [
    (1994, 1e52, "Alcubierre\n(masa de Júpiter)", "Alcubierre", COLORS["warp"]),
    (1997, 1e52, "Pfenning & Ford\n(desigualdades cuánticas)", "Restricción", COLORS["especulativa"]),
    (1999, 1e46, "Van den Broeck\n(pocas masas solares)", "Optimización", "#F39C12"),
    (2004, 1e46, "Visser et al.\n(condiciones energía)", "Restricción", COLORS["especulativa"]),
    (2018, 1e30, "Fell & Heisenberg\n(Einstein-Cartan)", "Gravedad mod.", "#8E44AD"),
    (2021, 1e15, "Lentz\n(solitón plasma)", "Energía positiva", "#1ABC9C"),
    (2021, 1e12, "Bobrick & Martire\n(taxonomía warp)", "Energía positiva", "#1ABC9C"),
    (2025, 1e35, "Diseños modulares\n(cilindros Gaussianos)", "Modular", "#E67E22"),
]

# Línea de producción humana anual
ax.axhline(PRODUCCION_HUMANA_J_ANUAL, color=COLORS["ingenieria"], linestyle="--",
           linewidth=2, alpha=0.7, zorder=1)
ax.text(2023, PRODUCCION_HUMANA_J_ANUAL * 1.5, "Producción humana anual\n(~1.8×10²⁰ J)",
        fontsize=8, color=COLORS["ingenieria"], fontstyle="italic", ha="center")

# Línea de tendencia (agregar pequeña perturbación a años duplicados)
years = np.array([h[0] for h in hitos])
energies = np.array([h[1] for h in hitos])
# Resolver años duplicados agregando epsilon
years_unique = years.astype(float)
for i in range(1, len(years_unique)):
    if years_unique[i] <= years_unique[i-1]:
        years_unique[i] = years_unique[i-1] + 0.15
# Suavizado para la línea de tendencia
years_smooth = np.linspace(1994, 2025, 100)
log_energies = np.log10(energies)
# Interpolación por segmentos con numpy (evita scipy)
from scipy.interpolate import interp1d
interp = interp1d(years_unique, log_energies, kind="cubic", fill_value="extrapolate")
ax.plot(years_smooth, 10**interp(years_smooth), "-", color=COLORS["text"],
        linewidth=1.5, alpha=0.4, zorder=1)

# Puntos de hitos
sizes = [180, 120, 150, 120, 150, 200, 200, 160]
for (year, energy, label, cat, color), size in zip(hitos, sizes):
    ax.scatter(year, energy, s=size, c=color, edgecolors="black",
               linewidth=0.8, zorder=5, alpha=0.9)
    # Etiquetas alternando arriba/abajo
    offset_y = 0.25 if year % 2 == 0 else -0.35
    va = "bottom" if year % 2 == 0 else "top"
    ax.annotate(label, (year, energy * 10**offset_y),
                fontsize=6.5, ha="center", va=va,
                color=COLORS["text"],
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white",
                         edgecolor=color, alpha=0.8))

ax.set_yscale("log")
ax.set_ylabel("Energía requerida [J]", fontweight="bold")
ax.set_xlabel("Año", fontweight="bold")
ax.set_title("Figura 2: Evolución de los requisitos energéticos\nde métricas warp drive (1994–2025)",
             fontweight="bold", pad=12)
ax.set_xlim(1992, 2027)
ax.set_ylim(1e8, 1e55)

# Escalas numéricas explícitas en el eje Y
from matplotlib.ticker import LogLocator, FuncFormatter
ax.yaxis.set_major_locator(LogLocator(base=10.0, numticks=10))
ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs='all', numticks=100))
import math as _math
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'$10^{{{int(round(_math.log10(y)))}}}$'))

# Líneas de referencia etiquetadas
refs_energia = [
    (1e12, "Energía mundial anual\n(~2025)", COLORS["ingenieria"]),
    (1e20, "Producción humana\nanual", COLORS["ingenieria"]),
    (1e30, "Energía de\nsupernova (1 s)", "#9B59B6"),
    (1e44, "Masa solar\n(~10⁴⁷ J)", COLORS["especulativa"]),
]
for ref_j, etiq, color in refs_energia:
    ax.axhline(ref_j, color=color, linestyle=":", linewidth=1, alpha=0.4)
    ax.text(2026.5, ref_j * 1.5, etiq, fontsize=6, color=color, ha="right", va="bottom", fontstyle="italic")

# Anotaciones de eras
ax.annotate("Era de\nimposibilidad\nfísica", xy=(1998, 1e50), fontsize=9,
            ha="center", color=COLORS["especulativa"], fontweight="bold",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.7))
ax.annotate("Era de\noptimización\nenergética", xy=(2010, 1e50), fontsize=9,
            ha="center", color="#F39C12", fontweight="bold",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.7))
ax.annotate("Era de energía\npositiva", xy=(2022, 1e50), fontsize=9,
            ha="center", color="#1ABC9C", fontweight="bold",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.7))

guardar_figura(fig, "figura2_evolucion_warp")
print("✓ Figura 2 generada: Evolución energética warp drives")
