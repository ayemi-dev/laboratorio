# CLI, API, modelo, agente y MCP · ejemplos para probarlos

Guía del video. Cada comando va en su propia línea y se copia tal cual. En el video se usó **Git Bash** en Windows (la terminal de [la terminal sin miedo](../g4-terminal-sin-miedo/)); en Mac y Linux los comandos son los mismos. Donde Windows PowerShell cambia, se indica.

## 0. Prepara la carpeta de práctica

Usa la carpeta `mi-pagina` de los videos anteriores, o crea una nueva. Adentro, un archivo `notas.txt` con estas tres líneas, sin acentos:

```text
falta: probar el sensor
listo: comprar cables
falta: subir el programa
```

Abre la terminal en esa carpeta: **Git Bash** o **Windows PowerShell** en Windows, la app **Terminal** en Mac, la terminal de tu sistema en Linux.

## 1. CLI: un programa que usas desde la terminal

Una CLI (interfaz de línea de comandos) es un programa que manejas escribiendo, sin ventanas ni botones. Git es una:

```sh
git --version
```

Responde con la versión instalada, por ejemplo:

```text
git version <la versión de tu equipo>
```

`git --version` hace lo mismo que `git version`. Funciona igual en Git Bash, PowerShell, Mac y Linux.

## 2. Modelo: el cerebro de la IA

El modelo es lo que entiende tu pregunta y escribe la respuesta. Ejemplos de hoy:

- **Gemini**, de Google: Gemini 4 Hydrogen, Gemini 4 Argon, Gemini 3.8 Flash, entre otros.
- **Claude**, de Anthropic: Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5, entre otros.

Las listas completas cambian seguido: [modelos de Gemini](https://ai.google.dev/gemini-api/docs/models) y [modelos de Claude](https://docs.claude.com/en/docs/about-claude/models/overview).

Si ya tienes Antigravity CLI (paso 4), puedes ver los modelos que te deja elegir:

```sh
agy models
```

## 3. API: cómo un programa le pide algo a otro

Una API es la puerta que un programa abre para que otros programas le pidan cosas. La de GitHub, por ejemplo, te da una frase al azar, sin cuenta ni llave:

Git Bash, Mac y Linux:

```sh
curl https://api.github.com/zen
```

Windows PowerShell:

```powershell
Invoke-RestMethod https://api.github.com/zen
```

Cada vez sale una frase distinta. En Windows PowerShell 5.1, `curl` es otro nombre de `Invoke-WebRequest` y muestra mucho más que la frase; por eso ahí se usa `Invoke-RestMethod`. Sin cuenta, GitHub acepta 60 peticiones por hora.

Así también le piden respuestas los programas a un modelo: la [API de Gemini](https://ai.google.dev/gemini-api/docs/quickstart), por ejemplo, recibe tu pregunta y devuelve el texto. Para esas sí necesitas una llave propia, que se guarda en una variable de entorno (por ejemplo, `GEMINI_API_KEY`), nunca dentro del código.

## 4. Agente: un modelo que usa herramientas y avanza por pasos

Un agente no solo responde: decide qué herramienta usar (leer un archivo, correr un comando), ve el resultado y sigue. En el video se usó **Antigravity CLI**, la terminal de los agentes de Google. Se instala desde su [página oficial](https://antigravity.google/product/antigravity-cli) (botón «Install») y la primera vez se abre sin opciones para iniciar sesión:

```sh
agy
```

Luego, en la carpeta de práctica, una pregunta que solo se responde leyendo el archivo:

```sh
agy -p "¿Qué me falta en notas.txt?"
```

Con `-p`, hace la tarea, responde y termina. Para responder, el agente abre `notas.txt` con una herramienta y te dice que falta probar el sensor y subir el programa (con sus propias palabras: el texto cambia en cada corrida).

Para ver los pasos que dio, pide la salida detallada:

```sh
agy -p "¿Qué me falta en notas.txt?" --output-format stream-json
```

Cada paso de herramienta aparece con su `tool_info`. Otros agentes de terminal, como [Claude Code](https://code.claude.com/docs/en/overview), funcionan con la misma idea.

## 5. MCP: el enchufe estándar para herramientas y datos

MCP (Model Context Protocol) es un estándar abierto para conectar aplicaciones de IA con archivos, bases de datos, buscadores y otras herramientas. Su documentación lo compara con un puerto USB-C: un mismo enchufe para muchos aparatos. Lo presentó Anthropic en noviembre de 2024 y desde diciembre de 2025 está en la Agentic AI Foundation, de la Linux Foundation.

En MCP, el agente es el **anfitrión** y cada **servidor MCP** le ofrece herramientas. El ejemplo del video es el servidor oficial de archivos, configurado en VS Code (necesitas [Node.js](https://nodejs.org/) para `npx`). Crea en tu proyecto el archivo `.vscode/mcp.json` con esto, tal cual:

```json
{
  "servers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "${workspaceFolder}"
      ]
    }
  }
}
```

`${workspaceFolder}` es la carpeta que tienes abierta en VS Code: el servidor solo puede tocar lo que está ahí. El mismo servidor se conecta a otras aplicaciones, como Claude Desktop, con su propio archivo de configuración; las instrucciones están en el [README del servidor](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem).

## Cómo se juntan

Tú escribes en una **CLI**; detrás trabaja un **agente**, que piensa con un **modelo**; los programas se piden cosas entre sí por **API**; el agente decide los pasos, y las herramientas que usa pueden llegarle por **MCP**. Como en una cocina: mostrador, ventanilla, chef y un solo enchufe para todos los aparatos.

Fuentes: documentación de Model Context Protocol (introducción, arquitectura y servidor de archivos), Anthropic (agentes, anuncio de MCP, donación a la Agentic AI Foundation, Claude Code y modelos de Claude), Google (Antigravity CLI y modelos y API de Gemini), GitHub (API REST y límites), MDN (API), Git (`git version`), curl y Microsoft Learn (`Invoke-WebRequest` en Windows PowerShell 5.1), consultadas el 20 de noviembre de 2026.
