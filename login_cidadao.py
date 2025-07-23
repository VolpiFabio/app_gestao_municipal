import streamlit as st
import requests
from auth_supabase import sign_in

# --- DEFINIÇÕES DE FUNÇÕES PRIMEIRO (BOA PRÁTICA) ---

@st.cache_data(ttl=3600)
def carregar_municipios():
    """Busca a lista de municípios da API."""
    try:
        url = "https://brasilapi.com.br/api/ibge/municipios/v1/SP"
        response = requests.get(url )
        response.raise_for_status()
        return [municipio['nome'] for municipio in response.json()]
    except Exception as e:
        st.error(f"Erro ao carregar municípios: {e}")
        return []

# --- FUNÇÃO PRINCIPAL QUE DESENHA A PÁGINA ---

def show():
    """Mostra a página de login completa."""
    st.set_page_config(layout="centered")
    
    # 1. DESENHA O TÍTULO PRIMEIRO
    st.markdown("""
    <div style='text-align:center; line-height:1.2;'>
        <h1 style='margin-bottom:0; font-size:2.5em;'>
            <span style='color:red;'>C</span>idadão 
            <span style='color:gray;'>D</span>igital
        </h1>
        <p style='margin-top:0; font-size:1.3em;'>Sistema de Gestão Municipal Integrado</p>
    </div>
    """, unsafe_allow_html=True)

    # Adiciona um espaço para respirar
    st.write("") 
    
    _col1, col2, _col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            email = st.text_input("E-mail", placeholder="seu@email.com") 
            password = st.text_input("Senha", type="password", placeholder="••••••••")
            submit = st.form_submit_button("Entrar", use_container_width=True)
            
            if submit:
                # --- INÍCIO DA DEPURAÇÃO ---
                # st.info("Botão 'Entrar' pressionado. Chamando a função sign_in...")
                # --- FIM DA DEPURAÇÃO ---
                sign_in(email, password)
        
        if st.button("Não tem uma conta? Cadastre-se", use_container_width=True, type="secondary"):
            st.session_state['page'] = 'signup'
            st.rerun()