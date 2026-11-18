# D6 · Explícale tu proyecto a la IA con un script de Python

Script de Python de 63 líneas que recorre una carpeta de proyecto y junta el árbol y los archivos clave en un solo archivo de Markdown (`contexto-<carpeta>.md`), listo para copiarlo y pegarlo en un chat antes de tu pregunta. Usa solo la biblioteca estándar (`sys` y `pathlib`).

## Comandos

1. (Opcional) Crea un proyecto de prueba con el script del video anterior de la saga:

```text
python nuevo_proyecto.py mi-app
```

2. Corre el script sobre tu carpeta:

```text
python contexto_ia.py mi-app
```

3. Abre `contexto-mi-app.md`, **revisa el texto antes de pegarlo** (si ves algo privado, quítalo), cópialo completo y pégalo en el chat antes de tu pregunta.

## Qué salta y qué incluye

- **Salta siempre:** `.venv`, `venv`, `node_modules`, `__pycache__`, `.git` y cualquier archivo cuyo nombre empiece con `.env` (no aparecen ni en el árbol ni en el contenido).
- **Incluye el contenido de:** `.py`, `.md`, `.txt`, `.json`, `.toml`, `.js`, `.jsx`, `.html` y `.css`, hasta **20 000 bytes** por archivo (si un archivo pasa del límite, anota `(omitido: pasa del límite)`). Funciona igual con un proyecto de React (salta `node_modules` y lee `.jsx`).

## Ejemplo incluido

La carpeta `ejemplo/` trae `main.py` y `test_main.py` para probar sobre la estructura de `mi-app`.

## Fuentes

- Python · Módulo `pathlib`: https://docs.python.org/3/library/pathlib.html
- Vite · Variables de entorno y archivos `.env`: https://vite.dev/guide/env-and-mode
- Google AI Studio · Estrategias para escribir prompts: https://aistudio.google.com/docs/prompting-strategies
- Anthropic · Buenas prácticas de prompts: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
