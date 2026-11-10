# Un servidor gratis para siempre, con 12 GB de RAM (Oracle Cloud Always Free)

**Datos verificados el 10 de noviembre de 2026** en la documentación oficial de Oracle. Pueden cambiar: revisa los enlaces antes de crear tu cuenta. Ayemi no tiene relación con Oracle.

## Qué incluye el nivel Always Free

| Recurso | Límite |
|---|---|
| Máquina ARM (Ampere A1, forma `VM.Standard.A1.Flex`) | 2 OCPU y 12 GB de RAM en total: una VM de 2 OCPU, o dos de 1 OCPU |
| Máquinas AMD (`VM.Standard.E2.1.Micro`) | Hasta 2, de 1/8 de OCPU y 1 GB de RAM cada una |
| Disco (Block Volume) | 200 GB en total, incluidos los discos de arranque, y 5 respaldos |
| Almacenamiento de objetos | 20 GB |

## La letra chiquita

- **Región principal:** lo gratuito solo se crea en la región principal de tu cuenta, así que elígela con cuidado.
- **Inactividad:** Oracle puede reclamar una VM gratuita si en 7 días el percentil 95 de CPU, la red y (en A1) la memoria quedan por debajo del 20 %.
- **Sin capacidad:** el error «Out of host capacity» indica una falta temporal de máquinas gratuitas en tu región. Intenta más tarde.
- **Cuenta de pago:** si la pasas a pago, Oracle no cobra lo que esté dentro de los límites gratuitos, pero sí todo lo que los exceda.

## Pasos, en resumen

1. Crea tu cuenta en https://www.oracle.com/cloud/free/ y elige tu región principal.
2. En la consola, crea una instancia con la forma `VM.Standard.A1.Flex` (procesador Ampere).
3. Asígnale 2 OCPU y 12 GB de memoria, y comprueba que aparezca la etiqueta «Always Free-eligible».
4. Guarda tu llave SSH privada en un lugar seguro. Nunca la subas a un repositorio.

La guía completa para publicar un sitio en esta VM llega con el tutorial de la saga A.

## Fuentes

- Recursos Always Free: https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm
- Cómputo ARM: https://docs.oracle.com/en-us/iaas/Content/Compute/References/arm.htm

---
Laboratorio Ayemi · CC BY-SA 4.0 · ¿Quieres tu proyecto en línea, configurado y seguro? https://ayemi.org/enlaces
