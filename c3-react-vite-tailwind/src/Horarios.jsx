const horas = [
  '09:00', '10:00', '11:00',
  '12:00', '16:00', '17:00',
]

const boton =
  'rounded-lg border border-teal-700 py-2 ' +
  'font-semibold text-teal-700'

export default function Horarios() {
  return (
    <section className="rounded-xl bg-white p-4">
      <h2 className="mb-3 font-bold">
        Horarios libres
      </h2>
      <div className="grid grid-cols-3 gap-2">
        {horas.map((h) => (
          <button key={h} className={boton}>
            {h}
          </button>
        ))}
      </div>
    </section>
  )
}
