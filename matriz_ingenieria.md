# Matriz Comparativa de Ingeniería — Propulsión Interestelar
# Orden: TRL descendente → menor dependencia de física especulativa → cercanía a validación experimental
# Fecha: 2026-05-28

---

## MATRIZ MAESTRA

| # | Concepto | Paper clave | Energía requerida | Principio físico | TRL | Estado físico | Bottleneck principal | Timeline estimado |
|---|---|---|---|---|---|---|---|---|
| 1 | **Navegación autónoma por púlsares (SEXTANT)** | Sheikh 2006 (10.2514/1.13331); NASA SEXTANT 2018 (10.1088/2058-7058/31/2/13) | Mínima (subsistema de navegación) | Timing de púlsares de rayos X | **6-7** | fisica_establecida | Precisión dependiente de fuentes; no es propulsión | Disponible ahora (demostrado en ISS 2018) |
| 2 | **Interstellar Probe (sonda al medio interestelar local)** | McNutt 2022 (10.1016/j.srt.2022.11.014) | Escala SLS/Starship (química) | Propulsión química + gravity assist | **6-7** | fisica_establecida | No llega a otra estrella; solo medio interestelar local (~100-200 AU) | 2030s (misión propuesta) |
| 3 | **VASIMR (prototipo VX-200)** | Díaz 2005 (10.1063/1.1867222); Squire 2010 (10.2514/6.2010-622) | 200 kW (prototipo); GW para interestelar | Plasma RF, Isp 5000-12000 s | **4-5** | fisica_establecida | Requiere fuente de potencia GW en espacio (fisión/fusión no disponible) | Operacional en LEO: 2030s; interestelar: no viable sin fusión |
| 4 | **UHTC (HfC, ZrC, HfB₂) para toberas extremas** | Fahrenholtz 2016 (10.1016/j.scriptamat.2016.10.018); Weng 2019 (10.1016/j.jeurceramsoc.2019.04.050); Binner 2020 (10.1111/jace.17059) | N/A (material) | Cerámicas ultra-alta temperatura, fusión >3000°C | **4-5** | fisica_establecida | Oxidación a alta temperatura; fabricación a gran escala | Disponible ahora para aplicaciones subsónicas; toberas: 2030s |
| 5 | **Superconductores HTS para fusión (ReBCO/YBCO)** | Whyte 2016 (10.1016/j.fusengdes.2016.03.069) | N/A (material) | Imanes toroidales 20 K, 20 T | **4-5** | fisica_establecida | Fabricación de cintas HTS largas; fragilidad mecánica | SPARC/ITER: 2030s; propulsión: 2050+ |
| 6 | **Blindaje pasivo (polietileno/H₂)** | [UNVERIFIED] — sin paper específico para 0.2c | N/A (material) | Bajo Z reduce fragmentación de rayos cósmicos | **3-4** | fisica_establecida | Espesor requerido vs masa; sin datos a 0.1-0.2c | Aplicable ahora (diseños de Marte); validación a 0.2c: 2040+ |
| 7 | **Nanotubos de carbono / grafeno para velas** | Fan 2015 (10.1088/2053-1583/2/2/021002); Hu 2020 (10.1021/acs.nanolett.0c02572) | N/A (material) | Resistencia 130 GPa, módulo 1 TPa, densidad <10 mg/cm³ | **3-4** | fisica_establecida | Fabricación a escala de m² con reflectividad >99.99% | Prototipos laboratorio ahora; velas interestelares: 2040+ |
| 8 | **Vela láser (Breakthrough Starshot)** | Parkin 2018 (10.1016/j.actaastro.2018.08.035) | ~2×10¹⁵ J (100 GW × 10 min) para 1g a 0.2c | Presión de radiación láser sobre vela reflectiva | **2-3** | fisica_establecida | Estabilidad beam-riding; coherencia de array faseado (100 m); frenado en destino; comunicación | Demo orbital: 2040s; Alpha Cen: 2060+ |
| 9 | **Beam-riding estabilizado (metasuperficies)** | Zacny 2017 (10.3847/2041-8213/aa619b); Shen 2019 (10.1021/acsphotonics.9b00484); Cheng 2020 (10.1140/epjp/s13360-020-00542-1) | N/A (subsistema de control) | Metasuperficies difractivas para auto-estabilización | **2-3** | fisica_establecida | Escalado a tamaños de misión; acoplamiento con alta potencia láser | Lab: ahora; integración con Starshot: 2040+ |
| 10 | **Metamateriales análogos de gravedad** | Smolyaninov 2010 (10.1103/PhysRevA.82.023819); Faccio 2010 (10.1140/epjst/e2010-01305-5) | N/A (experimento laboratorio) | Índice de refracción negativo simula espacio-tiempo curvo | **2-3** | fisica_establecida | Análogo, no propulsión real; no escala a ingeniería de transporte | Experimentos ahora; sin ruta a propulsión |
| 11 | **Propulsión nuclear de pulso (Orion)** | Long 2002 (10.2514/2.5969); Winterberg 2015 (10.2514/1.A33146) | ~10²¹ J (bombas de fusión) | Impulso por detonación nuclear externa | **3** | fisica_establecida | Tratado PTBT 1963 prohíbe pruebas; viabilidad política nula | Tecnología base: 1960s; legalmente inviable sin cambio de tratados |
| 12 | **Antimateria (antiprotones) — precursor** | Howe 2000 (10.2514/2.5661); Smith 2005 (10.1063/1.1867171) | ~10²¹ J para 1t a 0.5c (aniquilación) | Aniquilación p+p̄ → piones → empuje | **2-3** | fisica_establecida | Producción a escala ng/año; almacenamiento magnético; costo $6.4M/ng | Misiones precursoras (ng): 2040s; interestelar (g-kg): 2100+ |
| 13 | **Fusión inercial (Daedalus / Icarus)** | Long 2011 (10.1016/j.actaastro.2011.01.010); Ceyssens 2013 (10.1016/j.actaastro.2012.08.010); Ceyssens 2015 (10.1016/j.actaastro.2015.07.032) | ~6×10²¹ J (50000 t DHe³) | ICF con haz de electrones, 250 Hz, DHe³ | **1-2** | fisica_establecida | Fusión DHe³ no demostrada en laboratorio; 50000 t de propelente en órbita | Demostración fusión DHe³: 2050+; misión: 2150+ |
| 14 | **Fisión thrust sail (booster para fusión)** | Ceyssens 2015 (10.1016/j.actaastro.2015.07.032) | Variable (asistido por fisión) | Vela de fisión como booster para motor de fusión | **2** | fisica_establecida | Depende de disponibilidad de motor de fusión funcional | Post-fusión: 2150+ |
| 15 | **Fusión por haz de partículas (Winterberg)** | Winterberg 2009 (10.1016/j.actaastro.2009.01.054) | Variable (fusión-fisión autocatalítica) | Ignición por haz de electrones/iones | **2** | fisica_establecida | Configuración autocatalítica no demostrada | 2050+ |
| 16 | **Ramjet Bussard (incluso híbrido)** | Czerniawski & Niewiadomski 2010 (10.1016/j.actaastro.2009.11.009) | N/A (recolecta H interestelar) | Scoop magnético para H interestelar como propelente | **1** | fisica_establecida | Drag magnético > empuje a velocidades relevantes; conclusión: INVIABLE | Sin timeline (inviable) |
| 17 | **Warp drive — energía positiva (Bobrick-Martire)** | Bobrick & Martire 2021 (10.1088/1361-6382/abdf16) | Escala kg materia ordinaria (teórico) | Taxonomía de warp drives con tensor de energía-momento físico | **1** | especulativa | Requiere densidades de energía no observadas; gravedad modificada | Sin timeline (requiere nueva física) |
| 18 | **Warp drive — solitón plasmático (Lentz)** | Lentz 2021 (arXiv:2106.01073 [UNVERIFIED]) | Escala kg (teórico) | Solitón en Einstein-Maxwell-plasma | **1** | especulativa | Condiciones de plasma no verificadas; estabilidad del solitón | Sin timeline (requiere nueva física) |
| 19 | **Warp drive — Einstein-Cartan (Fell & Heisenberg)** | Fell & Heisenberg 2018 (10.1088/1361-6382/aae326) | No cuantificada | Acoplamiento de espín en Einstein-Cartan permite energía positiva | **1** | especulativa | Einstein-Cartan no verificado experimentalmente | Sin timeline (requiere nueva física) |
| 20 | **Warp drive — Alcubierre original** | Alcubierre 1994 (10.1088/0264-9381/11/5/073) | ~10⁵² J (masa de Júpiter) | Métrica de expansión/contracción del espacio-tiempo | **1** | especulativa | Materia exótica no existe; energía equivalente a masa de Júpiter | Sin timeline (inviable en física conocida) |
| 21 | **Warp drive — Van Den Broeck (energía reducida)** | Van Den Broeck 1999 (10.1088/0264-9381/16/12/314) | ~10⁴⁶ J (pocas masas solares) | Modificación geométrica de la burbuja | **1** | especulativa | Sigue requiriendo materia exótica; energía aún inalcanzable | Sin timeline |
| 22 | **Agujeros de gusano traversables** | Morris & Thorne 1988 (10.1119/1.15620); Visser 1989 (10.1103/PhysRevD.39.3182) | No cuantificada (materia exótica en garganta) | Puente espacio-temporal traversable | **1** | especulativa | Materia exótica; inestabilidad de la garganta; causalidad | Sin timeline (requiere nueva física) |
| 23 | **Energía oscura como propulsión** | González-Díaz 2007 (10.1016/j.physletb.2007.09.041) | No cuantificada (energía fantasma) | Acreción de energía oscura por burbuja warp | **1** | especulativa | Sin evidencia de extracción local de energía oscura | Sin timeline (especulativo) |
| 24 | **Energía de punto cero (ZPE)** | Haisch 1994 (10.1103/PhysRevA.49.678); refutado por Jaekel & Reynaud 1997 (10.1002/andp.19975090505) | No extraíble según consenso | Extracción de energía del vacío cuántico | **1** | especulativa | Consenso: ZPE no es extraíble; tensor de energía-momento del vacío es nulo en RG | Sin timeline (considerado callejón sin salida) |
| 25 | **Sondas Von Neumann (diseño original)** | Freitas 1980 (JBIS, SIN DOI) | ~10¹⁰ kg/sonda | Sonda autorreplicante con ISRU | **1** | especulativa | Fabricación autónoma a escala industrial; IA no existe; replicación 500-2000 años | Sin timeline (requiere AGI + fabricación autónoma) |
| 26 | **Sondas VN microscópicas (nanobots)** | Osmanov 2019 (10.1017/S1473550419000259) | Mínima (0.1 μm) | Nanobots replicables en nubes HII | **1** | especulativa | Solo viable en nubes HII; nanofabricación no demostrada | Sin timeline |
| 27 | **Enjambre Dyson + beam propulsion** | Sandberg 2015 (JBIS, SIN DOI [UNVERIFIED]); Barrow 1998 (libro, SIN DOI) | ~10²⁶ W (Tipo II) | Enjambre Dyson autorreplicante alimentando array láser | **1** | especulativa | Requiere civilización Tipo II; construcción ~100 años post-Tipo I | Post-2200 (requiere civilización Tipo I primero) |
| 28 | **Colonización galáctica (sondas VN + Dyson)** | Armstrong & Sandberg 2013 (10.1016/j.actaastro.2013.04.002); Wiley 2012 (10.1017/S1473550412000419); Bjørk 2007 (10.1017/S1473550407003709) | N/A (escala civilización) | Sondas VN jerárquicas exploran Galaxia en ~10⁷ años | Asume existencia de capacidad VN; no aborda ingeniería | — | Sin timeline (depende de VN + decisión civilizatoria) |

