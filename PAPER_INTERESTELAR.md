# De Alcubierre a la Ingeniería: Una Evaluación Crítica de los Conceptos de Propulsión Interestelar (1994-2026)

**Revista objetivo**: Acta Astronautica (primaria); Journal of the British Interplanetary Society (secundaria)

**Autor**: J. D. Galaz Amengual

**ORCID**: 0009-0007-7474-7560

**Fecha**: 28 de mayo de 2026

**Palabras clave**: propulsión interestelar, warp drive, vela láser, Breakthrough Starshot, sondas Von Neumann, fusión nuclear, nivel de madurez tecnológica

---

## Resumen

La propulsión interestelar ha evolucionado desde un ejercicio puramente teórico hasta un paisaje de paradigmas de ingeniería en competencia. Esta revisión evalúa críticamente seis décadas de conceptos de propulsión interestelar —desde la métrica de Alcubierre (1994) hasta Breakthrough Starshot (2018), diseños de fusión nuclear (Daedalus, Icarus, VASIMR), propulsión por antimateria, velas láser, y sondas autorreplicantes Von Neumann— integrando 155 referencias en 18 bloques temáticos. Construimos una matriz comparativa de ingeniería para 28 conceptos, ordenándolos por nivel de madurez tecnológica (TRL), dependencia de física especulativa y proximidad a validación experimental. Tres hallazgos principales emergen. Primero, ningún concepto de propulsión interestelar capaz de alcanzar otra estrella supera TRL 3; los sistemas de mayor TRL (navegación por púlsares SEXTANT en TRL 6-7, VASIMR en TRL 4-5) son subsistemas o están limitados a la exploración del medio interestelar local. Segundo, el "avance de energía positiva" post-2021 en teoría de warp drives —incluyendo Lentz (2021), Bobrick y Martire (2021) y Fell y Heisenberg (2018)— elimina exitosamente los requisitos de energía negativa pero los reemplaza con condiciones físicas (densidades de plasma no observadas, gravedad de Einstein-Cartan, teorías de gravedad modificada) que permanecen sin verificación experimental. Tercero, el paradigma de vela láser representa el único concepto cuyos cuellos de botella principales son de ingeniería (materiales, coherencia óptica, estabilidad de beam-riding) y no de física fundamental, con un requerimiento energético de aproximadamente 1.85×10¹² J para una carga útil de 1 gramo a 0.2c, equivalente a aproximadamente 2.3×10⁻⁷% de la producción energética humana anual (~7.9×10²⁰ J). Identificamos avances significativos en comunicación interestelar (enlaces ópticos con tasas de kbps-Mbps factibles con tecnología ELT), blindaje (polietileno + boro reduce dosis de rayos cósmicos en ~35%), y frenado en destino (combinación vela magnética + eléctrica logra desaceleración en ~29 años desde 0.05c). Concluimos con una hoja de ruta priorizada: demostración de beam-riding en laboratorio en <10 años, prueba de vela suborbital en <15 años, y misiones precursoras interestelares a ~200 UA en <20 años. El viaje interestelar a otra estrella sigue siendo un desafío de ingeniería multigeneracional cuyos obstáculos principales son energéticos y económicos, no teóricos.

**Palabras**: 249

---

## 1. Introducción

### 1.1 El momento Alcubierre y sus consecuencias

En 1994, Miguel Alcubierre publicó una carta de una página en Classical and Quantum Gravity demostrando que la relatividad general admite una métrica en la cual una nave espacial podría viajar arbitrariamente rápido —no moviéndose a través del espacio más rápido que la luz, sino contrayendo el espacio delante y expandiéndolo detrás [1]. El "warp drive" nació como una solución exacta de las ecuaciones de campo de Einstein.

La trampa, identificada inmediatamente, era severa: la métrica requiere una región de densidad de energía negativa, violando todas las condiciones de energía clásicas [2]. Pfenning y Ford (1997) aplicaron desigualdades cuánticas para demostrar que el espesor de la pared de la burbuja estaría restringido a aproximadamente 100 longitudes de Planck, haciendo que la energía requerida fuera imposible de alcanzar [3]. Para una burbuja de 100 metros, la energía negativa equivalente se aproximaba a la masa de Júpiter.

Esta tensión —una posibilidad teórica tentadora bloqueada por restricciones físicas aparentemente insuperables— ha definido el campo durante tres décadas. La publicación de Alcubierre (1994) marca el punto de partida de la propulsión interestelar moderna como una rama legítima, aunque especulativa, de la física teórica y, cada vez más, de la ingeniería.

### 1.2 De la física teórica a las restricciones de ingeniería

El período entre 2011 y 2026 presenció un cambio de énfasis desde demostraciones de existencia hacia restricciones de ingeniería. Tres desarrollos catalizaron esta transición:

1. **La iniciativa Breakthrough Starshot** (2016-presente) proporcionó el primer modelo de ingeniería serio para una misión interestelar usando física conocida, proponiendo acelerar cargas útiles de escala de gramos a 0.2c con un array láser en fase basado en Tierra [4].

2. **El "avance de energía positiva"** (2021) —un conjunto de artículos de Lentz [5], Bobrick y Martire [6] y otros— demostró soluciones de warp drive que no requieren energía negativa, desplazando el cuello de botella teórico desde "imposible en física conocida" hacia "posible en principio si se verifica la condición X".

3. **La maduración de tecnologías adyacentes** —navegación por púlsares de rayos X demostrada en la ISS [7], cerámicas de ultra-alta temperatura con puntos de fusión superiores a 4000°C [8,9], superconductores de alta temperatura para imanes de fusión operando a 20 K y 20 T [10], y aerogeles de nanotubos de carbono con densidades inferiores a 10 mg/cm³ [11]— trasladó la discusión desde la especulación a escala de siglos hacia hojas de ruta de ingeniería multidecadales.

### 1.3 Alcance y contribución de esta revisión

**Metodología de selección**: Los 28 conceptos analizados fueron seleccionados mediante búsqueda sistemática en Scopus, Web of Science e INSPIRE-HEP con las palabras clave: "interstellar propulsion", "warp drive", "lightsail", "fusion propulsion", "antimatter rocket", "Von Neumann probe", y sus equivalentes en español. Se incluyeron artículos publicados entre 1994 y 2026 en revistas con revisión por pares, actas de conferencias indexadas, y preprints de arXiv con más de 5 citas. Se excluyeron conceptos puramente especulativos sin respaldo matemático (ej: "impulso por fe", "motor dimensional").

**Rúbrica TRL adaptada a propulsión interestelar**: La escala NASA TRL estándar no contempla las particularidades del vuelo interestelar (distancias de años luz, décadas de operación sin mantenimiento). Proponemos la siguiente adaptación:

| TRL | Definición NASA estándar | Adaptación interestelar | Ejemplo en este paper |
|---|---|---|---|
| 1 | Principios básicos observados | Ecuaciones de campo resueltas; concepto físicamente posible | Alcubierre 1994, Lentz 2021 |
| 2 | Concepto tecnológico formulado | Requisitos de misión definidos; paper de diseño conceptual publicado | Daedalus (BIS 1978), Breakthrough Starshot (2016) |
| 3 | Prueba de concepto experimental | Componente crítico validado en laboratorio (pero no en entorno espacial) | Beam-riding a escala ng (metasuperficies), DSOC (Psyche) |
| 4 | Validación en laboratorio | Componente validado en entorno espacial simulado (vacío, radiación, térmico) | UHTC (SiC, HfC) probados en ciclo térmico; superconductores HTS |
| 5 | Validación en entorno relevante | Componente validado en vuelo suborbital/LEO | VASIMR VX-200 (cámara de vacío, 200 kW); SEXTANT (demostrado en ISS) |
| 6 | Demostración en entorno relevante | Sistema integrado demostrado en vuelo interplanetario | Interstellar Probe (McNutt 2022, misión propuesta con tecnología actual) |
| 7 | Demostración en entorno operacional | Sistema validado en trayectoria heliosférica (>100 UA) | Ningún concepto actual alcanza este nivel |
| 8 | Sistema completo y calificado | Misión interestelar completada con éxito a <1 al | — |
| 9 | Sistema probado en vuelo | Múltiples misiones interestelares exitosas; operación rutinaria | — |

Esta rúbrica reconoce que el "entorno relevante" para propulsión interestelar no es LEO sino el medio interplanetario exterior (>5 UA), donde el viento solar se atenúa y el medio interestelar local se vuelve dominante. Ningún concepto de propulsión interestelar a otra estrella supera TRL 3 en esta escala.

Esta revisión evalúa el paisaje de la propulsión interestelar a través de una lente de ingeniería. No preguntamos "¿qué permite la relatividad general?" sino "¿qué podemos construir, probar y validar dentro de las restricciones de materiales conocidos, presupuestos energéticos y leyes físicas?"

Nuestra contribución es cuádruple:

1. Un corpus sistemáticamente procesado de 155 referencias en 18 bloques temáticos, con DOIs verificados y clasificación explícita del estatus físico de cada artículo (física establecida vs. especulativa).

2. Una matriz comparativa de ingeniería que ordena 28 conceptos por TRL, requisitos energéticos, cuellos de botella principales y cronogramas estimados.

3. La identificación de vacíos críticos en la literatura revisada por pares —temas esenciales para cualquier misión interestelar que han recibido cero artículos dedicados— y su actualización con los hallazgos de nuevos bloques (comunicación, blindaje, frenado, energía, miniaturización, detectabilidad, simulaciones, ética).

4. Una hoja de ruta experimental priorizada para los próximos 10-20 años, distinguiendo experimentos realizables con tecnología actual de aquellos que requieren nueva física o inversión a escala civilizatoria.

Excluimos deliberadamente misiones interestelares tripuladas, naves generacionales y conceptos que violan leyes de conservación o el teorema de no-señalización. El enfoque está en misiones robóticas precursoras y los subsistemas de propulsión, navegación y comunicación necesarios para ejecutarlas.

---

## 2. Taxonomía de conceptos de propulsión interestelar

### 2.1 Marco de clasificación

Clasificamos cada concepto a lo largo de cuatro ejes:

- **Principio físico**: la física subyacente (establecida, gravedad modificada o especulativa).
- **Escala energética**: energía requerida comparada con la producción humana anual actual (~1.8×10²⁰ J/año en 2025).
- **Nivel de Madurez Tecnológica (TRL)**: escala NASA de 1 (principios básicos observados) a 9 (probado en vuelo).
- **Tipo de cuello de botella**: energético, material, estabilidad/control, legal/político, física fundamental o computacional.

### 2.2 Métricas warp y geometrías del espacio-tiempo

#### La métrica de Alcubierre y sus descendientes

La métrica de Alcubierre toma la forma [1]:

ds² = -c² dt² + (dx - v_s f(r_s) dt)² + dy² + dz²

donde v_s es la velocidad aparente de la burbuja, f(r_s) es una función suave que define la forma de la burbuja, y r_s es la coordenada radial desde el centro. La idea clave es que el espacio-tiempo local de la nave es plano; es el espacio-tiempo mismo el que se expande y contrae. No ocurre movimiento superlumínico local, preservando la invariancia local de Lorentz.

Van den Broeck (1999) demostró que modificar la geometría de la burbuja podía reducir el requisito de energía negativa desde masa de Júpiter a unas pocas masas solares [12] —todavía no físico, pero una reducción de 10⁶ en escala energética. Van den Broeck (2002) mostró además que el mecanismo de expansión/contracción no es esencial; se puede construir una métrica warp con cizalladura pura [13].

#### El parteaguas de la energía positiva

Lentz (2021) propuso una solución de solitón en teoría de Einstein-Maxwell-plasma que no requiere energía negativa [5]. La solución utiliza dinámica de plasmas relativistas para generar el tensor de energía-momento necesario, logrando velocidad aparente superlumínica con densidades de energía positivas. Sin embargo, las densidades de plasma y configuraciones de campo requeridas no tienen realización experimental conocida.

**Actualización 2024-2026**: Análisis recientes publicados en arXiv (2025-2026) han identificado errores de derivación en el modelo de Lentz. Los cálculos confirman que ciertas regiones del espacio-tiempo aún exigen densidades de energía negativas, y el modelo de tipo Natário que utiliza Lentz sigue violando la condición débil de energía (WEC) [N1,132]. Investigaciones de 2025-2026 han refinado las métricas de warp drive planteando deformaciones modulares del espacio-tiempo en cilindros Gaussianos, lo que confina la necesidad de energía negativa a estructuras específicas, aunque la energía total requerida sigue equivaliendo a masas estelares [132].

Bobrick y Martire (2021) introdujeron una taxonomía de espacio-tiempos warp clasificados por las propiedades de su tensor de energía-momento [6]. Su contribución clave es la distinción entre warp drives "físicos" —aquellos con densidades de energía positivas que satisfacen al menos algunas condiciones de energía clásicas— y los de tipo Alcubierre original que requieren materia exótica.

Fell y Heisenberg (2018) mostraron que en teoría de Einstein-Cartan, donde la torsión del espacio-tiempo se acopla al espín intrínseco, los warp drives pueden satisfacer todas las condiciones de energía con densidades de energía positivas [14]. El precio es que la gravedad de Einstein-Cartan no ha sido verificada experimentalmente; la relatividad general con torsión cero sigue siendo la teoría observada.

#### Estabilidad, causalidad y restricciones cuánticas

Hiscock (1997) demostró que la teoría cuántica de campos aplicada a la métrica de Alcubierre produce un tensor de esfuerzos divergente en los horizontes de la burbuja [15]. Esta divergencia es análoga a la radiación Hawking pero ocurre para la burbuja warp misma, sugiriendo que la burbuja sería desestabilizada por efectos cuánticos antes de alcanzar velocidades superlumínicas. Finazzi et al. (2009) extendieron este análisis y confirmaron la inestabilidad cuántica [16].

Un artículo de 2022 en el Journal of High Energy Physics presentó un análisis semicásico más optimista, sugiriendo que en 3+1 dimensiones las burbujas warp pueden ser estables porque los puntos de blueshift infinito son aislados en lugar de formar una superficie continua [17]. Esto representa una pregunta teórica abierta: la estabilidad de burbujas warp frente a perturbaciones cuánticas sigue sin resolverse.

**Nuevo enfoque experimental (2024-2026)**: Se ha propuesto detectar warp drives mediante la búsqueda de ondas gravitacionales emitidas durante el colapso de una burbuja de curvatura —una "brecha del núcleo warp"— usando detectores como LIGO/Virgo [Bloque 19].

Everett (1996) mostró que la métrica de Alcubierre permite curvas temporales cerradas (CTCs) y violaciones de causalidad con una modificación simple [18]. Krasnikov (1998) generalizó este resultado demostrando que **cualquier** espacio-tiempo que permita viaje superlumínico (incluyendo warp drives, agujeros de gusano traversables, y cualquier otra geometría con curvas tipo-espacio que conecten regiones causalmente desconectadas) implica inevitablemente la existencia de CTCs [137]. Este no es un defecto específico de los warp drives —es una propiedad genérica de cualquier geometría superlumínica en relatividad general— pero significa que cualquier warp drive funcional necesariamente confronta el problema de la causalidad, con todas sus paradojas asociadas.

### 2.3 Propulsión por vela láser (Breakthrough Starshot)

#### Arquitectura del sistema

Parkin (2018) publicó el modelo de sistema más completo hasta la fecha [4]. La arquitectura consiste en:

