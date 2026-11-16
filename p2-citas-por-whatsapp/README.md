# Citas por WhatsApp que se cruzan: la maqueta

Si agendas citas por WhatsApp, a veces dos clientes quedan a la misma hora y otros simplemente no llegan. Así lo resolveríamos en tres pasos. Esta maqueta los muestra funcionando para una barbería de ejemplo.

## Pruébala

Descarga `index.html` y ábrelo con doble clic en tu navegador. No necesita servidor, instalación ni cuenta.

1. **Agenda en línea.** Elige un servicio (Corte, Barba o Corte y barba), el día («Hoy» o «Mañana») y un horario libre. Los horarios ocupados aparecen deshabilitados y la duración del servicio se respeta para que no se empalmen citas.
2. **Confirmación por WhatsApp.** En «Panel del negocio», cada cita en «Por confirmar» tiene el botón «Confirmar por WhatsApp», que arma el mensaje y el enlace `wa.me` con un toque. Al cerrar la vista previa, pasa a «Confirmada».
3. **Recordatorios y cancelación.** En «Recordatorios de mañana» puedes abrir la vista previa del recordatorio de cada cita o marcar «Canceló» para que ese horario vuelva a ofrecerse en la vista del cliente.

Las citas viven en la memoria de la página: al recargar, vuelven los datos de ejemplo.

## El enlace de WhatsApp

WhatsApp documenta este formato en su [Centro de ayuda](https://faq.whatsapp.com/5913398998672934/?locale=es_LA):

```text
https://wa.me/<número en formato internacional>?text=<mensaje codificado>
```

El número va completo, sin `+`, espacios, paréntesis ni guiones. En México, `52` más los 10 dígitos. El mensaje se codifica con `encodeURIComponent`. El enlace **abre** el chat con el mensaje ya escrito; quien lo envía eres tú. No envía mensajes automáticos (para eso se necesita la plataforma de WhatsApp Business, que esta maqueta no usa).

## Para usarla de verdad

La maqueta es un punto de partida. Un sistema real necesita:

- Guardar las citas en una base de datos, no en la memoria del navegador.
- Separar la vista del cliente de tu panel del negocio, con inicio de sesión.
- Tus horarios, días y servicios reales.

Datos de ejemplo: los clientes («Cliente A» a «Cliente H») y los teléfonos (`0000000000`) no son reales. Verificado el 16 de noviembre de 2026. Ayemi no tiene relación con WhatsApp ni con Meta.

---
Laboratorio Ayemi · Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas tu página o tu sistema a la medida? https://ayemi.org/enlaces
