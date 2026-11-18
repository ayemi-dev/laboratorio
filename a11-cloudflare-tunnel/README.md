# A11 · Cloudflare Tunnel: tu proyecto en internet sin abrir puertos

Guía rápida de comandos y límites oficiales del **túnel rápido** (*Quick Tunnel*) de Cloudflare Tunnel, sin cuenta ni dominio propio.

## Comandos

En la carpeta del proyecto que quieres mostrar:

```bash
python -m http.server --bind 127.0.0.1
```

En Mac, usa `python3` en lugar de `python`.

En otra terminal, con el servidor anterior abierto:

```bash
cloudflared tunnel --url http://localhost:8000
```

## Instalar `cloudflared`

- **Mac:** `brew install cloudflared`
- **Windows:** descarga el `.msi` desde [developers.cloudflare.com/tunnel/downloads](https://developers.cloudflare.com/tunnel/downloads/)
- **Linux:** repositorio de paquetes en [pkg.cloudflare.com](https://pkg.cloudflare.com/)

## Qué sí y qué no

| Tema | Lo que hace | Fuente |
|---|---|---|
| **Sin cuenta** | El túnel rápido no pide cuenta ni dominio; entrega una dirección temporal en `trycloudflare.com` con HTTPS automático | Quick Tunnels · TryCloudflare |
| **Solo para pruebas** | Sin garantía de disponibilidad (*uptime*) | Quick Tunnels |
| **Límite de tráfico** | Hasta 200 peticiones en vuelo a la vez; las adicionales reciben error `429` | Quick Tunnels |
| **Server-Sent Events** | No admite Server-Sent Events (SSE) | Quick Tunnels |
| **Dirección temporal** | El subdominio cambia cada vez y deja de funcionar al detener `cloudflared` | Quick Tunnels |
| **Visibilidad** | Cualquiera con la dirección puede acceder a tu servicio local | Quick Tunnels |
| **Dirección fija** | El túnel está en todos los planes, pero pide cuenta de Cloudflare y un dominio propio agregado a ella (el dominio se paga; Cloudflare Registrar lo vende a costo). Hasta 1,000 túneles por cuenta | Create a tunnel · Registrar · Account limits |
| **Extra** | `--allowed-mail` pide un código por correo antes de entrar. En Windows, `cloudflared` no se actualiza solo | Quick Tunnels · Downloads |
| **Página estática permanente** | Si tu página es estática y la quieres permanente: GitHub Pages (video A9 del canal) | — |

## Fuentes oficiales

- [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)
- [Quick Tunnels y sus límites](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/)
- [Descarga de `cloudflared`](https://developers.cloudflare.com/tunnel/downloads/)
- [Crear un túnel remoto (dirección fija)](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/)
- [Límites de la cuenta](https://developers.cloudflare.com/cloudflare-one/account-limits/)
- [Módulo `http.server` de Python](https://docs.python.org/3/library/http.server.html)

Datos verificados el 17 de noviembre de 2026 en la documentación oficial de Cloudflare y de Python; los límites pueden cambiar. Ayemi no tiene relación con Cloudflare.
