import { useState } from 'react';
import { guardarTarea } from './api.js';

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
