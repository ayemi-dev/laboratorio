# De los requisitos a la maqueta con IA

Ya tienes tus requisitos (del video anterior: [De la idea a los requisitos con IA](../c1-idea-requisitos/)). Antes de programar o pagar por desarrollo, pídele a una IA una maqueta navegable en un solo archivo HTML, ábrela en tu navegador a tamaño de celular y revísala con 3 preguntas.

## Archivos incluidos

- [`prompt-maqueta.md`](prompt-maqueta.md): el prompt exacto seguido del documento de ejemplo de C1.
- [`lista-revision.md`](lista-revision.md): la lista de revisión completa.
- [`maqueta/v1/index.html`](maqueta/v1/index.html): la maqueta real generada por una IA (Gemini 4 Hydrogen Medium) con ese prompt, guardada sin editar.

## Cómo usarla

1. Copia el prompt de [`prompt-maqueta.md`](prompt-maqueta.md) y pega debajo tu documento de requisitos.
2. Guarda la respuesta HTML en un archivo `index.html` y ábrelo directo en tu navegador (doble clic, sin servidor).
3. Abre el modo de dispositivo en Chrome (`F12` y luego `Ctrl+Shift+M`; en Mac: `Cmd+Option+I` y `Cmd+Shift+M`).
4. Revisa con [`lista-revision.md`](lista-revision.md). Si algo falla, pide un cambio a la vez.

Funciona con cualquier asistente de IA. Una maqueta no guarda datos: sirve para decidir antes de programar.

## Fuentes oficiales

- Chrome DevTools · Device Mode: https://developer.chrome.com/docs/devtools/device-mode
- Chrome DevTools · Keyboard Shortcuts: https://developer.chrome.com/docs/devtools/shortcuts
- MDN · Viewport `<meta>` tag: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport
- W3C · WCAG 2.2 SC 2.5.8 Target Size (Minimum, Level AA): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- MDN · Dealing with files: https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Environment_setup/Dealing_with_files
- MDN · `<a>` HTML element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a

---
Laboratorio Ayemi · CC BY-SA 4.0 · ¿Necesitas tu página o tu sistema a la medida? https://ayemi.org/enlaces
