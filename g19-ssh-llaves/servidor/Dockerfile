# Servidor SSH de práctica del Laboratorio Ayemi (video G19).
# Solo para practicar en tu compu: usuario y contraseña de juguete (practica / practica).
# Publícalo únicamente en 127.0.0.1 (ver comandos.md) y bórralo al terminar.
FROM alpine:3.24

RUN apk add --no-cache openssh-server openssh-keygen \
 && ssh-keygen -A \
 && adduser -D -s /bin/sh practica \
 && echo "practica:practica" | chpasswd \
 && rm -f /etc/motd

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D", "-e"]
