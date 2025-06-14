# Exemplo Super Simples - Agente de Atendimento
# Execute com: streamlit run agente-simples.py

import streamlit as st
import os

st.title("🤖 Assistente Virtual - Seguros")

# Base de conhecimento simples (sem banco de dados)
conhecimento = {
    "seguro auto": """
    **Coberturas disponíveis:**
    - Colisão e Incêndio
    - Roubo e Furto
    - Danos a terceiros
    - Assistência 24h
    
    **Franquia:** A partir de R$ 1.500
    **Vigência:** 12 meses
    """,
    
    "seguro vida": """
    **Coberturas disponíveis:**
    - Morte natural ou acidental
    - Invalidez permanente
    - Despesas médicas
    - Auxílio funeral
    
    **Carência:** 2 anos para suicídio
    **Idade:** 18 a 65 anos
    """,
    
    "sinistro": """
    **Como acionar:**
    1. Ligue 0800 123 4567
    2. Tenha em mãos a apólice
    3. Descreva o ocorrido
    4. Aguarde o perito
    
    **Documentos necessários:**
    - Boletim de Ocorrência
    - CNH e documento do veículo
    - Fotos do local
    """,
    
    "cotação": """
    **Para fazer uma cotação, preciso saber:**
    - Tipo de seguro desejado
    - Seus dados pessoais
    - Informações do bem (se aplicável)
    
    Entre em contato:
    - WhatsApp: (11) 98765-4321
    - Email: cotacao@seguradora.com
    """
}

# Histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Mensagem inicial
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Olá! Sou o assistente virtual da seguradora. Como posso ajudar? Posso falar sobre seguro auto, seguro vida, sinistros ou cotações."
    })

# Exibir mensagens
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
if prompt := st.chat_input("Digite sua pergunta..."):
    # Adicionar pergunta do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Processar resposta (lógica simples)
    resposta = "Desculpe, não entendi sua pergunta. Posso ajudar com informações sobre:\n- Seguro Auto\n- Seguro Vida\n- Sinistros\n- Cotações"
    
    # Buscar na base de conhecimento
    prompt_lower = prompt.lower()
    for chave, info in conhecimento.items():
        if chave in prompt_lower:
            resposta = info
            break
    
    # Se mencionar preço ou valor
    if any(palavra in prompt_lower for palavra in ["preço", "valor", "quanto custa", "custo"]):
        resposta = """**Valores de Seguro:**
        
        Os valores variam conforme:
        - Perfil do segurado
        - Tipo de cobertura
        - Valor do bem
        
        Para uma cotação personalizada, clique no botão abaixo!"""
    
    # Adicionar resposta
    st.session_state.messages.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.markdown(resposta)

# Barra lateral com ações rápidas
with st.sidebar:
    st.header("Ações Rápidas")
    
    if st.button("📞 Falar com Atendente"):
        st.info("Conectando... Um atendente entrará em contato em breve.")
    
    if st.button("💰 Fazer Cotação"):
        st.info("Você será redirecionado para o formulário de cotação.")
    
    if st.button("📋 Ver Minha Apólice"):
        st.info("Faça login para acessar suas apólices.")
    
    if st.button("🚨 Reportar Sinistro"):
        st.error("Linha direta sinistros: 0800 123 4567")
    
    st.divider()
    
    st.caption("💡 Dica: Pergunte sobre tipos de seguro, coberturas ou processo de sinistro!")

# Rodapé
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("⏰ Atendimento 24/7")
with col2:
    st.caption("🔒 Dados protegidos")
with col3:
    st.caption("✅ Regulado pela SUSEP")
