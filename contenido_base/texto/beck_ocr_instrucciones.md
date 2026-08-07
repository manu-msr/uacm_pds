# Regenerar OCR para Beck

Este archivo documenta cómo regenerar el PDF OCR y el texto extraído de Beck si se borran, se dañan o se quiere repetir el proceso.

## Herramientas necesarias

Si las herramientas no están disponibles, instalar en el sistema:

```bash
sudo apt-get update
sudo apt-get install -y ocrmypdf tesseract-ocr tesseract-ocr-eng
```

## Generar PDF con OCR

Ejecutar desde la raíz del curso:

```bash
ocrmypdf --deskew --rotate-pages -l eng \
  "contenido_base/System Software An Introduction To Systems Programming by Leland L. Beck (z-lib.org).pdf" \
  "contenido_base/ocr/beck_ocr.pdf"
```

## Extraer texto buscable

Después de generar o regenerar el PDF OCR:

```bash
pdftotext -layout \
  "contenido_base/ocr/beck_ocr.pdf" \
  "contenido_base/texto/beck.txt"
```

## Verificación mínima

```bash
pdfinfo "contenido_base/ocr/beck_ocr.pdf"
rg -n "Loaders and Linkers|Compilers|Operating Systems|Assemblers" contenido_base/texto/beck.txt
```

Si esos comandos encuentran contenido, futuras notas pueden usar `contenido_base/texto/beck.txt` como fuente de consulta rápida. Para afirmaciones puntuales, verificar el pasaje localizado contra el PDF OCR.
