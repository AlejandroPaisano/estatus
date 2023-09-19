# estatus

# introduccion
En esta actividad se quierer realizar un programa que sea capaz de ver el estado de una aplicacion e interactuar con esta misma, ya sea para abrir dicha aplicacion o evitar que una aplicacion llegeu a abrirse, como en este caso. 
Aqui haremos uso de la funcion kill para evitar que una aplicacion abra durante el booteo del equipo

# desarrollo
![1](https://github.com/AlejandroPaisano/estatus/assets/91223611/bafba357-8b4b-4b79-bfc2-d33f27be45ab)
En la primer imagen podemos observar las dos funciones principales del programa, lock y argumentos, argumentos se encarga de confirmar que el programa tenga informacion con la cual trabajar, en caso contrario, no nos molestaremos en iniciar el programa.

Despues esta lock, que es la funcion que revisa la lista de procesos que se estan ejecutando y si encuentra el proceso para el que se le ha programado, mata ese proceso. 
Por ultio esta el codigo que inicia la funcion, que requiere que se referencia el propio archivo para inciar y quie ejecuta sus instruccciones en un while true, un ciclo infinito que impide que se abra el programa marcado hasta que el servicio termine
