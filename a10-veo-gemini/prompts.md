# Los tres prompts de Veo en Gemini (`a10-veo-gemini`)

Se pidieron tres prompts por separado en la app de Gemini (plan Google AI Pro, con Veo) el 13 de noviembre de 2026. La aplicación los juntó y entregó un solo video vertical de 30 segundos (720 × 1280, 24 fps, con sonido) compuesto por tres tomas de 10 segundos en el orden de los prompts.

## Prompt 1 · La idea (boceto en libreta)

```text
Vertical 9:16 close-up. Night, a small home electronics workbench lit by a warm desk lamp. A hand sketches a simple circuit diagram with a pencil in a notebook; next to it an unpowered microcontroller board and a breadboard with colorful jumper wires. Slow dolly-in, shallow depth of field, cinematic, realistic. Audio: soft pencil scratching, quiet room tone, distant city ambience. No text, no logos, no faces.
```

## Prompt 2 · La construcción (soldadura en placa)

```text
Vertical 9:16 macro shot. A soldering iron tip touches a pad on a small green printed circuit board; a thin wisp of smoke rises and the solder flows into a shiny joint. Slow orbit around the board, realistic, warm key light with a cool cyan rim light. Audio: gentle sizzle of solder, soft fan hum. No text, no logos, no faces.
```

## Prompt 3 · El aparato que se enciende

```text
Vertical 9:16. The finished small device on the same workbench: a compact white 3D-printed enclosure with a tiny screen. A finger presses a button, the screen lights up with a simple line graph and a small LED glows cyan. The camera slowly pulls back revealing a tidy workbench at night. Realistic, cinematic. Audio: a soft click, a short pleasant electronic chime, room tone. No readable brand names, no faces.
```

## Sugerencia

Para mantener la continuidad entre varias tomas sin que el chat junte las instrucciones en una sola entrega:

1. **Un prompt por toma:** envía un prompt por cada toma de 10 segundos en turnos o chats separados.
2. **Misma descripción de escena y luz:** repite en cada prompt el mismo lugar y el mismo esquema de iluminación (por ejemplo, `Night, a small home electronics workbench lit by a warm desk lamp` y `cool cyan rim light`).
3. **Audio y restricciones explícitas:** indica al final el sonido ambiente esperado (`Audio: ...`) y lo que no debe aparecer (`No text, no logos, no faces`).

---
Laboratorio Ayemi · CC BY-SA 4.0 · ¿Quieres tu proyecto en línea, configurado y seguro? https://ayemi.org/enlaces
