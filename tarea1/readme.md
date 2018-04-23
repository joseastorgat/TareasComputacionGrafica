### Archivos y Clases

Se cuenta con dos archivos, litoral.py y main.py

- litoral.py :  Contiene la clase que modela el perfil del litoral a estudiar
- main.py :  Contiene diversos estudios realizados usando la clase Litoral

### Métodos:


- litoral.py
	
	- Litoral: 
		- Constructor
			- set_geografia
		
		- cb:
			-cb_general
			-cb_atmosfera

		- geografia_to_nan
	
		- start
			- faux

		- plot
		- plot_log_scale
		- show_map
		- estadisticas

	- rho1: 
	- rho2: 

	- hora_string: Convierte una hora de float a una string HH:MM
	- get_omega_optimo: Retorna el parametro omega optimo del metodo de sobrerelajación sucesiva.


- main.py

	- test_horas
	- test_omegas
	- test_omegas2
	- main: Programa para que algun usuario pueda modelar litoral.


### USO:

	#Se debe crear el objeto clase Literal con parámetros h, escala, RRR (geografia)
	#al crear el objeto se crea la geografia
	
	lit=Litoral(h,escala,RRR)

	#Se deben dar las condiciones inicial
	#con la hora(float) que se desee modelar

	lit.cb(hora)

	#A continuación se debe iniciar las iteraciones
	#Los siguientes parametros:
	# max_iteraciones: numero máximo de iteraciones a realizar 
	# func: función que recibe(x,y) distancia desde un punto a al centro de la planta petrolera
	# e0: Error a considerar para convergencia
	# omega: Parametro omega de sobrerelajación sucesiva 

	lit.start(max_iteraciones, func, e0, omega )


	#Adicionalmente si se quiere obtener el omega optimo para usarlo:
	omega_optimo = get_omega_optimo(lit._w, lit._h)

	#A continuación con plot y plot_log_scale puede observar el mapa de temperaturas, y con estadisticas se entrega el min, max y valor promedio de temperatura