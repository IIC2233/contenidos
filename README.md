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

| Semana | Fechas        | Contenido                    | Detalle       |
| ------ | ------------- | ---------------------------- | ------------- |
| 1      | 04/8 - 10/8   | Introducción                 |               |
| 2      | 11/8 - 17/8   | Entorno de trabajo           | Actividad 1   |
| 3      | 18/8 - 24/8   | Estructuras de datos         | Actividad 2   |
| 4      | 25/8 - 31/8   | OOP Avanzado                 | Experiencia 1 |
| 5      | 01/9 - 07/9   | Iteradores                   | Actividad 3   |
| 6      | 08/9 - 14/9   | Excepciones                  | Experiencia 2 |
| 7      | 15/9 - 21/9   | -                            | Receso        |
| 8      | 22/9 - 28/9   | Funcional                    | Actividad 4   |
| 9      | 29/9 - 05/10  | -                            | Midterm       |
| 10     | 06/10 - 12/10 | Interfaz Gráfica 1           | Experiencia 3 |
| 11     | 13/10 - 19/10 | Threading                    | Actividad 5   |
| 12     | 20/10 - 26/10 | Serialización y Networking 1 | Experiencia 4 |
| 13     | 27/10 - 02/11 | Serialización y Networking 2 | Actividad 6   |
| 14     | 03/11 - 09/11 | Interfaces Gráficas 2        | Experiencia 5 |
| 15     | 10/11 - 16/11 | Tópicos Avanzados 1          | Actividad 7   |
| 16     | 17/11 - 23/11 | Tópicos Avanzados 2          | Cátedra       |
