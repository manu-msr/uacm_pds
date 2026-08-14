# IMP

Manuel Soto Romero

This repository documents the incremental design and implementation of a
compiler for **IMP**, the imperative language presented by Glynn Winskel. Each
version incorporates a complete compiler phase while preserving the components
developed in previous versions, from lexical analysis to C code generation.

The compiler is implemented in **Python**. **Lark** supports lexical and syntax
analysis, while the semantic checker and C code generator are implemented
through explicit traversals of the compiler's intermediate representations.
The repository contains the base IMP compiler developed in the course notes;
the IMP++ extensions belong to the student practice repositories.

## Repository Contents

### Lexical Analysis

* [IMP v1](IMP01): Lexical analyzer that converts IMP source text into tokens
  with type, lexeme, line, and column information.

### Syntax Analysis

* [IMP v2](IMP02): Preserves the lexical analyzer from v1 and adds the IMP
  grammar, parser, and abstract syntax tree.

### Semantic Analysis

* [IMP v3](IMP03): Preserves v2 and adds semantic verification, type rules,
  symbol information, and scope management.

### Code Generation

* [IMP v4](IMP04): Preserves v3 and adds C code generation and the integrated
  compiler pipeline.

No implementation version has been published yet. The available course notes
introduce the compiler architecture and the foundations of lexical analysis,
but they do not yet provide a complete executable phase. The version
directories currently reserve the planned progression.

## Purpose

The overarching aim of this repository is to provide a didactic progression
through the construction of a small compiler. Successive versions make it
possible to study:

* the transformation from source text to tokens,
* the relationship between grammars, parsing, and abstract syntax trees,
* semantic verification through types, symbols, and scopes,
* the preservation of meaning during translation to C, and
* the interfaces and tests required to integrate a compiler pipeline.

By developing the compiler one complete phase at a time, the repository serves
as a teaching resource for connecting formal language concepts with an
executable systems programming project.
