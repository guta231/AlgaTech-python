import paho.mqtt.client as mqtt
import pandas as pd
import time


BROKER = "20.206.203.145"
PORT = 1883
TOPIC_TEMPERATURA = "/TEF/device001/attrs/temperatura"
TOPIC_LUMINOSIDADE = "/TEF/device001/attrs/luminosidade"
TOPIC_FEEDBACK = "/TEF/device001/feedback"


TEMPERATURA_IDEAL = (20, 28) 
LUMINOSIDADE_IDEAL = (500, 2000)  


temperatura_atual = None
luminosidade_atual = None


ARQUIVO_CSV = 'dados_historicos.csv'


def converter_para_lux(valor_analogico):
    return (valor_analogico / 1023.0) * 2000  


def analisar_dados(temperatura, luminosidade):
    feedback = []
    if temperatura is not None and not (TEMPERATURA_IDEAL[0] <= temperatura <= TEMPERATURA_IDEAL[1]):
        feedback.append("Ajustar temperatura!")
    if luminosidade is not None and not (LUMINOSIDADE_IDEAL[0] <= luminosidade <= LUMINOSIDADE_IDEAL[1]):
        feedback.append("Ajustar luminosidade!")
    if not feedback:
        feedback.append("Condições ideais!")
    return " | ".join(feedback)


def salvar_dados_csv(temperatura, luminosidade, feedback):

    try:
        dados = pd.read_csv(ARQUIVO_CSV)
    except FileNotFoundError:
        dados = pd.DataFrame(columns=["Data", "Temperatura (°C)", "Luminosidade (lux)", "Feedback"])


    nova_linha = pd.DataFrame({
        "Data": [time.strftime('%Y-%m-%d %H:%M:%S')],
        "Temperatura (°C)": [temperatura],
        "Luminosidade (lux)": [luminosidade],
        "Feedback": [feedback]
    })

    
    dados = pd.concat([dados, nova_linha], ignore_index=True)

 
    dados.to_csv(ARQUIVO_CSV, index=False)

   
    print("Dados salvos no arquivo CSV:")
    print(dados.tail())


def on_message(client, userdata, msg):
    global temperatura_atual, luminosidade_atual
    if msg.topic == TOPIC_TEMPERATURA:
        temperatura_atual = float(msg.payload.decode())  
    elif msg.topic == TOPIC_LUMINOSIDADE:
        valor_analogico = int(msg.payload.decode())
        luminosidade_atual = converter_para_lux(valor_analogico)  

    if temperatura_atual is not None and luminosidade_atual is not None:
        feedback = analisar_dados(temperatura_atual, luminosidade_atual)
        salvar_dados_csv(temperatura_atual, luminosidade_atual, feedback)
        client.publish(TOPIC_FEEDBACK, feedback)

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.subscribe([(TOPIC_TEMPERATURA, 0), (TOPIC_LUMINOSIDADE, 0)])
client.loop_forever()
