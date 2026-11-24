// La dirección de tu API, desde .env
const API = import.meta.env.VITE_API_URL;
const TAREAS = `${API}/tareas`;

// GET: trae las tareas
async function pedirTareas() {
  const res = await fetch(TAREAS);
  if (!res.ok) {
    throw new Error(res.status);
  }
  return res.json();
}

// POST: guarda una tarea nueva
async function guardarTarea(texto) {
  const res = await fetch(TAREAS, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      texto,
      proyecto_id: 1,
    }),
  });
  if (!res.ok) {
    throw new Error(res.status);
  }
  const { id } = await res.json();
  return { id, texto };
}

export { pedirTareas, guardarTarea };
