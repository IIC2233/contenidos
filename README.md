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

| Semana | Fechas        | Contenido                           | Detalle               |
| ------ | --------------| ----------------------------------- | --------------------- |
| 1      | 03/08 - 09/08 | Introducción                        | Cátedra: Bienvenida   |
| 2      | 10/08 - 16/08 | Entorno de trabajo                  | Actividad 1           |
| 3      | 17/08 - 23/08 | Estructuras de datos (EDD)          | Actividad Diagnóstico |
| 4      | 24/08 - 30/08 | OOP Avanzado                        | Actividad 2           |
| 5      | 31/08 - 06/09 | Excepciones, Iterables e Iteradores | Actividad 3           |
| 6      | 07/09 - 13/09 | -                                   | Interrogación 1       |
| 7      | 14/09 - 20/09 | -                                   | Receso                |
| 8      | 21/09 - 27/09 | Programación funcional              | Actividad 4           |
| 9      | 28/09 - 04/10 | Threading                           | Actividad 5           |
| 10     | 05/10 - 11/10 | Serialización y Networking 1        | Actividad 6           |
| 11     | 12/10 - 18/10 | Serialización y Networking 2        | Actividad 7           |
| 12     | 19/10 - 25/10 | -                                   | Interrogación 2       |
| 13     | 26/10 - 01/11 | Interfaces Gráficas 1               | Actividad 8           |
| 14     | 02/11 - 08/11 | Interfaces Gráficas 2               | Actividad 9           |
| 15     | 09/11 - 15/11 | Tópicos Avanzados                   | Actividad 10          |
| 16     | 16/11 - 22/11 | Cierre                              | Cátedra: Cierre       |
| 17     | 23/11 - 29/11 | -                                   | Examen                |

## Licencia

Este repositorio contiene material del curso **Programación Avanzada** del **Departamento de Ciencia de la Computación** de la **Pontificia Universidad Católica de Chile**.

El contenido se encuentra bajo la licencia **Creative Commons Atribución–NoComercial–SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0)**.

Estos materiales se publican con fines exclusivamente educativos y como referencia para estudiantes. No está permitido utilizarlos con fines comerciales ni incorporarlos, total o parcialmente, en otros cursos, capacitaciones o materiales docentes sin la autorización expresa del autor.

Para más información, consulte el archivo `LICENSE.md` o visite: https://creativecommons.org/licenses/by-nc-nd/4.0/deed.es
