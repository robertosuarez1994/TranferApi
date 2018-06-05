# TransferApi
Api de transferencia de stocks entre sucursales en django

## Pasos a seguir para la instalacion
  * instalar Python de https://www.python.org/ python version:3.6.5
  * instalar pip https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py
  * instalar mediante pip virtualenv ejecutando "$pip install virtualenv" https://virtualenv.pypa.io/en/stable/  (*OPCIONAL)
  * dentro de la carpeta del proyecto descargado , ejecutamos virtualenv "nombre_del_entorno_virtual" (*OPCIONAL)
  * dirigirse a la carpeta que creo el entorno virtual y ejecutar el archivo activate.bat que esta el path "nombre_del_entorno_virtual\Scripts\activate.bat"
  * dentro de la carpeta del proyecto principal ejecutar $pip install django y despues $pip install djangorestframework y por ultimo pip install django-cors-headers
  * ejecutar la linea $python manage.py runserve
## Consideraciones
  * Cree un modelo , cuya intencion es la de menor repeticion posible
  * Pense en un modelo , flexible para que puedan adaptarse facilmente a mas sucursales y mas productos
  * Intente poner la logica del lado de la api para que no influya a la hora de cambiar el app frontend
  * El modelo solo guarda los productos en kilogramos
  * Faltaron algunos detalles por terminar, pero considerando que hasta una semana no habia creado ninguna api ni app en angular fue una semana de mucho aprendizaje. Espero no hay problemas mayores con las aplicaciones. 