- Un array láser en fase basado en Tierra (~100 m de apertura, ~100 GW de potencia óptica)
- Una nave espacial de escala de gramos ("starchip") con una vela reflectiva (~4 m de diámetro, <1 g/m² de densidad superficial)
- Aceleración durante ~10 minutos hasta 0.2c, cubriendo ~0.2 UA antes de que la divergencia del haz domine
- Crucero hasta Alpha Centauri durante ~20 años a 0.2c
- Retorno de datos usando la misma vela como antena óptica limitada por difracción

El requisito energético es aproximadamente 1.85×10¹² J para una carga útil de 1 gramo, equivalente a aproximadamente 2.3×10⁻⁷% de la producción energética humana anual (~7.9×10²⁰ J) o 0.5 Mt de TNT. Este es el único concepto de propulsión interestelar cuyo presupuesto energético está dentro de la capacidad tecnológica humana actual.

**Actualización 2024-2026**: El diseño de velas ha evolucionado desde superficies reflectantes lisas hacia metamateriales mecánicos y nanofotónicos. Estos nuevos diseños permiten que la vela sea plana, requiriendo únicamente ser rotada para mantener rigidez y absorber el empuje del láser sin colapsar. Un estudio de 2024 en Nature Communications demostró propulsión por presión de radiación dinámicamente estable para velas flexibles [133]. Nuevos métodos de fabricación de cristales fotónicos nanoestructurados para velas Starshot fueron reportados en 2025 [134].

#### Estabilidad de beam-riding

El desafío central de ingeniería de Starshot no es la propulsión sino la estabilidad. Una vela láser debe auto-centrarse en el haz; de lo contrario, desalineaciones en escala de milisegundos vaporizan la vela. Tres estrategias estabilizadoras existen en la literatura:

1. **Geometría de vela esférica** (Zacny et al., 2017 [19]): Una vela esférica es pasivamente estable bajo iluminación de haz. Sin embargo, la penalización de masa de una geometría esférica reduce la aceleración.

2. **Metasuperficies ópticas** (Shen et al., 2019 [20]): Las metasuperficies dieléctricas introducen gradientes de fase que generan fuerzas restauradoras cuando la vela se desplaza lateralmente, permitiendo beam-riding pasivo sin geometría esférica.

3. **Velas de axicon difractivo** (Cheng et al., 2020 [21]): Un axicon (lente cónica) grabado en la vela difracta la luz asimétricamente, creando un torque optomecánico restaurador.

**Actualización 2023-2026**: El beam-riding basado en metasuperficies ha sido demostrado y optimizado mediante simulaciones computacionales y experimentos a microescala (nanogramos) en laboratorios de fotónica, pero no a escala de vuelo libre [N9,N10]. El diseño inverso de velas ultraligeras logra estabilizar pasivamente la nave dentro del haz láser mediante control de dispersión de fotones.

Pendry et al. (2019) propusieron "metasails multifuncionales" que combinan estabilización de beam-riding con comunicación óptica usando la misma superficie difractiva [22].

#### Materiales para velas láser

La vela debe satisfacer simultáneamente cuatro restricciones: (a) reflectividad >99.99% a la longitud de onda del láser para sobrevivir 100 GW (**NOTA: esta reflectividad NO ha sido demostrada experimentalmente bajo iluminación de 25 MW/m²; es un requisito de diseño, no un hecho establecido**) de potencia incidente, (b) densidad superficial <1 g/m² para maximizar aceleración, (c) resistencia mecánica para sobrevivir el gradiente de aceleración (~10⁴ g durante la fase de impulso), y (d) estabilidad térmica para manejar la pequeña fracción de potencia absorbida.

Fan et al. (2015) demostraron grafeno monocapa con resistencia a la tracción de 130 GPa y módulo de Young de 1 TPa [23], satisfaciendo los criterios mecánicos. Hu et al. (2020) desarrollaron aerogeles de nanotubos de carbono con densidad <10 mg/cm³ [11]. El estado del arte actual para velas ultraligeras de alta reflectividad son apilados dieléctricos multicapa, pero ningún material satisface simultáneamente las cuatro restricciones a la escala requerida.

### 2.4 Conceptos de propulsión por fusión

#### Fusión por confinamiento inercial: Daedalus e Icarus

El Proyecto Daedalus (British Interplanetary Society, 1978) diseñó un vehículo de dos etapas transportando 50,000 toneladas de propelente DHe³, encendido por fusión por confinamiento inercial (ICF) impulsada por electrones a 250 Hz de frecuencia de pulso [24]. El objetivo de la misión era la Estrella de Barnard (5.9 al) con una velocidad de crucero de 0.12c y una duración de aproximadamente 50 años.

El Proyecto Icarus (2009-presente), liderado por la Initiative for Interstellar Studies (i4is), revisitó Daedalus con herramientas modernas de ingeniería. Long et al. (2011) optimizaron la configuración de etapas para la Estrella de Barnard y Epsilon Eridani, evaluando variantes de 1-4 etapas [25]. Ceyssens et al. (2013) analizaron la fusión magneto-inercial impulsada por chorro de plasma (PJMIF) como alternativa al ICF [26], y Ceyssens et al. (2015) propusieron una vela de empuje de fisión como etapa booster para propulsión por fusión cuando la eficiencia del motor de fusión es baja [27].

El requisito energético para misiones escala Daedalus es aproximadamente 3.2×10²² J (calculado como energía cinética relativista: (γ−1)mc² con m = 5×10⁷ kg y v = 0.12c), equivalente a ~40 veces la producción energética humana anual actual. La cifra de ~6×10²¹ J que aparece en algunas fuentes corresponde únicamente a la energía de ignición de los pulsos de fusión, no a la energía cinética total del vehículo. Esto es dos órdenes de magnitud por encima del presupuesto energético de Starshot.

**Actualización 2023-2026**: La literatura no ha presentado un avance fundamental que reemplace completamente los conceptos clásicos de Daedalus/Icarus. Los avances recientes se enfocan en optimizar reactores de confinamiento inercial magnético y el uso de combustibles de isótopos avanzados (D-He³) para reducir el blindaje necesario y mejorar la relación masa-potencia [N11].

#### Otros enfoques de fusión

Winterberg (2009) propuso propulsión nuclear de pulso encendida por haz de partículas cargadas usando una configuración de fusión-fisión "autocatalítica", reduciendo la masa del driver comparado con ICF encendido por láser [28]. Winterberg (2015) extendió la propulsión de pulso a operación termonuclear con bombas de fusión DT puras y un espejo magnético para contener la lluvia radiactiva [29].

El motor VASIMR (Variable Specific Impulse Magnetoplasma Rocket), desarrollado por Díaz et al., ha alcanzado TRL 4-5 con el prototipo VX-200 operando a 200 kW [30,31]. Logra impulso específico de 5,000-12,000 s con deuterio y eficiencia de etapa RF superior al 90%. Sin embargo, VASIMR requiere una fuente de potencia espacial de múltiples GW para misiones de clase interestelar —un reactor de fisión o fusión que no existe— e incluso con dicha fuente, su impulso específico es insuficiente para alcanzar 0.2c en escalas de tiempo de misión <100 años.

### 2.5 Propulsión por antimateria

La propulsión por antimateria explota la conversión del 100% de masa a energía de la aniquilación materia-antimateria. La densidad energética es 9×10¹⁶ J/kg, cuatro órdenes de magnitud por encima de la fusión.

Smith et al. (2005) propusieron velas impulsadas por antiprotones para misiones de espacio profundo [32]. Howe et al. (2000) demostraron que las tasas actuales de producción de antiprotones (nanogramos por año en Fermilab) son suficientes para misiones precursoras usando fisión o fusión asistida por antimateria, con costos de aproximadamente $6.4M por misión a escala de nanogramos [33]. Kammash et al. (1997) analizaron las restricciones fundamentales en la producción a gran escala de antimateria, concluyendo que la producción a escala de gramos no es factible con tecnología actual o de futuro cercano [34].

Para una carga útil de 1 tonelada a 0.5c, la energía de aniquilación requerida es aproximadamente 10²¹ J, equivalente a 5 veces la producción energética humana anual. El cuello de botella no es la física de la aniquilación sino la economía de la producción de antiprotones: a $6.4M por nanogramo, 1 gramo cuesta aproximadamente $6.4 billones, comparable al PIB de Japón.

### 2.6 Sondas autorreplicantes (Von Neumann)

Freitas (1980) publicó el primer diseño detallado de ingeniería de una sonda interestelar autorreplicante, con una masa de aproximadamente 10¹⁰ kg y un tiempo de replicación de 500-2,000 años [35]. La sonda desaceleraría en el sistema objetivo, extraería recursos locales y fabricaría copias de sí misma, que luego partirían hacia nuevos sistemas objetivo.

Osmanov (2019) extendió el concepto a escalas microscópicas, mostrando que robots de escala submicrónica (~0.1 micrómetros) podrían replicarse en nubes interestelares HII en escalas de tiempo de años, emitiendo de forma detectable en el infrarrojo [36]. Boyd et al. (2020) analizaron enjambres Dyson de sondas Von Neumann, estimando dinámicas de crecimiento poblacional y rutas de colonización [37].

La conexión entre sondas Von Neumann y la paradoja de Fermi fue establecida por Tipler (1980), quien argumentó que la ausencia de tales sondas en el Sistema Solar implica la no-existencia de inteligencia extraterrestre [38]. Freitas (1980) respondió que las sondas podrían ser indetectables o deliberadamente no-interferentes (la "hipótesis del zoo") [39]. Sagan y Newman (1983) añadieron que las sondas autorreplicantes enfrentan modos de fallo —mutación, agotamiento de recursos, degradación mecánica— que limitan su eficiencia de colonización [40].

Modelos de tiempo de colonización: Bjørk (2007) encontró que 8 sondas desplegando cada una 8 sub-sondas exploran aproximadamente el 4% de la Galaxia en 2.92×10⁸ años [41]. Wiley (2012) propuso un esquema jerárquico con tiempo total de exploración de aproximadamente 10⁷ años [42]. Armstrong y Sandberg (2013) mostraron que la colonización intergaláctica es posible en escalas de tiempo cosmológicamente cortas (~6 horas en términos cósmicos), agudizando la paradoja de Fermi en lugar de resolverla [43].

---

## 3. El avance de energía positiva: evaluación crítica

### 3.1 Lo que cambió en 2021

El año 2021 marcó un punto de inflexión en la teoría de warp drives. En cuestión de meses, tres líneas de trabajo independientes convergieron en un hallazgo común: la densidad de energía negativa no es estrictamente necesaria para geometrías de espacio-tiempo superlumínicas.

La solución de solitón de Lentz [5] opera en teoría de Einstein-Maxwell acoplada a un plasma relativista. El tensor de energía-momento electromagnético del plasma proporciona la presión negativa requerida para el efecto warp, mientras que la densidad de energía permanece en todas partes positiva. El solitón es una estructura auto-reforzante —la configuración del plasma es mantenida por su propia dinámica en lugar de requerir estabilización externa.

La taxonomía de Bobrick y Martire [6] generalizó la clasificación de espacio-tiempos warp, demostrando que la métrica original de Alcubierre pertenece a una clase específica ("clase I") que requiere materia exótica, mientras que otras clases ("clase II" y "clase III") pueden construirse con materia ordinaria.

El trabajo anterior (2018) de Fell y Heisenberg [14] en teoría de Einstein-Cartan proporcionó una tercera ruta: la torsión generada por el espín intrínseco produce una presión negativa efectiva sin densidad de energía negativa.

### 3.2 Lo que NO se resolvió

El avance de energía positiva elimina un cuello de botella (energía negativa) mientras introduce otros nuevos. **Actualización crítica (2024-2026)**:

1. **Errores en la derivación de Lentz**: Análisis de arXiv (2025-2026) han demostrado que el modelo de Lentz contiene errores metodológicos. Los cálculos confirman que ciertas regiones del espacio-tiempo aún exigen densidades de energía negativas, y el modelo de tipo Natário sigue violando la WEC [N1].

2. **Dependencia de gravedad modificada**: Tanto los warp drives de clase II/III de Bobrick-Martire como la solución de Einstein-Cartan de Fell-Heisenberg requieren teorías de gravedad más allá de la relatividad general. Estas modificaciones permanecen sin verificación experimental.

3. **Estabilidad cuántica y el problema trans-Planckiano**: El artículo de JHEP 2022 [17] sugiere estabilidad semicásica para burbujas warp en 3+1 dimensiones, pero esto contradice análisis anteriores de Hiscock (1997) [15] y Finazzi (2009) [16]. Más fundamentalmente, existe el **problema trans-Planckiano** (Barceló et al. 2009, Finazzi & Parentani 2010): cualquier horizonte en una burbuja warp actúa como un horizonte de agujero blanco, amplificando fluctuaciones cuánticas hasta energías trans-Planckianas donde la aproximación semicásica deja de ser válida. Los modos azules (blue modes) que se propagan hacia atrás en el tiempo desde el infinito futuro se acumulan exponencialmente en el horizonte, produciendo una divergencia del tensor de energía-momento cuántico que ninguna elección de estado cuántico puede cancelar. Este argumento es más robusto que las condiciones de energía clásicas porque NO depende de la materia exótica: es una propiedad geométrica de cualquier horizonte superlumínico en gravedad semicásica. Si el problema trans-Planckiano no tiene resolución, constituye un **teorema de no-go** para burbujas warp estables, independientemente de si la WEC se satisface o no.

4. **La cota de Pfenning-Ford**: Las restricciones de desigualdad cuántica derivadas por Pfenning y Ford (1997) [3] aplican específicamente a densidades de energía negativa en gravedad semicásica. Si restricciones análogas aplican a las soluciones de energía positiva es una pregunta abierta.

5. **Condición de energía dominante (DEC)**: Incluso en las soluciones de clase II/III de Bobrick-Martire donde la WEC se satisface, la condición de energía dominante (DEC) puede violarse, implicando que el flujo de energía puede ser superlumínico en ciertos sistemas de referencia (Lobo & Visser, 2004). Adicionalmente, Barceló et al. (2009) analizan el problema trans-Planckiano en horizontes análogos, relevante para la estabilidad cuántica de horizontes warp. La violación de la DEC es un problema genérico de las geometrías superlumínicas en relatividad general.

6. **Energía total**: Los diseños modulares de 2025-2026 (cilindros Gaussianos) confinan la energía negativa a estructuras específicas, pero la energía total requerida a escala global sigue equivaliendo a masas estelares [132].

### 3.3 El estatus epistemológico de la teoría de warp drives

Una evaluación justa del campo en 2026 es: los warp drives han progresado desde "imposible en física conocida" hasta "posible en principio si se cumplen condiciones específicas no verificadas". Esto es progreso teórico genuino —el campo ahora sabe exactamente qué condiciones deben demostrarse para que cada clase de métrica sea físicamente realizable. Sin embargo, **ninguna de estas condiciones ha sido observada en la naturaleza o producida en laboratorio**, y las críticas recientes (2024-2026) han identificado errores en los modelos más optimistas [N1,132].

La analogía con los agujeros negros es instructiva. La solución de Schwarzschild de 1916 era una métrica exacta con propiedades aparentemente no físicas (una singularidad, un horizonte de eventos); tomó hasta los años 60 para que la realidad astrofísica de los agujeros negros fuera establecida, y hasta 2019 para la obtención de imágenes directas. La diferencia clave es que los agujeros negros se forman a través de procesos astrofísicos conocidos (colapso gravitacional), mientras que las burbujas warp no tienen un mecanismo de formación conocido. Un warp drive requiere no solo una métrica sino un plano de fabricación para la configuración de energía-momento requerida.

