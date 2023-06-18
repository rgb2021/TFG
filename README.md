# Introducción
Desarrollo de la aplicacion SisGAC (Sistema de Gestion de Alarmas para Cultivos)
Es parte para mi TFE en UNIR

En este trabajo se ha construido un sistema de supervisión para cultivos inteligentes. Para ello se han usado sensores y otros elementos de bajo costo como son placas Arduino y Raspberry pi para la recolección de la información del cultivo.

![Conexiones sensores](/docs/sensores/Untitled Sketch_bb.png "Conexiones sensores")

Por otro lado se ha desarrollado una arquitectura de servicios en la plataforma de  AWS para gestionar los datos recibidos y generar alarmas. Aprovechando así las características del entorno en la nube de Amazon escalabilidad, flexibilidad, reducción de costos, alta disponibilidad ,seguridad y velocidad de desarrollo.

![Arquitectura del proyecto](/docs/imagenes/Arquitectura.drawio.png "Arquitectura del proyecto")

Finalmente los mensajes de alarma son enviados al usuario vía Telegram, a través de un Bot que puede interactuar con el usuario intentando que sea de la forma más cercana posible.

![Respuesta Bot](/docs/imagenes/respuesta.png "Respuesta Bot")
#
