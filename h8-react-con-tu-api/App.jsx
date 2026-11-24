import { useEffect, useState } from 'react';
import { pedirTareas } from './api.js';
import NuevaTarea from './NuevaTarea.jsx';

export default function App() {
  const [tareas, setTareas] = useState([]);
  const [carga, setCarga] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    let ignorar = false;
    pedirTareas()
      .then((datos) => {
        if (!ignorar) setTareas(datos);
      })
      .catch(() => {
        if (!ignorar) setError(true);
      })
      .finally(() => {
        if (!ignorar) setCarga(false);
      });
    return () => {
      ignorar = true;
    };
  }, []);

  function agregar(nueva) {
    setTareas([...tareas, nueva]);
  }

  if (carga) {
    return <p>Cargando…</p>;
  }
  if (error) {
    return <p>No se pudieron cargar.</p>;
  }

  return (
    <main>
      <h1>Mis tareas ({tareas.length})</h1>
      <ul>
        {tareas.map((t) => (
          <li key={t.id}>{t.texto}</li>
        ))}
      </ul>
      <NuevaTarea onNueva={agregar} />
    </main>
  );
}
