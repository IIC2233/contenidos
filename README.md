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

| Semana | Fechas      | Contenido                    | Detalle       |
| ------ | ----------- | ---------------------------- | ------------- |
| 1      | 03/3 - 09/3 | Introducción                 |               |
| 2      | 10/3 - 16/3 | Entorno de trabajo           | Actividad 0   |
| 3      | 17/3 - 23/3 | Estructuras de datos         | Actividad 1   |
| 4      | 24/3 - 30/3 | OOP Avanzado                 | Actividad 2   |
| 5      | 31/3 - 06/4 | Excepciones                  | Actividad 3   |
| 6      | 07/4 - 13/4 | Iteradores                   | Actividad 4   |
| 7      | 14/4 - 20/4 | -                            | No hay clases |
| 8      | 21/4 - 27/4 | Funcional                    | Actividad 5   |
| 9      | 28/4 - 04/5 | -                            | Receso        |
| 10     | 05/5 - 11/5 | Interfaz Gráfica 1           | Experiencia 1 |
| 11     | 12/5 - 18/5 | Threading                    | Actividad 6   |
| 12     | 19/5 - 25/5 | Serialización y Networking 1 | Actividad 7   |
| 13     | 26/5 - 01/6 | Networking 2                 | Actividad 8   |
| 14     | 02/6 - 08/6 | Interfaces Gráficas 2        | Experiencia 2 |
| 15     | 09/6 - 15/6 | Tópicos Avanzados            | Experiencia 3 |
| 16     | 16/6 - 22/6 | Tópicos Avanzados 2          | Cátedra       |