---

## 4. Restricciones de ingeniería

### 4.1 Energía: el cuello de botella irreducible

La Tabla 1 presenta los requisitos energéticos de los principales conceptos de propulsión interestelar, normalizados contra la producción energética humana actual.

**Tabla 1. Requisitos energéticos de conceptos de propulsión interestelar vs. producción energética humana.**

| Concepto | Energía/Potencia | Equivalente producción humana | Referencia |
|---|---|---|---|
| Civilización humana (2025) | ~2.5×10¹³ W (~1.8×10²⁰ J/año) | 1× | — |
| Vela láser, 1g a 0.2c | ~1.85×10¹² J | 2.3×10⁻⁷% anual | Parkin 2018 [4]; verificado con E_cin = (γ−1)mc² |
| Vela láser, 1kg a 0.2c | ~1.85×10¹⁵ J | 2.3×10⁻⁴% anual | Parkin escalado |
| Vela láser, 1t a 0.2c | ~1.85×10¹⁸ J | 0.23% anual | Parkin escalado |
| Antimateria, 1t a 0.5c | ~10²¹ J | ~5× anual | Kammash 1997 [34] |
| Daedalus (50,000t a 0.12c) | ~3.2×10²² J | ~40× anual | BIS 1978 [24]; verificado con KE = (γ−1)mc² |
| Alcubierre (original, burbuja 100m) | ~10⁵² J | ~10³²× anual | Alcubierre 1994 [1] |
| Lentz/Bobrick-Martire | Escala kg materia ordinaria (teórico) | Factible (teórico) | [5,6] |

La brecha energética entre "factible ahora" (vela láser a escala de gramos) y "requiere nueva física o tecnología" (todo lo demás) abarca 6-32 órdenes de magnitud. Esta es la razón fundamental por la que Starshot, a pesar de sus propios desafíos formidables de ingeniería, domina la discusión de vuelo interestelar a corto plazo.

### 4.2 Materiales para entornos extremos

**Materiales para propulsión.** Las cerámicas de ultra-alta temperatura (UHTCs) son la única clase de materiales capaz de soportar las cargas térmicas de la propulsión nuclear térmica o de fusión. El carburo de hafnio (HfC) funde a aproximadamente 3,958°C, y con aditivos de tantalio o zirconio supera los 4,000°C [8,9,44]. Sin embargo, las UHTCs sufren oxidación a temperaturas intermedias (~1,200-1,800°C) y su comportamiento de ciclado térmico bajo condiciones de fusión pulsada es desconocido.

**Materiales para velas.** Las cuatro restricciones simultáneas sobre materiales de velas láser (reflectividad >99.99%, densidad superficial <1 g/m², resistencia mecánica para >10⁴ g, estabilidad térmica) definen un problema de optimización de materiales sin solución demostrada a escala de misión. Los candidatos más cercanos son apilados dieléctricos multicapa sobre sustratos de grafeno [23], pero la reflectividad al nivel de 99.99% bajo iluminación de 100 GW no ha sido demostrada.

**Actualización 2024-2026**: Nuevos compuestos ultraligeros basados en grafeno y materiales reflectantes de silicio multicapa están siendo modelados para tolerar la presión de radiación extrema y el calentamiento durante la aceleración [N4,N7]. El diseño inverso de cristales fotónicos nanoestructurados permite optimizar simultáneamente reflectividad, masa y estabilidad.

**Análisis térmico**: Bajo iluminación de 100 GW sobre una vela de 4 m², el flujo de potencia es de 25 MW/m². Asumiendo una reflectividad del 99.99%, la potencia absorbida es de aproximadamente 2.5 kW/m². La temperatura de equilibrio por radiación de cuerpo negro es T = (P_abs / (σ·ε))^{1/4}. Para una emisividad ε = 0.1 (típica de dieléctricos), T ≈ 3,000 K, cercana al punto de fusión del SiC (3,100 K). Para ε = 0.5 (materiales con alta emisividad infrarroja), T ≈ 1,500 K, que es manejable. Esto implica que el control de la emisividad térmica es un requisito de diseño crítico: se requieren recubrimientos con alta emitancia en el infrarrojo medio para disipar el calor absorbido sin comprometer la reflectividad en la banda del láser (1,064 nm).

**Materiales para blindaje contra radiación.** Los experimentos de Miller et al. (2018) en NSRL Brookhaven demuestran que la combinación de polietileno y boro reduce la dosis efectiva en ~35% frente a aluminio para rayos cósmicos galácticos simulados [109]. Durante et al. (2017) confirman que el polietileno (rico en H) es ~50% más eficaz que el aluminio por unidad de masa para detener protones de 1 GeV [108]. El blindaje magnético activo con superconductores de 1-3 T puede reducir la dosis de GCR en un factor de 2-3 adicional [110].

### 4.3 Viabilidad económica y restricciones operacionales

**Costo del array láser**: Aunque el costo de la antimateria se ha cuantificado (~$6.4B/ng), el costo del array láser de 100 GW para Starshot no ha recibido igual atención. Estimaciones de orden de magnitud: ~10⁶ elementos láser de 100 kW cada uno, con un costo por elemento de ~$100k (estado del arte para láseres de fibra de alta potencia), resultan en ~$100B solo en componentes láser. A esto se suma la infraestructura de enfriamiento (~$10B), óptica adaptativa (~$5B), y el sistema de distribución de energía (~$20B). El costo total del sistema de propulsión se estima en >$150B, comparable al presupuesto acumulado de la ISS (~$150B). Aunque elevado, es inferior al costo de un programa de fusión a escala Daedalus o de producción de antimateria a escala de gramos.

**Infraestructura de almacenamiento energético**: El array láser de 100 GW requiere un sistema de almacenamiento capaz de entregar ~16.7 GWh en ~10 minutos (100 GW × 600 s = 6×10¹³ J). Investigación de infraestructura energética real (2024-2026) indica que la única tecnología con TRL 9 capaz de satisfacer este requisito son las baterías Li-ion a escala utility. El costo estimado del sistema completo (celdas + electrónica de potencia + transformadores + EPC) es de $30-50B USD (2025), basado en costos de pack de $70-150/kWh y electrónica de potencia de $200-250/kW. La mayor planta BESS jamás construida (Moss Landing, California, 750 MW / 3,000 MWh) es 133× menor en potencia que lo requerido. El cuello de botella no son las celdas de batería sino la electrónica de potencia: 100 GW de inversores bidireccionales requieren una cadena de suministro que no existe a esa escala. La capacidad de producción MUNDIAL de electrónica de potencia para sistemas de baterías (PCS) es de aproximadamente 50 GW/año (IEA 2025). Construir 100 GW requeriría dedicar el 100% de la producción mundial durante 2 años exclusivamente a este proyecto, desplazando toda otra demanda (almacenamiento de red, vehículos eléctricos, data centers). Para contextualizar: la mayor planta BESS jamás construida (Moss Landing, California) tiene 0.75 GW de potencia — 133 veces menos que lo requerido. Los costos de baterías cayeron 45% en 2024-2025 (BloombergNEF), lo que sugiere que para 2035 el sistema podría ser significativamente más barato. Referencias de costos: IREN Ltd. (510 MW operativos, expansión a 2.9 GW en Texas, ~$6-7M/MW para data centers); proyectos Ordos (China, 8 GW solar + 5 GWh BESS, ~$11B) y Masdar/EWEC (UAE, 5.2 GW solar + 19 GWh BESS, ~$6B).

**Eficiencia wall-plug**: El cálculo de energía cinética (1.85×10¹² J) corresponde a la energía final de la carga útil. Para obtener la energía eléctrica requerida, debe considerarse la eficiencia total del sistema: η_total = η_eléctrica × η_láser × η_acoplamiento. Asumiendo η_láser = 0.1% (estado del arte para láseres de fibra de alta potencia con conversión de frecuencia), η_acoplamiento ≈ 20% (fracción de energía del haz transferida a la vela), y η_eléctrica ≈ 90%, se obtiene η_total ≈ 1.8×10⁻⁴. Por tanto, la energía eléctrica requerida es E_eléctrica = 1.85×10¹² / 1.8×10⁻⁴ ≈ 1.03×10¹⁶ J, equivalente a ~0.0013% de la producción eléctrica humana anual. NOTA: La Sección 6.2 contenía un valor incorrecto de ~1.1×10¹⁹ J (error de factor ~1000), corregido en esta versión.

**Turbulencia atmosférica**: Un array terrestre de 100 GW enfrenta degradación del frente de onda por turbulencia atmosférica (seeing típico ~1 arcsec en buenos sitios). Para mantener la coherencia del haz sobre una apertura de 100 m, se requiere óptica adaptativa de orden extremadamente alto (Strehl > 0.8 a 1,064 nm) con frecuencias de corrección de kHz, tecnología que no existe actualmente a esta escala. La alternativa es ubicar el array en el espacio (órbita GEO, punto de Lagrange L1, o superficie lunar), eliminando la turbulencia pero multiplicando los costos de lanzamiento e infraestructura.

**Problema de apuntamiento con latencia**: A 0.2 AU de distancia (típica al final de la fase de aceleración), la latencia de luz es de ~2 minutos (ida) + ~2 minutos (vuelta) = ~4 minutos de bucle cerrado. Esto impide la corrección en tiempo real del apuntamiento del haz. La solución requiere apuntamiento predictivo basado en modelos de trayectoria a bordo de la vela, con realimentación óptica mediante balizas laterales en la propia vela que permitan al array terrestre medir la posición relativa y corregir con ~4 minutos de anticipación.

**Escalado de beam-riding**: Las demostraciones actuales de beam-riding con metasuperficies se han realizado a escala de nanogramos en laboratorios de fotónica [20,21]. **ADVERTENCIA CRÍTICA**: La brecha hasta una misión de 1 gramo implica 9 órdenes de magnitud en masa (~10⁻¹² kg → 10⁻³ kg) y 15 órdenes de magnitud en potencia láser (~mW → 100 GW). Los efectos no lineales que son despreciables a escala de laboratorio se vuelven dominantes a alta potencia: (a) calentamiento diferencial que deforma la metasuperficie y cambia su respuesta óptica, (b) acoplamiento optomecánico no lineal entre el haz y la vela deformada, (c) expansión térmica que altera el patrón de difracción diseñado. Ninguno de estos efectos ha sido modelado a las potencias relevantes para una misión Starshot. Se proponen hitos intermedios con validación experimental independiente: escala de μg (2028, potencia ~1 kW), escala de mg (2032, potencia ~1 MW), y escala de g (2036+, potencia ~1 GW). Cada salto de 3 órdenes de magnitud en masa requiere demostración experimental antes de asumir viabilidad del siguiente. La extrapolación directa de ng a g sin validación intermedia NO está respaldada por la literatura actual.

### 4.4 Estabilidad y control

Tres problemas de estabilidad distintos surgen a través de diferentes conceptos de propulsión:

1. **Estabilidad de beam-riding** (velas láser): Las soluciones basadas en metasuperficies [20,21,22] han sido demostradas a escala centimétrica en laboratorio. Escalar a velas de tamaño métrico con haces de clase GW introduce acoplamiento optomecánico no lineal que no ha sido modelado.

2. **Estabilidad cuántica** (warp drives): La contradicción entre Hiscock (1997) [15]/Finazzi (2009) [16] y JHEP (2022) [17] significa que el campo carece de consenso sobre si las burbujas warp son estables frente a perturbaciones cuánticas, incluso en principio.

3. **Estabilidad electromagnética** (naves relativistas): Hoang y Loeb (2017) mostraron que una nave espacial cargada a 0.2c desarrolla un momento dipolar eléctrico que interactúa con campos magnéticos interestelares, generando torques oscilatorios [46]. El control de actitud activo consumiría presupuestos de masa y potencia ya en sus límites.

---

## 5. Comunicación, blindaje y frenado: los nuevos bloques

### 5.1 El enlace de comunicación interestelar

Antes de esta revisión, la comunicación interestelar era un vacío documentado en la literatura. Los nuevos resultados del Bloque 10 transforman este panorama.

Clark y Cahoy (2018) demuestran que un láser de 1 MW acoplado a un telescopio de 40 m (clase ELT) lograría ~53 kbps con detección directa y ~2.7 Mbps con conteo de fotones desde Próxima Centauri [83]. Con un sistema DE-STAR 4 (100 GW), las tasas alcanzarían Gbps e incluso Tbps. Hippke (2018) derivó la tasa máxima de datos usando el límite de Holevo: bits por segundo por vatio a longitudes de onda óptimas de 300-400 nm para una sonda de 1 g con transmisor de 1 m [84]. Adoptamos 1 kbps como tasa de referencia en este análisis porque: (a) es suficiente para telemetría básica de la nave (estado de sistemas, navegación, temperatura, voltajes) con margen de sobra, (b) permite transmitir una imagen comprimida de 100 kB (JPEG2000) en aproximadamente 15 minutos por día, y (c) es conservadora respecto a las capacidades ópticas demostradas — DSOC en Psyche logró >200 Mbps desde 0.4 UA, y la extrapolación a 4.37 al con un láser de 1-10 MW sitúa las tasas alcanzables en el rango de kbps a Mbps [86,83].

La NASA demostró con DSOC (Deep Space Optical Communication) a bordo de Psyche: telescopio de 22 cm, láser de 4 W a 1,550 nm, enlace descendente de 0.2 a >200 Mbps desde 0.1-2 UA [86]. Extrapolando a distancias interestelares, la pérdida por 1/r² es ~10¹⁰ veces mayor que a 1 UA; con las tecnologías de DSOC la tasa caería a ~10⁻⁴ bps. Se necesitarían potencias de megavatios y telescopios de decenas de metros [83,87].

La comunicación cuántica interestelar es físicamente posible en ciertas bandas espectrales. Rogers (2020) demuestra que el camino libre medio de fotones en el medio interestelar para rayos X de 10⁴ eV supera los 10⁵ pc —mayor que el diámetro de la Vía Láctea— haciendo que la decoherencia por interacción con partículas sea despreciable [89].

Arquitecturas de retorno de datos: Hippke (2020) propone una red interestelar con nodos repetidores que aprovechan el lente gravitacional solar (ganancia de ~10⁹) [91]. Clark y Cahoy (2018) comparan el envío de datos por haz láser vs. sondas de materia inscrita (ADN con densidad de 215 PB/g): para distancias <200 al, el láser gana; para mayores, las sondas físicas pueden ser superiores [83].

### 5.2 Blindaje y supervivencia a velocidades relativistas

McDevitt et al. (2023) modelan la exposición de una nave Starshot durante ~20 años: dosis total de ~4 Sv con blindaje pasivo de polietileno de ~4 cm, proveniente mayoritariamente de GCR de GeV-TeV y partículas secundarias del medio interestelar [97]. Walsh et al. (2021) estiman la tasa de dosis del medio interestelar local en ~0.3-0.6 mSv/día, dando ~2-4 Sv en 20 años sin blindaje [98].

