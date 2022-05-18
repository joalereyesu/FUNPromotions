# FUNPromotions
El objetivo de este proyecto es crear una pagina en donde los usuarios podrán comprar boletos para la diferente variedad de eventos que ofrece la promotora FUN. 

## Primera entrega
Los objetivos de la primera entrega se concentraran en los que he visto en la clase de estructuras de datos.

**Arreglos unidimensionales:** Estructuras de arreglos unidimensionales que contenga:
- Conciertos del año
- Las fechas y horas de cada concierto
- Lugares en donde se llevara a cabo cada uno

**Arreglos multidimensionales:** Estructura de arreglos multidimensionales que contenga:
- Los artistas que participaran en el concierto (lineup)
- Las áreas disponibles en cada concierto con su respectivo precio

**Structs:** Estructuras que contenga la información del usuario a la hora de ingresar a la pagina (nombre, apellido, correo, usuario, contraseña.)

**Funcionalidades:**
El usuario tendrá las siguientes funcionalidades para la primera entrega:
- Crear una cuenta en la pagina principal (Sign Up)
- Ver los conciertos disponibles y su respectiva información 
- Ver las áreas disponibles con su respectivo precio
- Agregar un nuevo concierto

**Rutas funcionales disponibles:**
- Sign up
- Homepage
- Todos los eventos disponibles en el año
- Informacion de cada evento

**Diseño:**
Para el diseño de la pagina se utilizo HTML y CSS. 

**Testeo:**
- Unit tests para comprobar el funcionamiento de las funciones que acompaña la clase de usuario
- Postman para comprobar los request methods del API

## Segunda entrega
Los objetivos de la segunda entrega se concentraran en los que se ha visto en el segundo modulo de la clase de estructuras de datos.

**Mejoras de primera entrega:** En la primera entrega los arreglos con la data de los conciertos se encontraba en la parte del front end. En esta entrega se creo un archivo json en donde se encuentra la informacion de los conciertos para asi manipularla en el back end. 

**Queue:** Estructura que sera implementada para la waitlist de usuarios que se encontraran comprando tickets de los festivales
- El Queue contendra un tuple con el nombre de usuario y el codigo del festival
- Para motivos de visualizacion y funcionamiento, se eliminara un elemento de el queue cada 5 segundos. 
- Se tendra un Queue con ejemplos predeterminados por propositos de funcionalidad y visualizacion

**Stack:** Estructura que se implementara en el almacenamiento de tickets vendidos
- Cuando un usuario realice una compra de un ticket, se guardara en el stack un tuple con el usuario y el codigo del festival
- El usuario podra cancelar antes de aceptar, si cancela el tuple almacenado sera eliminado del stack y no se guardara la compra
- Se tendra un Stack con ejemplos predeterminados por propositos de funcionalidad

**Funcionalidades:**
- Opcion de comprar entrada para cualquiera de los festivales disponibles
- Waiting list mientras otros usuarios compran entradas
- Introducir informacion de compra 

## Entrega Final
Los objetivos de esta entrega final se concentra en los ultimos temas vistos en el curso de Estructuras de Datos en una pagina web de una promotora de festivales y eventos. 

**Funcionalidades de la aplicacion**
En esta entrega no se implemento nada visual, unicamente se agregaron estructuras para seguir construyendo una aplicacion eficiente. La promotora ahora podra contar con el almacenamiento de los usuarios que ya han comprado tickets de conciertos y son vinculados con la localidad disponible en cada festival y concierto. 

**Binary Search Tree:** Se implemento esta estructura para almacenar los conciertos y para que puedan ser encontrados de una manera mas sencilla y rapida. El arbol se ordena de acuerdo al __date stamp__ del evento y son almancenados en el arbol. Se implementa una insercion y busqueda logaritmica para asi eficientar el manejo de los eventos seleccionados y formar una plataforma mas rapida. 

**Graphs:** Esta estructura se implemento para almacenar los usuarios que han comprado entradas a eventos y vincularlos a la localidad adquirida. De esta manera los administradores de la pagina tienen un control de la venta de entradas y la actividad de sus usuarios. 

**Firebase Authentication:** Se implento firbase authentication para la creacion de nuevas cuentas y el inicio de sesion en la plataforma y para mantener un control de los usuarios almacenados y activos. 

**Unit Tests:** Cada estructura implementada y utilizada tiene su respectivo unit test, para asi comprobar que las mismas funcionen de manera adecuada y si existe algun problema sea atendido inmediatamente. 

**GitHub Actions:** Se implemento Continuous Integration en GitHub para asi automatizar los cambios que se hanj llevado a cabo en el codigo y tambien para automatizar los respectivos tests implementados. 

**JMeter:** Se utilizo JMeter para realizar pruebas de load testing para ver como se comporta la plataforma al momento de que varios usuarios estan accediendo las rutas disponibles por la pagina. De esta manera podemos ver si existe algun problema al momento de tratar con multiples usuarios y que tan bien funciona la aplicacion bajo estas circunstancias. 

**Diseño:** El diseño consiste en proveer al usuario con una plataforma amigable e interactiva. Se utilizo unicamente lenguaje CSS para crear el diseño. Se utilizo una paleta de colores que fuera agradable para el usuario con multiples animaciones para una experiencia unica y placentera. 

**Funcionalidades de todo el programa:** 
- Crear una cuenta en la plataforma utilizando autentificacion de firebase
- Iniciar sesion de usuarias ya existentes con firebase. 
- Pagina de inicio en donde se muestra la navegacion que ofrece el programa.
- Ver los conciertos disponibles ofrecidos por la promotora. 
- Seleccionar el evento deciado en donde se pueden ver la viariedad de precios en las diferentes localidades del evento. 
- Seleccionar la localidad deceada y comprar la entrada. 
- Se provee una lista de espera si se encuentran otros usuarios comprando entrada. 
- Al momento que sea el turno de comprar del usuario, se redirecciona a la pagina de compra en donde se presenta el ticket con la informacion del evento. En esta pestaña se puede ingresar los datos de la tarjea para realizar la compra. 
- Luego se ofrece la posibilidad al usuario de cancelar su ticket antes de proseguir. Si cancela el usuario no es almacenado y se redirecciona a la pagina de inicio. 

**Resumen de estructuras:**
1. Struct: Se implemento como una clase en pytho para almancenar la informacion del usuario como un objeto. 
2. Arreglos: Los conciertos provienen de un archivo json, estos son cargados al backend en arreglos y son recorridos y manipulados. 
3. Tree: Se almacena los conciertos en esta estructura para asi realizar inserciones y busquedas de manera mas eficiente al momento de utilizar informacion de los conciertos disponibles
4. Queue: Estructura que se utiliza para la funcionalidad de lista de espera en la compra de entradas. 
5. Stack: En esta estructura se almacenan los usuarios que ya han realizado la compra. 
6. Graph: Se almacenan los usuarios que han comprado entradas y se vinculan con la respectiva localidad y festival, para asi mantener un control de los usuarios. 

