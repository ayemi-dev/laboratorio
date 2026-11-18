# Inventario que nunca cuadra: la maqueta

Si llevas el inventario de tu tienda en una libreta o en un Excel y nunca cuadra con lo que hay en el estante, así lo resolveríamos en tres pasos. Esta maqueta los muestra funcionando para una tienda de abarrotes de ejemplo.

## Pruébala

Descarga `index.html` y ábrelo con doble clic en tu navegador. No necesita servidor, instalación ni cuenta.

1. **Entradas y salidas.** En «Registrar», elige el producto, el tipo («Entrada» o «Salida»), el motivo y la cantidad. Una salida mayor que la existencia se rechaza.
2. **Existencia al día y CSV.** En «Existencias», la cantidad se calcula siempre como `inicial + entradas − salidas` (nunca se edita a mano). Al tocar un producto ves el desglose, y con «Descargar existencias (CSV)» bajas `existencias-ejemplo.csv` con BOM UTF-8 y fin de línea CRLF.
3. **Alerta de mínimo y pedido por WhatsApp.** Cuando un producto llega a su mínimo o queda por debajo, se marca con «Por surtir» y aparece en la pestaña «Por surtir», donde puedes abrir la vista previa del mensaje para tu proveedor con el enlace `wa.me` ya armado.

Los movimientos viven en la memoria de la página: al recargar, vuelven los datos de ejemplo.

## Cómo abrir el CSV en Excel

Microsoft documenta la apertura de archivos CSV en [Soporte de Microsoft · Importar o exportar archivos de texto (.txt o .csv)](https://support.microsoft.com/es-es/office/importar-o-exportar-archivos-de-texto-txt-o-csv-5250ac4c-663c-47ce-937b-339e391393ba) y el uso de BOM UTF-8 para conservar los acentos en [Abrir archivos CSV UTF-8 correctamente en Excel](https://support.microsoft.com/es-es/office/abrir-archivos-csv-utf-8-correctamente-en-excel-8a935af5-3416-4edd-ba7e-3dfd2bc4a032). En Excel, ve al menú **Archivo**, opción **Abrir**, y selecciona `existencias-ejemplo.csv`.

## El enlace de WhatsApp

WhatsApp documenta este formato en su [Centro de ayuda](https://faq.whatsapp.com/5913398998672934/?locale=es_LA):

```text
https://wa.me/<número en formato internacional>?text=<mensaje codificado>
```

El número va completo, sin `+`, espacios, paréntesis ni guiones. En México, `52` más los 10 dígitos. El mensaje se codifica con `encodeURIComponent`. El enlace **abre** el chat con el mensaje ya escrito; quien lo envía eres tú. No envía mensajes automáticos ni las alertas llegan al celular (se muestran dentro de la maqueta).

## Para usarla de verdad

La maqueta es un punto de partida. Un sistema real necesita:

- Guardar los productos y movimientos en una base de datos, no en la memoria del navegador.
- Control de acceso para quien registra entradas y salidas.
- Tus productos, mínimos y proveedores reales.

Datos de ejemplo: la tienda, los productos, las cantidades, el proveedor («Proveedor A») y el teléfono (`0000000000`) no son reales. Verificado el 17 de noviembre de 2026. Ayemi no tiene relación con WhatsApp, Meta ni Microsoft.

---
Laboratorio Ayemi · Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas tu página o tu sistema a la medida? https://ayemi.org/enlaces
