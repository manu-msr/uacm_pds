# Contexto global para Codex

## Proyecto

- **Curso:** Programación de Sistemas.
- **Abreviatura:** PDS.
- **Enfoque:** programación de sistemas mediante el estudio y construcción de un compilador.
- **Rol de Codex:** asistente académico para generar notas, actividades, cuadernillos, prácticas y evaluaciones coherentes con todo el curso.
- **Regla central:** nunca diseñar en el vacío. Cada entrega debe encajar en el recorrido completo, respetar el temario vigente y conectarse con los productos anteriores y posteriores.
- **Mejora continua:** antes de crear, revisar o actualizar cualquier material, consultar también el registro vivo `Mejora continua .xlsx` y aplicar las correcciones vigentes que correspondan al tipo de material.

## Fuentes operativas y jerarquía

Codex debe trabajar con las siguientes fuentes, cada una con una función distinta:

- `temario_desglosado` determina **qué contenidos corresponden**, su numeración, secuencia y alcance curricular.
- La definición de IMP de Winskel determina el lenguaje base que se implementa en las notas y clases.
- La especificación canónica aprobada de IMP++ determina las extensiones, tipos, semántica, representación e interfaces compartidas que se desarrollan en las prácticas.
- `cig/<semestre>/cig_<semestre>.md` determina **cómo adaptar pedagógicamente los materiales al grupo real de cada semestre**.
- `Mejora continua .xlsx` reúne correcciones y aprendizajes acumulados sobre los materiales del curso.
- `contenido_base/` funciona como corpus técnico y pedagógico interno de apoyo.

Reglas de prioridad:

1. Una instrucción explícita y vigente del docente prevalece sobre las reglas generales de este archivo.
2. El CIG nunca modifica por sí mismo el temario, los objetivos, la secuencia curricular ni la especificación de IMP; orienta el **andamiaje, ritmo, carga, accesibilidad, ejemplos, apoyos y formas de participación**.
3. Si una adaptación sugerida por el CIG o por `Mejora continua .xlsx` entra en conflicto con el temario, la definición base de IMP o la especificación aprobada de IMP++, no resolver el conflicto silenciosamente.
4. No reproducir en materiales para el estudiantado la procedencia interna de estas fuentes.

## 1. Perfil del curso y decisiones finales

Curso universitario de sexto semestre para estudiantes de Ingeniería de Software.

El programa se construyó de manera colaborativa. Su columna vertebral proviene de la experiencia acumulada por una profesora que ya ha impartido la materia y conoce las principales dificultades del estudiantado. Las adiciones posteriores ofrecen un panorama nuevo, pero NO deben desplazar ni inflar artificialmente esa estructura central.

### Presentación del curso

- Programación de Sistemas estudia cómo se construye software que conecta lenguajes, programas y distintos niveles de abstracción.
- El desarrollo de un compilador para el lenguaje IMP será el hilo conductor.
- Las notas y clases construirán paso a paso un compilador funcional para el IMP básico de Winskel.
- Las prácticas partirán de esa implementación y la extenderán de manera acumulativa para construir IMP++.
- El recorrido irá del reconocimiento de tokens a la generación de código C, integrando análisis léxico, sintáctico y semántico.
- Al finalizar, se recuperará esta experiencia para extraer conclusiones aplicables a otras herramientas de sistemas.

### Justificación del enfoque

- El curso conserva el nombre institucional “Programación de Sistemas”.
- El compilador se utiliza como caso de estudio integrador porque permite trabajar especificaciones formales, diseño modular, transformaciones entre representaciones, manejo de errores, corrección, eficiencia y relación entre software y niveles de abstracción.
- Las unidades 2 a 5, centradas en compiladores, son la columna vertebral.
- La Unidad 1 sitúa el caso de estudio y la Unidad 6 permite regresar conceptualmente a la programación de sistemas.

### Tecnologías y lenguajes

- Lenguaje de implementación: Python 3.
- Herramienta para análisis léxico y sintáctico: Lark.
- Lenguaje base de las notas y clases: IMP de Winskel.
- Lenguaje fuente común de las prácticas: IMP++, extensión acumulativa y compatible de IMP.
- Lenguaje destino del compilador: C.
- Control de versiones y portafolio de código: Git en un repositorio privado y compartido por el equipo.
- Sistemas permitidos: Windows o Linux.
- Entornos posibles: Visual Studio Code, PyCharm u otro editor compatible con Python.
- Compilación del C generado: GCC, Clang u otro compilador compatible.
- Las dependencias deben registrarse en `requirements.txt`, incluida la versión de Lark.

### Restricciones de alcance

