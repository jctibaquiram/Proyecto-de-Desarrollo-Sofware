
El proyecto consistió en la practica de ingeniería de software para el desarrollo de una aplicación web. Las tareas llevadas a cabo se relacionan con la creación y gestión de entornos virtuales de python y el desarrollo del la aplicación web.
A continuación se enumenran los pasos que se siguieron para el desarrollo del poryecto:
1. Se creó una cuenta en Github para posteriormente generar un repositorio git en donde se cargarán los avances de VS Code.
2. se clonó el repositorio en VS code para trabajar en el repositorio del proyecto en VS code.
3. Se  instalaron bibliotecas y extensiones como pandas, streamlit, plotly-express y matplotlib.
4. Se generó un nuevo entorno virtual en VS code y se llamó vehicles_env en relación con el conjunto de datos que estamos usandousamos.
5. Descargamos el conjunto de los datos proporcionado en la plataforma, dicho conjunto correspondía con datos de vihiculos, entre los datos se incluye el precio, fabricante, odometro, año etc.
6. Para ampliar el conocimiento practico en VS Code, generamos un directorio llamado notebooks a partir de la terminal, aunque también VS code permite la creación directa en su interfaz.
7 Dentro del directorio notebooks creamos un jupyter notebook, no sin antes instalar la extensión de jupyter notebook en VS Code.
8. Abrimos el Jupyter notebooks y experimentamos con los ejemplos proporcionados para la creación de graficas que luego usariamos en el desarrollo de la aplicación virtual.
9. para el desarrollo de la aplicación virtual generamps un archivo de ython en la raiz del directorio del poryecto (app.py). en el archivo creado se importaron las librearias y extensiones previamente instaladas y se tomaron los datos de vihiculos previamente descargados para poder generar graficas.
10. Generamos el contenido de la aplicación web basada en Streamlit usando herramientas cómo st.header() para el encabezado, tambien St.write(para escribir cuando se ejecute if) , adicionalemnte incluimos st.plotly_chart() para generar graficos interactivos. Especificamente la aplicación web nos mostrara un enabezado asociado a el tipo de los datos de las visualizaciones "Venta de Vehiculos" para luego mostrarnos un histograma de la cantidad de vehiculos por odometro al presionar el boton que nos lo indica y luego tendremos una casilla de verificación, la cual al ser activada generara un grafico de disperión asociado a la relación entre preció y odometro.
11.Se modificó el archivo README que se incluye en el repositorio para contar con toda la información del desarrollo del proyecto.
12. Al finalizar la creación de la aplicación web y los diferentes archivos vamos al apartado de sorce control en VS code y empujamos los cambios al repositorio para contar con todos los archivos solicitados.

Conclusión:El desarrollo de este proyecto representó una experiencia práctica integral que me permitió aplicar conocimientos clave en herramientas de desarrollo de software, análisis de datos (en menor medida) y creación de aplicaciones web. En el proyecto, se fortalecieron competencias en el uso de la terminal, manejo de entornos virtuales, uso de comandos, control de versiones con Git y GitHub, y desarrollo interactivo en VS Code.

La implementación de la aplicación con Streamlit demostró la capacidad de transformar análisis de datos en productos digitales funcionales y accesibles. Además, se logró integrar visualizaciones dinámicas con una interfaz simple e intuitiva, cumpliendo con los requisitos técnicos establecidos.
