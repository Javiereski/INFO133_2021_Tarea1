import pymongo as pm
from datetime import datetime, date, time, timezone

client = pm.MongoClient()
db = client["fusa_prueba"]
archivos = db["archivos"]
tipo_fuente = db["tipo_fuente"]
usuarios = db["usuarios"]

test_archivo = { "ID": 1,
	    "fecha_grabacion": datetime.now(timezone.utc),
	    "ciudad": "Valdivia",
	    "duracion": 60,
	    "formato":"wav",
	    "latitud":  -39.8139,
	    "longitud": -73.2458,
	    "exterior": False,
	    "usuario": {"RUT": 19722223, "nombre": "Javier", "apellido": "Mansilla"},
	    "segmentos":[{"ID": 1,
	    			  "formato": "wav",
	    			  "duracion": 30,
	    			  "inicio": 0,
	    			  "fin": 30,
	    			  "etiquetas": [{"nombre_fuente": "parte_1", "descripcion": "lorem ipsum", "id_analizador": "humano"}]},

	    			 {"ID": 2,
	    			  "formato": "wav",
	    			  "duracion": 30,
	    			  "inicio": 31,
	    			  "fin": 60,
	    			  "etiquetas": [{"nombre_fuente": "parte_2", "descripcion": "lorem ipsum", "id_analizador": "maquina"}]}]
	    }

test_usuario = {"RUT": 19722223, "nombre": "Javier", "apellido": "Mansilla"}
test_tipo_fuente = {"tipo": 3, "archivos": [1,2]}

x = archivos.insert_one(test_archivo)
y = usuarios.insert_one(test_usuario)
z = tipo_fuente.insert_one(test_tipo_fuente)