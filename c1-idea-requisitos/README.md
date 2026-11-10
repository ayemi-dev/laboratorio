# De la idea a los requisitos con IA

Antes de pedirle código a una IA, pídele que te entreviste. Así no inventa lo que no le dijiste.

## Prompt

Cópialo y cambia la primera línea por tu idea:

```text
Quiero una app para agendar citas en mi consultorio.
Antes de escribir código, entrevístame: hazme una pregunta a la vez
para definir los requisitos (quién la usa, qué debe hacer, qué no hará
y qué datos guarda). Cuando termines, escribe un documento de requisitos.
```

## Cómo usarlo

1. **Responde una pregunta a la vez.** Si no sabes algo, dilo: «todavía no lo sé» también es un requisito.
2. **Corrige lo que suponga.** Si la IA asume algo que no dijiste, díselo.
3. **Pide el documento** con estas secciones: usuarios, funciones, fuera de alcance, datos y «terminado cuando».
4. **Con el documento, pide el código.** Si contratas a alguien, ese documento es lo que le entregas.

Funciona con cualquier asistente de IA.

## Documento de ejemplo

```text
Requisitos · App de citas

Usuarios
- Pacientes: ven horarios libres y agendan.
- Recepción: confirma y reprograma citas.
- Médico: consulta su agenda del día.

Funciones
- Ver horarios libres por día.
- Agendar y cancelar una cita.
- Recordatorio por WhatsApp 24 h antes.

Fuera de alcance
- Pagos en línea.
- Expediente clínico.

Datos
- Nombre, teléfono, fecha, hora y motivo de la cita.

Terminado cuando
- Un paciente agenda desde su celular en menos de 1 minuto.
```

---
Laboratorio Ayemi · CC BY-SA 4.0 · ¿Necesitas tu página o tu sistema a la medida? https://ayemi.org/enlaces
