# Projeto: ETL de Temperaturas no Rio de Janeiro

## 🔍 Visão Geral

Este projeto demonstra a criação de um pipeline completo de Engenharia de Dados para análise da temperatura média no estado do Rio de Janeiro em 2023.

O objetivo é mostrar, de forma estruturada e automatizada, como a temperatura tem variado com o tempo, utilizando dados reais, técnicas de ETL e visualização de insights.

---

## 🎯 Objetivos

- Extrair dados de temperatura de fontes públicas confiáveis
- Realizar tratamento, limpeza e agregações relevantes
- Armazenar os dados processados em banco relacional (SQLite)
- Visualizar insights de forma clara e compreensível
---

## 🛠️ Tecnologias Utilizadas

| Etapa        | Ferramentas/Ferramentas                          |
|--------------|--------------------------------------------------|
| Extração     | Python (`requests`, `pandas`)                    |
| Transformação| Python (`pandas` para limpeza e agregações)      |
| Carga        | SQLite                                            |
| Visualização | Power BI (ou alternativa com gráfico em notebook)|

---

## 🧱 Estrutura do Pipeline

1. **Extração**  
   - Coleta automática dos dados via API ou CSV
   - Armazenamento temporário em DataFrame

2. **Transformação**  
   - Conversão de tipos, padronização de colunas
   - Criação de colunas derivadas (ex: médias por mês, por bairro)
   - Tratamento de valores ausentes e dados inválidos

3. **Carga**  
   - Inserção dos dados limpos no banco SQLite
   - Estruturação em tabelas normalizadas

4. **Visualização**  
   - Gráficos de tendência por ano
   - Médias por estação/bairro/período

---

## 🗂️ Organização dos Arquivos

```

temperatura-rj-etl/
│
├── data/                 # Dados brutos e tratados
├── notebooks/            # Exploração inicial (se houver)
├── src/                  # Scripts de ETL
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── outputs/              # Arquivos gerados
├── README.md
└── requirements.txt

````

---

## 📊 Visualização

Gráfico da temperatura média mensal no RJ em 2023:

![Gráfico](notebooks/grafico_temperatura.png)


> *"A temperatura média no RJ aumentou 1.3ºC na última década, com maior concentração de picos entre novembro e março."*
---

## 📅 Status do Projeto

* [x] Escolha do dataset
* [x] Extração completa
* [x] Transformação estruturada
* [x] Carga e banco prontos
* [x] Visualização entregue
* [x] Documentação 100%

---

## 🤝 Contribuições

Este projeto é parte do meu portfólio como futuro Engenheiro de Dados. Feedbacks técnicos são bem-vindos!

---

## 📩 Contato

* LinkedIn: [Marcos Fonseca](https://www.linkedin.com/in/marcos-fonseca-63354a187)
* Email: [adm.marcosfonseca@gmail.com](mailto:adm.marcosfonseca@gmail.com)





