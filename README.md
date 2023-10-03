# BBVA Data Challenge 2023

Se requiere desarrollar un modelo predictivo que nos ayude a identificar a los clientes que abandonarán el segmento objetivo del banco.

##### Description

**¡Bienvenido al BBVA Data Challenge 2023!**

En este año el reto es desarrollar una solución de Machine Learning e Inteligencia Artificial que ayude al banco a identificar a los clientes que abandonarán el segmento objetivo del banco.

Por diversas razones como inactividad, reducción de saldos activos o pasivos, cancelación de productos o mal comportamiento, dejan de estar en el segmento objetivo del banco. Existen 5 motivos a predecir, por lo tanto, el problema de este año es multiclase.

##### Evaluación

La métrica de la evaluación será el [F1-score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html). (Considerar **average = 'macro'** )

period,ID,target
period_9,832f7b32987238c1f64604201db5014e8fc16880b96190,0
period_9,eb7427a081043d3bbb48505d4c51c11b1eca2d9626d2c6,2
period_9,75eda24460b525d666f2757d28674d858f370a839e1cd8,1
etc.


## Dataset Description

Para desarrollar la solución tienen disponibles los siguientes archivos:

## Archivos

* **customers.csv** - Contiene datos sociodemográficos; también, de tenencia de productos y ofertas en el banco.
* **balances.csv** - Contiene los datos de los saldo de crédito del Reporte Crediticio Consolidado.
* **liabilities.csv** - Datos de los saldos de ahorro de los clientes.
* **movements.csv** - Posee los datos de las compras realizas con la tarjeta del banco en 4 rubros de comercios.
* **digital.csv** - Posee los datos de la navegación de los clientes en las plataformas digitales del banco.
* **universe_train.csv** - Listado de clientes con la etiqueta del motivo del abandono del segmento objetivo.
* **universe_test.csv** - Listado de clientes a quienes hay que predecir el motivo del abandono del segmento objetivo.
* **sample_submission.csv** - Ejemplo del archivo de envío.
* **Diccionario de datos.xlsx** - Diccionario de los datos.


## Formato de envío

Para cada envío, los archivos deben tener 3 columnas:

* period: periodo de extracción de los datos
* ID: llave
* target: motivo de fuga del cliente (0, 1, 2, 3, 4 ó 5)

El formato debe ser como el siguiente:


# Datos - Universo - Target

| Pregunta                                                                                                                                                                       | Respuesta                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. ¿Qué significa que un cliente abandone el segmento?                                                                                                                       | Significa que el cliente dejó de cumplir con las características solicitadas.                                                                                                                                                                                              |
| 2. ¿Es necesario normalizar los datos para el modelo?                                                                                                                         | Depende de tu metodología de desarrollo. Sin embargo, los datos ya se encuentran escalados.                                                                                                                                                                                 |
| 3. ¿El target es binario o multiclase?                                                                                                                                        | Es multiclase.                                                                                                                                                                                                                                                               |
| 4. ¿Se puede usar información adicional a la proporcionada?                                                                                                                  | La información proporcionada está anonimizada, lo que dificulta hacer un match con datos externos.                                                                                                                                                                         |
| 5. ¿Qué representan las clases?                                                                                                                                              | El valor 0 representa que no hubo abandono, los valores del 1 al 5 representan los motivos de abandono o attrition del cliente.                                                                                                                                              |
| 6. ¿Cómo se dividió la validación en Kaggle (público y privado)?                                                                                                          | La división no fue aleatoria, fue cronológica.                                                                                                                                                                                                                             |
| 7. ¿Disponemos de un modelo entidad-relación o un diccionario de datos?                                                                                                      | No hay un modelo entidad-relación, pero se compartirá un excel con un diccionario de datos en Kaggle.                                                                                                                                                                      |
| 8. Sobre el escalado de datos de 0 a 5, ¿podrían aclararlo?                                                                                                                  | Los datos han sido anonimizados por razones de seguridad. Uno de los pasos fue escalar los datos de 0 a 5. El 0 representa el valor mínimo y el 5 el valor máximo (tomado de un percentil).                                                                                |
| 9. ¿Qué significa cada periodo?                                                                                                                                              | Son meses distintos en los que se obtuvo el listado de clientes del segmento objetivo.                                                                                                                                                                                       |
| 10. ¿El procesamiento de normalización o estandarización se hizo antes o después de dividir en entrenamiento y prueba?                                                     | Todos los datos han sido transformados sin especificar el momento.                                                                                                                                                                                                           |
| 11. ¿Es necesario hacer un preprocesamiento de datos?                                                                                                                         | Queda a criterio del concursante, pero es recomendable para mejorar la calidad del modelo.                                                                                                                                                                                   |
| 12. ¿Se pueden añadir o modificar variables durante el modelado?                                                                                                             | Sí, se pueden construir o modificar variables con los datos brindados según lo considere pertinente.                                                                                                                                                                       |
| 13. ¿Cómo debe ser el formato del archivo de test que se envía?                                                                                                             | Kaggle proporciona un ejemplo de cómo debe enviarse la data. Es importante seguir ese formato para la correcta evaluación.                                                                                                                                                 |
| 14. ¿El campo ID es el identificador único del cliente en todas las tablas o varía por entidad?                                                                             | El campo ID es el identificador único del cliente y es consistente a través de todas las tablas. Use el campo ID para cruzar información entre las diferentes tablas.                                                                                                     |
| 15. ¿La variable attrition en la tabla universe corresponde a los motivos de fuga que ocurrieron en ese periodo (t-0) o hace referencia a un evento futuro (por ejemplo t+1)? | Los motivos de attrition hacen referencia a un tiempo futuro que corresponden a un tiempo t+n.                                                                                                                                                                               |
| 16. ¿Podrían explicar la relación y diferencia entre las variables Period y Month?                                                                                          | Period es el mes del listado de clientes del segmento objetivo y Month indica los meses previos de datos para ese conjunto. Si Period hace referencia a diciembre 2022, se comparten los datos de "balances" desde enero 2022 (Month = 1) hasta diciembre 2022 (Month = 12). |
| 17. ¿Cada cliente está representado por un ID único, o puede que haya algún cliente que haya sido evaluado en periodos distintos y tenga más de un ID?                    | Cada cliente en cada periodo tiene un diferente ID, por lo que no se puede hacer seguimiento de un cliente específico, cada ID es único en la base de datos.                                                                                                               |
| 18. ¿Por qué la base "digital" no cuenta con period?                                                                                                                         | Los IDs son únicos en toda la base, por lo tanto, no es necesario tener el campo period para usar la base digital.                                                                                                                                                          |

### Install a VirtualEnv

**Terminal PowerShell/WSL:**

- If first time:
  - on **Linux** > `pip3 install virtualenv`
  - on **Windows** > `pip install virtualenv`
- Make `VirtualEnv`:
  - on **Linux/Mac** > `python3 -m virtualenv env`
  - on **Windows** > `python -m virtualenv env`
- Activate `.env` Virtual Environment
  - on **Linux/Mac** > `source env/bin/activate`
  - on **Windows** > `./env/Scripts/activate`
- Install libraries from **requirements.txt** >
  - on **Linux/Mac** >`pip3 install -r ./requirements.txt`
  - on **Windows** > `pip install -r ./requirements.txt`

### Install Kaggle

https://github.com/Kaggle/kaggle-api/blob/main/README.md