- Mantener el compilador de IMP como narrativa y producto acumulativo principal.
- No pedir en las prácticas que se reproduzca sin cambios la implementación básica ya desarrollada en notas y clase; cada práctica debe partir de esa versión y plantear una extensión significativa hacia IMP++.
- No incorporar una construcción a IMP++ sin definir antes cómo afecta, cuando corresponda, al lexer, la gramática, el AST, los tipos, la semántica y la generación de C.
- NO convertir el curso en un panorama extenso de sistemas operativos, sistemas embebidos u otras áreas.
- NO introducir tecnologías no previstas sin indicación explícita del docente.
- NO introducir optimizaciones complejas, SSA, análisis interprocedural u otras técnicas avanzadas salvo petición expresa.
- Si algo resulta demasiado avanzado para el punto del curso, simplificarlo sin perder la distinción conceptual importante.
- Lark apoya la implementación, pero no sustituye la explicación de expresiones regulares, autómatas, gramáticas y métodos de análisis.
- Usar “ligador” para `linker` y “cargador” para `loader`.

## 2. Caracterización Inicial del Grupo (CIG) y adaptación semestral

### CIG vigente

Para el semestre **2026-2**, la caracterización inicial del grupo se encuentra en:

`cig/20262/cig_20262.md`

Este archivo es la fuente operativa para conocer las condiciones reales del grupo y debe consultarse antes de crear, revisar, corregir o adaptar materiales del semestre.

La estructura será semestral. Cada periodo tendrá su propia carpeta y archivo:

```text
cig/
├── 20262/
│   └── cig_20262.md
├── 20271/
│   └── cig_20271.md
└── <semestre>/
    └── cig_<semestre>.md
```

No asumir que un CIG de un semestre describe a grupos posteriores. Cuando cambie el semestre, utilizar únicamente el CIG correspondiente. Si todavía no existe uno para el periodo activo, no reutilizar silenciosamente el anterior; trabajar con los criterios preventivos generales de este contexto hasta contar con nueva evidencia.

### Uso del CIG en materiales existentes

Antes de modificar o regenerar un material ya elaborado:

1. Consultar el CIG vigente.
2. Identificar hallazgos relevantes para ese tipo de material.
3. Conservar los objetivos, contenidos, secuencia curricular y alcance técnico.
4. Adaptar, cuando los datos lo justifiquen:
   - cantidad y densidad de contenido;
   - duración y carga de trabajo previo o extraclase;
   - ritmo y granularidad de las explicaciones;
   - conocimientos previos que pueden darse por firmes;
   - cantidad de ejemplos resueltos y práctica guiada;
   - apoyos de nivelación;
   - formas y frecuencia de retroalimentación;
   - modalidades de participación;
   - accesibilidad y alternativas de acceso;
   - requisitos tecnológicos y dependencia de equipo propio;
   - organización de actividades individuales o colaborativas.
5. Evitar cambios cosméticos que no respondan a un hallazgo o a una necesidad instruccional.

La adaptación debe conservar internamente la siguiente trazabilidad:

`hallazgo del CIG → implicación pedagógica → decisión de diseño`

No es necesario mostrar esa cadena en materiales para estudiantes salvo que el docente la solicite.

### Uso del CIG en materiales nuevos

Todo material nuevo del semestre debe diseñarse desde el inicio teniendo presente el CIG vigente. No crear primero un material genérico para después “personalizarlo” superficialmente.

En particular:

- Ajustar el andamiaje a la heterogeneidad real de conocimientos previos.
- Adecuar la carga al tiempo extraclase disponible reportado por el grupo.
- Priorizar los apoyos y formas de retroalimentación que la caracterización muestre como útiles.
- Diseñar alternativas razonables cuando existan restricciones de acceso tecnológico, tiempo, trabajo, transporte u otras condiciones grupales relevantes.
- No convertir tendencias grupales en etiquetas individuales.
- No exponer nombres, correos, diagnósticos, circunstancias personales ni respuestas sensibles del instrumento.
- No inferir características que el CIG no sostenga.

### Relación entre CIG y mejora continua

El CIG y `Mejora continua .xlsx` cumplen funciones complementarias:

- El **CIG** describe al grupo actual y orienta adaptaciones específicas para ese semestre.
- **Mejora continua** conserva aprendizajes sobre los materiales y su funcionamiento a través del tiempo.

Cuando ambos sugieran una modificación compatible, integrarla. Cuando exista tensión entre ellos, priorizar la evidencia del grupo actual para decisiones de adaptación pedagógica, siempre dentro del temario y del alcance técnico vigente.

## 3. Perfil del estudiantado

Las características concretas del grupo no deben inferirse a partir de cohortes anteriores ni de supuestos generales. Para el semestre activo, consultar primero el CIG correspondiente.

Como **criterios preventivos de diseño**, considerar que en un curso de esta naturaleza pueden presentarse diferencias en:

- experiencia previa con programación, Python, C, Git, terminales y herramientas de desarrollo;
- facilidad para trabajar con abstracciones formales;
- comprensión de textos técnicos y notación;
- autonomía para resolver tareas abiertas;
- disponibilidad de tiempo fuera de clase;
- acceso a equipo y software;
- seguridad para formular preguntas o participar públicamente.

Estos puntos no describen automáticamente al grupo. Sólo deben tratarse como características reales cuando el CIG vigente u otra evidencia del curso las sostenga.

Independientemente de las diferencias del grupo, cada material debe:

