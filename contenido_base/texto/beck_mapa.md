# Mapa de uso: Beck, _System Software_

Fuente original:
- `contenido_base/System Software An Introduction To Systems Programming by Leland L. Beck (z-lib.org).pdf`

Estado del archivo:
- El PDF original está escaneado como imagen.
- `pdftotext` no extrae texto útil directamente del original.
- La versión OCR generada está en `contenido_base/ocr/beck_ocr.pdf`.
- El texto extraído está en `contenido_base/texto/beck.txt`.
- El OCR sirve para búsqueda y localización de temas; si una nota depende de una afirmación puntual, verificar el pasaje específico antes de usarlo.

Referencia bibliográfica sugerida:
- Beck, L. L. (1997). _System Software: An Introduction to Systems Programming_ (3rd ed.). Addison-Wesley.

## Uso en el curso

Beck debe usarse como fuente técnica de apoyo para ubicar áreas de la programación de sistemas, especialmente cuando el tema requiera relacionar arquitectura de máquina y software de sistemas.

No debe usarse para adelantar detalles internos antes de que el temario los permita. En notas tempranas, basta con usarlo para clasificar áreas y nombrar herramientas.

## Capítulos relevantes

- Capítulo 1, `Background`: relación entre arquitectura de máquina y software de sistemas; introducción al enfoque del libro.
- Capítulo 2, `Assemblers`: ensambladores; funciones básicas, rasgos dependientes e independientes de la máquina y opciones de diseño.
- Capítulo 3, `Loaders and Linkers`: cargadores y ligadores; reubicación, ligadura, búsqueda de bibliotecas y opciones de diseño.
- Capítulo 4, `Macro Processors`: macroprocesadores; definición, expansión y alternativas de diseño.
- Capítulo 5, `Compilers`: compiladores; funciones básicas, análisis léxico, análisis sintáctico, generación de código, intérpretes y opciones de diseño.
- Capítulo 6, `Operating Systems`: sistemas operativos; funciones básicas, ambiente de ejecución, planificación, entrada/salida, memoria, protección y opciones de diseño.
- Capítulo 7, `Other System Software`: otros sistemas de software; gestores de bases de datos, editores de texto y depuradores interactivos.
- Capítulo 8, `Software Engineering Issues`: conceptos de ingeniería de software útiles para discutir diseño, especificación, modularidad y pruebas de software de sistemas.

## Terminología para materiales del curso

- Traducir `linker` siempre como `ligador`.
- Traducir `loader` como `cargador`.
- Usar `lenguaje ensamblador` cuando se hable del lenguaje de bajo nivel.
- Usar `ensamblador` cuando se hable de la herramienta que traduce lenguaje ensamblador.
- En materiales LaTeX, escribir nombres de tecnologías, lenguajes y herramientas con `\textsc{...}` cuando corresponda al estilo de la nota.

## Regla de uso por alcance

- Unidad 1: usar Beck solo para ubicar áreas y herramientas de software de sistemas.
- Unidades 2 a 5: usar Beck cuando apoye la narrativa de traductores, pero priorizar fuentes específicas de compiladores cuando el tema sea léxico, sintáctico, semántico o generación de código.
- Unidad 6: usar Beck con más detalle para sistemas operativos, ensambladores, cargadores, ligadores, máquinas virtuales y herramientas de análisis.
