# Introducción
las 3 V del Big Data
- la cantidad de datos (volumen)
- su complejidad (variedad)
- la velocidad a la que se recopilan y procesan (velocidad)

**Descubrimiento de Conocimiento en Bases de Datos /Knowledge Discovery in Databases (KDD)**

### Resumen general

La minería de datos es el proceso automático de descubrir información útil y patrones novedosos en grandes repositorios de datos. Surge de la confluencia de disciplinas como la estadística, la inteligencia artificial y el aprendizaje automático para enfrentar los desafíos de la era del "Big Data". El proceso no es directo; requiere una preparación exhaustiva de los datos (preprocesamiento) y una interpretación final de los resultados (posprocesamiento) para que la información sea realmente accionable en la toma de decisiones.

### 1.1 Que es data Mining?
- **Definición:** Es el descubrimiento automático de información útil en grandes conjuntos de datos para hallar patrones que de otro modo serían desconocidos.
    
- **Capacidad predictiva:** Permite predecir resultados futuros, como el gasto estimado de un cliente.
    
- **Diferenciación:** No se considera minería de datos a las búsquedas simples en bases de datos (como buscar una palabra clave), ya que estas usan técnicas tradicionales de computación.

### 1.2 Desafíos Motivadores

El desarrollo de la minería de datos fue impulsado por limitaciones de los métodos estadísticos tradicionales ante datos modernos:

- **Escalabilidad:** Los algoritmos deben manejar terabytes o petabytes de datos eficientemente.
    
- **Alta Dimensionalidad:** Ahora es común trabajar con miles de atributos (como en bioinformática), lo que genera la "maldición de la dimensionalidad".

- **Datos Heterogéneos:** Capacidad para mezclar texto, imágenes, audio y video en un mismo análisis.
    
- **Propiedad y Distribución:** Los datos no siempre están en un solo lugar; se requieren técnicas de minería distribuida que cuiden la privacidad.

### 1.3 Los Orígenes y la Ciencia de Datos

- **Confluencia de disciplinas:** Se nutre de la estadística (muestreo, hipótesis) y la IA/Aprendizaje Automático (algoritmos de búsqueda, modelos).
    
- **KDD:** La minería es una parte integral del proceso de convertir datos crudos en información útil.
    
- **Data Science:** Se describe como un campo interdisciplinario más amplio que utiliza la minería de datos junto con otras herramientas para obtener conocimientos.

### 1.4 Tareas de la Minería de Datos

Se dividen en dos categorías principales:

1. **Tareas Predictivas:** Su objetivo es predecir el valor de un atributo (variable dependiente) basado en otros (variables independientes).
    
    - _Clasificación:_ Para variables discretas (ej. predecir si un cliente comprará o no).
        
    - _Regresión:_ Para variables continuas (ej. predecir el precio de una acción).
        
2. **Tareas Descriptivas:** Buscan patrones que resuman relaciones subyacentes en los datos.
    
    - **Análisis de Asociación:** Descubrir características que aparecen juntas (ej. "quien compra pañales también compra leche").
        
    - **Análisis de Clúster (Agrupamiento):** Agrupar observaciones similares entre sí (ej. segmentación de clientes o tipos de noticias).
        
    - **Detección de Anomalías:** Identificar observaciones significativamente diferentes al resto (ej. detección de fraude en tarjetas de crédito).