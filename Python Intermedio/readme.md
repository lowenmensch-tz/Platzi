```
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/05/21
```

# Curso de Python Intermedio

Apuntes importantes sobre el curso de **Python intermedio**  
Curso disponible en [Platzi](https://platzi.com/clases/python-intermedio/)

## Slides

[Documento.pdf](https://static.platzi.com/media/public/uploads/slides-del-curso-de-python-intermedio_938f5787-3c10-4c3e-b0d0-d962e7dbec36.pdf)

## Zen de Python

Tim Peter 

**Creación:** 19-Aug-2004

El Zen de Python se compone por los principios para escribir tu código de manera clara, sencilla y precisa. Estos son:

- **Bello es mejor que feo**:Pyhton es estéticamente superior a cualquier otro lenguaje de programación. Al momento de escribir código, es mejor que sea de manera limpia y estética.
- **Explícito es mejor que implícito**:Hacer más fácil que las otras personas entiendan el código.
- **Simple es mejor que complejo**:Es mejor tener una implementación simple, que ocupe pocas lineas de código y sea entendible, a que sea una larga y complicada.
- **Complejo es mejor que complicado**:Si tenemos que extendernos en la implementación y hacerla más compleja para que el código si se entienda, esto es mejor que hacerlo simple y mal.
- **Plano es mejor que anidado**:El *anidamiento* es cuando tenemos un bloque de código dentro de otro bloque de código (dependiendo de este). Esto se nota en Python por la identación, nos quedarían estos bloques muy corridos a la derecha. Es mejor evitar el anidamiento, y hacer las cosas de **manera plana**.
- **Espaciado es mejor que denso**:Por la identación de Python (sus sangrías), este principio se nos hace imposible de esquivar. El código inevitablemente es espaciado.
- **La legibilidad es importante**:Es importante que otros programadores puedan entender lo que estamos escribiendo. Esto hace más fáciles las cosas cuando trabajemos con otros en los proyectos.
- **Los casos especiales no son lo suficientemente especiales cpmo para romper las reglas (sin embargo, la practicidad le gana a la pureza)**:Siempre que podamos respetar estas reglas que nos plantea Python, es mejor así. Sin embargo, si por el hecho de hacer un código muy puro o muy ‘Pythonista’, este pierde legibilidad, es mejor ser más prácticos y romper o saltearnos algunas de estas reglas para que el código sea más eficiente. Por lo tanto, llegado el momento debermos decidir si es mejor hacer las cosas de manera pura o práctica.
- **Los errores nunca deberían pasar silenciosamente (a menos que se silencien explícitamente)**:Manejar los erroes es fundamental. Cada error nos dice algo y hay que prestarle atención. A menos que seas capaz de silenciar un error explícitamente, aunque para esto hay que tener criterio.
- **Frente a la ambiguedad, evitar la tentación de adivinar**:Nuestro código debería solamente tener una interpretación. Si en un contexto significa algo, y en otro otra cosa, es mejor que lo revisemos y busquemos una solución.
- **Debería haber una, y preferiblemente sola, una manera obvia de hacerlo. (A pesar de que esa manera no sea obvia a menos que seas holandés)**:Esto hace referencia al creador de Python ''Guido van Rossum", que de manera muy inteligente encontrar las soluciones precisas a los problemas, y deberíamos imitarlo.
- **Ahora es mejor que nunca**:Es mejor desarrollar nuestra solución cuánto antes, no dejarlo para mañana o para mas adelante.
- **A pesar de que nunca es muchas veces mejor que *ahora* mismo**:Si por hacer las cosas ya y tenemos poco tiempo, si es mejor dejarlo para después y no hacerlo apurado y mal.
- **Si la implementación es díficil de explicar, es una mala idea, y si es fácil de explicar, es una buena idea**:Si somos capaces de explicar nuestra implementación a otros desarrolladores paso a paso, es una buena idea. En cambio si no podemos hacerlo, significa que ni nosotros entendemos la implementación y deberíamos repensar nuestra forma de encarar la solución.
- Los **espacios de nombres** son una gran idea, ¡Tengamos más de esos! (namespaces):Es el nombre que se ha indicado luego de la palabra import, es decir la ruta (namespace) del módulo. (Lo veremos a profundidad más adelante).

## ¿Qué es la documentación?

**La documentación es fundamental para aprender cualquier lenguaje de programación**, ya que nos ayuda a entender todas las pequeñas piezas para que todo funcione correctamente. **Está escrito en un lenguaje muy técnico.**

**PEP (Python Enhancement Proposals | Propuestas de mejoras de python)**

Son los documentos que conforman a todas las guías de estilo. Cómo deberíamos de escribir código  Python.

Nos indica como el lenguaje funciona y como se debería escribir de forma correcta. Todo lo relacionado a buenas practicas en la escritura del código (identacion, comentarios, nombres recomendados) 

- Style Guide for Python Code (PEP8):

    [PEP8](https://www.python.org/dev/peps/pep-0008/)

- PEP

    [PEPindex](https://www.python.org/dev/peps/)

- Documentación de python:

    [https://docs.python.org/3/](https://docs.python.org/3/)

## ¿Qué es un entorno virtual?

**Entorno de desarrollo virtual o env:**

Un entorno de desarrollo virtual python o simplemente entorno virtual python es un mecanismo que me permite gestionar programas y paquetes python sin tener permisos de administración, es decir, cualquier usuario sin privilegios puede tener uno o más “espacios aislados”. Donde poder instalar distintas versiones de programas y paquetes python. Para crear los entornos virtuales vamos a usar el programa virtualenv o el módulo venv y para instalar paquetes python vamos a usar el programa pip.

**Pypi(Python package index):**

Es un repositoro de paquetes de terceros que se pueden utilizar para proyectos en python, estos paquetes generalmente traen codigo que podemos utilizar para proyectos desde funciones clases y metodos que nos haran la vida mas facil al momento de desarrollar proyectos.

## El primer paso profesional: Creación de un entorno virtual

**Entornos virtuales**

**Creación de entorno y uso de variable para *invocar el entorno virtual***

`.bashrc`  archivo que contiene la configuración inicial, y usualmente se encuentra en nuestro `$HOME`

1. `sudo python3 -m venv /path/to/new/virtual/environment`
2. Ejecutar `sudo nano ~/.bashrc`
    - Sí usamos zshcr `sudo nano ~/.zshrc`
3. Ir al final del archivo
4. Agregar el comando: `alias avenv='source venv/bin/activate'`
5. Guardar presionando `ctrl + o` y luego salir con `ctrl + x`
6. Ejecutar la configuración de la terminal: `source ~/.bashrc`
7. Activar el entorno vitual `avenv`

De esa forma persistirá siempre, ya que el alias se guarda dentro del archivo de configuración de la termial

**Uso del entorno virtual**

1. Se crea una carpeta que contiene una versión de python y en la cual podrás instalar las dependencias (paquetes) de manera ahislada, dentro de esta carpeta nos interesa la carpeta bin, en la que se encuentra el comando de activación
2. **Activación de entorno**: `source venv\bin\activate` (venv o el nombre que le pusiste al entorno virtual)
3. **Desactivar el entorno**: `deactivate` **Alias**
4. Son atajos que creamos para evitar escribir comandos largos (sobre todo si lo hacemos de manera recurrente)

## Instalaciones de dependencias con PIP

**Pip (package installer for python)** Nos permite descargar paquetes de terceros para utilizarlos en nuestro enviroment, ademas se puede definir una versión especifica del paquete.

- `pip install <paquete>` instala el paquete (pandas , matplotlib, bokeh, etc) que se especifique
- `pip freeze` muestra todos los paquetes instalados en tu ambiente virtual

Si quisiéramos que alguien mas pueda ejecutará nuestro proyecto es importante compartir que librería y versión hemos empleado; eso se realiza con el comando:

```bash
pipfreeze > requirements.txt
```

El resultado de `pip freeze` se escribe en `requirements.txt` para instalar paquetes desde un archivo como `requirements.txt` ejecutamos:

```bash
pipinstall -r requirements.txt
```

Básicamente, `pip` es como el `npm` de JavaScript, y el archivo `requeriments.txt`

es como el `package.json` de JavaScript.

Es importante recordar que esto se debe correr con el entorno virtual activado, de esta manera todas las dependencias que instalemos se guardaran para este entorno virtual (de lo contrario se guardarían de manera global).

Algo importante, si estás manejando git, es bueno siempre ignorar la carpeta `venv`

esto porque realmente no nos importa subir todo eso al repositorio, puedes mirarlo como que `venv`es el `node_modules`  de JavaScript, a fin de cuentas, cualquier otro programador que trabaje con nuestro código creará su propio entorno virtual e instalará dependencias que dejamos en nuestro `requeriments.txt.`

El operador `>` en la terminal es algo especial de UNIX, ya que este operador lo que hace es redirigir la salida de cualquier comando hacia donde lo mandes, por defecto la salida es en la terminal, pero al usar `>`  le dijimos a la terminal que, en lugar de que la salida sea en la terminal, que se redirija al archivo `requeriments.txt`. Si quieren jugar con ello, pueden hacerlo con este ejemplo:

```bash
ls -al > test.txt
```

, eso creará un archivo llamado

```bash
test.txt
```

## Una alternativa: Anaconda

Anaconda es un programa de Python que contiene los paquetes más utilizados en temas de ingeniería, matemáticas o ciencia, como pueden ser Matplotlib, SciPy y NumPy. Cuenta con versiones para los tres sistemas operativos más importantes: Mac, Windows y Linux.

Y es un ambiente de trabajo para la ciencia de datos que permite hacer funcionar aplicaciones y administrar fácilmente distintos paque- tes. Así, Anaconda Navigator puede buscar paquetes en Anaconda Cloud o en otros repositorios, y está disponible para ambientes Windows, macOS y Linux.

![https://static.platzi.com/media/user_upload/Conda-9450dd76-6a83-475c-a1dd-b9ea9241dd24.jpg](https://static.platzi.com/media/user_upload/Conda-9450dd76-6a83-475c-a1dd-b9ea9241dd24.jpg)

## Funciones anónimas: lambda

Las funciones anónimas solo pueden tener una línea de código

```bash
lambda: arguments: expression
```

## High order functions: filter, map y reduce

**Función de orden superior:**

Es una función que recibe como parámetro a otra función

La diferencia entre **filter y map**:

- *filter* devuelve True or False según el valor esté dentro de los criterios buscados o no. En caso de que no cumpla con la condición, no será devuelto y la lista se verá reducida por este filtro.
- *Map* funciona muy parecido, pero su diferencia radica en que no puede eliminar valores de la lista del array entregado. Es decir, el output tiene la misma cantidad de valores que el input.

Cómo funciona **reduce**:

- *Reduce* toma 2 valores entregados como parámetros y el iterador como otro parámetro. Realiza la función con estos 2 valores, y luego con el resultado de esto y el valor que le sigue en el array. Y así hasta pasar por todos los valores de la lista.

**Use de filter**

```python
my_list = [1, 4, 5, 6, 9, 13, 19 ,21]
#filter( function, list )
list(
        filter(
            lambda x: x%2 !=0, my_list
        )
    )

```

**Uso de map**

```python
my_list = [1, 4, 5, 6, 9, 13, 19 ,21]
#map( function, list )  
list(map(lambda x: x**2, my_list))
```

**Uso de reduce**

```python
import functools 
my_list = [2, 2, 2, 2, 2]
# functools.reduce( function, list )
functools.reduce( lambda x, y: x*y, my_list )
```

**Código avanzado python**

```python
#Agrega un nuevo atributo 'old' al diccionario
#concatenación de diccionarios
# python < 3.9 {**dict1, **dict2}
# python 3.9   dict1 | dict2
old_people = list(
		map(
			lambda worker: 
			{**worker, **{'old': worker['age'] > 70}} 
			, DATA
			)
	)
```

## Los errores en el código

![https://static.platzi.com/media/user_upload/Selection_333-c63590c2-26a7-4d31-91e0-0913c2e83497.jpg](https://static.platzi.com/media/user_upload/Selection_333-c63590c2-26a7-4d31-91e0-0913c2e83497.jpg)

![Curso%20de%20Python%20Intermedio%2014aca0750b164080958843803dec8b2d/Untitled1.png](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Faa917e57-376c-4c04-8c20-89ae67272838%2FUntitled1.png?id=14aca075-0b16-4080-9588-43803dec8b2d&table=block&spaceId=033a3589-22a4-4a7b-9962-b80a21342092&width=3840&userId=017701f4-4fa1-4b44-9596-49d1d5fe44f7&cache=v2)

Exception

![Curso%20de%20Python%20Intermedio%2014aca0750b164080958843803dec8b2d/Untitled1%201.png](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F5de87939-d53c-4057-9ef1-1ca0f77b7512%2FUntitled1.png?id=4491e2b0-2a37-40b1-9429-20032b07eafe&table=block&spaceId=033a3589-22a4-4a7b-9962-b80a21342092&width=3840&userId=017701f4-4fa1-4b44-9596-49d1d5fe44f7&cache=v2)

**Errores en el código**

Cuando python nos avisa que tenemos un error en el código nos avienta un mensaje que conocemos como traceback, puesde ser debido a:

- Errores de Sintaxis (SyntaxError) → escribimos mal alguna palabra clave (typo), el programa no se ejecuta.
- Excepciones (Exeption) → Producen un colapso o interrupción de la lógica del programa en alguna línea en específico por ejemplo (todas las líneas anteriores se ejecutan), pueden ser de varios tipos, generalmente aparecen cuando no existe un componente clave en la ejecución o hay alguna imposibilidad lógica (matemática) para efectuar la instrucción, también pueden generarse dentro del código o fuera de el (elevar una excepción)

**Lectura de un traceback**

- La manera correcta de leer un traceback es iniciar por el final, en el caso de un error de sintaxis nos indicará en qué línea se encuentra dicho error.
- En el caso de excepciones la última línea nos indicará el tipo de exepcion que se generó (generalmente son autoexplicativas pero si no entienedes que paso puedes buscar este error)
- La penúltima línea nos indicará dende se encuentra el error (archivo y línea)
- La antepenúltima línea nos muestra “most recent call last” lo que significa que la llamada más reciente es la última (el programa se cerró después de esa llamada, se genero un error)

**Elevar una excepción**

- Cuando tenemos una excepción en python lo que sucede es que se crea un objeto de tipo exception que se va moviendo a través de los bloques de código hasta llegar al bloque principal si es que no se maneja dicha excepción en algún bloque intermedio el programa se interrumpe y genera el traceback

## Debugging

![https://code.visualstudio.com/assets/docs/editor/debugging/debugging_hero.png](https://code.visualstudio.com/assets/docs/editor/debugging/debugging_hero.png)

**Debug actions**

![https://code.visualstudio.com/assets/docs/editor/debugging/toolbar.png](https://code.visualstudio.com/assets/docs/editor/debugging/toolbar.png)

- Continue / Pause F5

    Permite pausar la ejecución del programa

- Step Over F10

    Permite avanazr un solo paso en el programa

- Step Into F11

    Ingresamos a un bloque secundario del programa (funciones)

- Step Out Shift+F11

    Salimos del bloque secundario

- Restart Ctrl+Shift+F5

    Reinicia el programa

- Stop Shift+F5

    detiene el programa

**Nota:**

- Existen herramientas de debugging propias de python como el módulo **pdb** o los **breakpoints** (a partir de python 3.7)

## Manejo de excepciones

**Manejo de Excepciones**

- try except → Anidamos nuestro programa en dos bloques de código, el primero es el programa per se (el que se ejecuta normalmente, sin errores) y el segundo representa las instrucciones a seguir en caso de error.

    ```python
    try:
    	<bloque1>
    except <error> as <alias>:
    	<bloque 2>
    ```

    - `<error>` es un parámetro opcional, permite capturar sólo el tipo de error indicado, si no se coloca captura todos los errores posibles (es buena práctica capturar cada tipo de error por separado)
    - `as <alias>` nos permite crear un alias al error, para trabajar con él.

- raise → Esta instrucción nos permite generar errores, es decir crear nuestros propios errores cuando detectemos que nuestro programa no actúa como debería con cierto tipo de datos

    ```python
    raise <NombreError>("<descripci[on del error>")
    ```

- fynally → Es una bloque de código que se ejecuta exista un error o no (un tercer bloque después de try except), no es muy usual pero puede darse para cerrar archivos, conexiones a BBDD o liberar recursos

## Assert statements

![Curso%20de%20Python%20Intermedio%2014aca0750b164080958843803dec8b2d/Untitled1%202.png](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F36ec199e-9823-4734-8cbe-bd30b616a387%2FUntitled1.png?id=e9894599-d2cb-4e5e-a877-5eec95f88bb5&table=block&spaceId=033a3589-22a4-4a7b-9962-b80a21342092&width=3840&userId=017701f4-4fa1-4b44-9596-49d1d5fe44f7&cache=v2)

![Curso%20de%20Python%20Intermedio%2014aca0750b164080958843803dec8b2d/Untitled1%203.png](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fb7398afe-703a-4afc-8a4d-841d3ab6a903%2FUntitled1.png?id=def180c4-ea8c-41a1-9a5a-c3e2d416ffa3&table=block&spaceId=033a3589-22a4-4a7b-9962-b80a21342092&width=3840&userId=017701f4-4fa1-4b44-9596-49d1d5fe44f7&cache=v2)

**Assert statements**

- Es una manera poco usual de manejar los errores en python
- Evalúa una condicional, si esta se cumple continuamos con el flujo normal del python, si no se cumple eleva un error del tipo `AssertionError` y nos muestra un mensaje.
- Su sintaxis es:

```python
assert <condicion>, <"mensaje">
<código>
```

## ¿Cómo trabajar con archivos?

**Modos de Apertura**

- **r** -> Solo lectura
- **r+** -> Lectura y escritura
- **w** -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
- **w+** -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
- **a** -> Añadido (agregar contenido). Crea el archivo si éste no existe
- **a+** -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

**Adicionalmente**

Existen varias extensiones de archivos con los que podemos interactuar con python (js,csv,py,css,json,xml)Para abrir un archivo seguimos las siguiente estructura

```python
with open(<ruta>, <modo_apertura>)as <nombre>
```

`with` Es un manejador contextual, nos ayuda a controlar el flujo del archivo (sirve para que el archivo no se dañe cuando existe algún cierre inesperado)

`open(ruta,modo_apertura)`: es una función que necesita de dos parámetros

- `ruta`: es donde se encuentra nuestro archivo en nuestro equipo
- `modo_de_apertura`: como vamos a abrir el archivo, los modificadores son:r → modo de lecturaw → modo de escritura (sobreescribe el archivo)a → modo append (añade información al final del archivo)

`as <nombre>` nos ayuda a darle una abreviatura o un nombre a los datos que acabamos de leer