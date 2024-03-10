
# 📺 ETL com Python - Caso Netflix 

Neste projeto parte do Bootcamp squad.io, foram realizados processos de ETL (Extract, Transform, Load) com base em tabelas de registro da Netflix. 

### 🛠️ Ferramentas utilizadas
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## 1.1. Os dados, o problema e os objetivo
Todos os dias vários arquivos .xlsx chegam vindos do Brasil, Itália e França despadronizados mas para criar dashboards e fazer outras análises é necessários unificar estes arquivo em somente um único arquivo .csv e aplicar padrões de rastreabilidade e confiabilidade. Portando o objetivo é criar uma solução para resolver este problema. 

## 1.2. Importação das bibliotecas e carregamento dos dados
A bibliotecas utilizadas foram o pandas, os, glob.

# ⛏️ 2. Processo de ETL 
Aqui foi criado um processo para que os dados da extensão .xlsx ao chegarem na pasta de destino, sejam unificados em um arquivo único do tipo .csv que contém colunas para identificar: país de origem, promoção no momento da compra, e arquivo de origem. 