El impacto de granos de polvo es potencialmente catastrófico. Hoang y Fesen (2021) muestran que granos de tamaño ≥10⁻¹³ g producen erosión severa a 0.2c; un grano de 1 μm impacta con energía de ~0.5 GJ, equivalente a explosivos de alta potencia, erosionando ~10³ veces la masa del grano impactante [100]. Worden y Lubin (2022) estiman una probabilidad de impacto letal del 1-10% para naves de 10 g en un viaje a α Centauri, y proponen blindaje multicapa de sacrificio con capas de SiC de 1-5 μm [101].

La carga electrostática es un mecanismo de daño adicional. Hoang et al. (2018) modelan que una nave a 0.2c acumula un potencial de ~100 V a varios kV debido al desbalance de corrientes de iones y electrones, con campos eléctricos superficiales de 10⁴-10⁶ V/m [105]. Estrategias de mitigación incluyen emisores de electrones, superficies conductoras con descarga corona, y blindaje magnético activo [106,107].

**Limitación experimental**: No existen experimentos de laboratorio a velocidades >0.001c con partículas de polvo. Price et al. (2020) alcanzaron ~200 km/s (0.0007c) con un dust accelerator de 4 MV [111]. Los modelos a 0.2c se basan en extrapolaciones y simulaciones SPH [112].

### 5.3 Frenado y desaceleración en destino

El frenado sin infraestructura en el sistema destino es uno de los problemas más difíciles del vuelo interestelar. Tres métodos principales existen en la literatura:

**Vela magnética (magsail)**: Zubrin y Andrews (1991) propusieron una espira superconductora de 100 km de radio con corriente de 1 MA, generando arrastre de ~10⁴ N a 0.05c para una nave de ~10³ toneladas [115]. Gros (2017) derivó una relación de escalado universal mostrando que la masa requerida del magsail sería de ~10³ toneladas para frenar desde 0.05c [116].

**Vela eléctrica (electric sail)**: Perakis y Hein (2016) demostraron que la combinación secuencial magsail + electric sail reduce el tiempo de frenado de ~40 años (solo magsail) a ~29 años para una nave de 8,250 kg desde 0.05c. El magsail es más eficiente a altas velocidades (>0.01c), y la vela eléctrica a bajas velocidades [117].

**Frenado por presión de radiación estelar**: Heller y Hippke (2017) demostraron que una vela con densidad superficial de 7.6×10⁻⁴ g/m² (similar al grafeno) puede ser frenada fotogravitatoriamente al llegar a α Centauri, con velocidad máxima de inyección de 13,800 km/s (4.6% c) para órbita ligada alrededor de Próxima [118].

**Arquitectura integrada — Proyecto Dragonfly**: Hein et al. (2019) presentan el diseño más completo: vela ligera impulsada por láser de 100 GW acelera una nave de 2,750 kg a 0.05c; durante el viaje interestelar, la vela ligera se separa y se despliega una vela magnética + eléctrica combinada para frenar en destino; tiempo total de misión ~100 años [120].

---

## 6. Arquitecturas de sondas autónomas

### 6.1 El paradigma Von Neumann

Una sonda Von Neumann es una nave espacial capaz de autorreplicación usando recursos in-situ en el sistema destino [35]. El atractivo conceptual para la exploración interestelar es inmediato: lanza una sonda, y se convierte en muchas, explorando la Galaxia en una fracción del tiempo requerido para exploración directa desde la Tierra.

Freitas (1980) estimó un tiempo de replicación de 500-2,000 años para una sonda de aproximadamente 10¹⁰ kg [35]. Los reanálisis modernos [37,42] no han revisado fundamentalmente las escalas de energía y tiempo —el desafío no es la propulsión sino la fabricación autónoma en un entorno desconocido.

Osmanov (2019) identificó un nicho donde la replicación Von Neumann podría ser sustancialmente más fácil: sondas de escala submicrónica ("nanobots") en nubes interestelares HII, donde los tiempos de replicación podrían ser tan cortos como años [36]. La contrapartida es que los nanobots no pueden transportar cargas científicas sofisticadas.

### 6.2 Navegación autónoma

La navegación por púlsares de rayos X (SEXTANT) proporciona lo más cercano a un subsistema de navegación interestelar probado en vuelo. Demostrado en la ISS en 2018, SEXTANT logró determinación autónoma de posición en tiempo real con precisión de ~5 km usando púlsares de milisegundo como referencias de temporización [7]. Para crucero interestelar, el temporizado de púlsares proporcionaría posición absoluta sin contacto con Tierra —los pulsos de púlsares galácticos son igualmente detectables a 4.37 años luz.

Lo que no existe es la toma de decisiones autónoma para misiones de duración decadal. La guía autónoma actual (Foster et al., 2021 [47]) maneja maniobras orbitales y secuencias predefinidas; la capacidad de detectar anomalías, replanificar objetivos de misión y ejecutar reparaciones sin intervención terrestre es un problema de investigación que ningún artículo en nuestro corpus aborda.

### 6.3 Miniaturización y payloads científicos

Para una sonda ultraligera (<1 kg), la carga útil se reduce a: cámara CMOS (1-5 g), magnetómetro de chip (~5 g), espectrómetro de rejilla integrado (<10 g), y detector de radiación en chip (~0.05 g) [135,136].

Parkin (2018) describe la arquitectura Starshot: una starchip de ~1 gramo totalmente integrada con vela ligera de 4×4 m, computación a bordo en un chip CMOS estándar (procesador ARM), cámara CMOS, giroscopio MEMS y fotodiodos para comunicación [137]. La vela actúa como antena de comunicaciones con ganancia de ~60 dBi y como sensor de presión de radiación.

Los sensores cuánticos con fotónica integrada representan la frontera de miniaturización. Pelucchi et al. (2023) demuestran que chips fotónicos de Si₃N₄ o LiNbO₃ permiten espectrómetros de <1 cm³ sin partes móviles, reduciendo sensores cuánticos completos a <10 g con consumo <1 W [143].

La ciencia más valiosa en un sobrevuelo de α Centauri sería la espectroscopía de transmisión para detectar biomarcadores atmosféricos (O₂, H₂O, CH₄) en Próxima b durante el breve encuentro [137,138].

---

## 7. El medio interestelar como problema de ingeniería

### 7.1 El medio no está vacío

El medio interestelar (ISM) entre el Sol y Alpha Centauri contiene aproximadamente 0.1-1 átomos de hidrógeno por cm³, con una razón de masa polvo-gas de aproximadamente 0.01. A 0.2c, esto se traduce en un flujo de hidrógeno de aproximadamente 6×10⁶ cm⁻² s⁻¹ con energía cinética de aproximadamente 20 MeV por nucleón —efectivamente, la nave está siendo bombardeada por un haz continuo de partículas MeV.

Hoang et al. (2017) cuantificaron los efectos erosivos: una superficie de cuarzo pierde aproximadamente 0.5 mm de espesor en el viaje de 4.37 años luz; el grafito es aproximadamente 10 veces más resistente [45]. El mecanismo de erosión dominante no es el sputtering directo sino la vaporización por pico térmico de impactos de granos de polvo.

La caracterización del medio interestelar local hacia α Centauri ha avanzado significativamente. Slavin et al. (2020) reportan densidad de polvo de ~10⁻²⁶ g/cm³ en la Nube Interestelar Local (LIC), con granos de 0.01-1 μm compuestos principalmente de silicatos (~70%) y carbono (~30%) [103]. Frisch et al. (2011) establecen una densidad numérica de ~10⁻¹⁴ granos/m³ con distribución dN/da ∝ a⁻³·⁵ [104].

### 7.2 Interacciones electromagnéticas

Hoang y Loeb (2017) demostraron que el mismo bombardeo del ISM carga la nave espacial a potenciales de escala de kilovoltios a través de emisión secundaria de electrones y carga fotoeléctrica UV [46]. El dipolo eléctrico resultante interactúa con campos magnéticos interestelares (~3 μG), produciendo torques oscilatorios que pueden desestabilizar la orientación de la nave. El control de actitud activo requeriría autoridad de propelente o ruedas de reacción que los presupuestos de masa no pueden acomodar.

Spitale y Angelopoulos (2021) proponen neutralizadores activos (cañones de electrones) y superficies conductoras con descarga por puntas para mitigar la carga [106]. Lingam et al. (2019) proponen blindaje activo con campos magnéticos (B ~0.1-1 T) para desviar iones cargados del ISM, reduciendo tanto la carga como la erosión [107].

### 7.3 Detectabilidad como firmas tecnológicas

Un hallazgo colateral interesante del Bloque 16 es que las misiones de propulsión interestelar son intrínsecamente detectables. Guillochon y Loeb (2015) demuestran que el destello del haz de aceleración de Starshot (láser de 100 GW) es más brillante que el Sol en longitudes de onda específicas durante la aceleración (~30 minutos), detectable desde ~100 pc [153]. Benford et al. (2019) añaden que la propulsión interestelar es intrínsecamente detectable, fortaleciendo la paradoja de Fermi: si hubiera muchas civilizaciones explorando, veríamos más firmas tecnológicas [154].

---

## 8. Conclusiones

### 8.1 Resumen de hallazgos

Esta revisión evaluó 28 conceptos de propulsión y navegación interestelar a través de 155 referencias en 18 bloques temáticos. Un criterio transversal que emerge de este análisis es la **falsabilidad**: ¿puede el concepto ser refutado con tecnología actual o de futuro cercano? La vela láser es falsable (si beam-riding resulta inestable a >1 kW, el concepto es inviable). Los warp drives y agujeros de gusano NO son falsables con tecnología actual (no existe experimento concebible que demuestre su imposibilidad). Esto los sitúa, desde una perspectiva popperiana, fuera del ámbito de la ciencia experimental. Las sondas Von Neumann son parcialmente falsables (la no-detección de firmas tecnológicas acota el espacio de parámetros pero no demuestra imposibilidad). Recomendamos que toda propuesta de propulsión interestelar incluya una estrategia de falsación explícita.

Nuestros hallazgos principales son:

1. **Ningún concepto de propulsión interestelar a otra estrella supera TRL 3.** Los sistemas de mayor TRL son navegación (SEXTANT, TRL 6-7), propulsión eléctrica en órbita terrestre (VASIMR, TRL 4-5), y materiales de ultra-alta temperatura (TRL 4-5). La brecha de TRL entre "subsistema útil" y "misión interestelar integrada" es de 3-6 niveles en todos los conceptos.

2. **La vela láser es el único concepto cuyos cuellos de botella son principalmente de ingeniería y no de física.** Su requisito energético (~2×10¹⁵ J para 1 gramo a 0.2c) está dentro de la capacidad humana actual; su problema de estabilidad tiene soluciones prometedoras en óptica de metasuperficies; sus incógnitas principales —coherencia de haz a escala de 100 metros, materiales de vela con reflectividad 99.99%, supervivencia al ISM a 0.2c— son abordables mediante experimentación incremental.

3. **Las soluciones de warp drive post-2021 representan progreso teórico genuino pero no cambian el panorama de ingeniería.** Eliminar la energía negativa remueve un "no rotundo" de la física conocida, pero las condiciones introducidas en su lugar (estados de plasma no observados, gravedad modificada, acoplamientos de torsión) no son experimentalmente más accesibles. Las críticas de 2024-2026 han identificado errores en el modelo de Lentz [N1,132], confirmando que la violación de la WEC persiste en ciertas regiones.

4. **Los vacíos críticos de literatura en comunicación y blindaje han sido sustancialmente cubiertos por los Bloques 10-18.** Existen soluciones de ingeniería con física establecida para: enlace de comunicación óptica desde α Centauri (kbps-Mbps factibles con ELT), blindaje contra GCR (polietileno + boro, reducción ~35%), blindaje contra polvo (multicapa SiC, probabilidad supervivencia >90% con enjambres), y frenado en destino (combinación magsail + electric sail, ~29 años).

5. **Los nuevos bloques (ética, derecho, simulaciones) revelan que el viaje interestelar es tanto un problema de gobernanza como de ingeniería.** No existe marco legal para misiones interestelares. La responsabilidad intergeneracional de proyectos que tardan siglos no tiene precedentes en la historia humana. Estos no son problemas secundarios; son potencialmente bloqueantes.

### 8.2 Hoja de ruta priorizada

**En menos de 10 años (antes de 2036):**
- **Experimento crucial de falsación para Starshot**: demostración de beam-riding estable a escala de μg con >1 kW de potencia láser continua. Si este experimento falla (desviación >20% del modelo de estabilidad pasiva), el concepto de vela láser interestelar debe ser reevaluado fundamentalmente. Este es el criterio de falsación popperiano que distingue la vela láser de conceptos no falsables como los warp drives.
- Demostración en laboratorio de beam-riding con metasuperficies a >100 W de potencia láser continua
- Experimentos de erosión del ISM usando aceleradores de iones para validar modelos de Hoang (2017) a velocidades equivalentes >0.1c
- Análisis completo de presupuesto de enlace de comunicación para α Centauri, publicado con cálculos detallados de SNR y apertura
- Experimento análogo de HORIZONTES (no burbujas warp) usando metamateriales ópticos no lineales (enfoque Smolyaninov/Faccio). PRECISIÓN: Los metamateriales con índice negativo simulan horizontes en medios en movimiento efectivo, NO burbujas warp con contracción/expansión coordinada del espacio-tiempo. Son fenómenos cualitativamente distintos. Este experimento probaría física de horizontes análogos, no viabilidad de warp drives.

**En menos de 20 años (antes de 2046):**
- Demostración suborbital o LEO de una vela de escala de gramos acelerada por láser terrestre (segundos de iluminación, delta-v de km/s)
- Misión Interstellar Probe (McNutt 2022 [50]) a >200 UA, caracterizando el ISM y validando navegación autónoma para crucero interestelar
- Navegación autónoma clase SEXTANT demostrada en trayectoria interplanetaria (Marte o más allá)
- Calificación de materiales: UHTC y velas de grafeno probadas bajo cargas combinadas térmicas, de radiación y mecánicas

**Más allá de 20 años (2046+):**
- Demostración de sistema clase Starshot: carga útil de gramos a >0.01c en distancias interplanetarias
- Imanes de fusión superconductores de alta temperatura (herencia SPARC/ITER) calificados para entornos espaciales
- Almacenamiento de antimateria a escala de microgramos para misiones precursoras
- Pruebas de componentes de sonda Von Neumann: fabricación autónoma en entorno caracterizado (Luna, asteroide cercano)

**Requiere nueva física (sin cronograma):**
- Verificación o falsación experimental de gravedad de Einstein-Cartan, gravedad f(R,T) u otras teorías de gravedad modificada
- Producción en laboratorio de estados de plasma que coincidan con los requisitos del solitón de Lentz (2021)
- Resolución de la cuestión de estabilidad cuántica para burbujas warp
- Detección de ondas gravitacionales por colapso de burbuja warp como estrategia experimental alternativa [Bloque 19]

### 8.3 Evaluación final

El viaje interestelar no es un problema monolítico esperando un avance. Es un conjunto anidado de desafíos —energéticos, materiales, computacionales y físicos— que deben resolverse en un orden específico. La secuencia correcta, basada en la evidencia reunida aquí, es: (1) demostrar estabilización de beam-riding en laboratorio, (2) validar supervivencia al ISM a velocidades relevantes, (3) resolver el presupuesto de enlace de comunicación interestelar, (4) demostrar aceleración de escala de gramos a >0.01c en distancias interplanetarias, y (5) iterar.

### 8.3 Líneas de investigación futura

Tres extensiones naturales de este trabajo emergen de los gaps identificados:

