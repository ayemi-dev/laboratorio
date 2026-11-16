# Qué es React: componentes, JSX, props y estado

Segundo video de la serie **Desarrollo web: stacks y frameworks** del Laboratorio Ayemi. [React](https://react.dev/) es una biblioteca de JavaScript para construir interfaces de usuario (versión actual 19.3, código abierto con licencia MIT). Aquí tienes la misma lista de tareas del video anterior, ahora armada con React.

## Las cuatro ideas en este código

| Idea | Qué es | Dónde se ve |
|---|---|---|
| Componentes | Piezas de la interfaz con su propia lógica y apariencia | `src/App.jsx` líneas 3–5 (`Tarea`) y 7–31 (`App`) |
| JSX | Marcado parecido a HTML que devuelve cada componente | `src/App.jsx` línea 4 (`<li>{texto}</li>`) y líneas 18–29 |
| Props | Datos que le pasas a un componente | `src/App.jsx` línea 3 (`{ texto }`) y línea 23 (`texto={t}`) |
| Estado | Lo que el componente recuerda; al cambiar, React vuelve a llamarlo | `src/App.jsx` líneas 8–12 (`useState`) y 14–16 (`setTareas`) |

## Córrela

Necesitas Node.js 26 (la versión LTS vigente; se probó con la 26.13.1). La demo corre en React 19.3.1 con Vite 8.3.8.

```bash
npm install
npm run dev
```

Abre la dirección local que imprime Vite (por defecto `http://localhost:5173/`). Presiona **Agregar** para ver cómo cambia el estado y se agrega «Aprender React» a «Mis tareas».

## Cómo se creó el proyecto con Vite

Para empezar sin framework, la documentación de React recomienda una herramienta de compilación como Vite. Este proyecto se creó con:

```bash
npm create vite@latest h2-react -- --template react --no-interactive
```

## Programas y sitios

| Recurso | Enlace |
|---|---|
| Aprende React (documentación oficial) | https://react.dev/learn |
| Versiones de React | https://react.dev/versions |
| Empezar un proyecto | https://react.dev/learn/creating-a-react-app |
| Sin framework (Vite) | https://react.dev/learn/build-a-react-app-from-scratch |
| Guía de Vite | https://vite.dev/guide/ |
| Repositorio de React | https://github.com/facebook/react |

Datos verificados el 16 de noviembre de 2026 en la documentación oficial de React y Vite. Ayemi no tiene relación con el proyecto React, con Meta ni con Vite.

---
Código: MIT · Guía: CC BY-SA 4.0 · ¿Necesitas tu página o tu sistema a la medida? Lo construimos: https://ayemi.org/enlaces
