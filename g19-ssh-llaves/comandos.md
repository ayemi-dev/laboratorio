# SSH con llaves · entra a un servidor sin contraseña

Guía del video. Cada comando va en su propia línea y se copia tal cual. Todo se corre en **Git Bash** (Windows) o en la terminal de **Linux** o **Mac**. Necesitas **Docker** (Docker Desktop en Windows y Mac) para el servidor de práctica.

> **Regla de oro:** la llave **privada** (`id_ed25519`, sin `.pub`) nunca se comparte, ni se pega en un chat, ni se sube a GitHub. La única que se comparte es la **pública** (`id_ed25519.pub`).

## 1. Levanta el servidor de práctica

Descarga la carpeta [`servidor/`](servidor/) de esta guía, entra a la carpeta que la contiene y construye la imagen:

```sh
docker build -t ssh-practica servidor
```

Arráncalo, publicado **solo en tu compu** (`127.0.0.1`), en el puerto 2222:

```sh
docker run -d --name ssh-practica --hostname servidor-practica -p 127.0.0.1:2222:22 ssh-practica
```

Comprueba el puerto:

```sh
docker port ssh-practica
```

```text
22/tcp -> 127.0.0.1:2222
```

El servidor tiene un usuario y una contraseña de juguete: `practica` / `practica`. Por eso se publica solo en `127.0.0.1`: si quitas esa parte, Docker lo abre a toda tu red.

## 2. Crea tu par de llaves

```sh
ssh-keygen -t ed25519 -C practica
```

- `-t ed25519` es el tipo de llave.
- `-C practica` es el comentario que va al final de la pública. Sin él, `ssh-keygen` pone tu usuario y el nombre de tu equipo.

Te hace tres preguntas: dónde guardarla (Enter, para `~/.ssh/id_ed25519`) y la frase de paso, dos veces. Para practicar, déjala vacía (Enter y Enter).

Debe terminar con algo así (la huella y el dibujo cambian con cada llave):

```text
Your identification has been saved in ~/.ssh/id_ed25519
Your public key has been saved in ~/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:... practica
```

> **Si ya tienes una llave `id_ed25519`**, `ssh-keygen` te pregunta si la reemplazas (`Overwrite (y/n)?`). Responde **n**: esa llave quizá ya la usas en otro lado. Para practicar, crea otra con otro nombre: `ssh-keygen -t ed25519 -C practica -f ~/.ssh/practica` y cambia la última línea de `config` a `IdentityFile ~/.ssh/practica`.

> **Sugerencia:** en una llave para un servidor real, ponle frase de paso. Si la olvidas, no se recupera; la puedes cambiar con `ssh-keygen -p`.

## 3. Pública y privada

```sh
ls ~/.ssh
```

```text
id_ed25519  id_ed25519.pub
```

- `id_ed25519`: la **privada**. No la abras en pantalla, no la copies, no la compartas.
- `id_ed25519.pub`: la **pública**. Esta sí:

```sh
cat ~/.ssh/id_ed25519.pub
```

Es una sola línea que empieza con `ssh-ed25519` y termina con `practica`.

## 4. Un alias en `~/.ssh/config`

Abre (o crea) el archivo `~/.ssh/config` con tu editor, por ejemplo con VS Code:

```sh
code ~/.ssh/config
```

y agrega estas cinco líneas (son las de [`servidor/config`](servidor/config)):

```text
Host practica
    HostName 127.0.0.1
    Port 2222
    User practica
    IdentityFile ~/.ssh/id_ed25519
```

Revísalo:

```sh
cat ~/.ssh/config
```

Ahora `practica` quiere decir «el servidor de `127.0.0.1`, puerto 2222, usuario `practica`, con esta llave».

## 5. Sube tu llave pública

```sh
ssh-copy-id practica
```

- La **primera vez** que te conectas a un servidor, `ssh` te muestra su huella y pregunta `Are you sure you want to continue connecting (yes/no/[fingerprint])?`. En el servidor de práctica escribe `yes`. En un servidor real, compara la huella con la que te dé quien lo administra.
- Luego te pide la contraseña **una sola vez**: `practica` (no se ve mientras la escribes).
- Debe terminar con `Number of key(s) added: 1`.

`ssh-copy-id` agrega tu llave pública al final de `~/.ssh/authorized_keys` **en el servidor**.

> **¿No tienes `ssh-copy-id`?** (por ejemplo, en PowerShell de Windows). Hazlo a mano con esta línea en Git Bash, Linux o Mac (pide la contraseña una vez):
>
> ```sh
> cat ~/.ssh/id_ed25519.pub | ssh practica "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
> ```

## 6. Entra sin contraseña

```sh
ssh practica
```

Ya no pide contraseña. Estás en el servidor (el prompt cambia). Comprueba quién eres:

```sh
whoami
```

```text
practica
```

Y mira la lista de llaves autorizadas: es la misma línea que tu `id_ed25519.pub`.

```sh
cat ~/.ssh/authorized_keys
```

Sal del servidor:

```sh
exit
```

## 7. Al terminar, borra el servidor de práctica

```sh
docker rm -f ssh-practica
docker image rm ssh-practica
```

Si creaste la llave solo para practicar, puedes quitar también las cinco líneas de `practica` de `~/.ssh/config`. Las llaves `id_ed25519` y `id_ed25519.pub` ya las puedes usar con tus servidores reales: sube la pública con `ssh-copy-id` y la privada se queda donde está.

## Fuentes

- `ssh`: https://man.openbsd.org/ssh.1 — «The server knows the public key, and only the user knows the private key.»
- `ssh-keygen`: https://man.openbsd.org/ssh-keygen.1 — de la pública: «There is no need to keep the contents of this file secret.»; de la privada: «This file should not be readable by anyone but the user.»
- `ssh_config`: https://man.openbsd.org/ssh_config.5
- `sshd` (`authorized_keys`): https://man.openbsd.org/sshd.8
- `ssh-copy-id`: https://man7.org/linux/man-pages/man1/ssh-copy-id.1.html
- Publicar puertos en Docker: https://docs.docker.com/engine/network/port-publishing/ — con `127.0.0.1`, «only the Docker host can access the published container port.»

Verificado el 22 de noviembre de 2026.
