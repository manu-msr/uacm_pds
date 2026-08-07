# Práctica 1: analizador léxico para IMP

Esta carpeta contiene el punto de partida de la práctica. Los archivos tienen una
versión mínima funcional y tareas marcadas con `TODO`. No contienen la solución
completa.

## Convención concreta de trabajo

La sintaxis abstracta de IMP se toma de Winskel. Para escribir archivos de texto
usaremos esta convención ASCII:

- localidades: una o más letras, seguidas opcionalmente por dígitos;
- numerales: uno o más dígitos; el signo `-` se reconoce por separado;
- aritmética: `+`, `-`, `*`;
- booleanos: `true`, `false`, `=`, `<=`, `!`, `&&`, `||`;
- comandos: `skip`, `:=`, `;`, `if`, `then`, `else`, `while`, `do`;
- agrupación: `(` y `)`;
- espacios, tabuladores y saltos de línea: se reconocen, pero no se emiten.

Esta convención concreta no añade comandos a IMP. Sólo fija cómo se escribirán sus
símbolos durante el curso.

## Archivos que se completan

- `afd_localidades.py`: AFD manual para el patrón de las localidades.
- `lexer_imp.py`: especificación léxica incremental con Lark y tabla inicial de
  localidades.
- `pruebas_lexer.py`: pruebas que se habilitan conforme avanza la práctica.

`probar_lexer.py` es el controlador para observar la salida. La carpeta `ejemplos`
contiene entradas para las distintas etapas.

## Preparación

Crear y activar un entorno virtual:

```bash
python -m venv .venv
```

En Linux:

```bash
source .venv/bin/activate
```

En PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar la dependencia registrada:

```bash
python -m pip install -r requirements.txt
```

## Primeras ejecuciones

El estado inicial sólo reconoce localidades:

```bash
python probar_lexer.py ejemplos/minimo.imp
```

Ejecutar las pruebas habilitadas:

```bash
python -m unittest -v pruebas_lexer.py
```

Cuando se complete la gramática:

```bash
python probar_lexer.py ejemplos/flujo.imp --tabla
python probar_lexer.py ejemplos/error.imp
```

## Regla de trabajo

Realiza un cambio pequeño, ejecuta una prueba, registra el resultado y crea un commit
descriptivo. No habilites una prueba hasta llegar al paso indicado en su comentario.