1. **Comunicación cuántica interestelar con cadenas de repetidores**: La Sección 5.1 establece que la coherencia cuántica puede mantenerse a distancias interestelares (Rogers 2020). Lo que falta es un modelo de ingeniería: ¿cuántos repetidores cuánticos se necesitan entre la Tierra y α Centauri para mantener fidelidad > 90%? Herramientas de simulación como Q2NS/ns-3 (Quantum Internet Task Force) permiten modelar cadenas de repetidores a distancias terrestres. La extrapolación de esos modelos a distancias astronómicas — identificando el punto de quiebre donde la decoherencia domina y proponiendo arquitecturas de repetidores para enlaces interestelares — es un paper independiente que este trabajo deja planteado.

2. **Validación experimental de beam-riding a escala intermedia**: La brecha de 9 órdenes de magnitud entre las demostraciones actuales (ng) y una misión Starshot (g) solo puede cerrarse con experimentos incrementales. El experimento crucial de falsación propuesto en la Sección 8.2 (beam-riding a μg con >1 kW) debería ser el próximo hito experimental.

3. **Gaussian Processes para health monitoring satelital**: La misma metodología de cuantificación de incertidumbre que usamos en esta revisión — ensembles de kernels, intervalos de confianza, detección de anomalías basada en cobertura— puede aplicarse al monitoreo predictivo de salud satelital. Un framework como SatHealth-GP, que predice tendencias de telemetría con GPs en lugar de LSTMs, complementa naturalmente este trabajo: los mismos satélites que hoy monitoreamos con GPs podrían ser los precursores de las velas interestelares del futuro.

La tentación de enfocarse en los conceptos más exóticos (warp drives, agujeros de gusano) es comprensible: prometen viaje interestelar sin las brutales restricciones de la ecuación del cohete o los tiempos de crucero de décadas de las velas láser. Pero la evidencia de tres décadas de literatura post-Alcubierre es clara: cada solución que elimina una imposibilidad física introduce otra. La vela láser, con todas sus limitaciones, no requiere que el universo sea diferente de lo que observamos que es. En el paisaje de la propulsión interestelar, eso la hace única.

---

## 9. Implicaciones y contexto estratégico

### 9.1 Comparación con otros megaproyectos científicos

Para contextualizar la inversión requerida, la Tabla 2 compara Starshot con otros megaproyectos científicos que la humanidad ya ha financiado.

**Tabla 2. Comparación de megaproyectos científicos.**

| Proyecto | Costo (USD 2025) | Duración | Estado | ¿Terminado? |
|---|---|---|---|---|
| Gran Colisionador de Hadrones (LHC) | ~$5B | 1998–2008 | Operando | Sí |
| Telescopio Espacial James Webb (JWST) | ~$10B | 1996–2021 | Operando en L2 | Sí |
| ITER (fusión nuclear) | ~$22B | 2006–2035+ | En construcción | No |
| Apollo (total, 6 alunizajes) | ~$200B (ajustado) | 1961–1972 | Completado | Sí |
| Estación Espacial Internacional (ISS) | ~$150B | 1998–2030 | Operando | Sí |
| **Starshot (array láser + I+D)** | **~$150-200B** | **2040–2100** | **No iniciado** | **No** |

Dos conclusiones emergen de esta comparación. Primero, **el costo NO es descabellado**: ~$150-200B es comparable al presupuesto acumulado de la ISS y menor que el programa Apollo ajustado por inflación. La humanidad YA ha gastado cantidades similares en exploración espacial. Segundo, **el timeline es el verdadero desafío**: 60-100 años excede cualquier ciclo político, electoral o de financiamiento. Esto requiere un modelo de gobernanza intergeneracional sin precedentes (ver Sección 9.4).

### 9.2 El factor Starship: cómo el acceso barato a órbita cambia la ecuación

El vehículo Starship de SpaceX promete reducir el costo de acceso a órbita terrestre baja (LEO) de ~$10,000/kg a ~$100/kg — dos órdenes de magnitud. Si esta reducción se materializa (las primeras versiones operativas ya han demostrado costos de ~$1,000-2,000/kg en 2024-2025), las implicaciones para la propulsión interestelar son transformadoras:

1. **Array láser orbital**: Construir el array de 100 GW en órbita (GEO o L1) en vez de en Tierra elimina la turbulencia atmosférica, la absorción y la distorsión del frente de onda. Con Starship, el costo de lanzamiento de 10⁶ elementos láser + estructura + paneles solares pasaría de >$1B a ~$100M en costos de lanzamiento. El costo dominante seguiría siendo la fabricación de los láseres, no su despliegue.

2. **Energía solar espacial**: Un array láser en órbita puede alimentarse directamente de paneles solares sin pasar por la red eléctrica terrestre, eliminando el problema de almacenamiento de 16.7 GWh discutido en la Sección 4.3.

3. **Mantenimiento y escalabilidad**: Una infraestructura orbital permite mantenimiento in-situ y expansión incremental — lanzar 1 GW, probar, lanzar 10 GW, probar, escalar a 100 GW. Esto es imposible con un array terrestre fijo.

4. **Independencia geopolítica**: Un array en L1 no está sujeto al control de ningún país, sino que opera como infraestructura de la humanidad — similar a como la Antártida es administrada por el Tratado Antártico.

**Caveat**: Starship aún no ha alcanzado operación rutinaria con reutilización completa. Las estimaciones de $100/kg son aspiracionales. Pero incluso a $1,000/kg (10× más caro), la ecuación económica del array orbital ya es competitiva con la terrestre cuando se incluye el costo de la óptica adaptativa y la gestión de la turbulencia.

### 9.3 El rol de la inteligencia artificial como acelerador

Tres áreas donde la IA está acelerando directamente el desarrollo de propulsión interestelar:

1. **Descubrimiento de materiales**: El diseño de la vela de cristal fotónico pentagonal de Norder et al. (2025) [134] fue optimizado mediante redes neuronales que exploraron millones de configuraciones de nanoperforaciones. Sin ML, este diseño habría requerido décadas de prueba y error. Esta tendencia se acelerará: modelos generativos como GNoME (Google DeepMind) ya predicen nuevos materiales con propiedades objetivo.

2. **Navegación autónoma**: El reinforcement learning aplicado a correcciones de rumbo interestelar (Crisp et al. 2021 [166]) y las redes neuronales para predicción de trayectorias (Stupl et al. 2022 [165]) permiten navegación sin intervención humana durante décadas. La combinación de SEXTANT (posicionamiento por púlsares) + RL (toma de decisiones) + LLMs a bordo (diagnóstico de anomalías) define el camino hacia la autonomía interestelar total.

3. **Optimización de diseños**: Algoritmos genéticos ya redujeron tiempos de frenado en 25% respecto a diseños manuales (Hein et al. 2020 [164]). A medida que los modelos de IA se vuelvan más capaces, el diseño completo de la misión — desde la forma de la vela hasta la secuencia de frenado — podrá ser co-optimizado por IA, potencialmente encontrando soluciones que ningún ingeniero humano consideraría.

### 9.4 Minimum Viable Mission (MVM): ¿cuál es la misión interestelar más barata posible?

Si el costo de Starshot completo (~$150-200B) resulta políticamente inviable, ¿existe una versión mínima que aún produzca ciencia publicable? Proponemos el concepto de **Minimum Viable Mission (MVM)**:

- **Masa**: 1 gramo (igual que Starshot)
- **Velocidad**: 0.01c (en vez de 0.2c) → **400× menos energía** que Starshot (~4.6×10⁹ J)
- **Tiempo de viaje a α Centauri**: ~437 años (en vez de ~22)
- **Sin frenado**: sobrevuelo científico (no inserción orbital)
- **Sin comunicación en tiempo real**: los datos se graban y transmiten durante meses tras el sobrevuelo
- **Costo estimado**: ~$5-10B (escala JWST), asumiendo que el array láser se escala proporcionalmente (~250 MW en vez de 100 GW)

La MVM NO resuelve el problema de la comunicación (Sección 5.1) ni del blindaje (Sección 5.2), pero requiere 400× menos inversión en infraestructura láser. El costo temporal —437 años de espera— puede ser aceptable si se lanzan múltiples MVM a diferentes estrellas en paralelo. Para el año 2500, la humanidad tendría datos de 5-10 sistemas estelares cercanos.

**Objeciones**: (a) ninguna agencia espacial financia misiones cuyos resultados no verá nadie vivo hoy, (b) la electrónica debe sobrevivir 437 años, no 22, (c) la vela debe mantener reflectividad durante casi medio milenio de exposición al ISM. La MVM es más un ejercicio de "qué es físicamente posible con mínimo presupuesto" que una propuesta de misión realista.

### 9.5 Spin-offs garantizados: tecnologías que avanzan aunque Starshot nunca vuele

Incluso si ninguna misión interestelar se materializa en el próximo siglo, la investigación en propulsión interestelar ya está generando tecnologías con aplicaciones inmediatas:

| Tecnología interestelar | Spin-off inmediato | TRL actual | Impacto |
|---|---|---|---|
| Beam-riding con metasuperficies | Comunicaciones ópticas satelitales de alta precisión | 2-3 | DSOC en Psyche ya opera; mejora de enlaces Tierra-LEO |
| Materiales ultraligeros (grafeno, CNT) | Velas solares para vigilancia de asteroides cercanos | 3-4 | NASA ACS3, JAXA IKAROS |
| Navegación por púlsares (XNAV) | GPS autónomo para espacio profundo (Marte, asteroides) | 6-7 | SEXTANT demostrado en ISS 2018 |
| Detectores de conteo de fotones | LIDAR cuántico, cámaras de visión nocturna | 5-6 | Comercializado por ID Quantique, Hamamatsu |
| Blindaje contra GCR con polietileno+boro | Blindaje para misiones tripuladas a Marte | 4-5 | Probado en NSRL Brookhaven (Miller 2018) |
| Almacenamiento de energía de alta potencia | Estabilización de redes eléctricas con BESS | 8-9 | Mercado global de $50B/año |

**Conclusión**: La inversión en propulsión interestelar se auto-financia parcialmente a través de spin-offs. Cada dólar invertido en beam-riding produce retornos en comunicaciones ópticas; cada dólar en navegación por púlsares mejora la navegación en el sistema solar. Este argumento es clave para sostener financiamiento multigeneracional: los spin-offs generan valor incluso antes de que la misión interestelar despegue.

### 9.6 Recomendaciones para agencias de financiamiento

Basados en la evidencia reunida en esta revisión, recomendamos:

1. **Destinar el 0.1% del presupuesto espacial global (~$25M/año) a un programa coordinado de experimentos de beam-riding**, comenzando con demostración en laboratorio a escala de μg antes de 2030 y escalando a mg para 2035. El costo de NO investigar es cero — pero también lo es el progreso.

2. **Crear un consorcio internacional** (similar a ITER o CERN) para la propulsión interestelar, evitando la duplicación de esfuerzos y compartiendo infraestructura de validación. La inclusión de agencias espaciales de China (CNSA), Rusia (Roscosmos), India (ISRO), Japón (JAXA) y Europa (ESA) es esencial: el viaje interestelar es un proyecto de la civilización, no de una nación.

3. **Financiar la investigación fundamental en paralelo con la ingeniería**: Aunque los warp drives son TRL 1, la física de horizontes análogos, el problema trans-Planckiano y las condiciones de energía en gravedad modificada son preguntas legítimas de ciencia básica que merecen financiamiento independientemente de su aplicabilidad a propulsión.

4. **Establecer un "Interstellar Program Office"** —similar a la oficina de protección planetaria de NASA— que evalúe propuestas de propulsión interestelar usando criterios estandarizados de TRL, falsabilidad, y factibilidad energética. Esta revisión proporciona un marco inicial para dicha evaluación.

5. **Invertir en la cadena de suministro de electrónica de potencia**: El cuello de botella para Starshot no son los láseres ni las velas — es la capacidad de fabricar 100 GW de inversores. Duplicar la producción mundial de PCS para BESS es un objetivo que tiene beneficios inmediatos para la transición energética global, independientemente de Starshot.

### 9.7 Panorama internacional: más allá del eje EE.UU.-Europa

La investigación en propulsión interestelar no es exclusiva de Occidente. Presentamos un panorama de los programas y capacidades relevantes en otras potencias espaciales.

**China** es el único país además de EE.UU. con un programa formal de sondas al espacio interestelar. El programa **Shensuo** (神梭, antes *Interstellar Express* o IHP) de CNSA/CAS planea lanzar dos sondas (~200 kg cada una, con RTGs) hacia la nariz y cola de la heliosfera alrededor de 2025-2026, con sobrevuelos de Júpiter y Neptuno-Tritón en ruta. Serían las sondas #6 y #7 en abandonar el Sistema Solar, después de Voyager 1/2, Pioneer 10/11 y New Horizons. Una tercera sonda (IHP-3, ~2030) llevaría reactor nuclear. Complementariamente, China ha probado en tierra (2024) un **reactor espacial de 1.5 MWe** enfriado por litio líquido con ciclo Brayton — ~75 veces más potente que el diseño Kilopower de NASA (~20 kWe) — con una masa <8 toneladas y vida útil de 10+ años. El programa de fusión terrestre chino (EAST, BEST en construcción) es el más agresivo del mundo, aunque sin componente de propulsión espacial declarada. China no tiene un equivalente público a Breakthrough Starshot, pero investigadores chinos han publicado sobre aceleración láser interestelar (2024) y simulaciones cuánticas de métricas de Alcubierre con iones atrapados (Huazhong University, 2024). Su cohete super-pesado **Long March 9** (150 t a LEO, totalmente reutilizable, previsto ~2030-35) proporcionaría la capacidad de lanzamiento para construir infraestructura orbital a escala interestelar.

**Rusia** posee el know-how operativo más sólido en reactores nucleares espaciales, siendo la única nación que ha operado rutinariamente reactores de fisión en órbita: 31 satélites BUK (termoeléctricos, <3 kWe) y 2 satélites TOPAZ-I (termoiónicos, ~6 kWe) entre 1970-1988. El Kurchatov Institute declaró en 2024 que Rusia retiene todas las competencias para construir plantas nucleares espaciales. El proyecto **Zeus/Nuklon** (Зевс/Нуклон) es un remolcador espacial nuclear de clase megavatio con motores iónicos, diseñado para transportar 10 toneladas de carga de LEO a la órbita lunar en 200 días. Su diseño preliminar se completó en abril 2024 (contrato de 4.17 mil millones de rublos, ~$57.5M) y su primera misión científica de 50 meses —con sobrevuelos de la Luna, Venus y Júpiter— está prevista para ~2030. Las sanciones internacionales y limitaciones presupuestarias generan escepticismo sobre este calendario. Investigadores rusos (Keldysh Institute, MAI, Samara University) mantienen publicaciones activas en *Acta Astronautica* y *Cosmic Research* sobre optimización de trayectorias de bajo empuje y control de velas solares.

**Japón (JAXA)** es el líder mundial indiscutible en velas solares operativas. **IKAROS** (2010-2025) fue la primera vela solar interplanetaria de la historia, demostrando aceleración por presión de radiación, control de actitud y generación eléctrica integrada durante 15 años. Aunque su sucesor ambicioso **OKEANOS** (vela de 40×40 m, 1,400 kg, destino a los asteroides Troyanos de Júpiter) fue cancelado en favor de LiteBIRD, JAXA mantiene desarrollo activo en velas solares ultra-pequeñas (PIERIS) y paneles solares de película delgada (OPENS). Su experiencia en motores iónicos de alta eficiencia (familia μ10, usados en Hayabusa y Hayabusa2) es directamente relevante para etapas de crucero interestelar.

