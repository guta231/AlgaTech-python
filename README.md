# Código Python para Monitoramento e Feedback de Temperatura e Luminosidade

## Contexto do Projeto
Este projeto foi desenvolvido como parte do **Global Solution (GS)**, uma iniciativa acadêmica semestral do curso de Engenharia de Software da FIAP. O objetivo é utilizar tecnologias inovadoras para resolver desafios reais de forma sustentável e eficiente.

O sistema proposto utiliza a Internet das Coisas (IoT) para monitorar o cultivo de **microalgas**, que têm um enorme potencial como fonte de energia renovável. O cultivo eficiente das microalgas depende de condições ambientais ideais, como temperatura e luminosidade. Este projeto automatiza o monitoramento dessas condições, otimizando o processo de cultivo e potencializando o aproveitamento energético das microalgas.

## Descrição
Este código utiliza o protocolo MQTT para monitorar os dados de **temperatura** e **luminosidade** em tempo real. Ele verifica se os dados estão dentro dos limites ideais e armazena as informações em um arquivo CSV. Feedbacks automáticos são gerados para orientar ajustes no ambiente, garantindo o crescimento ideal das microalgas.

## Requisitos
- **Python 3.x**
- **Biblioteca paho-mqtt**: Para instalação, use o comando:
  ```bash
  pip install paho-mqtt
  
## Relatório com Principais Insights Gerados

###Insights Obtidos:

1. **Monitoramento Automático**:
   - Dados de temperatura e luminosidade são monitorados continuamente por sensores e enviados via MQTT.
   - O sistema gera feedbacks em tempo real para ajustes ambientais.

2. **Limites Ideais para o Cultivo**:
   - **Temperatura**: 20-28 °C.
   - **Luminosidade**: 500-2000 lux.

3. **Armazenamento e Análise de Dados**:
   - Os dados coletados são armazenados em um arquivo CSV (`dados_historicos.csv`) com timestamps.
   - Esses dados podem ser analisados para identificar padrões e realizar ajustes de longo prazo.

4. **Eficiência Operacional**:
   - A otimização do cultivo pode aumentar significativamente a produtividade de microalgas para diversos fins.

### Benefícios do Sistema:
- Automação do monitoramento das condições ambientais.
- Redução de custos operacionais no cultivo de microalgas.
- Criação de uma base de dados histórica para análises avançadas.

## Como Usar

### Configuração MQTT:
- Atualize o endereço do **broker** MQTT, a **porta** e os **tópicos** no código, se necessário.

## Execução do Código

1. **Execute o script Python**:
   ```bash
   python index.py

### Integrantes:

| Nome                | RM      |
|---------------------|---------|
| Gustavo Henrique    | 556712  |
| Milena Garcia       | 555111  |
| Enzo Dias           | 558225  |