---

## ORDENAMIENTO POR VIABILIDAD INGENIERIL

### Categoría A: Disponible o casi disponible (TRL ≥ 4)
1. Navegación por púlsares (TRL 6-7)
2. Interstellar Probe al medio local (TRL 6-7)
3. VASIMR en LEO (TRL 4-5)
4. Materiales UHTC (TRL 4-5)
5. Superconductores HTS (TRL 4-5)

**Conclusión preliminar**: Ninguno de los conceptos de propulsión interestelar a otras estrellas tiene TRL > 5. Los sistemas con TRL 6-7 son de navegación o exploración del medio interestelar local (<200 AU).

### Categoría B: Factible con ingeniería incremental (TRL 2-3)
1. Vela láser Starshot
2. Beam-riding con metasuperficies
3. Antimateria a escala de nanogramo (misiones precursoras)
4. Propulsión nuclear de pulso (ingeniería viable, legalmente bloqueada)

**Conclusión preliminar**: La vela láser es el concepto con mejor relación factibilidad/ambición. No requiere nueva física. Sus bottlenecks son de ingeniería (materiales, coherencia de array, estabilidad), no de principios físicos.

### Categoría C: Requiere avance fundamental en física (TRL 1)
1. Warp drives (todos los modelos, incluyendo post-Lentz)
2. Agujeros de gusano traversables
3. Energía oscura / ZPE como fuente de propulsión
4. Sondas Von Neumann de escala industrial

