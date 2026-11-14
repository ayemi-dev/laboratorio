# Pedidos por WhatsApp, sin libreta: la maqueta

Si tomas pedidos por WhatsApp y los anotas en una libreta, los mensajes se pierden y al final del día cuentas todo a mano. Así lo resolveríamos en tres pasos. Esta maqueta los muestra funcionando.

## Pruébala

Descarga `index.html` y ábrelo en tu navegador. No necesita servidor, instalación ni cuenta.

1. **Catálogo.** Elige productos, escribe un nombre y un WhatsApp de 10 dígitos, y envía el pedido.
2. **Tablero.** El pedido aparece en «Nuevos». Con «Preparar» y «Entregado» avanza de estado.
3. **Avisar.** Arma el mensaje para el cliente y un enlace `wa.me` que abre WhatsApp con el texto ya escrito.
4. **Resumen.** Pedidos del día, entregados, por entregar y lo más pedido.

Los pedidos viven en la memoria de la página: al recargar, vuelven los de ejemplo.

## El enlace de WhatsApp

WhatsApp documenta este formato en su [Centro de ayuda](https://faq.whatsapp.com/5913398998672934/?locale=es_LA):

```text
https://wa.me/<número en formato internacional>?text=<mensaje codificado>
```

El número va completo, sin `+`, espacios, paréntesis ni guiones. En México, `52` más los 10 dígitos. El mensaje se codifica con `encodeURIComponent`. El enlace **abre** el chat con el mensaje escrito; quien lo envía eres tú. Para enviar avisos automáticos se necesita la API de WhatsApp Business, que esta maqueta no usa.

## Para usarla de verdad

La maqueta es un punto de partida. Un sistema real necesita:

- Guardar los pedidos en una base de datos, no en la memoria del navegador.
- Separar la página del cliente (catálogo) de la tuya (tablero y resumen), con inicio de sesión.
- Tu catálogo real, con fotos y existencias.

Datos de ejemplo: los clientes y los teléfonos (`0000000000`) no son reales. Verificado el 13 de noviembre de 2026. Ayemi no tiene relación con WhatsApp ni con Meta.

---
Laboratorio Ayemi · Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas tu página o tu sistema a la medida? https://ayemi.org/enlaces
