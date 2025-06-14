# Agente de Seguros

Este repositório contém diferentes versões de agentes de seguros desenvolvidos com Streamlit para auxiliar usuários em processos de cotação e atendimento.

## Estrutura do Projeto

```
agente-seguros/
├── agents/                   # Diferentes versões dos agentes
│   ├── agente-simples.py     # Versão mais simples do agente
│   └── agente-seguros-starter.py  # Versão mais completa com múltiplos agentes
├── data/                     # Dados e configurações
├── utils/                    # Utilitários e funções auxiliares
├── config/                   # Arquivos de configuração
├── requirements.txt          # Dependências do projeto
└── README.md                 # Este arquivo
```

## Como executar localmente

1. Clone o repositório
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Execute o aplicativo desejado:
   ```
   # Versão simples
   streamlit run agents/agente-simples.py
   
   # Versão completa
   streamlit run agents/agente-seguros-starter.py
   ```
4. Acesse `http://localhost:8501` no seu navegador

## Como fazer deploy no Streamlit Cloud

1. Acesse [Streamlit Cloud](https://share.streamlit.io/)
2. Clique em "New app"
3. Conecte sua conta do GitHub
4. Selecione o repositório `agente-seguros`
5. Escolha o branch principal (main)
6. No campo "Main file path", selecione o arquivo do agente desejado:
   - `agents/agente-simples.py`
   - `agents/agente-seguros-starter.py`
7. Clique em "Deploy!"

## Agentes Disponíveis

1. **Agente Simples** (`agente-simples.py`)
   - Versão básica para demonstração
   - Funcionalidades essenciais de atendimento

2. **Agente Completo** (`agente-seguros-starter.py`)
   - Versão mais avançada
   - Múltiplos agentes especializados
   - Interface mais rica e completa
