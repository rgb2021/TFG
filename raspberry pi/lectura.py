import serial
import json
import pymongo
from datetime import datetime
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import ssl
import json

ser = serial.Serial('/dev/ttyACM0', 9600) # Configurar el puerto serie USB

# Configura la conexión con la base de datos en Atlas
cliente = pymongo.MongoClient("mongodb+srv://XXXXXXXXXXXXXXXXXXXXXXXXXX")
db = cliente["TFG"]
coleccion = db["lecturas_sensores"]

# funcion para la conexion a AWS iot
def on_connect(client, userdata, flags, rc):
	if rc==0:
		print("connected OK Returned code=",rc)
	else:
		print("Bad connection Returned code=",rc)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))


def on_log(client, userdata, level, buf):
	print("log: ",buf)
    
def on_disconnect(client, userdata, rc):
	print("Disconnected: " + mqtt.error_string(rc))

if __name__ == '__main__':
	client = mqtt.Client(client_id="RaspiTFG")
	client.on_connect = on_connect
	client.on_message = on_message
	client.on_disconnect = on_disconnect
	client.on_log=on_log
	client.tls_set(ca_certs='../certs/root-CA.crt', certfile='../certs/RaspiTFG.cert.pem', keyfile='../certs/RaspiTFG.private.key', tls_version=ssl.PROTOCOL_SSLv23)
	client.tls_insecure_set(True)
	client.connect("a19936h45xlf8j-ats.iot.eu-central-1.amazonaws.com", 8883, 60) #Taken from REST API endpoint - Use your own. 

	client.loop_start()

	while True:
		if ser.in_waiting > 0:
			data = ser.readline().decode('utf-8').rstrip() # Leer los datos entrantes
			dt_string = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")
			try:
				json_data = json.loads(data) # Decodificar los datos JSON
				json_data["fecha"] = dt_string
				print("dato recibido" , json_data , sep="->")
				coleccion.insert_one(json_data)
				json_string = json.dumps(json_data,default=str)
				client.publish("mediciones/sensores", payload=json_string, qos=0, retain=False)
			except Exception as err:
				print(f"Unexpected {err=}, {type(err)=}")
