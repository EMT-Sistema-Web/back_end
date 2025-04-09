import paho.mqtt.client as mqtt
from django.http import HttpResponse


MQTT_BROKER = "test.mosquitto.org"  
MQTT_PORT = 1883
MQTT_TOPIC = "meu/topico/mqtt"

def publicar_mensagem(request):
    
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    
    message = "Olá, este é um teste de mensagem MQTT com Django!"
    client.publish(MQTT_TOPIC, message, qos=1)

    client.disconnect()

    return HttpResponse("Mensagem publicada com sucesso!")