- explicar paso a paso y evitar saltos lógicos innecesarios;
- seguir la progresión **intuición → ejemplo → formulación técnica → aplicación**;
- usar ejemplos pequeños en IMP antes de generalizar;
- mostrar entradas, transformaciones y salidas explícitas;
- evitar párrafos innecesariamente largos y utilizar secciones breves, listas y mini-checkpoints cuando favorezcan la comprensión;
- reforzar ideas centrales con variaciones útiles, sin repetir de forma mecánica;
- distinguir con claridad qué construye el estudiantado y qué automatiza Lark;
- ajustar el nivel de apoyo, cantidad de ejemplos y carga a partir del CIG vigente.

## 4. Objetivos e indicadores

### Objetivos del curso

- Comprender el papel de los compiladores dentro de la programación de sistemas.
- Analizar e implementar las principales fases de un compilador.
- Traducir programas de IMP e IMP++ a código C preservando su significado.
- Integrar las fases desarrolladas en un sistema modular y funcional.

### Indicadores de logro

El estudiantado deberá:
- Identificar las principales áreas de la programación de sistemas y explicar el papel de los compiladores.
- Describir las fases de un compilador y la información que se comunica entre ellas.
- Definir tokens, lexemas y reglas léxicas mediante expresiones regulares.
- Implementar con Python y Lark un analizador léxico para IMP.
- Especificar la sintaxis de IMP mediante una gramática libre de contexto.
- Implementar con Lark un analizador sintáctico que produzca una representación estructurada.
- Construir y recorrer árboles de sintaxis abstracta.
- Implementar tablas de símbolos y manejar los alcances de los identificadores.
- Construir un verificador de tipos que detecte y reporte errores semánticos.
- Generar una representación intermedia y traducir programas de IMP++ a código C.
- Comprobar que el código generado compile, se ejecute y preserve el comportamiento del programa fuente.
- Integrar las fases en un compilador modular.
- Diseñar pruebas para programas correctos y errores léxicos, sintácticos y semánticos.
- Documentar las decisiones de diseño, implementación, pruebas y tiempos de desarrollo.
- Utilizar Git para organizar el código, conservar su evolución y documentar el proyecto.

## 5. Temario vigente

El temario oficial y su desglose por unidades y temas se encuentran en el archivo `temario_desglosado`. Codex debe consultarlo antes de generar cualquier material y tratarlo como la fuente de verdad para la numeración, los títulos y el alcance de los temas.

## 6. Flujo pedagógico y narrativa

### Flujo general

`programación de sistemas -> compilador como caso de estudio -> análisis léxico -> análisis sintáctico -> análisis semántico -> generación de C -> integración -> conclusiones sobre software de sistemas`

### Dos recorridos coordinados

- **Notas y clase:** desarrollar de forma guiada una implementación funcional del IMP básico de Winskel en cada fase del compilador.
- **Prácticas:** recibir esa implementación como punto de partida y extenderla para incorporar las construcciones aprobadas de IMP++.
- La extensión es acumulativa: una construcción léxica añadida en la Práctica 1 debe conservarse e integrarse en la sintaxis, el AST, la semántica y la generación de código de las prácticas posteriores.
- Las prácticas deben exigir transferencia y toma de decisiones sobre la extensión, no la repetición literal del ejemplo resuelto en clase.

Flujo de trabajo de las prácticas:

`IMP funcional desarrollado en clase -> extensión léxica IMP++ -> extensión sintáctica y AST -> extensión semántica -> generación de C e integración`

### Repositorio docente incremental de IMP

- La carpeta raíz `IMP/` contiene el repositorio incremental del compilador del IMP básico desarrollado en notas y clase. Es un producto docente distinto de los repositorios privados de los equipos y de las extensiones de IMP++.
- Sus versiones son acumulativas: `IMP01` corresponde al lexer; `IMP02`, al lexer, parser y AST; `IMP03` agrega verificación semántica, tipos y alcances; `IMP04` agrega generación de C e integración.
- Cada vez que una nota complete una fase funcional del compilador, actualizar en la misma tarea la versión correspondiente de `IMP/` y su índice. Una fase se considera completa sólo si el código puede ejecutarse, incluye instrucciones y dependencias, cuenta con ejemplos y supera pruebas representativas.
- Si una nota sólo presenta conceptos, decisiones de diseño o fragmentos parciales, conservar la versión como pendiente; no publicar esos fragmentos como una implementación completa.
- No copiar al repositorio base las extensiones de IMP++ desarrolladas para las prácticas. `IMP/` conserva la implementación canónica del IMP de Winskel que reciben los equipos.
- Después de actualizar `IMP/`, informar explícitamente al docente qué versión cambió, qué pruebas se ejecutaron y que los archivos están listos para que él suba los cambios. No realizar la publicación externa salvo solicitud explícita.

### Narrativa por unidad

- U1: Situar la programación de sistemas y presentar el compilador, su arquitectura y sus fases.
- U2: Convertir caracteres en tokens mediante reglas léxicas, expresiones regulares y autómatas; construir el analizador léxico de IMP.
- U3: Reconocer la estructura de IMP mediante gramáticas; construir su analizador sintáctico y una representación estructurada.
- U4: Añadir significado estático mediante atributos, reglas semánticas, tipos, símbolos y alcances; construir el verificador de tipos.
- U5: Pasar de la representación validada a código C, comprobar la preservación del comportamiento e integrar el compilador.
- U6: Recuperar lo aprendido para explicar modularidad, corrección, eficiencia, portabilidad, niveles de abstracción y relación con otras herramientas de sistemas.

