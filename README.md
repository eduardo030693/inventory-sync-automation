# Sincronizador de Inventarios

Este robot tiene la funcion de descargar, procesar y cargar la informacion del inventario de Chavitar.

Este sincronizador tiene el proposito de automatizar un proceso muy tardado y repetitivo, que costaba demasiado tiempo en realizarse. Despues de su implementacion, se ahorraron en promedio entre 30 a 40 minutos ,que se tardaba el personal encargado en realizar el proceso en excel. Ademas, se puede estar actualizando automaticamente cada 2 minutos, lo cual permite tener informacion rapida y precisa de las existencias de cada producto que tenga movimientos de entradas o salidas.

Este proceso consiste en realizar una comparacion entre el inventario ERP de la empresa, y la web con la que se procesan los pedidos. Primeramente, el sincronizador entra a la web por medio de la libreria selenium, escribe el usuario y la contraseña, ingresa hasta donde se encuentra el inventario, copia el inventario y lo empieza a procesar hasta darle el formato deseado, posteriormente se realiza el mismo proceso con el inventario guardado en el procesador de pedidos. Al terminar el proceso anterior se realiza la comparacion para dejar solamente las existencias actuales, de acuerdo a la informacion que se extrae del ERP de la empresa, cuando se termina la comparacion se crea un documento con la informacion necesaria y de nuevo con selenium se carga dento de la web para procesar pedidos.

Este proceso se realiza completamente automatico, a primera hora del dia se enciende el sincronizador para que trabaje todo el dia y se detiene al final del turno manualmente.

Este proyecto se divide en 4 modulos:

Modulo A:

(En desarrollo)

Modulo B:

(En desarrollo)

Modulo C:

En este modulo se desarrollo el script encargado de comparar los dos inventarios extraidos tanto del ERP de la empresa, como de la web de procesamiento de pedidos.

La comparacion se realiza de la siguiente forma:

Primero nos interesa que se actualicen las existencias de los codigos que tubieron algun movimiento de entrada o salida de mercancia.

Segundo, se actualizan a cero los codigos que no aparecen dentro del inventario que se descarga del ERP.

Tercero, se agregan los codigos nuevos al inventario que se sube a la web.

Y por ultimo, se convierten en cero todas las existencias negativas que haya en el inventario del ERP.

Modulo D:

(En desarrollo)

En este proyecto aprendi a construir un proyecto de automatizacion desde cero, ya que no cuento con una carrera en esta materia, por lo cual estoy aprendiendo a traves de la creacion y la experimentacion de nuevas tecnologias. Entre las tecnologias que aprendi un poco de su funcionamiento es PANDAS y SELENIUM.

Se tomaron decisiones importantes para que el script funcionara correctamente, una de esas desiciones fue utilizar strip, para quitar los espacios que puedan quedar en el inventario y asi evitar confusiones al momento de aplicar las demas funciones y metodos. Otra decision importante fue utilizar pandas, ya que permite analizar los datos y darles el formato necesario para su analisis y transformacion.

Por ultimo me parece importante conocer otras librerias como BeautifulSoup, o Polars para realizar este proyecto, ya que puede tener ciertos beneficios y mejorar el codigo.
