# CLI, API, modelo, agente y MCP en un minuto

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi. Cinco palabras que hoy salen en todos lados, explicadas con ejemplos reales en la terminal y con una sola idea: son piezas de la misma cadena. Sigue a [la terminal, nivel 2](../g9-terminal-scripts/): el agente del video lee el mismo `notas.txt`.

| Término | Qué es | Ejemplo para probar |
|---|---|---|
| **CLI** | Un programa que usas escribiendo en la terminal | `git --version` |
| **Modelo** | El cerebro de la IA: entiende y responde | Gemini (Google), Claude (Anthropic) |
| **API** | Cómo un programa le pide algo a otro | `curl https://api.github.com/zen` |
| **Agente** | Un modelo que además usa herramientas y avanza por pasos | `agy -p "¿Qué me falta en notas.txt?"` |
| **MCP** | El estándar abierto para conectar agentes con herramientas y datos | `.vscode/mcp.json` con el servidor oficial de archivos |

## Cómo se juntan: una cocina

- **Mostrador = CLI**: ahí pides.
- **Ventanilla = API**: por ahí pasa la orden de un lado a otro.
- **Chef = modelo**: el que piensa.
- **El chef cocinando por pasos con sus aparatos = agente.**
- **Un solo enchufe para todos los aparatos = MCP.** La documentación de MCP lo compara con un puerto USB-C para la IA.

La guía, con cada ejemplo paso a paso en Windows, Mac y Linux, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Qué es MCP (Model Context Protocol) | https://modelcontextprotocol.io/docs/getting-started/intro |
| Arquitectura de MCP: anfitrión, cliente y servidor | https://modelcontextprotocol.io/docs/learn/architecture |
| Servidor oficial de archivos para MCP | https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem |
| Qué es un agente (Anthropic) | https://www.anthropic.com/engineering/building-effective-agents |
| Antigravity CLI | https://antigravity.google/product/antigravity-cli |
| Antigravity CLI sin ventana (`-p`) | https://antigravity.google/docs/cli/headless/ |
| Claude Code, otro agente de terminal | https://code.claude.com/docs/en/overview |
| Modelos de Gemini | https://ai.google.dev/gemini-api/docs/models |
| Modelos de Claude | https://docs.claude.com/en/docs/about-claude/models/overview |
| Qué es una API (MDN) | https://developer.mozilla.org/en-US/docs/Glossary/API |
| API de GitHub: la frase zen | https://docs.github.com/en/rest/meta/meta#get-the-zen-of-github |
| `git --version` | https://git-scm.com/docs/git-version |
| curl | https://curl.se/docs/manpage.html |
| Video anterior: la terminal, nivel 2 | [`../g9-terminal-scripts/`](../g9-terminal-scripts/) |

Datos verificados el 20 de noviembre de 2026 en la documentación oficial de Model Context Protocol, Anthropic, Google, GitHub, Mozilla, Git y curl. Ayemi no tiene relación con ninguno de ellos.

---
Guía: CC BY-SA 4.0 · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
