# Configuración de estilo unificado para figuras del paper
# Paper: "De Alcubierre a la Ingeniería"
# Target: Acta Astronautica / JBIS

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# ── Paleta de colores científicamente legible ──
COLORS = {
    "establecida": "#2166AC",     # Azul profundo - física establecida
    "especulativa": "#B2182B",    # Rojo - especulativa
    "ingenieria": "#4DAF4A",      # Verde - ingeniería
    "desconocida": "#999999",     # Gris - desconocido
    "warp": "#D73027",            # Rojo brillante - warp drives
    "laser_sail": "#4575B4",      # Azul medio - velas láser
    "fusion": "#FDAE61",          # Naranja - fusión
    "antimateria": "#9B59B6",     # Púrpura - antimateria
    "vn_probe": "#1ABC9C",        # Turquesa - sondas VN
    "comunicacion": "#2ECC71",    # Verde brillante - comunicación
    "blindaje": "#E74C3C",        # Rojo coral - blindaje
    "frenado": "#F39C12",         # Ámbar - frenado
    "energia": "#E67E22",         # Naranja oscuro - energía
    "grid": "#E0E0E0",            # Gris claro - grillas
    "text": "#333333",            # Gris oscuro - texto
}

# ── Configuración global Matplotlib ──
def setup_style():
    """Aplica el estilo unificado a todas las figuras."""
    plt.rcParams.update({
        # Tipografía LaTeX
        "text.usetex": False,  # False para compatibilidad sin LaTeX instalado
        "font.family": "serif",
        "font.serif": ["DejaVu Serif", "Times New Roman", "Computer Modern Roman"],
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "legend.fontsize": 8,
        # Dimensiones de figura (Acta Astronautica: ~19cm ancho columna)
        "figure.figsize": (7.5, 5.0),
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.05,
        # Estilo de ejes
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.3,
        "grid.color": COLORS["grid"],
        "axes.facecolor": "white",
        "figure.facecolor": "white",
        # Líneas y marcadores
        "lines.linewidth": 1.5,
        "lines.markersize": 6,
        "lines.markeredgewidth": 0.5,
        # Leyenda
        "legend.frameon": True,
        "legend.framealpha": 0.9,
        "legend.edgecolor": COLORS["grid"],
        "legend.fancybox": False,
    })


def figura_nueva(ancho=7.5, alto=5.0, nrows=1, ncols=1):
    """Crea una figura nueva con el estilo unificado.

    Args:
        ancho: Ancho en pulgadas (default 7.5 = ~19cm)
        alto: Alto en pulgadas
        nrows, ncols: Subplot grid

    Returns:
        fig, axes
    """
    setup_style()
    fig, axes = plt.subplots(nrows, ncols, figsize=(ancho, alto))
    if nrows == 1 and ncols == 1:
        axes = [axes]
    return fig, axes


def guardar_figura(fig, nombre, formatos=("pdf", "png")):
    """Guarda la figura en formatos vectorial (PDF) y raster (PNG).

    Args:
        fig: matplotlib Figure
        nombre: Nombre base del archivo (sin extensión)
        formatos: Tuple de formatos de salida
    """
    import os
    outdir = os.path.join(os.path.dirname(__file__), "..", "output", "figuras")
    os.makedirs(outdir, exist_ok=True)
    for fmt in formatos:
        path = os.path.join(outdir, f"{nombre}.{fmt}")
        fig.savefig(path, format=fmt, bbox_inches="tight", pad_inches=0.05)
        print(f"  → {path}")
    plt.close(fig)


def etiquetar_barras(ax, etiquetas, rotacion=45):
    """Rota etiquetas del eje X para legibilidad."""
    ax.set_xticklabels(etiquetas, rotation=rotacion, ha="right", fontsize=8)


# ── Constantes físicas ──
C = 299792.458           # Velocidad de la luz [km/s]
AU = 149597870.7         # Unidad Astronómica [km]
PC = 3.085677581e13      # Pársec [km]
LY = 9.460730472e12      # Año luz [km]
YR_TO_S = 31557600       # Año juliano [s]
G = 6.67430e-20          # Constante gravitacional [km³/(kg·s²)]
M_SOL = 1.98847e30       # Masa solar [kg]
PRODUCCION_HUMANA_J_ANUAL = 1.8e20  # Producción energética humana anual [J]

print("✓ style_config.py cargado — estilos unificados listos.")
