# Práctica 1: lexer de IMP++

El proyecto contiene un analizador léxico funcional para IMP. La práctica
consiste en extender `imp.lark` para reconocer IMP++ sin romper los casos base.
Se trabaja en equipos de una a tres personas.

## Equipo y repositorio

<!-- TODO: completa esta sección antes de entregar. -->

- Nombre del equipo:
- Integrantes y usuarios de GitHub:
- Enlace al repositorio privado:
- Estado de la invitación a `manu-msr`:

## Preparación

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

Instala la dependencia:

```bash
python -m pip install -r requirements.txt
```

## Orden de trabajo

1. Ejecuta el ejemplo y las pruebas base. Deben pasar desde el inicio.
2. Completa los `TODO` de `imp.lark` por bloques.
3. Retira en `tests/test_lexer_imp_mas_mas.py` sólo el `@unittest.skip` de la
   característica que acabas de implementar.
4. Corrige la especificación hasta que pasen todas las pruebas.
5. Agrega un caso válido propio y otro con un carácter no reconocido.

## Comandos

```bash
python lexer.py ejemplos/imp_base.imp
python -m unittest -v
python lexer.py ejemplos/imp_mas_mas.imp
python lexer.py ejemplos/error_lexico.imp
```

Al inicio, las pruebas de IMP deben pasar y las de IMP++ deben aparecer como
`skipped`. El ejemplo `error_lexico.imp` debe terminar con línea, columna y
carácter no reconocido.

## Registro de trabajo

<!-- TODO: completa esta sección antes de entregar. -->

- Resultado final de las pruebas:
- Decisión tomada sobre una regla léxica:
- Estimación inicial:
- Tiempo real:

## Antes de entregar

- [ ] El repositorio es privado y da acceso al equipo y a `manu-msr`.
- [ ] El equipo tiene como máximo tres integrantes.
- [ ] Una persona del equipo publicó la liga al repositorio en los comentarios de la actividad en Google Classroom.
- [ ] Las pruebas de IMP y de IMP++ pasan.
- [ ] No queda ningún `@unittest.skip` ni `TODO`.
- [ ] Se agregó un caso válido y uno con error léxico.
- [ ] `requirements.txt` conserva la versión de Lark.
