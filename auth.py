# auth.py
import streamlit as st

def login(username):
    """Função para registrar o estado de login na sessão."""
    st.session_state['logged_in'] = True
    st.session_state['username'] = username
    # Você pode adicionar mais dados do usuário aqui se precisar
    # st.rerun()

def logout():
    """Função para limpar a sessão e forçar o redirecionamento para o login."""
    # Itera sobre uma lista de chaves para limpar a sessão
    for key in ['logged_in', 'username', 'user_id']:
        if key in st.session_state:
            del st.session_state[key]
    # st.rerun()

