import { useState } from 'react';

async function guardarTarea(texto) {
  const res = await fetch('/api/tareas', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ texto }),
  });
  if (!res.ok) {
    throw new Error(res.status);
  }
  return res.json();
}

function NuevaTarea({ onNueva }) {
  const [texto, setTexto] = useState('');
  const [error, setError] = useState('');
  const [envio, setEnvio] = useState(false);

  function cambiar(e) {
    setTexto(e.target.value);
  }

  async function enviar(e) {
    e.preventDefault();
    const limpio = texto.trim();
    if (limpio === '') {
      setError('Escribe una tarea.');
      return;
    }
    setError('');
    setEnvio(true);
    try {
      onNueva(await guardarTarea(limpio));
      setTexto('');
    } catch {
      setError('No se pudo guardar.');
    } finally {
      setEnvio(false);
    }
  }

  return (
    <form onSubmit={enviar}>
      <label htmlFor="texto">Nueva tarea</label>
      <input
        id="texto"
        value={texto}
        onChange={cambiar}
        aria-invalid={error !== ''}
        aria-describedby="error-texto"
      />
      <p id="error-texto" role="alert">
        {error}
      </p>
      <button disabled={envio}>
        {envio ? 'Guardando…' : 'Guardar'}
      </button>
    </form>
  );
}

export default NuevaTarea;
