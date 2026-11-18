# Comandos · A11 · Cloudflare Tunnel

## 1. Servir una carpeta local en el puerto 8000 (solo en tu equipo)

```bash
python -m http.server --bind 127.0.0.1
```

En Mac, usa `python3`:

```bash
python3 -m http.server --bind 127.0.0.1
```

## 2. Abrir el túnel rápido hacia ese puerto

En otra terminal, mientras el servidor de Python sigue abierto:

```bash
cloudflared tunnel --url http://localhost:8000
```

## 3. Instalar `cloudflared`

```text
Mac:      brew install cloudflared
Windows:  descarga el .msi desde https://developers.cloudflare.com/tunnel/downloads/
Linux:    repositorio de paquetes en https://pkg.cloudflare.com/
```
