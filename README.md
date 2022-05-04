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