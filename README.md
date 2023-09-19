# estatus

# introduccion
En esta actividad se quierer realizar un programa que sea capaz de ver el estado de una aplicacion e interactuar con esta misma, ya sea para abrir dicha aplicacion o evitar que una aplicacion llegeu a abrirse, como en este caso. 
Aqui haremos uso de la funcion kill para evitar que una aplicacion abra durante el booteo del equipo

# desarrollo
![1](https://github.com/AlejandroPaisano/estatus/assets/91223611/bafba357-8b4b-4b79-bfc2-d33f27be45ab)
En la primer imagen podemos observar las dos funciones principales del programa, lock y argumentos, argumentos se encarga de confirmar que el programa tenga informacion con la cual trabajar, en caso contrario, no nos molestaremos en iniciar el programa.

Despues esta lock, que es la funcion que revisa la lista de procesos que se estan ejecutando y si encuentra el proceso para el que se le ha programado, mata ese proceso. 
Por ultio esta el codigo que inicia la funcion, que requiere que se referencia el propio archivo para inciar y quie ejecuta sus instruccciones en un while true, un ciclo infinito que impide que se abra el programa marcado hasta que el servicio termine

![3](https://github.com/AlejandroPaisano/estatus/assets/91223611/227fbd4b-1d78-45c6-bc4e-201c41408783)
Una vez que el programa esta hecho, pasamos al nssm para convertirlo en un servicio. para ello  primero debemos poner el nssm en algun lugar que el sistema identifique como un camino por defecto, por ejemplo, la carpeta roaming.
Hecho lo anterior, iniciaremos el powershell de windows en modo administrador e introduciremos el comando nssm isntall seguido del nombre del archivo, como aqui el servicio ya se instalo, mostrare la ventana de edit.

![2](https://github.com/AlejandroPaisano/estatus/assets/91223611/ed3c6003-b148-45e8-9bb5-baa554f595cc)
Dentro de la ventana, eligiremos la ubicacion del lugar donde sera interpretado el codigo, el lugar del script que deseamos convertir en servicio y los argumentos que usaremos para el servicio, en este caso, el nonmbre del
archivo y la aplicacion a cerrar.

En mi caso personal elegir la aplicacion de discord debido a que esta se inicia, no importa que tanto la haya sacado de las asplicaciones de arranque del sistema. Hecho lo anterior, presionaremos el boton de edit service o install service, tambien podemos cambiar si el servicio se iniciara de forma automatica o manual.

![4](https://github.com/AlejandroPaisano/estatus/assets/91223611/e0d1771b-cd25-4372-941e-652737dc14a3)

Para iniciar el servicio, solo escribimos nssm start y el nombre del servicio, de esta forma tendremos un servicio que se encargara de eliminar un proceso del sistema y de asegurarse que no surja, si queremos terminarlo, basta con escribir nssm.exe stop y el nombre del servicio
![5](https://github.com/AlejandroPaisano/estatus/assets/91223611/f5e8443a-972c-4e59-a047-dadcd4dddb02)

# conclusiones
La verdad es que nunca habia realizado algo relacionado a servicios con anterioridad. Si, sabia que existian y otras cosas, pero nunca antes habia llegado a tener la necesidad o interes por trabajar dentro de los mismos servicios.
La verdad es que es mas inttuitivo de lo que esperaba, incluso podria decir que es algo amable dentro de lo que cabe en cuanto a trabajar en consola. Tambien puedo ver la utilidad en poder manejar de forma mas personal el como ciertos servicios interactuan con el sistema.
Por ejemplo, poder configurar la computadora para bloquear redes sociales o aplicaciones de videojuegos durante ratos de estudio, y aunque es cierto que se puede conseguir esto con aplicaciones externas,creo que vale mas hacerlo de forma personalizada, tanto por temas de gustos del usuario como por cuestiones de privacidad.
