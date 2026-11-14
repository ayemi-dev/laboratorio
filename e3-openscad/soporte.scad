// Soporte para celular · Laboratorio Ayemi
// Medidas en mm. El Customizer vuelve
// controles los comentarios con [rango].
grosor_cel = 11;  // [6:0.5:16]
ancho = 70;       // [50:5:100]
angulo = 65;      // [50:5:80]
ranura_cable = true;

/* [Hidden] */
pared = 4;
alto = 90;        // largo del respaldo
labio = 14;       // tope del frente
x0 = pared + grosor_cel;
fondo = x0 + alto * cos(angulo) + 12;
ax = x0 + pared + alto * cos(angulo) / 2;
az = alto * sin(angulo) / 2;

module perfil() {
  intersection() {      // nada bajo el piso
    square([fondo, alto]);
    offset(r = 1.5) offset(delta = -1.5) {
      square([fondo, pared]);     // base
      square([pared, labio]);     // labio
      translate([x0, 0])          // respaldo
        rotate(angulo - 90)
          square([pared, alto]);
      hull() {                    // apoyo
        translate([ax, az]) circle(d = pared);
        translate([fondo - pared, 0])
          square(pared);
      }
    }
  }
}

difference() {
  rotate([90, 0, 0])
    linear_extrude(ancho, center = true)
      perfil();
  if (ranura_cable)              // cable
    translate([-1, -6, -1])
      cube([x0, 12, labio + 2]);
}
