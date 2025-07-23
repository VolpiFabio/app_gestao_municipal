# main.py
import streamlit as st
import login_cidadao as login_cidadao
import home  # Sua página home
import signup

# Inicializar session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'page' not in st.session_state:
    st.session_state.page = 'login'

def main():
    # Se o usuário estiver logado, mostra a home
    if st.session_state.get('logged_in', False):
        home.show()
    # Se não estiver logado, verifica qual página mostrar
    else:
        if st.session_state.page == 'login':
            login_cidadao.show()
        elif st.session_state.page == 'signup':
            signup.show()

if __name__ == "__main__":
    main()