### Reglas de progresión

- Respetar qué conceptos ya fueron vistos y no depender de temas posteriores.
- Conectar brevemente cada tema con el producto previo y el siguiente.
- Mantener la definición de IMP de Winskel como base común a lo largo de todos los materiales.
- Mantener una sola especificación aprobada de IMP++ y aplicarla de manera consistente en todas las prácticas.
- Si la especificación de una extensión de IMP++ no está disponible, NO inventarla silenciosamente. Solicitarla o presentar una propuesta claramente marcada para aprobación antes de generar materiales o código.
- Toda decisión sobre el AST debe ser compatible con el verificador de tipos y el generador de C posteriores.
- Cada práctica debe identificar qué implementación básica de IMP recibe, qué parte de IMP++ agrega y qué interfaz entrega a la práctica siguiente.
- Las prácticas son acumulativas; no rediseñar una extensión o interfaz de manera incompatible sin explicar la migración necesaria.

## 7. Planeación semanal vigente

Semestre de 16 semanas, seguido por el periodo de certificación.

- Semana 1: 1.1 Panorama de la programación de sistemas y el compilador como caso de estudio.
- Semana 2: 1.2 Estructura y fases de un compilador; 2.1 función del analizador léxico, tokens, lexemas y patrones.
- Semana 3: 2.2 expresiones regulares; 2.3 autómatas finitos.
- Semana 4: 2.4 reglas léxicas y tabla de símbolos; 2.5 diseño e implementación del analizador léxico. Entrega de la Práctica 1.
- Semana 5: 3.1 gramáticas libres de contexto, derivaciones y árboles.
- Semana 6: primer examen parcial. NO desarrollar temas nuevos.
- Semana 7: 3.2 ambigüedad y transformación de gramáticas; 3.3 análisis descendente, predictivo y LL.
- Semana 8: 3.4 análisis ascendente y LR; 3.5 construcción y manejo de errores del analizador sintáctico.
- Semana 9: 4.1 traducción dirigida por la sintaxis y atributos. Entrega de la Práctica 2.
- Semana 10: 4.2 reglas y esquemas de traducción; 4.3 tipos, símbolos y alcances.
- Semana 11: segundo examen parcial. NO desarrollar temas nuevos.
- Semana 12: 4.4 verificación de tipos e implementación del analizador semántico.
- Semana 13: 5.1 lenguajes fuente, intermedio y destino; 5.2 AST y código de tres direcciones. Entrega de la Práctica 3.
- Semana 14: 5.3 selección de instrucciones y generación de código C.
- Semana 15: 5.4 preservación y evaluación; 5.5 integración y pruebas; 6.1 síntesis de la programación de sistemas.
- Semana 16: tercer examen parcial. NO desarrollar temas nuevos.
- Periodo de certificación: entrega de la Práctica 4 integradora.

### Reglas de calendario

- Las semanas de examen no incluyen desarrollo de temas.
- No colocar una práctica en la misma semana ni en la semana inmediatamente anterior a un examen.
- Distribución vigente: Práctica 1 en semana 4, examen en semana 6; Práctica 2 en semana 9, examen en semana 11; Práctica 3 en semana 13, examen en semana 16; Práctica 4 en certificación.

## 8. Prácticas acumulativas: Python, Lark, IMP++ y C

Punto de partida común: el compilador del IMP básico de Winskel desarrollado en notas y clase.

Lenguaje común de las prácticas: IMP++, definido como la siguiente extensión acumulativa y compatible de IMP. Esta es la especificación canónica aprobada para las cuatro prácticas.

### Organización de los equipos y del repositorio

- Todas las prácticas se realizan en equipos de una a tres personas.
- Cada equipo trabaja en un repositorio Git privado y acumulativo para las cuatro prácticas.
- En la Práctica 1, el equipo debe crear el repositorio, dar acceso a todas las personas integrantes y añadir a `manu-msr` como colaborador.
- El `README.md` debe registrar los nombres y usuarios de Git de quienes integran el equipo.
- El historial debe permitir reconocer la evolución del compilador y la participación del equipo.

### Especificación canónica de IMP++

IMP++ conserva las construcciones de IMP y agrega:

- declaraciones con tipos `int` y `bool`;
- bloques delimitados por `{` y `}` con alcance anidado;
- salida mediante `print`;
- ciclos `for`;
- actualizaciones `++` y `--`;
- identificadores que pueden contener guion bajo;
- comentarios de una línea iniciados por `//`.

Quedan fuera de esta versión: funciones, arreglos, cadenas, `break`, `continue` y entrada interactiva.

Gramática concreta aprobada:

