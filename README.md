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

| Semana | Fechas      | Contenido                    | Detalle |
| ------ | ----------- | ---------------------------- | ------- |
| 1      | 03/3 - 09/3 | Introducción                 |         |
| 2      | 10/3 - 16/3 | Entorno de trabajo           |         |
| 3      | 17/3 - 23/3 | _Built in_                   |         |
| 4      | 24/3 - 30/3 | OOP Avanzado                 |         |
| 5      | 31/3 - 06/4 | Excepciones                  |         |
| 6      | 07/4 - 13/4 | Iteradores                   |         |
| 7      | 14/4 - 20/4 | -                            |         |
| 8      | 21/4 - 27/4 | Funcional                    |         |
| 9      | 28/4 - 04/5 | -                            |         |
| 10     | 05/5 - 11/5 | Interfaz Gráfica 1           |         |
| 11     | 12/5 - 18/5 | Threading                    |         |
| 12     | 19/5 - 25/5 | Serialización y Networking 1 |         |
| 13     | 26/5 - 01/6 | Networking 2                 |         |
| 14     | 02/6 - 08/6 | Interfaces Gráficas 2        |         |
| 15     | 09/6 - 15/6 | Tópicos Avanzados            |         |
| 16     | 16/6 - 22/6 | Tópicos Avanzados 2          |         |
