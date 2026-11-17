# Comparativa: VS Code y Zed

Datos verificados el 16 de noviembre de 2026 en la documentación oficial de Visual Studio Code y de Zed. Ayemi no tiene relación con Microsoft ni con Zed Industries, y no recomienda ninguno de los dos editores.

## Comparativa general

| Aspecto | Visual Studio Code | Zed |
|---|---|---|
| Gratis | Sí (uso personal o comercial) | Sí (plan Personal) |
| Sistemas | Windows, macOS y Linux | macOS, Linux y Windows |
| Código abierto | Su base `Code - OSS` (MIT); la distribución de Microsoft usa licencia de producto | Sí (`GPL-3.0-or-later`, con partes `Apache-2.0`) |
| Terminal y Git | Integrados | Integrados |
| Depurador | Incluido (JavaScript, TypeScript y Node.js; otros lenguajes con extensiones) | Incluido mediante DAP |
| Extensiones | Miles en el Visual Studio Marketplace | Menos que VS Code (indicado en su documentación) |
| IA integrada | Sí, y se puede apagar (`chat.disableAIFeatures`) | Sí, y se puede apagar por completo |
| Versión al 16 de noviembre de 2026 | 1.146 | 1.28.1 |

## Probar Zed viniendo de VS Code

Al instalar Zed, ofrece importar la configuración principal desde VS Code. No importa extensiones ni atajos de teclado.

Si te saltaste ese paso, abre la paleta de comandos en Zed y ejecuta (uno por línea):

```text
zed: import vs code settings
zed: toggle base keymap selector
```

Con el segundo comando puedes elegir el mapa de teclas base de VS Code para mantener atajos familiares.

## Requisitos de Zed

- **macOS:** macOS 12.0 (Monterey) o posterior.
- **Windows:** Windows 11 versión 22H2 o posterior.
- **Linux:** procesadores de 64 bits Intel/AMD (`x86_64`) o Arm (`aarch64`).

## Fuentes oficiales

- Visual Studio Code: https://code.visualstudio.com/
- FAQ de VS Code: https://code.visualstudio.com/docs/supporting/faq
- Marketplace de extensiones: https://code.visualstudio.com/docs/configure/extensions/extension-marketplace
- Zed: https://zed.dev/
- Documentación de Zed: https://zed.dev/docs/
- Migrar de VS Code a Zed: https://zed.dev/docs/migrate/vs-code
- Requisitos de instalación de Zed: https://zed.dev/docs/installation
- Atajos en Zed: https://zed.dev/docs/key-bindings