```ebnf
programa      ::= declaracion* sentencia+

declaracion   ::= tipo LOC ":=" expresion ";"
tipo          ::= "int" | "bool"

sentencia     ::= "skip" ";"
                | asignacion ";"
                | LOC "++" ";"
                | LOC "--" ";"
                | "print" "(" expresion ")" ";"
                | "if" expresion "then" bloque "else" bloque
                | "while" expresion "do" bloque
                | "for" "(" asignacion ";" expresion ";" actualizacion ")" bloque
                | bloque

bloque        ::= "{" declaracion* sentencia* "}"

asignacion    ::= LOC ":=" expresion
actualizacion ::= asignacion | LOC "++" | LOC "--"

expresion     ::= disyuncion
disyuncion    ::= conjuncion ("||" conjuncion)*
conjuncion    ::= igualdad ("&&" igualdad)*
igualdad      ::= comparacion ("=" comparacion)?
comparacion   ::= suma ("<=" suma)?
suma          ::= producto (("+" | "-") producto)*
producto      ::= unaria ("*" unaria)*
unaria        ::= "!" unaria | "-" unaria | primaria
primaria      ::= NUM | "true" | "false" | LOC | "(" expresion ")"
```

#### Especificación léxica e interfaz de tokens

- `NUM = [0-9]+`.
- En IMP básico, `LOC = [A-Za-z]+[0-9]*`.
- En IMP++, `LOC = [A-Za-z][A-Za-z0-9_]*`.
- `COMMENT = //[^\n]*`; los comentarios y los espacios se ignoran.
- Los tokens compuestos `:=`, `<=`, `&&`, `||`, `++` y `--` deben reconocerse completos, antes que sus prefijos.
- Palabras reservadas heredadas de IMP: `true`, `false`, `skip`, `if`, `then`, `else`, `while` y `do`.
- Palabras reservadas nuevas de IMP++: `int`, `bool`, `print` y `for`.
- Nombres estables de tokens heredados: `NUM`, `LOC`, `TRUE`, `FALSE`, `SKIP`, `IF`, `THEN`, `ELSE`, `WHILE`, `DO`, `PLUS`, `MINUS`, `TIMES`, `EQ`, `LE`, `NOT`, `AND`, `OR`, `ASSIGN`, `SEMI`, `LPAR` y `RPAR`.
- Nombres estables de tokens nuevos: `INT`, `BOOL`, `PRINT`, `FOR`, `LBRACE`, `RBRACE`, `INC`, `DEC` y `COMMENT`. `COMMENT` no se entrega al parser porque se ignora.

#### Compatibilidad, tipos y alcances

- Todo programa válido de IMP debe seguir siendo reconocido por IMP++.
- Una localidad usada sin declaración explícita se considera una variable global implícita de tipo `int`; esto conserva la compatibilidad con IMP.
- Una declaración introduce una variable en el alcance actual. Declarar dos veces el mismo nombre en ese alcance es un error; un bloque anidado sí puede ocultar una declaración externa.
- Los inicializadores y las asignaciones requieren tipos iguales.
- `+`, `-`, `*`, `++`, `--` y `<=` operan sobre enteros; `<=` produce un booleano.
- `!`, `&&` y `||` operan sobre booleanos.
- `=` compara expresiones del mismo tipo y produce un booleano.
- Las condiciones de `if`, `while` y `for` deben ser booleanas.
- `print` acepta expresiones enteras o booleanas.

#### Desazucarado y representación

- `X++` se representa como `X := X + 1`.
- `X--` se representa como `X := X - 1`.
- `for (inicio; condicion; actualizacion) { cuerpo }` se representa como `inicio; while condicion do { cuerpo; actualizacion; }`.
- El desazucarado se realiza en la fase sintáctica o al construir el AST, después de reconocer y conservar correctamente los tokens de IMP++.
- La Práctica 1 entrega el lexer extendido; la Práctica 2 integra esta gramática y el desazucarado; la Práctica 3 implementa tipos y alcances; la Práctica 4 traduce las construcciones resultantes a C.

### Práctica 1. Extensión del analizador léxico para IMP++

- Partir del analizador léxico funcional de IMP desarrollado en notas y clase.
- Agregar `INT`, `BOOL`, `PRINT`, `FOR`, `LBRACE`, `RBRACE`, `INC`, `DEC` y comentarios ignorados; extender `LOC` para admitir guion bajo.
- Extender el analizador con Python y Lark sin alterar el reconocimiento de IMP básico.
- Para trabajar el lexer de forma independiente puede utilizarse Lark con `parser=None`, `lexer="basic"` y el método `lex()`.
- Probar entradas de IMP, entradas nuevas de IMP++ y errores léxicos.

### Práctica 2. Extensión del analizador sintáctico para IMP++

- Partir del analizador sintáctico y del AST funcionales para IMP desarrollados en notas y clase.
- Extender la gramática y el AST para las construcciones de IMP++ introducidas en la Práctica 1.
- Integrar el lexer extendido y usar Lark, preferentemente mediante `parser="lalr"` cuando la gramática lo permita.
- Probar programas de IMP, programas de IMP++ y errores sintácticos.

### Práctica 3. Extensión del análisis semántico para IMP++

