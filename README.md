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

| Semana | Fechas        | Contenido                           | Detalle             |
| ------ | --------------| ----------------------------------- | ------------------- |
| 1      | 02/03 - 08/03 | Inrtoducción                        | Cátedra: Bienvenida |
| 2      | 09/03 - 15/03 | Entorno de trabajo                  | Actividad 1         |
| 3      | 16/03 - 22/03 | Estructuras de datos (EDD)          | Actividad 2         |
| 4      | 23/03 - 29/03 | OOP Avanzado                        | Actividad 3         |
| 5      | 30/03 - 05/04 | -                                   |                     |
| 6      | 06/04 - 12/04 | Excepciones, Iterables e Iteradores | Actividad 4         |
| 7      | 13/04 - 19/04 | Programación funcional              | Experiencia 1       |
| 8      | 20/04 - 26/04 | Threading                           | Actividad 5         |
| 9      | 27/04 - 03/05 | Interfaz Gráfica 1                  | Experiencia 2       |
| 10     | 04/05 - 10/05 | Serialización y Networking 1        | Actividad 6         |
| 11     | 11/05 - 17/05 | Serialización y Networking 2        | Experiencia 3       |
| 12     | 18/05 - 24/05 | -                                   | Receso              |
| 13     | 25/05 - 31/05 | -                                   |                     |
| 14     | 01/06 - 07/06 | Interfaces Gráficas 2               | Experiencia 4       |
| 15     | 08/06 - 14/06 | Tópicos Avanzados 1                 | Actividad 7         |
| 16     | 15/06 - 21/06 | -                                   |                     |
| 17     | 22/06 - 28/06 | -                                   | Cátedra: Cierre     |
