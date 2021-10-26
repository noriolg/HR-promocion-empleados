# HR-promocion-empleados

El departamento de recursos humanos de una empresa multinacional ha almacenado los datos de las promociones internas del último año. Con estos datos la empresa quiere conocer si existen patrones determinados a la hora de promocionar a un empleado o no. Además esta empresa quiere saber si puede tomar alguna medida en el futuro para orientar la mejora de las carreras profesionales de sus empleados.

Para ello la empresa os pide:

* Realizar un análisis exploratorio de los datos detallando aquellos aspectos más relevantes que hayáis encontrado.
* Construir un modelo de clasificación que prediga la probabilidad de que un empleado sea promocionado o no basandonos en el histórico que tenemos.
* Desarrollar un cuadro de mando con Dash que resuma los aspectos más relevantes que hayáis extraido en el análisis exploratorio y pueda aconsejar a un empleado en las acciones que puede tomar para incrementar su probabilidad de ascenso.

¿Qué recomendaciones le daríais al departamento de recursos humanos basándoos en los datos?

## Información de los datos:
Las variables que tenemos en los datos son las siguientes:

* employee_id: Identificador del empleado
* department: Departamento del empleado
* region: Región del empleado
* educacion: Nivel de estudios
* gender: Género del empleado
* recruitment_channel: Manera en la que el empleado ha sido contratado
* no_of_trainings: Número de formaciones que ha realizado el empleado en el último año
* age: Edad del empleado
* previous_year_rating: Puntuación obtenida en la evaluación durante los años anteriores
* length_of_service: Años de servicio
* awards_won: Si ha ganado algún premio durante el último año
* avg_training_score: Puntuación media de las formaciones realizadas
* is_promoted: 1 si ha sido ascendido y 0 en caso contrario.