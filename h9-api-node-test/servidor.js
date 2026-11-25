// Arranca la API en el puerto 3000
import { crearApp } from './app.js';

const app = crearApp('tareas.db');
app.listen(3000, () => {
  console.log('API en el puerto 3000');
});
