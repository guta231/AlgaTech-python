# Código Python para Monitoramento e Feedback de Temperatura e Luminosidade

## Descrição
Este código utiliza o protocolo MQTT para monitorar os dados de temperatura e luminosidade de um sistema de microalgas, fornecendo feedback sobre o estado dessas condições ambientais. O sistema verifica se as condições de temperatura e luminosidade estão dentro dos limites ideais e envia um feedback, informando se ajustes são necessários.

## Requisitos
- **Python 3.x**
- **Biblioteca paho-mqtt**: Para instalação, use o seguinte comando:
  ```bash
  pip install paho-mqtt
