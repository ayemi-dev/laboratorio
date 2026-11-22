# ¿Fue la IA? No: fue un archivo · Valida tus JSON antes de subirlos

Guía del video. Cada comando va en su propia línea y se copia tal cual. Todo se corre en **Git Bash** (Windows) o en la terminal de **Linux** o **Mac**. Solo necesitas **Python 3**, que ya trae el validador: no hay que instalar nada más.

> **En Linux y Mac** el comando suele llamarse `python3` en lugar de `python`. Si `python --version` no responde, usa `python3` en todos los comandos de esta guía.

> **Regla de oro:** un archivo de configuración se revisa **antes** de subirlo. Si el revisor sale con un código distinto de 0, el archivo no sube.

## 1. Arma el archivo de práctica

En una carpeta nueva, **fuera** de tus proyectos, crea un `config.json` al que le falta una coma (después de `true`):

```sh
printf '{\n  "servicio": "vuelos",\n  "activo": true\n  "reintentos": 3\n}\n' > config.json
```

```sh
cat config.json
```

Debe mostrar cinco líneas; la tercera, `"activo": true`, **sin** coma al final.

## 2. Valídalo

```sh
python -m json.tool config.json
```

Debe responder con el error, la línea y la columna:

```text
Expecting ',' delimiter: line 4 column 3 (char 45)
```

Se queja en la **línea 4** porque ahí empieza lo que no esperaba: después de `true` tenía que venir una coma.

## 3. Mira el código de salida

```sh
echo $?
```

Debe mostrar `1`: el validador terminó con error. Así es como un script o un despliegue automático sabe que algo salió mal.

## 4. Arréglalo y vuelve a validar

Agrega la coma al final de la línea que termina en `true`:

```sh
sed -i 's/true$/true,/' config.json
```

> **En Mac**, `sed -i` pide un sufijo, aunque sea vacío: `sed -i '' 's/true$/true,/' config.json`. También puedes abrir el archivo y escribir la coma a mano.

```sh
python -m json.tool config.json
```

Ahora imprime el JSON con sangría de cuatro espacios, ya con la coma:

```text
{
    "servicio": "vuelos",
    "activo": true,
    "reintentos": 3
}
```

```sh
echo $?
```

Debe mostrar `0`: todo bien, ya puede subir.

## 5. Revisa todos los JSON de tu proyecto de una vez

Desde la carpeta de tu proyecto. Revisa cada `.json` (sin entrar a `node_modules` ni a `.git`) y, si uno está mal, te muestra el error y el nombre del archivo; si todos están bien, no imprime nada:

```sh
find . -name '*.json' -not -path '*/node_modules/*' -not -path '*/.git/*' | while read -r f; do python -m json.tool "$f" > /dev/null || echo "revisa: $f"; done
```

> **Ojo:** algunos archivos `.json` permiten comentarios, como `tsconfig.json` o los de `.vscode/`. No son JSON estricto y este comando los marcará con error aunque estén bien: ignóralos o sácalos con otro `-not -path`.

## 6. Que tu despliegue automático lo frene

En GitHub Actions, un paso que sale con un código distinto de 0 falla y los pasos siguientes no corren. Basta con validar antes de desplegar. Por ejemplo, un paso de un flujo de trabajo:

```yaml
- name: Validar config.json
  run: python -m json.tool config.json
```

Si `config.json` está roto, el paso falla y el despliegue que venga después no se ejecuta.

## Lo que dicen los informes oficiales

- **Windows, 19 de julio de 2024:** una actualización de configuración de CrowdStrike (el «Channel File 291») provocó la pantalla azul en 8.5 millones de equipos. No fue un ciberataque. Fuentes: [Microsoft](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/) y [CrowdStrike](https://www.crowdstrike.com/en-us/blog/falcon-update-for-windows-hosts-technical-details/).
- **Vuelos en Estados Unidos, 11 de enero de 2023:** la FAA pausó todas las salidas nacionales y rastreó la falla hasta un archivo de base de datos dañado. Fuente: [FAA](https://www.faa.gov/newsroom/faa-notam-statement).

Validar un JSON no habría evitado esas caídas tal cual pasaron: la lección es la costumbre de **revisar cualquier archivo de configuración antes de que llegue a producción**.

---
Guía: CC BY-SA 4.0 · Código: MIT · ¿Necesitas algo más específico? Lo construimos: https://ayemi.org/enlaces
