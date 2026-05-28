# Propulsion Interestelar — Paper de Revision Cientifica

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![DOI](https://img.shields.io/badge/DOI-Zenodo--pending-orange)](https://zenodo.org)
[![License](https://img.shields.io/badge/License-CC--BY%204.0-green)](LICENSE)
[![Repo](https://img.shields.io/badge/repo-CienciaEstelar%2Fpropulsion--interestelar-purple)](https://github.com/CienciaEstelar/propulsion-interestelar)
[![Hash](https://img.shields.io/badge/reproducible-SHA256--verified-success)](datos/hash_reproducibilidad.json)

**"De Alcubierre a la Ingenieria: Una Evaluacion Critica de los Conceptos de Propulsion Interestelar (1994–2026)"**

---

## Que es esto

Paper de revision con calidad de publicacion academica que evalua **28 conceptos de propulsion interestelar** a traves de **155 referencias** en 18 bloques tematicos. Desde la metrica de Alcubierre (1994) hasta Breakthrough Starshot (2018), fusion nuclear (Daedalus/Icarus), antimateria, velas laser, y sondas autorreplicantes Von Neumann.

**Target journals**: Acta Astronautica (primario) | Journal of the British Interplanetary Society (secundario)

### Hallazgos principales

| # | Hallazgo | Evidencia |
|---|---|---|
| 1 | **Ningun concepto de propulsion interestelar a otra estrella supera TRL 3** | 28 conceptos evaluados con rubrica TRL adaptada |
| 2 | **La vela laser es el unico camino realista a corto plazo** | E_cin = 1.85e12 J para 1g a 0.2c (~0.09% del consumo diario humano) |
| 3 | **Los warp drives post-2021 NO eliminan la necesidad de nueva fisica** | Reemplazan energia negativa con condiciones igual de inaccesibles |
| 4 | **El error de sincronizacion sin correccion es de ~5e4 AU en Alpha Cen** | Delta_t ~ 1.4e10 ms (CORREGIDO, factor 100x vs version anterior) |
| 5 | **Se requiere emisividad controlada (eps>0.2) para no fundir la vela** | T_eq(eps=0.1) = 3240 K > T_fusion SiC (3100 K) |

---

## Estructura del repositorio

```
propulsion-interestelar/
├── PAPER_INTERESTELAR.md          # Paper completo en espanol
├── derivaciones_paper.ipynb       # Notebook Jupyter: TODAS las derivaciones
├── derivaciones/                  # Paquete Python de calculos reproducibles
│   ├── constantes.py              #   Constantes fisicas CODATA 2022 + IAU 2015
│   ├── cinematica.py              #   Cinematica relativista: gamma, E_cin
│   ├── starshot.py                #   Vela laser: termico, divergencia, costo
│   ├── sincronizacion.py          #   Sincronizacion temporal (CORREGIDO C1)
│   ├── reproducibilidad.py        #   Hash SHA-256 de verificacion global
│   └── __init__.py                #   Indice del paquete
├── figuras/                       # Scripts generadores de figuras
│   ├── generar_figuras.py         #   Script maestro (6 figuras)
│   ├── style_config.py            #   Estilo unificado Matplotlib
│   ├── figura1_matriz_trl.py      #   TRL vs Energia (scatter plot)
│   ├── figura2_evolucion_warp.py  #   Evolucion energetica warp drives
│   ├── figura3_arquitectura.py    #   Diagrama de mision integrada
│   ├── figura4_link_budget.py     #   Presupuesto enlace optico + ruido
│   ├── figura5_sincronizacion.py  #   Sincronizacion relativista
│   └── figura6_gaps_cobertura.py  #   Mapa de cobertura del corpus
├── output/
│   ├── PAPER_INTERESTELAR.pdf     # PDF compilado (18pp, 646KB)
│   └── figuras/                   # Figuras vectoriales (PDF + PNG)
├── literatura_procesada.md        # Corpus original (82 refs, Bloques 1-9)
├── literatura_procesada_v2.md     # Corpus ampliado (97 refs, Bloques 10-18)
├── gaps_identificados.md          # Gaps y contradicciones en la literatura
├── matriz_ingenieria.md           # Matriz comparativa de 28 conceptos
├── sintesis_critica.md            # Respuestas a 6 preguntas clave
├── AUDITORIA_PAPER.md             # Auditoria final con verificacion Crossref
├── compile_paper.py               # Compilador automatico (figuras -> LaTeX -> PDF)
├── calculos_paper.py              # TODOS los calculos en un solo script
├── verify_dois.py                 # Verificacion DOIs contra Crossref API (88.1%)
├── validacion_corpus.py           # Validacion de integridad del corpus
├── requirements.txt               # Dependencias Python
└── .gitignore
```

---

## Reproducibilidad total — Un solo comando

```bash
git clone https://github.com/CienciaEstelar/propulsion-interestelar.git
cd propulsion-interestelar
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Verificar TODOS los calculos (debe producir el hash de referencia)
python -m derivaciones.reproducibilidad

# Generar las 6 figuras
python figuras/generar_figuras.py

# Compilar el PDF (requiere pandoc + LaTeX)
python compile_paper.py
```

**Hash SHA-256 de reproducibilidad**: `e3a783a05c431bec9ffbee25d761a69e30d09df69c278cd7cc327696a00405c3`

Si ejecutas `verificar_todo()` en cualquier maquina, con cualquier SO, el hash DEBE ser identico. Si cambia, constantes o formulas fueron modificadas.

---

## Calculos verificados

| Variable | Valor | Unidad | Paper ref |
|---|---|---|---|
| gamma (v=0.2c) | 1.020621 | — | Seccion 1 |
| E_cin Starshot (1g, 0.2c) | 1.853e12 | J | Seccion 2.3 |
| T_eq vela (eps=0.1, R=99.99%) | 3240 | K | Seccion 4.2 |
| T_eq vela (eps=0.5, R=99.99%) | 2167 | K | Seccion 4.2 |
| E_cin Daedalus (50kt, 0.12c) | 3.271e22 | J | Seccion 2.4 |
| Delta_t sincronizacion | 1.393e10 | ms | Seccion 5.1 |
| E_Alcubierre | 1.706e44 | J | Seccion 2.2 |
| SNR optico (1 MW, 4.37 al) | 18.33 | — | Seccion 5.1 |
| Costo array laser | 1.35e11 | USD | Seccion 4.3 |
| Costo antimateria (1 g) | 6.4e15 | USD | Seccion 2.5 |
| Tiempo colonizacion galactica | 1.2e7 | anos | Seccion 6.1 |

---

## Correcciones aplicadas (post-revision unificada de 5 evaluadores)

| ID | Issue | Severidad | Correccion |
|---|---|---|---|
| C1 | Error sincronizacion (factor ~100) | CRITICA | 1.4e8 -> 1.4e10 ms. Figura 5 rehecha |
| C2 | Referencias sin DOI verificable | CRITICA | Movidas a Anexo A con advertencia |
| C3 | Presupuesto ruido enlace optico | CRITICA | Figura 4 rehecha con fondo+scint+jitter |
| C4 | Energia Daedalus inconsistente | CRITICA | 6e21 -> 3.27e22 J (E_cin total) |
| C5 | Sin analisis termico vela | CRITICA | Anadido T_eq para eps=0.05-0.90 |
| C6 | Sin discusion DEC | CRITICA | Anadida Seccion 3.2 |
| A2 | Sin costo array laser | ALTA | Estimado ~$150B |
| A3 | Sin discusion turbulencia | ALTA | Anadida con alternativa orbital |
| A5 | Sin wall-plug efficiency | ALTA | eta_total = 1.8e-4 calculado |
| M1 | Sin rubrica TRL explicita | MODERADA | Tabla TRL adaptada en Seccion 1.3 |
| M3 | Sin hitos go/no-go | MODERADA | Anadidos en Seccion 8.2 |
| B4 | Comparacion diaria incorrecta | BAJA | 0.01x -> ~0.001x |

---

## Codigo abierto relacionado

| Repositorio | Estrellas | Descripcion |
|---|---|---|
| [WarpFactory](https://github.com/NerdsWithAttitudes/WarpFactory) | 343 | Toolkit numerico de warp drives (MATLAB) |
| [poliastro](https://github.com/poliastro/poliastro) | 1008 | Astrodinamica en Python |
| [einsteinpy](https://github.com/einsteinpy/einsteinpy) | 693 | Relatividad General en Python |
| [OpenXNAV](https://github.com/JHUAPL/OpenXNAV) | 3 | Navegacion por pulsares (JHU/APL) |
| [FlexSailSim](https://github.com/Starshot-Lightsail/FlexSailSim) | 6 | Simulador velas Starshot (Caltech) |
| [MIT-STARLab/Optical-Link-Budget](https://github.com/MIT-STARLab/Optical-Link-Budget) | 25 | Link budget optico (Python/MATLAB) |
| [pykep](https://github.com/esa/pykep) | 411 | Diseno trayectorias interplanetarias (ESA) |
| [PINT](https://github.com/nanograv/PINT) | — | Timing de pulsares (NANOGrav) |

---

## Datasets abiertos utilizados

- [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/) — +5500 exoplanetas confirmados
- [IBEX (NASA/Princeton)](https://ibex.princeton.edu/DataRelease) — Medio interestelar local (LISM)
- [CRaTER (LRO)](http://crater-web.sr.unh.edu/) — Radiacion cosmica galactica
- [SPICE Toolkit (NASA/NAIF)](https://naif.jpl.nasa.gov/naif/toolkit.html) — Efemerides planetarias
- [CDS VizieR](https://vizier.cds.unistra.fr/) — Catalogos astronomicos

---

## Autor

**Juan de Dios Galaz Amengual**

- ORCID: [0009-0007-7474-7560](https://orcid.org/0009-0007-7474-7560)
- GitHub: [CienciaEstelar](https://github.com/CienciaEstelar)
- Email: juan1993@proton.me
- Santiago, Chile

---

## Como citar

```bibtex
@article{galaz2026propulsion,
  title={{De Alcubierre a la Ingenieria: Una Evaluacion Critica
          de los Conceptos de Propulsion Interestelar (1994-2026)}},
  author={Galaz Amengual, Juan D.},
  journal={En preparacion para Acta Astronautica},
  year={2026},
  note={Repositorio: github.com/CienciaEstelar/propulsion-interestelar}
}
```

## Licencia

Paper y scripts de analisis: CC-BY 4.0. El corpus de referencias es de dominio publico (extraido de bases de datos academicas abiertas).
