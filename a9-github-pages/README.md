# GitHub Pages: publica tu página sin pagar hosting

**Datos verificados el 13 de noviembre de 2026** en la documentación oficial de GitHub. Pueden cambiar: revisa los enlaces antes de publicar. Ayemi no tiene relación con GitHub.

GitHub Pages es un hospedaje de **sitios estáticos**: toma los archivos HTML, CSS y JavaScript de un repositorio de GitHub y los publica como sitio web.

## Qué da sin pagar

- Con **GitHub Free**, Pages funciona en **repositorios públicos**. Los repositorios privados con Pages son de los planes de pago (Pro, Team y Enterprise).
- Tu sitio queda en `https://<tu-usuario>.github.io` (sitio de usuario, uno por cuenta) o en `https://<tu-usuario>.github.io/<repositorio>` (sitio de proyecto, uno por repositorio).
- HTTPS automático en los dominios `github.io`. También admite dominio propio.

## Límites

| Límite | Valor |
|---|---|
| Tamaño del sitio publicado | 1 GB como máximo |
| Repositorio de origen | 1 GB recomendado |
| Tráfico | 100 GB al mes (límite suave) |
| Compilaciones | 10 por hora (límite suave; no aplica si publicas con tu propio flujo de GitHub Actions) |
| Tiempo de despliegue | 10 minutos como máximo |

Si te pasas, GitHub puede dejar de servir tu sitio o escribirte para sugerirte opciones.

## La letra chiquita

- **No es para negocios:** no se permite como hospedaje de una tienda en línea, de un sitio cuyo fin principal sea vender ni de software como servicio (SaaS).
- **Nada sensible:** no lo uses para recibir contraseñas ni números de tarjeta.
- **Siempre público:** el sitio se ve en internet aunque el repositorio sea privado. Revisa que no haya datos sensibles en el repositorio.
- **Visitas:** GitHub registra la IP de quien visita el sitio, por seguridad.

## Pasos, en resumen

1. Crea un repositorio público y sube tu `index.html` (también sirve `index.md` o `README.md`) con Git: `git add .`, `git commit -m "mi sitio"` y `git push`.
2. En el repositorio, entra a **Settings > Pages** y elige la rama y la carpeta que se publican.
3. Espera: los cambios pueden tardar hasta 10 minutos en verse.

Git y GitHub paso a paso: serie **Herramientas de desarrollador** del Laboratorio.

## Fuentes

- Qué es GitHub Pages: https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages
- Límites: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- Crear un sitio: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- HTTPS: https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https

---
Laboratorio Ayemi · CC BY-SA 4.0 · ¿Quieres tu proyecto en línea, configurado y seguro? https://ayemi.org/enlaces
