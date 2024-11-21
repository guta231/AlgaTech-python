import paho.mqtt.client as mqtt

# Configurações MQTT
BROKER = "20.206.203.145"
PORT = 1883
TOPIC_TEMPERATURA = "/TEF/device001/attrs/temperatura"
TOPIC_LUMINOSIDADE = "/TEF/device001/attrs/luminosidade"
TOPIC_FEEDBACK = "/TEF/device001/feedback"

# Limites ideais
TEMPERATURA_IDEAL = (20, 28)  # Temperatura em °C
LUMINOSIDADE_IDEAL = (500, 2000)  # Luminosidade em lux

# Variáveis globais para armazenar os dados
temperatura_atual = None
luminosidade_atual = None

# Função para converter leitura analógica (0-1023) em lux (ajuste conforme o sensor)
def converter_para_lux(valor_analogico):
    return (valor_analogico / 1023.0) * 2000  # Exemplo: 0-1023 mapeado para 0-2000 lux

# Função de análise
def analisar_dados(temperatura, luminosidade):
    feedback = []
    if temperatura is not None and not (TEMPERATURA_IDEAL[0] <= temperatura <= TEMPERATURA_IDEAL[1]):
        feedback.append("Ajustar temperatura!")
    if luminosidade is not None and not (LUMINOSIDADE_IDEAL[0] <= luminosidade <= LUMINOSIDADE_IDEAL[1]):
        feedback.append("Ajustar luminosidade!")
    if not feedback:
        feedback.append("Condições ideais!")
    return " | ".join(feedback)

# Callback para lidar com mensagens recebidas
def on_message(client, userdata, msg):
    global temperatura_atual, luminosidade_atual
    if msg.topic == TOPIC_TEMPERATURA:
        temperatura_atual = float(msg.payload.decode())  # Convertendo para float
    elif msg.topic == TOPIC_LUMINOSIDADE:
        valor_analogico = int(msg.payload.decode())
        luminosidade_atual = converter_para_lux(valor_analogico)  # Convertendo para lux
    
    # Se ambos os dados estiverem disponíveis, analisar e enviar feedback
    if temperatura_atual is not None and luminosidade_atual is not None:
        feedback = analisar_dados(temperatura_atual, luminosidade_atual)
        client.publish(TOPIC_FEEDBACK, feedback)

# Configuração MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.subscribe([(TOPIC_TEMPERATURA, 0), (TOPIC_LUMINOSIDADE, 0)])
client.loop_forever()
