# auth_supabase.py (MODO DE DEPURAÇÃO MÁXIMA)
import streamlit as st
from supabase import create_client, Client

# A inicialização não muda.
@st.cache_resource
def init_connection() -> Client:
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        return create_client(url, key)
    except Exception as e:
        st.error(f"Erro fatal ao conectar com o Supabase: {e}")
        return None

supabase_client = init_connection()

# --- Funções de Autenticação ---

def sign_up(email, password):
    # Esta função já está funcionando, não precisa de debug.
    try:
        res = supabase_client.auth.sign_up({"email": email, "password": password})
        st.success("Cadastro realizado com sucesso! Por favor, faça o login.")
        st.balloons()
    except Exception as e:
        st.error(f"Erro no cadastro: {getattr(e, 'message', e)}")

def sign_in(email, password):
    """Realiza o login do usuário com depuração máxima."""
    if supabase_client is None:
        st.error("Conexão com o Supabase não estabelecida.")
        return

    # # --- INÍCIO DA DEPURAÇÃO ---
    # st.info("1. Função sign_in foi chamada.")
    # st.json({
    #     "Email recebido": email,
    #     "Senha recebida": "Sim" if password else "Não" # Não mostre a senha real
    # })
    # # --- FIM DA DEPURAÇÃO ---

    try:
        res = supabase_client.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        
        # --- INÍCIO DA DEPURAÇÃO ---
        st.success("2. Supabase respondeu SEM ERRO. Autenticação OK.")
        st.json({
            "ID do Usuário": res.user.id,
            "E-mail do Usuário": res.user.email,
            "Token de Acesso Existe": "Sim" if res.session.access_token else "Não"
        })
        # --- FIM DA DEPURAÇÃO ---
        
        st.session_state['logged_in'] = True
        st.session_state['username'] = res.user.email
        st.session_state['user_id'] = res.user.id
        
        st.info("3. Estado da sessão do Streamlit foi atualizado. Redirecionando...")
        st.rerun()

    except Exception as e:
        # --- INÍCIO DA DEPURAÇÃO ---
        st.error("2. Supabase respondeu COM ERRO.")
        st.json({
            "Tipo do Erro": type(e).__name__,
            "Mensagem do Erro": f"{e}"
        })
        # --- FIM DA DEPURAÇÃO ---
        st.session_state['logged_in'] = False

def sign_out():
    for key in ['logged_in', 'username', 'user_id']:
        if key in st.session_state:
            del st.session_state[key]
    if supabase_client:
        supabase_client.auth.sign_out()
    
