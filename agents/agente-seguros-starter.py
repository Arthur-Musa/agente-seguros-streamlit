import streamlit as st
from langchain_anthropic import ChatAnthropic
from langchain.memory import ConversationBufferMemory
import os

# Configuração da página
st.set_page_config(page_title="Central de Agentes - Seguradora", layout="wide")

# Título e seleção de agente
st.title("🏢 Central de Agentes Autônomos")
col1, col2 = st.columns([1, 3])

with col1:
    agente_selecionado = st.selectbox(
        "Escolha o Agente:",
        ["Analista de Risco", "Atendimento ao Cliente", "Processador de Sinistros", 
         "Consultor de Produtos", "Compliance"]
    )

# Configurar personalidade baseada no agente
personalidades = {
    "Analista de Risco": """Você é um analista de risco especializado em seguros.
    Suas habilidades incluem: análise de dados, scoring de risco, detecção de padrões.
    Responda de forma técnica mas clara.""",
    
    "Atendimento ao Cliente": """Você é um assistente de atendimento especializado em seguros.
    Suas habilidades incluem: explicar coberturas, tirar dúvidas sobre apólices, auxiliar em cotações.
    Use linguagem simples e acessível.""",
    
    "Processador de Sinistros": """Você é um especialista em processamento de sinistros.
    Suas habilidades incluem: análise de documentos, estimativa de danos, detecção de fraudes.
    Seja objetivo e procedimental.""",
    
    "Consultor de Produtos": """Você é um consultor especializado em produtos de seguro.
    Suas habilidades incluem: recomendar produtos, personalizar coberturas, identificar oportunidades.
    Seja consultivo e focado nas necessidades do cliente.""",
    
    "Compliance": """Você é um analista de compliance para seguradoras.
    Suas habilidades incluem: verificar conformidade, monitorar regulações, gerar relatórios.
    Seja preciso e cite regulamentações quando relevante."""
}

# Inicializar memória e chat
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()
    st.session_state.messages = []

# Área principal de chat
with col2:
    st.subheader(f"💬 Conversando com: {agente_selecionado}")
    
    # Container para mensagens
    chat_container = st.container()
    
    # Exibir histórico
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
    
    # Input do usuário
    if prompt := st.chat_input("Digite sua mensagem..."):
        # Adicionar mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Configurar LLM com personalidade
        llm = ChatAnthropic(
            model="claude-3-sonnet-20240229",
            temperature=0.3,
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        
        # Criar prompt com contexto
        system_prompt = personalidades[agente_selecionado]
        full_prompt = f"{system_prompt}\n\nUsuário: {prompt}\nAssistente:"
        
        # Gerar resposta
        with st.spinner("Processando..."):
            response = llm.invoke(full_prompt)
            response_text = response.content
            
            # Adicionar resposta ao histórico
            st.session_state.messages.append({"role": "assistant", "content": response_text})
            
            # Rerun para atualizar o chat
            st.rerun()

# Barra lateral com informações
with st.sidebar:
    st.header("📊 Painel de Controle")
    st.metric("Conversas Hoje", "147")
    st.metric("Tempo Médio Resposta", "2.3s")
    st.metric("Satisfação", "94%")
    
    st.divider()
    
    st.header("🔧 Configurações")
    if st.button("Limpar Conversa"):
        st.session_state.messages = []
        st.session_state.memory = ConversationBufferMemory()
        st.rerun()
    
    st.divider()
    
    st.info("""
    **Capacidades do Agente:**
    - Processamento em tempo real
    - Integração com bases de dados
    - Análise de documentos
    - Geração de relatórios
    """)
