#  Prueba Técnica Omni.pro - Python Developer
## Andrés Fernando Aranguren Silva
- --
## 5. Construir un microservicio de Clientes en Django.

### Descripción del Problema:

- Debe tener CRUD (Create, Read, Update, Delete) por cada una de las entidades de la base de datos.

### Solución: 
Las operaciones CRUD en django constan de dos partes los endpoints que son los urls y las vistas las cuales sirven para realizar las operaciones con la base de datos usando el ORM de Django por defect. Estos componentes pueden ser encontrados en los siguientes enlaces:
<h3>Endpoints</h3>

- <a href="https://github.com/afarangurens/OmniProMicroservicio/blob/main/API/urls.py#:~:text=)%2C-,%23%20Operaciones%20CRUD%20de%20la%20tabla%20Clientes,)%2C,-%23%20Operaciones%20CRUD%20de">Endpoints Clientes</a></h5>

- <a href="https://github.com/afarangurens/OmniProMicroservicio/blob/main/API/urls.py#:~:text=)%2C-,%23%20Operaciones%20CRUD%20de%20la%20tabla%20Pa%C3%ADses,)%2C,-%23%20Operaciones%20CRUD%20de">Endpoints Paises</a></h5>

- <a href="https://github.com/afarangurens/OmniProMicroservicio/blob/main/API/urls.py#:~:text=)%2C-,%23%20Operaciones%20CRUD%20de%20la%20tabla%20Estados,)%2C,-%23%20Operaciones%20CRUD%20de">Endpoints Estados</a></h5>

- <a href="https://github.com/afarangurens/OmniProMicroservicio/blob/main/API/urls.py#:~:text=)%2C-,%23%20Operaciones%20CRUD%20de%20la%20tabla%20Ciudades,)%2C,-%23%20Operaciones%20CRUD%20de">Endpoints Ciudades</a></h5>

- <a href="https://github.com/afarangurens/OmniProMicroservicio/blob/main/API/urls.py#:~:text=)%2C-,%23%20Operaciones%20CRUD%20de%20la%20tabla%20Tiendas,)%2C,-%23">Endpoints Tiendas</a></h5>

<h3>Operaciones CRUD</h3>

- <a href="https://github.com/afarangurens/OmniProMicroservicio/blob/main/API/views.py">CRUD</a></h5>

- --
- Debe tener documentación del api basado en ReDoc o Swagger UI

- Debe tener los siguientes endpoints específicos:
1. <a href="https://github.com/afarangurens/OmniProMicroservicio/blob/main/API/urls.py#:~:text=)%2C-,%23%20Operaciones%20CRUD%20de%20la%20tabla%20Ciudades,)%2C,-%23%20Operaciones%20CRUD%20de">Consulta de todas las ciudades de un estado.</a></h5>

2. <a href="https://github.com/afarangurens/OmniProMicroservicio/blob/main/API/urls.py#:~:text=)%2C-,%23%20Operaciones%20CRUD%20de%20la%20tabla%20Ciudades,)%2C,-%23%20Operaciones%20CRUD%20de">Consulta de todos los clientes de una tienda.</a></h5>

3. <a href="https://github.com/afarangurens/OmniProMicroservicio/blob/main/API/urls.py#:~:text=)%2C-,%23%20Operaciones%20CRUD%20de%20la%20tabla%20Ciudades,)%2C,-%23%20Operaciones%20CRUD%20de">Consulta los clientes por estado.</a></h5>


- Debe cumplir con el siguiente diagrama entidad relación:
<p align="center">
	<img src="https://github.com/afarangurens/OmniProMicroservicio/blob/main/Prueba%20OMNI.jpg">>
</p>

<a href="https://github.com/afarangurens/OmniProMicroservicio/blob/main/API/models.py">Modelos en ORM de Django.</a></h5>
- Debe usar PostgreSQL como motor de base de datos.

- Debe hacer un Script de prueba, el cual debe:
1. Crear 10 clientes.
2. Crear 10 países.
3. Crear 5 estados por país.
4. Crear 2 ciudades por estado.
5. Crear 8 tiendas.

El script que genera las pruebas antes mencionadas se encuentra en:
<a href="https://github.com/afarangurens/OmniProMicroservicio/blob/main/API/management/commands/insertdata.py"> Script Insertar Datos</a>
Y se corre en la consola de la siguiente manera:

        python manage.py insertdata

6. Los clientes que tengan id 5, 8 y 9 deben cambiar su nombre por Julian.
7. Los clientes que tengan id 1, 7 y 6 deben tener la tienda con el id 5 como tienda favorita.

El script que genera las pruebas antes mencionadas se encuentra en:
<a href="https://github.com/afarangurens/OmniProMicroservicio/blob/main/API/management/commands/insertdata.py"> Script Actualizar Datos</a>
Y se corre en la consola de la siguiente manera:

        python manage.py updatedata


- Debe entregar una url de repo publico en alguna de las siguientes herramientas github o bitbucket

- Debe tener las instrucciones de despliegue y debe correr el servicio.

- Puntos adicionales si se entrega el deploy en una nuble publica en capa gratuita como AWS, GCP, AZURE, entre otras.

La aplicación se encuentra alojada en el siguiente enlace: https://omnipro-microservice.herokuapp.com/

- Código en inglés con comentarios en español.
- --

# Instrucciones de despliegue.

1. Primero se debe clonar el repositorio utuilizando el comando:

        git clone https://github.com/afarangurens/OmniProMicroservicio.git
        cd OmniproMicroservicio

2. Debido a que Django varía en sus versiones tanto de Python como de Framework lo más recomendable en la práctica es realizar un entorno de ecosistema para poder instalar los requerimientos necesarios y que no comprometan las variables de entorno del sistema operativo, para esto se crea un entorno utilizando:

        python -m venv .venv
    Y se activa con el comando:
         
        .venv\Scripts\Activate
    
3. Se deben instalar los requerimientos del archivo requirements.txt para poder correr el programa utilizando el comando:

        pip install requirements.txt

4. Acceder a la carpeta que contenga el archivo 'manage.py' el cual es el archivo utilizado para correr todas las funcionalidades.

5. Se debe crear una base de datos en PostgreSQL que se llame 'omniprodb', con un usuario admin llamado 'postgres' con contraseña '1234', para poder hacer las respectivas migraciones.

6. Se debe correr el siguiente código para crear todas las tablas de la base de datos.

        python manage.py migrate

7. Para correr los Scripts de creación de datos y de actualización de datos es necesario utilizar los comandos:

        python manage.py insertdata
        python manage.py updatedata

8. Por último para correr la aplicación se debe utilizar el comando:

        python manage.py runserver