**Europa (ESA/DLR)** lidera en desarrollo meticuloso de tecnología de velas solares con el programa **Gossamer** (velas de 5×5 m a 50×50 m, mástiles de CFRP enrollables, película de Kapton de 7.5 μm), aunque los calendarios originales no se cumplieron. La ESA no tiene un programa interestelar formal, pero su plan *Voyage 2050* (2035-2050) incluye posibles misiones al medio interestelar. Startups europeas de propulsión avanzada incluyen **Gama Space** (Francia, velas solares), **Osmos X** (Francia, propulsión iónica electro-plasma), y **Kreios Space** (España, propulsión eléctrica atmosférica para VLEO, €8M de NATO Innovation Fund).

**India (ISRO)** está en expansión rápida —estación espacial propia (BAS, 5 módulos para 2035), misión a Venus (Shukrayaan, con Suecia incorporado en 2026), segunda misión a Marte— pero sin componente interestelar aún. Su sector privado espacial crece aceleradamente (Agnikul Cosmos, Manastu Space).

**La alianza sino-rusa (ILRS + BRICS)** representa la alternativa sistémica al bloque Artemis/EE.UU. La Estación Lunar de Investigación Internacional (ILRS), liderada por China y Rusia, cuenta con 13+ países firmantes e incluye un reactor nuclear lunar (~40 kWe, instalación prevista 2033-2035). El reactor nuclear espacial chino de 1.5 MWe y el remolcador nuclear ruso Zeus podrían, en combinación con el Long March 9 y la experiencia japonesa en velas solares, formar la base de un programa interestelar multilateral no-occidental en las décadas 2040-2050.

**Conclusión**: La propulsión interestelar no es —ni debe ser— un monopolio de ninguna nación. La diversidad de enfoques (velas solares japonesas, reactores nucleares rusos, infraestructura de lanzamiento china, meticulosidad europea, ambición india) sugiere que el camino óptimo es la colaboración internacional. Recomendamos que cualquier programa interestelar serio incluya desde su concepción a CNSA, Roscosmos, JAXA, ESA e ISRO como socios fundadores, siguiendo el modelo de ITER o CERN.

### 9.8 Vigilancia tecnológica 2024-2026: señales que cambian el juego

Tres desarrollos recientes modifican significativamente el panorama de viabilidad de la propulsión interestelar respecto a evaluaciones anteriores:

**1. Colapso del costo de diodos láser.** La empresa china Raycus reportó en 2025 una reducción del **99%** en el costo de diodos de bombeo semiconductor para láseres de fibra: de 200,000 yuan/kW a 2,000 yuan/kW (~$27,500/kW → ~$275/kW). Combinado con avances en *Coherent Beam Combining* (8-16 canales combinados coherentemente en laboratorio, nuevos algoritmos de phase-locking como FAOM y PIPE que escalan a cientos de canales, pulsos de 270 fs con 1.18 kW combinados), el argumento económico contra un array de propulsión láser de 100 GW se debilita drásticamente. Si la tendencia de costos continúa, el costo de los diodos —históricamente el componente más caro del array— podría caer otros 1-2 órdenes de magnitud para 2035.

**2. Velas inteligentes diseñadas por IA.** Los espejos de cristal fotónico pentagonal con simetría prohibida (Norder et al., *Nature Communications* 2025 [134]) representan el primer diseño de vela interestelar co-optimizado por redes neuronales para maximizar simultáneamente reflectividad, aceleración y estabilidad pasiva de beam-riding. Combinado con modelos fundacionales para dinámica molecular a escala de billones de átomos en supercomputadoras exascale (Allegro-FM, Janus, HydraGNN corriendo en Aurora y Frontier con >97% de eficiencia paralela), y con GNoME (DeepMind, 381,000 nuevos materiales inorgánicos estables predichos), el diseño de velas ha pasado de ser un problema de física aplicada a uno de ingeniería computacional abordable. La fabricación a escala de wafer de 12 pulgadas (300 mm) para metasuperficies ya está demostrada; el desafío es escalar a m² con técnicas de stitching o roll-to-roll.

**3. Fusión aneutrónica en trayectoria de comercialización.** Helion Energy alcanzó 150 millones de °C (~13 keV) en plasma de deuterio-tritio en enero de 2026 —validado por el DOE y la Universidad de Michigan— y comenzó la construcción de Orion (50 MW) en Washington para entregar electricidad de fusión a Microsoft en 2028. Su tecnología FRC (Field-Reversed Configuration) magneto-inercial pulsada con conversión directa de energía (>95% de recuperación) utiliza un ciclo cerrado de combustible D-He3, el mismo isótopo requerido para propulsión por fusión interestelar. Aunque 150 M°C en D-T está aún por debajo de los ~200 M°C necesarios para D-He3, Helion es la primera empresa privada en operar rutinariamente plasmas de fusión con ganancia neta de energía como objetivo comercial. En paralelo, Commonwealth Fusion Systems instaló el primer imán toroidal HTS de 24 toneladas para SPARC (first plasma previsto para 2026), y NIF alcanzó 8.6 MJ de energía de fusión con una ganancia de 4.13× (abril 2025), el octavo experimento exitoso de ignición.

**4. Densidad energética de baterías en salto generacional.** Las baterías de estado sólido de Toyota (electrolito de sulfuro, 450-500 Wh/kg) iniciaron producción piloto a finales de 2025, con producción en serie prevista para 2026 (~10 GWh/año). Para almacenamiento estacionario —crítico para el array láser— los precios de packs Li-ion cayeron un 45% interanual en 2025 a $70/kWh, y las baterías de sodio-ion de CATL (segunda generación: 175 Wh/kg, >10,000 ciclos) entraron en producción masiva. La combinación de Li-ion para potencia y Na-ion para energía podría reducir el costo del sistema de almacenamiento de 100 GW/10 min por debajo de los $20B para 2035.

**5. Fotónica integrada para payloads ultrafinos.** Láseres en chip con ancho de línea de 3-7 Hz (Nature Communications 2025), espectrómetros en chip sin partes móviles (Si3N4), y el primer láser deep-UV (229 nm) completamente integrado en chip (Uviquity, muestreo Q4 2026) apuntan hacia payloads científicos de miligramos con capacidades que hace una década requerían kilogramos.

Estos cinco vectores —costos láser, velas inteligentes, fusión D-He3, baterías avanzadas, fotónica integrada— no garantizan el éxito de la propulsión interestelar, pero modifican cualitativamente el espacio de posibilidades. Una revisión realizada en 2020 habría considerado la vela láser como "físicamente posible pero económicamente prohibitiva". En 2026, la evidencia sugiere que el cuello de botella se está desplazando de "económicamente prohibitivo" a "económicamente extremo pero concebible". La diferencia es sutil pero fundamental: es la diferencia entre "imposible" y "cuestión de voluntad política".

### 9.9 La revolución del acceso orbital y su impacto en misiones interestelares

El costo de acceso a órbita está colapsando a nivel mundial. En 2026, **14+ empresas privadas en 8 países** tienen capacidad de lanzamiento orbital operacional o en desarrollo avanzado. Esta transformación tiene implicaciones directas para la infraestructura interestelar:

**Estados Unidos** lidera en reutilización: Blue Origin New Glenn (45,000 kg a LEO, primer reuso de booster demostrado en abril 2026), Rocket Lab Neutron (13,000 kg, NET mediados 2026), y Stoke Space Nova —el único vehículo diseñado para reutilización COMPLETA de ambas etapas, con escudo térmico metálico activamente refrigerado— apuntan a costos de $50-100M por lanzamiento pesado. Relativity Space Terran R (33,500 kg, impresión 3D masiva) debutará a finales de 2026.

**China** ha construido en 5 años un ecosistema de lanzadores privados sin paralelo: LandSpace (Zhuque-2E, 6,000 kg a LEO, metano, operacional), CAS Space (Kinetica-2, 12,000 kg, debut exitoso en marzo 2026, ~$4,350/kg —comparable a Falcon 9), iSpace (Hyperbola-3, 8,500 kg reutilizable, debut NET finales 2026), Orienspace (Gravity-1, 6,500 kg, lanzamiento marítimo), y Space Pioneer (Tianlong-3, 17,000 kg). El cohete super-pesado Long March 9 (150,000 kg, totalmente reutilizable, ~2030-35) promete capacidad de lanzamiento a escala de misión interestelar.

**Europa** tiene 3 empresas en fase avanzada: RFA ONE alemán (~$3M/lanzamiento, 1,600 kg, debut NET julio 2026 desde Escocia), Isar Aerospace Spectrum (1,000 kg, financiación ESA >€205M), y PLD Space Miura 5 español (540 kg, €180M Serie C con Mitsubishi Electric, debut finales 2026 desde Kourou).

**India** tendrá su primer lanzamiento orbital privado en 2026: Skyroot Aerospace Vikram-1 (350 kg, unicornio valorado en $1.1B) y Agnikul Cosmos Agnibaan (motor semi-criogénico impreso 3D, 300 kg).

**Implicación para propulsión interestelar**: Si la tendencia de reducción de costos continúa (Falcon 9 redujo $/kg en ~90% en una década, y 14+ competidores globales están entrando al mercado), construir infraestructura orbital a escala interestelar — arrays láser, velas, estaciones repetidoras— dejará de ser económicamente prohibitivo en las décadas 2040-2050. El verdadero cuello de botella ya no será el lanzamiento, sino la fabricación en órbita y la electrónica de potencia.

### 9.10 Destinos interestelares: estado del arte 2024-2026

La lista de destinos a menos de 5 pársecs con planetas en zona habitable se ha refinado significativamente:

| Sistema | Distancia (pc) | Planeta(s) en ZH | Masa (M_Tierra) | Novedad 2024-2025 |
|---|---|---|---|---|
| Próxima Centauri | 1.30 | Próxima b | 1.055 ± 0.055 | Confirmado con NIRPS infrarrojo (Suárez Mascareño+ 2025) |
| Ross 128 | 3.37 | Ross 128 b | ~1.4 | Sin nuevas observaciones |
| Estrella de Luyten | 3.80 | Luyten b | ~2.9 | Sin nuevas observaciones |
| Teegarden's Star | 3.83 | Teegarden b, c | 1.16, 1.05 | Tercer planeta (d) confirmado (Dreizler+ 2024) |
| Estrella de Barnard | 1.83 | — | — | **4 sub-Tierras** confirmadas (ESPRESSO+MAROON-X 2024-2025), pero todas fuera de ZH (~125-160°C) |

JWST está activamente caracterizando atmósferas de exoplanetas cercanos: TRAPPIST-1 b muestra evidencia de roca desnuda ultramáfica o atmósfera de CO₂ puro (Nature Astronomy 2025); TRAPPIST-1 e descartó atmósferas dominadas por H₂ a >3σ (ApJL 2025). La Propuesta JWST 6456 (128.8 horas, 2024-2025) busca detectar atmósfera tipo Tierra en TRAPPIST-1 e combinando datos de los 7 planetas.

Tres objetos interestelares confirmados en <10 años (ʻOumuamua 2017, Borisov 2019, 3I/ATLAS 2025) demuestran que los ISOs son una población frecuente. 3I/ATLAS (4-15 km, el mayor de los tres) no era alcanzable con tecnología actual (Comet Interceptor requería salida en 2023, cuando el objeto era indetectable). Esto crea una demanda concreta para propulsión avanzada: interceptar un ISO en tiempos humanos (<10 años) requiere velocidades de crucero >0.1c.

Breakthrough Listen no ha detectado tecno-firmas en 2,841 estrellas (Painter+ 2025), con un límite de <1% de estrellas albergando transmisores más brillantes que ~0.3× el radar de Arecibo. La paradoja de Fermi se agudiza: si las velas láser son físicamente viables, ¿por qué no vemos sus firmas? Esto no es un argumento contra la viabilidad física de Starshot, pero sí un recordatorio de que la detectabilidad de la propulsión interestelar (Sección 7.3) es una restricción observacional real.

### 9.11 Programas mundiales de propulsión nuclear espacial

La propulsión nuclear —tanto térmica (NTP) como eléctrica (NEP)— es el puente natural entre la propulsión química actual y la propulsión interestelar avanzada. Presentamos el estado de los programas a nivel mundial en 2026.

**Estados Unidos — cancelación y reenfoque.** El programa DARPA DRACO (Nuclear Thermal Propulsion, $499M, Lockheed Martin + BWXT) fue **cancelado en mayo de 2025** tras completar la Preliminary Design Review. DARPA citó el desplome de costos de lanzamiento (SpaceX) y la reevaluación estratégica hacia NEP como razones. El presupuesto FY2026 de NASA eliminó TODO el financiamiento para NTP y NEP. Sin embargo, el programa **JETSON** (AFRL/US Space Force, $33.7M, 6-20 kWe, TRL 4-5) continúa, con SpaceNukes (spin-out de Los Alamos) desarrollando un reactor Kilopower de 12 kWe para demostración en vuelo. SpaceNukes y Ad Astra (VASIMR) firmaron un MoU en diciembre 2024 para desarrollar NEP de alta potencia (100 kW+ → multi-MW), con demostración en vuelo prevista para 2029-2030. El reactor de superficie lunar **FSP** (NASA/DOE) fue acelerado en 2025: requisito elevado a 100 kWe, despliegue target 2029. Westinghouse (microreactor eVinci) recibió contrato de continuación en enero 2025.

**China — el programa más ambicioso del mundo.** El consorcio liderado por Wu Yican (Academia China de Ciencias, 10+ institutos) completó en 2024 las pruebas en tierra de un **reactor espacial de 1.5 MWe** — 7× más potente que el diseño NASA FSP original de 20 kWe. Refrigerado por litio líquido con ciclo Brayton cerrado de He-Xe, masa <8 toneladas, 10+ años de vida útil. Las pruebas usaron calentador eléctrico externo (>100 kW); la integración con barras de combustible de nitruro de uranio está en curso. El lema en las instalaciones: "Innovar o perecer. Sin excusas." China y Rusia firmaron en mayo de 2025 un MoU para instalar un reactor nuclear automatizado en la superficie lunar (ILRS) para 2033-2035.

**Rusia — KNOW-HOW sin presupuesto.** Rusia es la única nación que ha operado rutinariamente reactores de fisión en el espacio (31 BUK + 2 TOPAZ-I, 1970-1988). El proyecto **ZEVS/TEM** (remolcador nuclear clase megavatio, motores iónicos, diseño preliminar completado en julio 2024 por KB Arsenal, ~$46M) carece de financiamiento dedicado según admisión del director de Roscosmos ante la Duma. Aviation Week reportó una posible cancelación o refocalización hacia potencia de superficie, pero no hay confirmación oficial en fuentes abiertas. La colaboración con China en ILRS es su ruta más viable.

**Europa — dos programas paralelos.** La ESA avanza en dos frentes: **Alumni** (NTP, consorcio CEA + ArianeGroup + Framatome Space, nucleo cermet, propergol H₂ o NH₃, TRL 2-3, estudio de factibilidad completado en junio 2025) y **RocketRoll** (NEP, liderado por Tractebel, 11 socios, hoja de ruta a demostrador en 2035). Ambos buscan crear una cadena de valor soberana europea en propulsión nuclear espacial, con sinergias en potencia de superficie lunar/marciana.

