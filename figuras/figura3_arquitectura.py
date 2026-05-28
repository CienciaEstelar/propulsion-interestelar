#!/usr/bin/env python3
"""Figura 3: Diagrama de arquitectura integrada de misión interestelar.
Versión robusta — sin FancyBboxPatch, usando Rectangle nativo."""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from style_config import *
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle as MplRectangle, FancyArrowPatch
import numpy as np

fig, all_axes = figura_nueva(ancho=10, alto=6.5)
ax = all_axes[0]
ax.set_xlim(0, 14)
ax.set_ylim(0, 8)
ax.axis("off")
ax.set_title("Figura 3: Arquitectura integrada de misión interestelar\n"
             "Aceleración por vela láser + crucero + frenado magnético/eléctrico + comunicación óptica",
             fontweight="bold", fontsize=11, pad=12)

# Paleta para cajas
C_SISTEMA = "#FFF3E0"
C_CRUCERO = "#E3F2FD"
C_FRENADO = "#E8F5E9"
C_DESTINO = "#F3E5F5"
BORDER_SOL = "#F39C12"
BORDER_LASER = COLORS["laser_sail"]
BORDER_FRENADO = COLORS["ingenieria"]
BORDER_DESTINO = "#9B59B6"

def caja(ax, x, y, w, h, facecolor, edgecolor, linewidth=2, alpha=0.75):
    """Dibuja un rectángulo redondeado simulado con líneas gruesas."""
    rect = MplRectangle((x, y), w, h, facecolor=facecolor, edgecolor=edgecolor,
                      linewidth=linewidth, alpha=alpha, zorder=2,
                      joinstyle="round", capstyle="round")
    ax.add_patch(rect)
    return rect

def texto(ax, x, y, txt, size=8, bold=False, color=None, ha="center", va="center"):
    """Añade texto con estilo unificado."""
    kw = {"fontsize": size, "ha": ha, "va": va, "color": color or COLORS["text"]}
    if bold:
        kw["fontweight"] = "bold"
    ax.text(x, y, txt, **kw)

# ═══════════════════════════════════════════════════════════════
# FASE 1: SISTEMA TIERRA (Array láser)
# ═══════════════════════════════════════════════════════════════
caja(ax, 0.3, 2.5, 2.5, 3.0, C_SISTEMA, BORDER_SOL)
texto(ax, 1.55, 5.2, "SISTEMA TIERRA", size=8, bold=True, color="#E67E22")
texto(ax, 1.55, 4.8, "(Array láser 100 GW)", size=7, color="#E67E22")
texto(ax, 1.55, 4.2, "Array faseado 100 m", size=6.5)
texto(ax, 1.55, 3.9, "100 GW optico", size=6.5)
texto(ax, 1.55, 3.6, "Yb:YAG 1064 nm", size=6.5)
texto(ax, 1.55, 3.3, "~10 min aceleracion", size=6.5)

# Flecha de aceleración (estilo simple)
ax.annotate("", xy=(4.5, 4.0), xytext=(2.9, 4.0),
            arrowprops=dict(arrowstyle="->", color=COLORS["laser_sail"],
                           lw=3, alpha=0.8))
# Haz láser (triángulo)
ax.fill_between([2.9, 4.5], [4.3, 4.8], [3.7, 3.2], alpha=0.10, color=COLORS["laser_sail"])
texto(ax, 3.7, 5.1, "Haz laser (~0.2 AU)", size=6, color=COLORS["laser_sail"])

# ═══════════════════════════════════════════════════════════════
# FASE 2: CRUCERO INTERESTELAR
# ═══════════════════════════════════════════════════════════════
caja(ax, 4.8, 2.5, 4.0, 3.0, C_CRUCERO, BORDER_LASER)
texto(ax, 6.8, 5.2, "CRUCERO INTERESTELAR", size=8, bold=True, color=COLORS["laser_sail"])
texto(ax, 6.8, 4.8, "(~22 años a 0.2c)", size=7, color=COLORS["laser_sail"])
texto(ax, 6.8, 4.2, "Vela plegada/separada", size=6.5)
texto(ax, 6.8, 3.9, "Blindaje multicapa SiC", size=6.5)
texto(ax, 6.8, 3.6, "RTG Pu-238 (~120 W)", size=6.5)
texto(ax, 6.8, 3.3, "Navegacion por pulsares", size=6.5)
texto(ax, 6.8, 3.0, "Reloj atomico DSAC", size=6.5)

# Peligros del ISM (caja de alerta)
caja(ax, 7.7, 4.2, 1.0, 1.2, "#FFEBEE", COLORS["especulativa"], linewidth=1.5, alpha=0.85)
texto(ax, 8.2, 4.95, "PELIGROS ISM", size=5.5, bold=True, color=COLORS["especulativa"])
texto(ax, 8.2, 4.6, "Polvo", size=5.5, color=COLORS["especulativa"])
texto(ax, 8.2, 4.4, "Carga elect.", size=5.5, color=COLORS["especulativa"])
texto(ax, 8.2, 4.2, "GCR (4 Sv)", size=5.5, color=COLORS["especulativa"])

