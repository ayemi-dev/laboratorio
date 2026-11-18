# De la maqueta a React, Vite y Tailwind en 1 minuto

Tercer video de la **saga C · Web moderna** del Laboratorio Ayemi. Toma la rejilla de horarios de [la maqueta de C2](../c2-requisitos-maqueta/maqueta/v1/index.html) (`c2-requisitos-maqueta`) y la convierte en tu primer componente real con **React 19.3.1**, **Vite 8.3.8** y **Tailwind CSS 4.3.5** (los tres de código abierto con licencia MIT).

## Córrelo

Necesitas **Node.js 20.19** o más reciente (o 22.12+); se probó con **Node.js 26.13.1** (la versión LTS más reciente).

```bash
npm install
npm run dev
```

Abre en tu navegador la dirección local que imprime Vite (por defecto `http://localhost:5173/`).

## Cómo se creó el proyecto

Los cinco comandos reales usados en el video, uno por línea:

```bash
npm create vite@latest citas -- --template react
cd citas
npm install
npm install tailwindcss @tailwindcss/vite
npm run dev
```

Si quieres evitar preguntas interactivas al crear el proyecto con `create-vite`, usa la opción `--no-interactive`:

```bash
npm create vite@latest citas -- --template react --no-interactive
```

## Los dos cambios de Tailwind

1. En `vite.config.js`, agrega el complemento `@tailwindcss/vite` junto al de React:
   - `import tailwindcss from '@tailwindcss/vite'`
   - `plugins: [react(), tailwindcss()]`
2. En `src/index.css`, deja una sola línea:
   - `@import "tailwindcss";`

Sugerencia: pasa las demás pantallas de la maqueta igual, una por una, y diseña para celular primero (en Tailwind, las clases sin prefijo aplican en todas las pantallas y `md:` aplica desde `48rem` / `768 px` hacia arriba).

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Primeros pasos con Vite | https://vite.dev/guide/ |
| Tailwind CSS con Vite | https://tailwindcss.com/docs/installation/using-vite |
| Diseño responsivo en Tailwind | https://tailwindcss.com/docs/responsive-design |
| React sin framework | https://react.dev/learn/build-a-react-app-from-scratch |
| Versiones de Node.js | https://nodejs.org/en/about/previous-releases |
| Video anterior (C2 · Maqueta con IA) | [c2-requisitos-maqueta/](../c2-requisitos-maqueta/) |

Datos verificados el 17 de noviembre de 2026 en la documentación oficial de Vite, Tailwind CSS, React y Node.js. Ayemi no tiene relación con el proyecto React, con Meta, con Vite, con Tailwind Labs ni con la OpenJS Foundation.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas tu página o tu sistema a la medida? Lo construimos: https://ayemi.org/enlaces
