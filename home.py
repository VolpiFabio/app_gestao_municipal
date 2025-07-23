import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta
from auth_supabase import sign_out


def show():
    st.markdown(
        """
        <style>
            .stAppDeployButton {display:none;}
        </style>
        """,
        unsafe_allow_html=True
    )


    # Inicializar a página selecionada se não existir
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = "Home"  # página padrão

    # configuração da aba web e sidebar
    st.set_page_config(
        page_title="Cidadão Digital",
        page_icon="🏢",
        layout="wide",
        initial_sidebar_state="expanded"  # Sidebar sempre aberta
    )

    # sidebar e menu
    with st.sidebar:
        st.markdown(
            """
            <div style='text-align:center;'>
                <h1 style='margin-bottom:0;'>Menu</h1>
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown("---")

        
        st.markdown("### 🧭 Navegação")

        menu_items = [
            ("🏠", "Home", "Home"),
            ("⚙️", "Configurações", "Configurações"),
            ("🪪", "Cidadão", "Cidadão"),
            ("🧷", "Clipping", "Clipping"),
            ("👤", "Cadastro de Usuario", "Cadastro de Usuario"),
            ("📊", "Relatórios", "Relatórios"),
            ("🔉", "Campanha", "Campanha"),
            ("📞", "Contato", "Contato"),
            ("🎂", "Eventos", "Eventos"),
            ("🏠", "Imóveis", "Imóveis"),
            ("🗺️", "Geo", "Geo"),
            ("🧑‍🧒‍🧒", "Iniciativa", "iniciativa" )
        ]

        for icon, label, key in menu_items:
            # Verificar se é a página atual para destacar
            if st.session_state.selected_page == key:
                # Botão ativo (destacado)
                st.markdown(f"""
                <div style="
                    background-color: #e1f5fe;
                    border-left: 4px solid #1976d2;
                    padding: 8px 12px;
                    margin: 4px 0;
                    border-radius: 4px;
                    color: #1976d2;
                    font-weight: bold;
                ">
                    {icon} {label}
                </div>
                """, unsafe_allow_html=True)
            else:
                # Botão normal (clicável)
                if st.button(f"{icon} {label}", key=f"btn_{key}", use_container_width=True):
                    st.session_state.selected_page = key
                    st.rerun()
        
        st.markdown("---")
        
        # Seção de informações do usuário e logout
        st.markdown("### 👤 Usuário")
        
        # Mostrar informações do usuário (se disponível)
        if 'username' in st.session_state:
            st.markdown(f"**Logado como:** {st.session_state.username}")
        else:
            st.markdown("**Logado como:** Administrador")
        
        # Botão de logout estilizado
        st.markdown("""
        <style>
        .logout-button {
            background-color: #ff4b4b !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.5rem 1rem !important;
            font-weight: bold !important;
            width: 100% !important;
            margin-top: 10px !important;
        }
        .logout-button:hover {
            background-color: #ff6b6b !important;
            color: white !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.button(
            "🚪 Sair", 
            on_click=sign_out,
            key="logout_btn", 
            use_container_width=True, 
            help="Sair do sistema"
        )
            
        
        # Adicionar espaço no final
        st.markdown("<br>", unsafe_allow_html=True)
        
        
    # Conteúdo principal baseado na seleção do menu
    page_key = st.session_state.selected_page

    if st.session_state.selected_page == "Home":
        # CSS customizado para a página inicial
        st.markdown("""
        <style>
        .main-title {
            text-align: center;
            color: #1976d2;
            font-size: 3.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .subtitle {
            text-align: center;
            color: #666;
            font-size: 1.5rem;
            margin-bottom: 3rem;
        }
        .logo-container {
            display: flex;
            justify-content: center;
            margin: 2rem 0;
        }
        .welcome-card {
            background: linear-gradient(red, #E0BBB6, red);
            padding: 2rem;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin: 2rem 0;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }
        .feature-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
            text-align: center;
            margin: 1rem 0;
            border-left: 4px solid #1976d2;
        }
        </style>
        """, unsafe_allow_html=True)
        
    # Logo e título principal
        st.markdown("""
        <div class="logo-container">
            <div style="font-size: 8rem; color: #1976d2;">🏢</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='text-align:center; line-height:1.2;'>
            <h1 style='margin-bottom:0; font-size:2.5em;'>
                <span style='color:red;'>C</span>idadão 
                <span style='color:gray;'>D</span>igital
            </h1>
            <p style='margin-top:0; font-size:1.3em;'>Sistema de Gestão Municipal Integrado</p>
        </div>
        """, unsafe_allow_html=True)



        
        # Card de boas-vindas
        st.markdown("""
        <div class="welcome-card">
            <h2>🎉 Bem-vindo ao Sistema Cidadão Digital!</h2>
            <p style="font-size: 1.2rem; margin-top: 1rem;">
                Plataforma completa para gestão de serviços municipais e atendimento ao cidadão.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Seção de funcionalidades principais
        st.markdown("## 🚀 Principais Funcionalidades")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="feature-card">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🪪</div>
                <h3>Gestão de Cidadãos</h3>
                <p>Cadastro e gerenciamento completo de informações dos cidadãos</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="feature-card">
                <div style="font-size: 3rem; margin-bottom: 1rem;">📊</div>
                <h3>Relatórios</h3>
                <p>Análises detalhadas e relatórios gerenciais em tempo real</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="feature-card">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🏠</div>
                <h3>Gestão de Imóveis</h3>
                <p>Controle completo do cadastro imobiliário municipal</p>
            </div>
            """, unsafe_allow_html=True)
            
        with col4:
            st.markdown("""
            <div class="feature-card">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🗺️</div>
                <h3>Geo</h3>
                <p>Mapeamento Municipal</p>
            </div>
            """, unsafe_allow_html=True)
            
        # Seção de acesso rápido
        st.markdown("## ⚡ Acesso Rápido")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("🪪 Novo Cidadão", use_container_width=True):
                st.session_state.selected_page = "Cidadão"
                st.rerun()
        
        with col2:
            if st.button("📊 Ver Relatórios", use_container_width=True):
                st.session_state.selected_page = "Relatórios"
                st.rerun()
        
        with col3:
            if st.button("🏠 Cadastrar Imóvel", use_container_width=True):
                st.session_state.selected_page = "Imóveis"
                st.rerun()
        
        with col4:
            if st.button("⚙️ Configurações", use_container_width=True):
                st.session_state.selected_page = "Configurações"
                st.rerun()
        
    if st.session_state.selected_page == "Configurações":
        st.markdown("Configurações internas > **Configurações de notificações**")
        st.markdown("""
            <h6 style="background-color: #0000FF;
            padding: 10px; 
            border-radius: 5px; 
            display: inline-block; 
            color: white;
            margin: 0;">
                Configurações de notificações
            </h6>
            """, unsafe_allow_html=True)
        
        
        st.write("")
        st.write("")
        st.write("")
        st.markdown("**Validação Situação do cadastro**")
        
        st.markdown("""
            <h6 style="background-color: gray;
            padding: 15px; 
            border-radius: 5px; 
            color: white;
            margin: 0;">
                Situação do cadastro: Aprovação pendente >
            </h6>
            """, unsafe_allow_html=True)
        
        st.write("")
        st.write("")
        
        st.markdown("""
            <h6 style="background-color: gray;
            padding: 15px; 
            border-radius: 5px; 
            color: white;
            margin: 0;">
                Situação do cadastro: Em análise >
            </h6>
            """, unsafe_allow_html=True)
        
        st.write("")
        st.write("")
        
        st.markdown("""
            <h6 style="background-color: gray;
            padding: 15px; 
            border-radius: 5px; 
            color: white;
            margin: 0;">
                Situação do cadastro: Ativo >
            </h6>
            """, unsafe_allow_html=True)
        
        st.write("")
        st.write("")
        
        st.markdown("""
            <h6 style="background-color: gray;
            padding: 15px; 
            border-radius: 5px; 
            color: white;
            margin: 0;">
                Situação do cadastro: Bloqueado
            </h6>
            """, unsafe_allow_html=True)
        
        st.write("")
        st.write("")
        
        st.markdown("""
            <h6 style="background-color: gray;
            padding: 15px; 
            border-radius: 5px; 
            color: white;
            margin: 0;">
                Situação do cadastro: Aguardando informações >
            </h6>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("**Situação-Emissão/Entrega do cadastro**")
        
        st.markdown("""
            <h6 style="background-color: gray;
            padding: 15px; 
            border-radius: 5px; 
            color: white;
            margin: 0;">
                Situação do cadastro: Aguardando emissão >
            </h6>
            """, unsafe_allow_html=True)
        
        st.write("")
        st.write("")
        
        st.markdown("""
            <h6 style="background-color: gray;
            padding: 15px; 
            border-radius: 5px; 
            color: white;
            margin: 0;">
                Situação do cadastro: Impresso >
            </h6>
            """, unsafe_allow_html=True)
        
        st.write("")
        st.write("")
        
        st.markdown("""
            <h6 style="background-color: gray;
            padding: 15px; 
            border-radius: 5px; 
            color: white;
            margin: 0;">
                Situação do cadastro: Enviado >
            </h6>
            """, unsafe_allow_html=True)
        
        st.write("")
        st.write("")
        
        st.markdown("""
            <h6 style="background-color: gray;
            padding: 15px; 
            border-radius: 5px; 
            color: white;
            margin: 0;">
                Situação do cadastro: Entregue >
            </h6>
            """, unsafe_allow_html=True)
        
        st.write("")
        st.write("")
        
        st.markdown("""
            <h6 style="background-color: gray;
            padding: 15px; 
            border-radius: 5px; 
            color: white;
            margin: 0;">
                Situação do cadastro: Não entregue >
            </h6>
            """, unsafe_allow_html=True)
        
        st.write("")
        st.write("")
        
        col1, col2, col3 = st.columns([12, 1, 1])

        with col3:
            st.markdown("""
            <style>
            button[kind="primary"] {
                background-color: green !important;
                color: white !important;
            }
            </style>
            """, unsafe_allow_html=True)
            
            if st.button("Salvar", key="salvar_config", type="primary"):
                pass
    

    elif st.session_state.selected_page == "Cidadão":
        tab1, tab2,tab3,tab4 = st.tabs(["Novo Cadastro", "Pesquisar", "Validações", "Gerenciar Cartão Cidadão"])
