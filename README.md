# Monitoramento de Servidor, Rede e Internet com IoT

Este projeto é uma aplicação de monitoramento em tempo real de servidor, rede e velocidade da internet, construída com **Python** e **Dash**. Ele coleta informações sobre o uso de CPU, memória e realiza testes de velocidade da internet, exibindo esses dados através de gráficos interativos.

## Índice
- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Como Executar](#como-executar)
- [Monitoramento na Nuvem](#monitoramento-na-nuvem)
- [Licença](#licença)

## Sobre o Projeto

Este projeto foi desenvolvido para ajudar uma pequena empresa, a Detec, a monitorar o desempenho dos servidores, conexões de internet em tempo real de seus clientes. Utilizamos **IoT** para coletar dados de CPU e memória, além de testar a velocidade da internet. A aplicação é visualizada por meio de gráficos dinâmicos criados com **Dash**, sem necessidade de customização com HTML ou CSS.

## Funcionalidades

- **Monitoramento de CPU**: Acompanha o uso da CPU em tempo real.
- **Monitoramento de Memória**: Exibe o uso de memória do sistema.
- **Teste de Velocidade da Internet**: Mede as velocidades de download e upload.
- **Atualizações em Tempo Real**: Os gráficos são atualizados a cada 5 segundos.

## Tecnologias Utilizadas

As principais tecnologias utilizadas neste projeto são:

- **Python**: Linguagem de programação principal.
- **Dash**: Framework para criação de dashboards interativos.
- **Plotly**: Biblioteca de gráficos interativos.
- **psutil**: Biblioteca para monitoramento de recursos do sistema (CPU, memória).
- **speedtest-cli**: Biblioteca para testar a velocidade da internet.
- **AWS (Amazon Web Services)**: Para hospedagem e monitoramento na nuvem (opcional).

## Instalação

### Pré-requisitos

- **Python 3.6+**: Certifique-se de ter o Python instalado em seu sistema.
- **Pip**: Gerenciador de pacotes Python.

### Passos para Instalação

1. Clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/ciane-pereira/Monitoramento-projeto.git
   cd monitoramento-projeto