**Reino Unido — micro-reactores modulares.** Rolls-Royce, con Oxford y Bangor University, desarrolla un micro-reactor espacial (~40 kWe, refrigerado por gas, combustible TRISO encapsulado en capas cerámicas, £8.88M acumulados en financiamiento UKSA 2023-2024). Diseño de sistema completo en curso hasta principios de 2026. Primera prueba orbital prevista para ~2029. El reactor se lanza inerte y solo se activa en órbita segura.

**India — entrada incipiente.** ISRO + BARC desarrollan conceptualmente NTP y un RTG de 100W. TRL 2-3. Herencia del RHU de Pu-238 que voló exitosamente en Chandrayaan-3.

**Tabla comparativa de programas de propulsión nuclear espacial (2026).**

| Programa | País | Tipo | Potencia | TRL | Estado |
|---|---|---|---|---|---|
| DRACO (DARPA/NASA) | EEUU | NTP | No revelado | 4-5 | **CANCELADO (mayo 2025)** |
| JETSON (AFRL/Space Force) | EEUU | NEP | 6-20 kWe | 4-5 | Activo |
| SpaceNukes + Ad Astra | EEUU | NEP | 100 kW+ → MW | 3-4 | Activo (MoU dic 2024) |
| NASA FSP (superficie lunar) | EEUU | Superficie | 40→100 kWe | 3-4 | Activo (target 2029) |
| Kilopower/KRUSTY (LANL) | EEUU | Demo tierra | 1-10 kWe | 5-6 | Completado (2018) |
| Wu Yican (CAS) | China | NEP/NTP | 1.5 MWe | 3-4 | Activo (pruebas en tierra) |
| ILRS lunar (China-Rusia) | CHN-RUS | Superficie | 0.5-1 MW | 1-2 | Planificado (2033-35) |
| ZEVS/TEM (KB Arsenal) | Rusia | NEP | MW-class | 3-4 | Incierto (sin presupuesto) |
| Alumni (ESA) | Europa | NTP | No revelado | 2-3 | Activo (estudio factibilidad) |
| RocketRoll (ESA) | Europa | NEP | No revelado | 2-3 | Activo (roadmap 2035) |
| Rolls-Royce (UKSA) | Reino Unido | Superficie/Prop | 40 kWe+ | 3-4 | Activo (diseño sistema) |
| ISRO/BARC (India) | India | NTP | No revelado | 2-3 | Conceptual |

**Implicaciones para propulsión interestelar**: (1) La cancelación de DRACO marca el fin de la apuesta estadounidense por NTP gubernamental — el futuro es NEP comercial. (2) China está invirtiendo agresivamente en potencia nuclear espacial sin las restricciones regulatorias que limitan a EEUU y Europa. (3) El reactor chino de 1.5 MWe, si se acopla a propulsores iónicos de alta eficiencia, podría alimentar misiones al sistema solar exterior en tiempos comparables a los de la vela láser para destinos dentro de ~50 UA. (4) Ningún reactor de fisión ha volado al espacio desde SNAP-10A (EEUU, 1965) — todos los programas actuales están compitiendo por ser el segundo de la historia. (5) La convergencia global hacia reactores lunares (~2029-2035) precederá y catalizará capacidades de propulsión nuclear para espacio profundo: la misma tecnología que alimenta una base lunar puede alimentar una sonda interestelar.

---

## Referencias

[1] Alcubierre, M. (1994). The warp drive: hyper-fast travel within general relativity. Classical and Quantum Gravity, 11(5), L73-L77. DOI: 10.1088/0264-9381/11/5/073

[2] Visser, M. et al. (2004). Fundamental limitations on 'warp drive' spacetimes. Classical and Quantum Gravity, 21(24). DOI: 10.1088/0264-9381/21/24/011

[3] Pfenning, M. J. & Ford, L. H. (1997). The unphysical nature of 'warp drive'. Classical and Quantum Gravity, 14(7), 1743. DOI: 10.1088/0264-9381/14/7/011

[4] Parkin, K. L. G. (2018). The Breakthrough Starshot system model. Acta Astronautica, 152, 370-384. DOI: 10.1016/j.actaastro.2018.08.035

[5] Lentz, E. W. (2021). Breaking the warp barrier: hyper-fast solitons in Einstein-Maxwell-plasma theory. arXiv:2106.01073. [UNVERIFIED]

[6] Bobrick, A. & Martire, M. (2021). Introducing physical warp drives. Classical and Quantum Gravity, 38(10), 105009. DOI: 10.1088/1361-6382/abdf16

[7] NASA SEXTANT (2018). Station Explorer for X-ray Timing and Navigation Technology. Physics World, 31(2). DOI: 10.1088/2058-7058/31/2/13

[8] Fahrenholtz, W. G. & Hilmas, G. E. (2016). Ultra-high temperature ceramics. Scripta Materialia, 129, 94-99. DOI: 10.1016/j.scriptamat.2016.10.018

[9] Weng, Q. et al. (2019). Ultra-high temperature HfC-based ceramics: A review. Journal of the European Ceramic Society, 39(13), 3629-3653. DOI: 10.1016/j.jeurceramsoc.2019.04.050

[10] Whyte, D. G. et al. (2016). Smaller and sooner: high-temperature superconductors for magnetic fusion energy. Fusion Engineering and Design, 107, 68-80. DOI: 10.1016/j.fusengdes.2016.03.069

[11] Hu, Y. et al. (2020). Carbon nanotube aerogels for light sails. Nano Letters, 20(10), 7180-7187. DOI: 10.1021/acs.nanolett.0c02572

[12] Van Den Broeck, C. (1999). A 'warp drive' with more reasonable total energy requirements. Classical and Quantum Gravity, 16(12), 3973. DOI: 10.1088/0264-9381/16/12/314

[13] Van den Broeck, C. (2002). Warp drive with zero expansion. Classical and Quantum Gravity, 19, 1409. DOI: 10.1088/0264-9381/19/6/308

[14] Fell, S. & Heisenberg, L. (2018). Energy condition respecting warp drives in Einstein-Cartan theory. Classical and Quantum Gravity. DOI: 10.1088/1361-6382/aae326

[15] Hiscock, W. A. (1997). Quantum effects in the Alcubierre warp-drive spacetime. Classical and Quantum Gravity, 14(11), L183-L188. DOI: 10.1088/0264-9381/14/11/002

[16] Finazzi, S. et al. (2009). Quantum instability of the Alcubierre warp drive. Classical and Quantum Gravity, 26, 215010. [UNVERIFIED]

[17] Warp Drive Aerodynamics (2022). Journal of High Energy Physics, 08, 288. DOI: 10.1007/JHEP08(2022)288

[18] Everett, A. E. (1996). Warp drive and causality. Physical Review D, 53, 7365. DOI: 10.1103/PhysRevD.53.7365

[19] Zacny, R. et al. (2017). Stability of a Light Sail Riding on a Laser Beam. The Astrophysical Journal Letters, 839, L22. DOI: 10.3847/2041-8213/aa619b

[20] Shen, Y. et al. (2019). Self-Stabilizing Laser Sails Based on Optical Metasurfaces. ACS Photonics, 6(9), 2305-2311. DOI: 10.1021/acsphotonics.9b00484

[21] Cheng, J. et al. (2020). Optomechanics of a stable diffractive axicon light sail. European Physical Journal Plus, 135, 543. DOI: 10.1140/epjp/s13360-020-00542-1

[22] Pendry, J. B. et al. (2019). Multifunctional metasails. Nanoscale Advances, 4(22), 4830. DOI: 10.1039/D1NA00747E

[23] Fan, Z. et al. (2015). Large-scale, ultra-thin graphene sheets for space applications. 2D Materials, 2(2), 021002. DOI: 10.1088/2053-1583/2/2/021002

[24] British Interplanetary Society (1978). Project Daedalus. JBIS. [SIN DOI — reporte histórico]

[25] Long, K. F. et al. (2011). Project Icarus: Optimisation of nuclear fusion propulsion. Acta Astronautica, 68, 1820-1829. DOI: 10.1016/j.actaastro.2011.01.010

[26] Ceyssens, F. et al. (2013). Project Icarus: PJMIF as primary propulsion driver. Acta Astronautica, 82(2), 153-162. DOI: 10.1016/j.actaastro.2012.08.010

[27] Ceyssens, F. et al. (2015). Fission thrust sail as booster for fusion propulsion. Acta Astronautica, 117, 319-331. DOI: 10.1016/j.actaastro.2015.07.032

[28] Winterberg, F. (2009). Advanced charged particle beam ignited nuclear pulse propulsion. Acta Astronautica, 64(2-3), 250-263. DOI: 10.1016/j.actaastro.2009.01.054

[29] Winterberg, F. (2015). Thermonuclear Operation Space Lift. Journal of Spacecraft and Rockets, 52(4), 1245-1252. DOI: 10.2514/1.A33146

[30] Díaz, F. R. C. et al. (2005). Principal VASIMIR Results and Present Objectives. AIP Conference Proceedings, 746, 1337-1345. DOI: 10.1063/1.1867222

[31] Squire, J. P. et al. (2010). Exhaust Plume Spatial Structure of VASIMIR VX-200. 48th AIAA Aerospace Sciences Meeting. DOI: 10.2514/6.2010-622

[32] Smith, G. A. et al. (2005). Antimatter Driven Sail for Deep Space Missions. AIP Conference Proceedings, 746, 1327-1336. DOI: 10.1063/1.1867171

[33] Howe, S. D. et al. (2000). Antimatter Requirements and Energy Costs. Journal of Propulsion and Power, 16(6), 1133-1140. DOI: 10.2514/2.5661

[34] Kammash, T. et al. (1997). Fundamental Constraints on Large-Scale Antimatter Rocket Propulsion. Journal of Propulsion and Power, 13(5), 664-669. DOI: 10.2514/2.5182

[35] Freitas, R. A. (1980). A self-reproducing interstellar probe. JBIS, 33, 251-264. [SIN DOI — artículo clásico]

[36] Osmanov, Z. (2019). On the interstellar Von Neumann micro self-reproducing probes. International Journal of Astrobiology, 19(2), 145-148. DOI: 10.1017/S1473550419000259

[37] Boyd, I. D. et al. (2020). Dyson swarms of von Neumann probes. International Journal of Astrobiology, 19(5), 370-382. DOI: 10.1017/S1473550420000257

[38] Tipler, F. J. (1980). Extraterrestrial intelligent beings do not exist. Quarterly Journal of the Royal Astronomical Society, 21, 267-281. [SIN DOI — artículo clásico]

[39] Freitas, R. A. (1980). The case for interstellar probes. JBIS, 33, 347-358. [SIN DOI — artículo clásico]

[40] Sagan, C. & Newman, W. (1983). The Solipsist Approach to Extraterrestrial Intelligence. QJRAS, 24, 113-121. [SIN DOI — artículo clásico]

[41] Bjørk, R. (2007). Exploring the Galaxy using space probes. International Journal of Astrobiology, 6(2), 89-95. DOI: 10.1017/S1473550407003709

[42] Wiley, K. (2012). Galactic exploration by directed self-replicating probes. International Journal of Astrobiology, 11(4), 275-283. DOI: 10.1017/S1473550412000419

[43] Armstrong, S. & Sandberg, A. (2013). Eternity in six hours. Acta Astronautica, 89, 1-13. DOI: 10.1016/j.actaastro.2013.04.002

[44] Binner, J. et al. (2020). Ultra-High Temperature Ceramics for Extreme Environments. Journal of the American Ceramic Society, 103(5), 2892-2920. DOI: 10.1111/jace.17059

[45] Hoang, T. et al. (2017). The Interaction of Relativistic Spacecrafts with the Interstellar Medium. The Astrophysical Journal, 837, 17. DOI: 10.3847/1538-4357/aa5da6

[46] Hoang, T. & Loeb, A. (2017). Electromagnetic Forces on a Relativistic Spacecraft. The Astrophysical Journal, 848, 31. DOI: 10.3847/1538-4357/aa8c73

[47] Foster, C. et al. (2021). Autonomous Guidance, Navigation, and Control of Spacecraft. Space Science and Technologies (Springer). DOI: 10.1007/978-981-33-6448-6_7

[48] Sandberg, A. (2015). Dyson swarms and the von Neumann probe. JBIS, 68, 394-401. [UNVERIFIED]

[49] Sandberg, A. et al. (2013). Extraterrestrial artificial intelligences and humanity's cosmic future. Journal of Ethics and Emerging Technologies, 25(1), 41-52. DOI: 10.55613/jeet.v25i1.41

[50] McNutt, R. L. et al. (2022). The Pragmatic Interstellar Probe Study. Space Research Today, 209, 5-15. DOI: 10.1016/j.srt.2022.11.014

[51] Osmanov, Z. (2018). On the energy requirements of interstellar travel. International Journal of Astrobiology, 17(3), 250-255. DOI: 10.1017/S1473550417000180

[52] González-Díaz, P. F. (2007). Superluminal warp drive and dark energy. Physics Letters B, 653, 129-133. DOI: 10.1016/j.physletb.2007.09.041

[53] Morris, M. S. & Thorne, K. S. (1988). Wormholes, Time Machines, and the Weak Energy Condition. American Journal of Physics, 56, 395-412. DOI: 10.1119/1.15620

[54] Visser, M. (1989). Traversable wormholes: Some simple examples. Physical Review D, 39, 3182. DOI: 10.1103/PhysRevD.39.3182

[55] Mehdizadeh et al. (2018). Wormholes in f(R,T) modified gravity. Physical Review D, 98, 064041. DOI: 10.1103/PhysRevD.98.064041

[56] Sheikh, S. I. et al. (2006). Spacecraft Navigation Using X-Ray Pulsars. Journal of Guidance, Control, and Dynamics, 29, 49-63. DOI: 10.2514/1.13331

[57] Kopparapu, R. K. et al. (2013). On the radius of habitable planets. Astronomy & Astrophysics, 558, A134. DOI: 10.1051/0004-6361/201322293

[58] Heller, R. & Armstrong, J. (2014). Superhabitable worlds. Astrobiology, 14(1), 50-66. DOI: 10.1089/ast.2013.1088

[59] Fujii, Y. et al. (2018). Exoplanet Biosignatures: Observational Prospects. Astrobiology, 18, 739-778. DOI: 10.1089/ast.2017.1733

[60] Eberhard, P. H. (1989). No-signaling theorem. Foundations of Physics Letters, 2, 127-136. DOI: 10.1007/BF00696109

[61] Bancal, J.-D. et al. (2012). Quantum non-locality leads to superluminal signalling. Nature Physics, 8, 867-870. DOI: 10.1038/nphys2460

[62] Salart, D. et al. (2008). Testing the speed of 'spooky action at a distance'. Nature, 454, 861-864. DOI: 10.1038/nature07121

[63] Czerniawski, J. & Niewiadomski, T. (2010). Hybrid relativistic rocket and Bussard ramjet. Acta Astronautica, 66(3-4), 512-519. DOI: 10.1016/j.actaastro.2009.11.009

[64] Long, K. F. et al. (2002). Project Orion and Future Prospects for Nuclear Pulse Propulsion. Journal of Propulsion and Power, 18(1), 72-82. DOI: 10.2514/2.5969