# ═══════════════════════════════════════════════════════════════
# FASE 3: FRENADO EN DESTINO
# ═══════════════════════════════════════════════════════════════
caja(ax, 9.2, 2.5, 2.5, 3.0, C_FRENADO, BORDER_FRENADO)
texto(ax, 10.45, 5.2, "FRENADO", size=8, bold=True, color=COLORS["ingenieria"])
texto(ax, 10.45, 4.8, "(~29 años)", size=7, color=COLORS["ingenieria"])
texto(ax, 10.45, 4.2, "Magsail (>0.01c)", size=6.5)
texto(ax, 10.45, 3.9, "Electric sail", size=6.5)
texto(ax, 10.45, 3.6, "(<0.01c)", size=6.5)
texto(ax, 10.45, 3.3, "Presion radiacion", size=6.5)
texto(ax, 10.45, 3.0, "estelar (ajuste)", size=6.5)

# ═══════════════════════════════════════════════════════════════
# FASE 4: ALPHA CENTAURI
# ═══════════════════════════════════════════════════════════════
caja(ax, 12.0, 2.5, 1.8, 3.0, C_DESTINO, BORDER_DESTINO)
texto(ax, 12.9, 5.2, "ALPHA CENTAURI", size=8, bold=True, color=BORDER_DESTINO)
texto(ax, 12.9, 4.8, "(4.37 al)", size=7, color=BORDER_DESTINO)
texto(ax, 12.9, 4.2, "Proxima b", size=6.5)
texto(ax, 12.9, 3.9, "Alpha Cen A/B", size=6.5)
texto(ax, 12.9, 3.6, "Sobrevuelo", size=6.5)
texto(ax, 12.9, 3.3, "cientifico", size=6.5)
texto(ax, 12.9, 3.0, "Retorno datos", size=6.5)

# ═══════════════════════════════════════════════════════════════
# ENLACE DE COMUNICACIÓN
# ═══════════════════════════════════════════════════════════════
x_com = np.array([1.5, 3.5, 6.5, 10.0, 12.5, 6.5, 1.5])
y_com = np.array([2.3, 2.0, 1.7, 1.9, 2.3, 2.5, 2.3])
ax.plot(x_com, y_com, "--", color=COLORS["comunicacion"], linewidth=1.8, alpha=0.6, zorder=1)

# Caja de anotación del enlace
caja(ax, 4.8, 1.1, 4.0, 0.8, "white", COLORS["comunicacion"], linewidth=1.5, alpha=0.9)
texto(ax, 6.8, 1.6, "Enlace optico bidireccional", size=6.5, bold=True, color=COLORS["comunicacion"])
texto(ax, 6.8, 1.35, "1-1000 kbps | ELT 39m | Codigos SCPPM/LDPC", size=6, color=COLORS["comunicacion"])

# ═══════════════════════════════════════════════════════════════
# LÍNEA TEMPORAL
# ═══════════════════════════════════════════════════════════════
ax.arrow(0.2, 0.6, 13.3, 0, head_width=0.10, head_length=0.2,
         fc=COLORS["text"], ec=COLORS["text"], linewidth=1.5, zorder=5)
for x_pos, label in [(0.2, "t=0"), (4.5, "~10 min"),
                       (6.8, "~22 años"), (10.5, "~29 años"),
                       (13.0, "t~51 años")]:
    texto(ax, x_pos, 0.35, label, size=5.5, color=COLORS["text"])

# ═══════════════════════════════════════════════════════════════
# LEYENDA
# ═══════════════════════════════════════════════════════════════
leyenda_y = 0.05
elementos = [
    (BORDER_LASER, "Propulsion (vela laser)"),
    (COLORS["comunicacion"], "Comunicacion optica"),
    (COLORS["especulativa"], "Blindaje / ISM"),
    (BORDER_FRENADO, "Frenado (magsail+E-sail)"),
    (BORDER_SOL, "Energia (RTG/fision)"),
]
w_leyenda = 2.5
for i, (color, label) in enumerate(elementos):
    x0 = 0.3 + i * w_leyenda
    ax.add_patch(MplRectangle((x0, leyenda_y), 0.25, 0.12,
                 facecolor=color, edgecolor="black", linewidth=0.5))
    texto(ax, x0 + 0.35, leyenda_y + 0.06, label, size=5.5, ha="left", va="center")

guardar_figura(fig, "figura3_arquitectura_mision")
print("✓ Figura 3 generada: Arquitectura integrada de misión interestelar")
