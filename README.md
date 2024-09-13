# Contenidos

### Preguntas frecuentes
1. Abro los _notebooks_, hago cambios para ver cómo funcionan, y a la semana siguiente al hacer `git pull` me sale un error que dice:
   > `Your local changes to the following files would be overwritten by merge`
   
   ¿Qué puedo hacer? 🤔
   
   Siempre puedes clonar el repositorio otra vez, pero no es la idea. Lo más correcto es: guardar los cambios en alguna otra parte, hacer `pull`, y luego volver a aplicar tus cambios. Para eso, utiliza los siguientes comandos:
   ```bash
   git stash     # Guarda los cambios hechos en otra parte. Desaparecen del working directory.
   git pull      # El pull que queríamos hacer en un principio.
   git stash pop # Regresa los cambios hechos por ti al working directory.
   ```


### Desglose contenidos

| Semana | Fechas      | Contenido                    | Detalle                 |
| ------ | ----------- | ---------------------------- | ----------------------- |
| 1      | 05/8 - 11/8 | Introducción                 |                         |
| 2      | 12/8 - 18/8 | Entorno de trabajo           |Actividad 0, jueves feriado|
| 3      | 19/8 - 25/8 | Estructuras de datos         | Actividad 1             |
| 4      | 26/8 - 01/9 | OOP Avanzado                 | Actividad 2             |
| 5      | 02/9 - 08/9 | Modelación OOP e iterables   | Experiencia 1           |
| 6      | 09/9 - 15/9 | Excepciones                  | Experiencia 2           |
| 7      | 16/9 - 22/9 | -                            | Receso                  |
| 8      | 23/9 - 29/9 | Programación Funcional       | Actividad 3             |
| 9      | 30/9 - 06/10 | Theading                    | Actividad 4, midterm    |
| 10     | 07/10 - 13/10 | Serialización y Networking  | Actividad 5             |
| 11     | 14/10 - 20/10 | Networking 2                | Experiencia 3           |
| 12     | 21/10 - 27/10 | Interfaz Gráfica 1          | Experiencia 4           |
| 13     | 28/10 - 03/11 | -                           | Jueves y viernes feriado |
| 14     | 04/11 - 10/11 | Interfaz Gráfica 2          | Experiencia 5           |
| 15     | 11/11 - 17/11 | Tópicos Avanzados           |                         |
