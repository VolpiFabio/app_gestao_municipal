# signup.py
import streamlit as st
from auth_supabase import sign_up

def show():
    st.set_page_config(layout="centered")
    st.markdown("<h1 style='text-align: center;'>Crie sua Conta</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("signup_form"):
            email = st.text_input("E-mail")
            password = st.text_input("Senha", type="password")
            submit_button = st.form_submit_button("Cadastrar")

            if submit_button:
                if not email or not password:
                    st.error("Por favor, preencha todos os campos.")
                else:
                    # Chama a função de cadastro do Supabase
                    sign_up(email, password)
        
        # Botão para voltar para a tela de login
        if st.button("Já tem uma conta? Faça o login"):
            st.session_state['page'] = 'login' # Usaremos isso para navegar
            st.rerun()
