# Projeto: ETL de Temperaturas no Rio de Janeiro

## 🌡️ Visão Geral

Este projeto implementa um pipeline completo de Engenharia de Dados para analisar a temperatura média no estado do Rio de Janeiro em 2023.

O objetivo é demonstrar, de forma estruturada e automatizada, como a temperatura tem variado ao longo do tempo, utilizando dados reais, técnicas de ETL e visualização de insights.

---

## 🎯 Objetivos

* Extrair dados de temperatura de fontes públicas confiáveis
* Realizar tratamento, limpeza e agregações relevantes
* Armazenar os dados processados em banco relacional (SQLite)
* Visualizar insights por meio de gráficos e análises
* Automatizar o processo com logging e notificações por e-mail

---

## 🛠️ Tecnologias Utilizadas

* Python 3.x
* Bibliotecas: `pandas`, `matplotlib`, `seaborn`, `sqlite3`, `smtplib`, `email`, `logging`, `python-dotenv`
* Banco de dados: SQLite
* Agendamento: Task Scheduler (Windows)([GitHub][1])

---

## 🔄 Pipeline ETL

1. **Extração**: Coleta de dados de temperatura de fontes públicas.
2. **Transformação**: Limpeza e agregação dos dados para análise.
3. **Carga**: Armazenamento dos dados transformados em um banco SQLite.
4. **Visualização**: Geração de gráficos para identificar tendências e padrões.
5. **Automação**: Implementação de logging e envio de notificações por e-mail após a execução do pipeline.

---

## 📧 Notificações por E-mail

O pipeline envia notificações automáticas por e-mail após cada execução, indicando sucesso ou falha.

### 🔐 Configuração de Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

env:
EMAIL_USER=seu_email@gmail.com
EMAIL_RECEIVER=destinatario_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_app


**Importante**: Adicione o arquivo `.env` ao `.gitignore` para evitar o versionamento de informações sensíveis.

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:

   git clone https://github.com/Zao01/Temperatura-rj-etl.git
   cd Temperatura-rj-etl

2. Instale as dependências:

  .pip install -r requirements.txt
   
3. Configure as variáveis de ambiente conforme instruções acima.

4. Execute o pipeline:

  . python main.py

---

## 📝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 📬 Contato

Para dúvidas ou sugestões, entre em contato: [adm.marcosfonseca@gmail.com](mailto:adm.marcosfonseca@gmail.com)

---