- Partir del verificador funcional para IMP desarrollado en notas y clase.
- Definir e implementar las reglas semánticas o de tipos que requieran las construcciones de IMP++.
- Recorrer el AST extendido y conservar la gestión de símbolos y alcances.
- Probar casos correctos y errores semánticos de IMP++ sin romper los casos de IMP.

### Práctica 4. Generación de código para IMP++ e integración

- Partir del generador de C para IMP desarrollado en notas y clase.
- Traducir a C las construcciones incorporadas en IMP++.
- Integrar las versiones extendidas del análisis léxico, sintáctico y semántico con la generación de código.
- Compilar y ejecutar el C generado.
- Comparar resultados obtenidos con el comportamiento esperado.
- Entregar durante el periodo de certificación.

### Reglas técnicas

- Lark debe usarse en las fases léxica y sintáctica.
- El verificador de tipos y el generador de C deben implementarse explícitamente en Python mediante recorridos sobre la representación construida.
- No permitir que `Transformer` o `Visitor` oculten la explicación conceptual: documentar qué información recibe y produce cada recorrido.
- Cada práctica extiende la anterior y debe conservar interfaces claras entre fases.
- La implementación básica proporcionada en clase debe ser funcional, breve y estar disponible como punto de partida antes de solicitar su extensión.
- Incluir ejemplos mínimos compartidos de IMP e IMP++ para comprobar tanto la compatibilidad hacia atrás como el pipeline extendido.

## 9. Certificación y portafolio

Modalidad: Portafolio.

### Distribución

- Tres exámenes parciales colegiados: 60% total, 20% cada uno.
- Cuatro prácticas acumulativas: 40% total, 10% cada una.
- No existe un proyecto final con porcentaje separado; la Práctica 4 es la integración final dentro del 40%.

### Reporte de cada práctica

- Introducción: propósito y problema que se resolverá.
- Desarrollo: análisis, entradas, salidas, solución, decisiones de diseño e implementación.
- Conclusiones: resultados, dificultades, aprendizajes y áreas de mejora.
- Evidencias de funcionamiento.
- Pruebas realizadas y resultados.
- Manejo de casos de error.
- Estimación inicial y tiempo real de desarrollo.
- Referencia al código fuente en el repositorio.

### Repositorio Git privado, colaborativo y acumulativo

Estructura sugerida:

```text
/practicas/
    practica1_analizador_lexico/
    practica2_analizador_sintactico/
    practica3_verificador_tipos/
    practica4_generacion_codigo/
/ejemplos_imp/
/pruebas/
README.md
requirements.txt
```

El repositorio deberá incluir:
- acceso para las personas integrantes del equipo y para `manu-msr`;
- identificación del equipo en el `README.md`;
- `README.md` con descripción, instalación y ejecución.
- `requirements.txt` con la versión de Lark.
- Código modular y con nombres descriptivos.
- Documentación de componentes relevantes.
- Ejemplos de IMP y resultados esperados.
- Pruebas para casos correctos y casos de error.
- Historial que permita observar la evolución del compilador.

### Producto final esperado

`programa IMP++ -> análisis léxico -> análisis sintáctico -> verificación de tipos -> generación de C`

El compilador debe procesar programas válidos, reportar los errores detectados y generar C que compile y se ejecute con los resultados esperados.

## 10. Plantilla obligatoria para notas de clase

Cuando el usuario pida notas de clase, usar esta estructura:

1. Título con curso, unidad y tema.
2. Párrafo de introducción presentando qué se verá.
3. Secciones de contenido alineadas con el tema vigente y las fuentes técnicas.
4. Párrafo de conclusión.
5. Referencias.

### Reglas de estilo

- No crear secciones separadas llamadas “Unidad” o “Tema”; incluir esa información en el título.
- No cerrar con “Resumen conceptual” ni “Preguntas de reflexión”, salvo petición explícita.
- Mantener ejemplos, definiciones y observaciones dentro de las secciones donde sean útiles.
- Numerar las observaciones.
- En LaTeX, escribir tecnologías, lenguajes y herramientas con `\textsc{...}`; por ejemplo, `\textsc{Python}`, `\textsc{Lark}`, `\textsc{IMP}` y `\textsc{C}`.
- La conclusión debe conectar con el siguiente paso sin desarrollar contenido todavía no visto.
- Las referencias deben provenir de `contenido_base` o de fuentes explícitamente aceptadas para el curso.

## 11. Estrategias didácticas

A) Intuición primero
- Iniciar con el problema que resuelve el concepto.
- Ofrecer un ejemplo o analogía corta.
- Introducir después la formulación técnica.

B) Ejemplo guiado
- Mostrar entrada → pasos intermedios → salida.
- Señalar en qué se fija el compilador y qué decisión toma.
- En ejemplos acumulativos, mostrar la salida de una fase como entrada de la siguiente.

C) Incrementalidad
- Primera versión: caso correcto y mínimo.
- Segunda versión: error típico y su detección.
- Tercera versión: caso borde, si aplica.

D) Microevaluación
- Integrar mini-checkpoints dentro del contenido cuando sean útiles.
- No convertirlos en una sección extensa de ejercicios; los ejercicios completos pertenecen al cuadernillo.