**Conclusión preliminar**: Los conceptos de warp drive han evolucionado de "imposible" (Alcubierre 1994) a "posible en principio con física modificada" (Lentz 2021, Bobrick-Martire 2021). Sin embargo, todos requieren condiciones que no se han verificado experimentalmente.

### Categoría D: Conceptualmente refutados o inviables
1. Ramjet Bussard (Czerniawski 2010: drag > empuje)
2. ZPE como fuente de energía (Jaekel & Reynaud 1997)

---

## ANÁLISIS TRANSVERSAL

### Dependencia de física especulativa

| Categoría | Conceptos | % del corpus |
|---|---|---|
| Solo física establecida (RG + QFT estándar) | Vela láser, fusión, antimateria, Orion, VASIMR, materiales | ~60% |
| Requiere gravedad modificada | Warp drives (Einstein-Cartan, Einstein-Maxwell-plasma, f(R,T)) | ~25% |
| Requiere AGI o tecnología post-Singularidad | Sondas VN, Dyson swarm autónomo | ~10% |
| Refutado por física establecida | ZPE, ramjet Bussard | ~5% |

### Bottlenecks por tipo

| Tipo | Conceptos afectados | Severidad |
|---|---|---|
| **Energético** | Todos los de propulsión directa | Crítico: diferencia de 10⁷-10³² entre producción humana actual y requerimientos |
| **Materiales** | Velas láser, toberas de fusión, blindaje | Alto: materiales existen pero no validados a condiciones interestelares |
| **Estabilidad/Control** | Warp drives, velas láser, antimateria | Alto: beam-riding pasivo es prometedor; estabilidad warp es desconocida |
| **Legal/Político** | Orion (PTBT 1963) | Bloqueante: requiere cambio de tratados internacionales |
| **Física fundamental** | Warp drives, wormholes, ZPE | Bloqueante: todos requieren nueva física no verificada |
| **Computacional/AI** | Sondas VN, navegación autónoma | Alto: AGI no existe; autonomía multi-década no demostrada |
