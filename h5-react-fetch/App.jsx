import { useEffect, useState } from 'react';

async function pedirTareas() {
  const res = await fetch('/api/tareas');
  if (!res.ok) {
    throw new Error(res.status);
  }
  return res.json();
}

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
    </main>
  );
}