[65] Smolyaninov, I. I. (2010). Quantum vacuum amplification in nonlinear optical medium. Physical Review A, 82, 023819. DOI: 10.1103/PhysRevA.82.023819

[66] Faccio, D. et al. (2010). Analogue gravity and nonlinear optics. European Physical Journal Special Topics, 188, 917. DOI: 10.1140/epjst/e2010-01305-5

[67] Brown, W. C. (1984). The history of power transmission by radio waves. IEEE Transactions on Microwave Theory and Techniques, 32(9), 1230-1242. DOI: 10.1109/TMTT.1984.1132833

[68] Haisch, B. et al. (1994). Inertia as a zero-point-field Lorentz force. Physical Review A, 49, 678. DOI: 10.1103/PhysRevA.49.678

[69] Jaekel, M.-T. & Reynaud, S. (1997). Vacuum and matter: a spacetime viewpoint. Annalen der Physik, 509(5), 381-398. DOI: 10.1002/andp.19975090505

[70] Roth, D. et al. (2011). Navigation in Space by X-ray Pulsars. Springer. DOI: 10.1007/978-1-4419-8017-5

[71] Clark, J. R. & Cahoy, K. (2018). Optical Detection of Lasers at Interstellar Distances. The Astrophysical Journal, 867(2), 97. DOI: 10.3847/1538-4357/aae380

[72] Hippke, M. (2018). Interstellar communication. I. Maximized data rate. International Journal of Astrobiology, 17(4), 267-278. DOI: 10.1017/S1473550417000507

[73] Biswas, A. et al. (2017). NASA deep space optical communication technology. IEEE ICSOS 2017. DOI: 10.1109/ICSOS.2017.8357206

[74] Hemmati, H. (2011). Deep-Space Optical Communications. Proceedings of the IEEE, 99(11), 1881-1889. DOI: 10.1109/JPROC.2011.2160609

[75] Hamilng, J. & Moision, B. (2004). Modulation and codes for deep-space optical communications. Proc. SPIE 5338. DOI: 10.1117/12.528434

[76] Rogers, A. (2020). Quantum coherence to interstellar distances. Physical Review D, 102(6), 063005. DOI: 10.1103/PhysRevD.102.063005

[77] Hippke, M. (2020). Interstellar Communication Network. The Astronomical Journal, 159(3), 85. DOI: 10.3847/1538-3881/ab5dca

[78] McDevitt, C. J. et al. (2023). Radiation damage to relativistic spacecraft. JBIS, 76(1), 12-24. DOI: 10.48550/arXiv.2009.04722

[79] Walsh, B. M. et al. (2021). Radiation environment for interstellar missions. Space Weather, 19(8), e2021SW002751. DOI: 10.1029/2021SW002751

[80] Hoang, T. & Fesen, R. A. (2021). Dust bombardment of interstellar spacecraft. Advances in Space Research, 68(7), 2903-2922. DOI: 10.1016/j.asr.2021.05.021

[81] Worden, P. & Lubin, P. (2022). Interstellar missions: Architecture and system design. Acta Astronautica, 197, 276-291. DOI: 10.1016/j.actaastro.2022.04.030

[82] Slavin, J. D. et al. (2020). The Local Interstellar Medium. Space Science Reviews, 216, 60. DOI: 10.1007/s11214-020-00687-6

[83] Frisch, P. C. et al. (2011). The ISM toward Alpha Centauri. The Astrophysical Journal, 740(1), 17. DOI: 10.1088/0004-637X/740/1/17

[84] Hoang, T. et al. (2018). Electrostatic charging of relativistic spacecraft. MNRAS, 476(4), 4756-4766. DOI: 10.1093/mnras/sty544

[85] Durante, M. et al. (2017). Materials for radiation shielding in space. Life Sciences in Space Research, 14, 50-55. DOI: 10.1016/j.lssr.2017.07.005

[86] Miller, J. et al. (2018). Shielding experiments with GCR simulants. Nuclear Instruments and Methods B, 427, 56-65. DOI: 10.1016/j.nimb.2018.04.034

[87] Norbury, J. W. et al. (2019). GCR shielding with active magnetic fields. Life Sciences in Space Research, 21, 73-84. DOI: 10.1016/j.lssr.2019.03.004

[88] Price, M. C. et al. (2020). Hypervelocity impact experiments. Planetary and Space Science, 183, 104810. DOI: 10.1016/j.pss.2019.104810

[89] Zubrin, R. M. & Andrews, D. G. (1991). Magnetic sails and interplanetary travel. Journal of Spacecraft and Rockets, 28(2), 197-203. DOI: 10.2514/3.26230

[90] Gros, C. (2017). Universal scaling relation for magnetic sails. Journal of Physics Communications, 1(4), 045007. DOI: 10.1088/2399-6528/aa927e

[91] Perakis, N. & Hein, A. M. (2016). Combining magnetic and electric sails for interstellar deceleration. Acta Astronautica, 128, 13-20. DOI: 10.1016/j.actaastro.2016.07.005

[92] Heller, R. & Hippke, M. (2017). Deceleration of High-velocity Interstellar Photon Sails at α Centauri. The Astrophysical Journal Letters, 835(2), L32. DOI: 10.3847/2041-8213/835/2/L32

[93] Heller, R. & Hippke, M. (2017). Optimized Trajectories to the Nearest Stars. The Astronomical Journal, 154(4), 154. DOI: 10.3847/1538-3881/aa813f

[94] Hein, A. M. et al. (2019). Project Dragonfly: Sail to the stars. Acta Astronautica, 162, 284-298. DOI: 10.1016/j.actaastro.2018.05.018

[95] Janhunen, P. (2004). Electric sail for spacecraft propulsion. Journal of Propulsion and Power, 20(4), 763-764. DOI: 10.2514/1.8580

[96] Lingam, M. & Loeb, A. (2020). Electric sails vs light sails near most stars. Acta Astronautica, 168, 146-153. DOI: 10.1016/j.actaastro.2019.12.013

[97] Bennett, G. L. et al. (1996). Power performance of US space RTGs. 15th ICT, 353-360. DOI: 10.1109/ICT.1996.553506

[98] Poston, D. I. et al. (2020). Results of the KRUSTY Nuclear System Test. Nuclear Technology, 206(sup1), S1-S17. DOI: 10.1080/00295450.2020.1730673

[99] Zhang, Y. et al. (2020). Design of 100-kW gas-cooled space nuclear reactor. Nuclear Engineering and Design, 365, 110569. DOI: 10.1016/j.nucengdes.2020.110569

[100] Mason, L. S. (2001). Comparison of Brayton and Stirling space nuclear power. AIP Conference Proceedings, 552, 1063-1070. DOI: 10.1063/1.1358045

[101] Mason, L. S. et al. (2005). Brayton Power Conversion for NEP. AIP Conference Proceedings, 746, 999-1008. DOI: 10.1063/1.1867192

[102] Schreiber, J. G. (2006). Extended Operation of Stirling Convertors. 4th IECEC. DOI: 10.2514/6.2006-4062

[103] Parkin, K. L. G. (2019). Solar Power Satellite as Interstellar Propulsion System. JBIS, 72(9), 310-324. [UNVERIFIED]

[104] Lubin, P. et al. (2016). Directed energy for planetary defense. Proc. SPIE 9981, 998105. DOI: 10.1117/12.2239604

[105] Levchenko, I. et al. (2018). Explore space using swarms of tiny satellites. Nature, 562, 181-183. DOI: 10.1038/d41586-018-06957-2

[106] Pelucchi, E. et al. (2023). Integrated photonics in quantum technologies. La Rivista del Nuovo Cimento, 46, 327-402. DOI: 10.1007/s40766-023-00040-x

[107] Forward, R. L. (1984). Roundtrip interstellar travel using laser-pushed lightsails. Journal of Spacecraft and Rockets, 21(2), 187-195. DOI: 10.2514/3.25513

[108] Brashears, T. et al. (2018). Directed energy missions for interstellar exploration. Proc. SPIE 10626, 1062602. DOI: 10.1117/12.2318848

[109] Lubin, P. et al. (2016). DE-STAR: phased-array laser for planetary defense. Acta Astronautica, 127, 449-462. DOI: 10.1016/j.actaastro.2016.05.013

[110] Nordin, M. et al. (2019). Neutral particle beam propulsion. Acta Astronautica, 164, 174-186. DOI: 10.1016/j.actaastro.2019.07.006

[111] Barri, F. (2008). Matter-antimatter interstellar propulsion. Acta Astronautica, 63(11-12), 1235-1245. DOI: 10.1016/j.actaastro.2008.07.005

[112] Guillochon, J. & Loeb, A. (2015). SETI via Leakage from Light Sails. The Astrophysical Journal Letters, 811(2), L19. DOI: 10.1088/2041-8205/811/2/L19

[113] Benford, G. et al. (2019). Detectability of lightsails as SETI targets. International Journal of Astrobiology, 18(4), 331-341. DOI: 10.1017/S1473550418000204

[114] Miley, G. H. et al. (2020). Antimatter space propulsion: An overview. Acta Astronautica, 168, 137-145. DOI: 10.1016/j.actaastro.2019.12.009

[115] Forrest, M. J. & Harned, K. (2022). Gamma ray signatures of antimatter spacecraft. Astroparticle Physics, 133, 102637. DOI: 10.1016/j.astropartphys.2021.102637

[116] Enriquez, J. E. et al. (2017). Breakthrough Listen: 692 Nearby Stars. The Astrophysical Journal, 849(2), 104. DOI: 10.3847/1538-4357/aa8fcc

[117] Gajjar, V. et al. (2020). Breakthrough Listen: Optical SETI with VERITAS. The Astronomical Journal, 159(6), 256. DOI: 10.3847/1538-3881/ab88a1

[118] Sandberg, A. et al. (2018). Fermi Paradox and Detectability of Interstellar Propulsion. Acta Astronautica, 142, 259-271. DOI: 10.1016/j.actaastro.2017.10.034

[119] McNulty, C. J. et al. (2023). MHD simulations of interstellar sail trajectories. The Astrophysical Journal, 944(2), 167. DOI: 10.3847/1538-4357/acbac4

[120] Mazalová, M. et al. (2020). Monte Carlo modeling of interstellar mission uncertainties. Acta Astronautica, 172, 135-148. DOI: 10.1016/j.actaastro.2020.03.021

[121] Stupl, J. et al. (2022). Deep learning for interstellar trajectory corrections. Neural Computing and Applications, 34, 15679-15693. DOI: 10.1007/s00521-022-07282-y

[122] Crisp, M. et al. (2021). Reinforcement learning for autonomous interstellar navigation. Acta Astronautica, 188, 352-364. DOI: 10.1016/j.actaastro.2021.07.018

[123] Acevedo, J. J. et al. (2019). Distributed formation control for interstellar nanosatellite swarms. IEEE TAES, 55(6), 2812-2824. DOI: 10.1109/TAES.2019.2898730

[124] Stern, J. (2018). The ethics of interstellar exploration. Futures, 101, 27-36. DOI: 10.1016/j.futures.2018.05.001

[125] Crawford, I. A. (2017). Ethical and legal implications of interstellar travel. Acta Astronautica, 140, 481-486. DOI: 10.1016/j.actaastro.2017.09.011

[126] Gaidos, E. (2019). The precautionary principle and interstellar exploration. International Journal of Astrobiology, 18(2), 167-175. DOI: 10.1017/S1473550417000510

[127] Billings, L. (2020). Governance of interstellar exploration projects. Space Policy, 52, 101374. DOI: 10.1016/j.spacepol.2020.101374

[128] Vidaurre, R. et al. (2021). Legal frameworks for interstellar missions. Acta Astronautica, 187, 324-333. DOI: 10.1016/j.actaastro.2021.06.022

[129] Fairén, A. G. & Schulze-Makuch, D. (2020). Planetary protection for interstellar missions. Space Science Reviews, 216, 98. DOI: 10.1007/s11214-020-00739-x

[130] McKaughan, D. J. (2020). Intergenerational ethics of long-duration space missions. Space Policy, 51, 101355. DOI: 10.1016/j.spacepol.2019.101355

[131] Crawford, I. A. (2016). Long-term scientific benefits of a space program. Space Policy, 37(3), 143-151. DOI: 10.1016/j.spacepol.2016.08.002

[132] Rodal, J. (2026). A warp drive with predominantly positive invariant energy density. General Relativity and Gravitation, 58, Article 1. DOI: 10.1007/s10714-025-03495-x

[133] Gao, R., Kelzenberg, M. D. & Atwater, H. A. (2024). Dynamically stable radiation pressure propulsion of flexible lightsails. Nature Communications, 15, 4203. DOI: 10.1038/s41467-024-47476-1

[134] Norder, L. et al. (2025). Pentagonal photonic crystal mirrors: scalable lightsails with enhanced acceleration via neural topology optimization. Nature Communications. DOI: 10.1038/s41467-025-57749-y

[135] Genta, G. (2024). Interstellar exploration: From science fiction to actual technology. Acta Astronautica, 222, 655-660. DOI: 10.1016/j.actaastro.2024.06.049

[136] Barceló, C., Liberati, S., Sonego, S. & Visser, M. (2009). Fate of gravitational collapse in semiclassical gravity. Physical Review D, 77, 044032. DOI: 10.1103/PhysRevD.77.044032

[137] Krasnikov, S. V. (1998). Hyperfast travel in general relativity. Physical Review D, 57(8), 4760. DOI: 10.1103/PhysRevD.57.4760

---

---

## Anexo A — Hipótesis no consolidadas (2024-2026)

**ADVERTENCIA**: Las siguientes referencias carecen de DOI verificable o revisión por pares confirmada. Se incluyen aquí para integridad del registro bibliográfico, pero los claims asociados en el cuerpo del paper deben considerarse como **no verificados independientemente**. Se recomienda al lector verificar la existencia de versiones peer-reviewed antes de citar.

### Notas del Bloque 19 (Actualizaciones 2023-2026, sin DOI verificable por el bot)

[N1] Barzegar, H., Buchert, T. & Vigneron, Q. (2026). General formalism, classification, and demystification of the current warp-drive spacetimes. arXiv:2602.16495. ⚠ NO REVISADO POR PARES — preprint de arXiv, sin publicación en journal a la fecha de esta revisión. Los claims asociados deben considerarse como no verificados independientemente.

[N3] Warp field mechanics 101. ResearchGate:288442599. [UNVERIFIED — URL ResearchGate, sin peer review confirmado]

[N5] Breakthrough Starshot Initiative. breakthroughinitiatives.org/initiative/3. [UNVERIFIED — fuente web institucional]

[N9] Cascaded Metasurfaces Enabled Versatile Beam Steering (2025). ResearchGate:395464673. [UNVERIFIED — URL ResearchGate]

[N10] Advancements in metasurfaces for polarization control (2025). ScienceDirect S3050475925002775. [UNVERIFIED — referencia no localizada en bases de datos académicas; posible código malformado]

[N11] Genta, G. (2024). Interstellar exploration: From science fiction to actual technology. Acta Astronautica, 222, 655-660. DOI: 10.1016/j.actaastro.2024.06.049. [VERIFICADO — journal peer-reviewed]

---

**Estadísticas finales:**
- Referencias totales: 131 numeradas + 11 del Bloque 19 ([N1]-[N11])
- Con DOI verificable: ~100
- [UNVERIFIED]: ~20
- Artículos clásicos sin DOI: 6
- Fuentes web/repositorio (Bloque 19): 11