E) Lenguaje claro
- Evitar definiciones enciclopédicas y formalismo innecesario.
- Si una definición formal es indispensable, acompañarla inmediatamente con un ejemplo.
- Evitar que el estudiante salte al código antes de analizar el problema.

## 12. Fuentes pedagógicas y diseño instruccional

En `contenido_base` se encuentran las fuentes técnicas del curso. Los materiales sobre pedagogía, diseño instruccional y elaboración de recursos didácticos están reunidos en la subcarpeta `contenido_base/pedagogicos`. Estos materiales sirven para decidir estructura, mediación, ritmo, señalización, ejemplos, accesibilidad y evaluación; NO deben utilizarse para agregar contenido técnico ajeno al temario.

### Reglas de consulta

- Para fundamentar conceptos de programación de sistemas y compiladores, consultar las fuentes técnicas ubicadas en `contenido_base` y sus recursos auxiliares correspondientes.
- Para diseñar notas, cuadernillos, actividades, presentaciones, videos y evaluaciones, consultar también `contenido_base/pedagogicos` y aplicar sus orientaciones cuando sean pertinentes.
- Mantener separadas ambas funciones: las fuentes técnicas determinan el contenido disciplinar; las fuentes pedagógicas orientan cómo organizarlo, explicarlo y evaluarlo.

### Fuentes pedagógicas disponibles en `contenido_base/pedagogicos`

- Aprendizaje combinado.pdf
- Designing Instructional Materials – Instruction in Libraries and Information Centers.pdf
- EJ1233924.pdf
- Engaging Students with Guided Notes _ U-M LSA LSA Technology Services.pdf
- Evidence-Based Presentation Design Recommendations.pdf
- FyfeMcNeilSonGoldstone2014_EdPsychRev.pdf
- Guía-secuencias-didacticas_Angel Díaz.pdf
- How Students Attempt to Reduce Abstraction in the Learning of Mathematics and in the Learning of Computer Science.pdf

### Buenas prácticas

- Reducir información extránea y mantener una idea central por bloque.
- Usar encabezados claros, listas breves, contraste alto y espacio visual.
- Incluir una pregunta guía o mapa breve cuando facilite la navegación.
- Seguir la progresión concreto → abstracto → regreso al ejemplo.
- En procedimientos, usar problema → análisis → solución → verificación.
- Usar notas guiadas y pausas de procesamiento en temas difíciles.
- En presentaciones, preferir diagramas o esquemas frente a texto largo.
- No usar imágenes decorativas.
- Diseñar secuencias como apertura -> desarrollo -> cierre.
- Pensar la evaluación desde el diseño: diagnóstico, retroalimentación y evidencia final.
- En materiales para estudiantes, no mencionar `contenido_base`, este contexto ni fuentes internas.

## 13. Fuente técnica especial: Beck y OCR

### Archivo original

- `contenido_base/System Software An Introduction To Systems Programming by Leland L. Beck (z-lib.org).pdf`

### Archivos auxiliares esperados

- `contenido_base/texto/beck_mapa.md`
- `contenido_base/texto/beck_ocr_instrucciones.md`
- `contenido_base/ocr/beck_ocr.pdf`
- `contenido_base/texto/beck.txt`

### Reglas operativas

- El PDF original está escaneado como imagen; `pdftotext` no extrae texto útil directamente.
- Consultar primero `contenido_base/texto/beck.txt` y buscar con `rg`.
- Si no existe, usar `beck_mapa.md` para localizar capítulos, sin inventar detalles.
- El OCR sirve para localizar; las afirmaciones finas deben contrastarse con el PDF OCR o páginas renderizadas.
- No mencionar OCR, mapas internos o `contenido_base` en materiales para estudiantes.

### Uso conceptual

- Beck sirve para presentar áreas de la programación de sistemas y su relación con la arquitectura de máquina.
- En U1, usarlo para el panorama y para justificar al compilador como software de sistemas.
- En U2-U5, priorizar fuentes de compiladores; usar Beck sólo para conexiones puntuales.
- En U6, usarlo para relacionar el compilador con ensambladores, cargadores, ligadores, máquinas virtuales, editores y depuradores, sin convertir el cierre en otra unidad panorámica extensa.

### Terminología

- `linker` = ligador.
- `loader` = cargador.
- Distinguir “lenguaje ensamblador” de “ensamblador” como herramienta.

## 14. Entregables y formato esperado

### 14.1 Notas de clase
- Usar la plantilla de la sección 9.
- Ubicar el tema dentro del pipeline sólo cuando ayude a comprenderlo.
- Al terminar una nota, evaluar si ya contiene una fase funcional completa del compilador. Si es así, actualizar la versión correspondiente y el índice de `IMP/`, verificarla e informar al docente que está lista para subir.

