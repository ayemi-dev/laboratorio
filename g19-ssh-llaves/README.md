# SSH con llaves: entra a un servidor sin contraseña

Video de la serie **Herramientas de desarrollador** del Laboratorio Ayemi. Continúa [la terminal sin miedo](../g4-terminal-sin-miedo/) y [Cloudflare Tunnel](../a11-cloudflare-tunnel/): ahora entras a un servidor desde la terminal sin escribir contraseña, con un par de llaves. Todo contra un **servidor de práctica en Docker**, en tu propia compu. En Git Bash (Windows), Linux y Mac.

- **`ssh-keygen -t ed25519`** crea un par de llaves: la **privada** (`id_ed25519`) y la **pública** (`id_ed25519.pub`).
- La **pública** se comparte y va al servidor. La **privada nunca sale de tu compu**: no se pega en un chat, no se manda por correo y no se sube a GitHub.
- **`~/.ssh/config`** le da un alias al servidor, con su dirección, puerto y usuario.
- **`ssh-copy-id`** sube tu llave pública al servidor (te pide la contraseña una sola vez) y la deja en `~/.ssh/authorized_keys`.
- Desde ahí, **`ssh practica`** entra sin contraseña.

## El servidor de práctica

[`servidor/Dockerfile`](servidor/Dockerfile) arma un servidor SSH mínimo con la imagen oficial de Alpine Linux 3.24 y `openssh-server`. Tiene un usuario y una contraseña de juguete (`practica` / `practica`), así que se publica **solo en `127.0.0.1`**: nadie fuera de tu compu lo ve. Al terminar, se borra.

[`servidor/config`](servidor/config) es el alias que va en `~/.ssh/config`.

## Los comandos del video

| Comando | Qué hace |
|---|---|
| `ssh-keygen -t ed25519 -C practica` | Crea tu par de llaves |
| `ls ~/.ssh` | Muestra la privada (`id_ed25519`) y la pública (`id_ed25519.pub`) |
| `cat ~/.ssh/id_ed25519.pub` | Muestra la pública: esa sí se comparte |
| `docker port ssh-practica` | Muestra en qué puerto de tu compu está el servidor |
| `cat ~/.ssh/config` | Muestra el alias del servidor |
| `ssh-copy-id practica` | Sube tu llave pública (pide la contraseña una vez) |
| `ssh practica` | Entra sin contraseña |

La guía completa, paso por paso y con lo que debe salir, está en [`comandos.md`](comandos.md).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Manual de OpenSSH | https://www.openssh.org/manual.html |
| `ssh` | https://man.openbsd.org/ssh.1 |
| `ssh-keygen` | https://man.openbsd.org/ssh-keygen.1 |
| `ssh_config` (el archivo `config`) | https://man.openbsd.org/ssh_config.5 |
| `sshd` y `authorized_keys` | https://man.openbsd.org/sshd.8 |
| `ssh-copy-id` | https://man7.org/linux/man-pages/man1/ssh-copy-id.1.html |
| Publicar puertos en Docker | https://docs.docker.com/engine/network/port-publishing/ |
| Imagen oficial de Alpine | https://hub.docker.com/_/alpine |
| Git for Windows (Git Bash) | https://gitforwindows.org/ |
| Videos anteriores | [`../g4-terminal-sin-miedo/`](../g4-terminal-sin-miedo/) y [`../a11-cloudflare-tunnel/`](../a11-cloudflare-tunnel/) |

Datos verificados el 22 de noviembre de 2026 en el manual de OpenSSH (páginas man de OpenBSD y `ssh-copy-id` de OpenSSH portátil), la documentación de Docker y Docker Hub. Ayemi no tiene relación con OpenSSH, OpenBSD, Docker, Alpine Linux ni Git for Windows.

---
Guía: CC BY-SA 4.0 · Código: MIT · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
