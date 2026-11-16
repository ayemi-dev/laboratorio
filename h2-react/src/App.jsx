import { useState } from 'react';

function Tarea({ texto }) {
  return <li>{texto}</li>;
}

export default function App() {
  const [tareas, setTareas] = useState([
    'Diseñar la interfaz',
    'Crear la API',
    'Guardar en la base',
  ]);

  function agregar() {
    setTareas([...tareas, 'Aprender React']);
  }

  return (
    <main>
      <h1>Mis tareas ({tareas.length})</h1>
      <ul>
        {tareas.map((t, i) => (
          <Tarea key={i} texto={t} />
        ))}
      </ul>
      <button onClick={agregar}>
        Agregar
      </button>
    </main>
  );
}