### 14.2 Cuadernillos de ejercicios
- Asociarlos a una nota específica y nombrarlos “Cuadernillo de ejercicios NN”.
- Usar ejercicios breves, graduados y con espacio para responder.
- Incluir sólo conceptos ya vistos.
- Mantener el estilo visual de las notas.
- Generar versión para estudiantes y versión para el profesor con sufijo `_respuestas_profesor`.
- En la versión del profesor, colocar cada respuesta después de su ejercicio; no usar una clave final salvo petición.

### 14.3 Actividades en clase
- Incluir objetivo, instrucciones, tiempo sugerido y solución o guía breve.
- Priorizar trabajo en parejas y discusión guiada cuando aplique.

### 14.4 Prácticas
- Respetar la definición acumulativa de la sección 7.
- Incluir consigna, producto esperado, casos de prueba mínimos, criterios de entrega y relación con la práctica anterior y la siguiente.
- No modificar silenciosamente la gramática, el AST o las interfaces compartidas.
- Preparar ejemplos que permitan verificar cada fase de forma aislada y el pipeline integrado.

### 14.5 Exámenes, quizzes o Kahoot
- Alinear las preguntas con el nivel realmente trabajado.
- Combinar definiciones aplicadas, trazas, construcción breve y diagnóstico de errores.
- Incluir clave de respuestas y justificación breve.
- Recordar que los tres parciales son colegiados.

### 14.6 Ejercicios guiados de compiladores
- Indicar siempre entrada -> transformación -> salida esperada.
- Mostrar el procedimiento como una receta razonada.
- Usar IMP como lenguaje común salvo indicación distinta.

### 14.7 Presentación semanal, video y evaluación breve
- La presentación semanal habla del tema, no de la logística ni del video.
- El video complementa las notas con explicaciones y ejemplos; no las lee ni las duplica.
- La evaluación breve predeterminada consta de dos preguntas de opción múltiple, dos de verdadero/falso y una de ordenar con máximo cuatro elementos.

## 15. Consistencia y control de alcance

- No asumir conocimientos de temas futuros.
- No inventar la especificación de IMP, reglas de tipos o traducción a C.
- No cambiar nombres de nodos, formatos del AST o contratos entre módulos sin propagar el cambio.
- No introducir estructuras o teoría avanzada que no sean necesarias para los indicadores.
- No hacer que Lark resuelva automáticamente aquello que la actividad pretende que el estudiante comprenda.
- Si una petición queda fuera de alcance, proponer una versión básica alineada o advertirlo explícitamente.
- Conservar siempre el hilo: cada fase recibe una representación, la valida o transforma y produce la entrada de la fase siguiente.

## 16. Mejora continua y retroalimentación acumulativa

### Fuente operativa

- El archivo `Mejora continua .xlsx`, ubicado en la raíz del proyecto, es el registro vivo de observaciones y propuestas de corrección sobre los materiales del curso.
- Debe consultarse antes de crear, revisar, corregir o regenerar cualquier material, aunque la petición no lo mencione expresamente.
- Las filas que se añadan al archivo se consideran retroalimentación acumulativa para entregas posteriores. Aplicar todas las correcciones pertinentes según la semana y el tipo de material, no sólo la entrada más reciente.
- Si una observación es generalizable, aplicarla también a materiales equivalentes de otras semanas cuando corresponda.
- Si una corrección entra en conflicto con el temario, la planeación, la definición base de IMP, la especificación aprobada de IMP++ o una instrucción explícita vigente del docente, no resolver el conflicto silenciosamente: señalarlo antes de producir el material.
- No mencionar este registro interno ni quién detectó la observación en los materiales destinados al estudiantado.

### Corrección vigente

- En los cuadernillos con ejercicios que incluyan un banco de palabras, desordenar las palabras respecto de la secuencia de respuestas. Verificar que el banco no revele las respuestas por aparecer en el mismo orden en que deben utilizarse.

## 17. Instrucción final para Codex

Ante cualquier petición:

1. Identificar el semestre activo y consultar su CIG en `cig/<semestre>/cig_<semestre>.md`.
2. Consultar `Mejora continua .xlsx` y determinar qué observaciones acumuladas son aplicables a la entrega.
3. Identificar unidad, tema, semana y posición dentro del pipeline.
4. Determinar qué productos de prácticas ya existen y cuáles debe preparar el material.
5. Respetar los prerrequisitos y usar sólo lo visto hasta ese punto.
6. Verificar la especificación vigente de IMP y las interfaces compartidas antes de generar código o ejercicios dependientes de ellas.
7. Traducir los hallazgos pertinentes del CIG en decisiones de diseño sin modificar el alcance curricular.
8. Aplicar las estrategias didácticas de este contexto y las correcciones pertinentes del registro de mejora continua.
9. Mantener coherencia terminológica, técnica y narrativa.
10. Entregar únicamente la pieza solicitada en su formato correspondiente.
11. Revisar que la pieza contribuya a **notas → video complementario → actividad guiada → repaso/evaluación**, sin duplicar funciones.
12. Si se modifica un material existente, comprobar que la adaptación al CIG preserve su propósito original y la continuidad con los materiales anteriores y posteriores.
13. Si una nota completa una fase funcional del compilador, sincronizar `IMP/`, ejecutar sus pruebas e informar que la versión está lista para que el docente la suba.
