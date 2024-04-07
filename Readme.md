## Reto Curso Django - Ada School

Reto tomado de [wix/tdd-katas](https://github.com/wix/tdd-katas#readme)

#¡Hola!

##Antes de empezar:

Intenta no leer hacia adelante.
Haz una tarea a la vez. El truco es aprender a trabajar incrementalmente.
Esta kata demuestra los problemas de las funciones y objetos con alcance estático.

Todos los tests siempre deben pasar, independientemente de las condiciones del entorno.

Escribe una clase Saludador con una función saludar que reciba un nombre como entrada y produzca Hola <nombre> como salida. 
La firma de saludar no debe cambiar a lo largo de la kata. Puedes construir el objeto Saludador como prefieras.
saludar recorta el input.
saludar capitaliza la primera letra del nombre.
saludar devuelve Buenos días <nombre> cuando la hora es de 06:00 a 12:00.
saludar devuelve Buenas tardes <nombre> cuando la hora es de 18:00 a 22:00.
saludar devuelve Buenas noches <nombre> cuando la hora es de 22:00 a 06:00.
saludar registra en la consola cada vez que se llama.