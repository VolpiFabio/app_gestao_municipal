# Sistema de Gestão Municipal Integrado

![Status do Projeto](https://img.shields.io/badge/status-em%20desenvolvimento-yellow )

Bem-vindo ao repositório do **Sistema de Gestão Municipal Integrado**, uma aplicação web desenvolvida com Streamlit e Python, projetada para ser um portal integrado de serviços para cidadãos de diversos municípios.

> **Nota:** Este projeto está atualmente em fase de desenvolvimento ativo. Novas funcionalidades estão sendo adicionadas e a estrutura pode mudar.

## 📋 Sobre o Projeto

O objetivo do Sistema de Gestão Municipal Integrado é centralizar e simplificar o acesso a serviços e informações municipais, oferecendo uma plataforma única onde os cidadãos podem se autenticar e interagir com a gestão de sua cidade.

A aplicação está sendo construída com uma arquitetura modular, permitindo fácil expansão e manutenção.

## ✨ Funcionalidades Atuais

*   **Sistema de Autenticação Seguro:**
    *   Cadastro de novos usuários.
    *   Login com e-mail e senha.
    *   Logout seguro.
*   **Integração com Banco de Dados na Nuvem:** Utiliza o **Supabase** como backend para gerenciar usuários e dados, garantindo persistência e escalabilidade.
*   **Interface Dinâmica:** A interface se adapta ao status do usuário (logado ou deslogado), mostrando a tela de login ou a página principal.
*   **Deploy Contínuo:** A aplicação está hospedada no Streamlit Community Cloud e é atualizada automaticamente a cada novo `push` no repositório.

## 🚀 Próximos Passos (Roadmap)

A lista abaixo representa as funcionalidades planejadas para as próximas versões:

- [ ] **Dashboard do Cidadão:** Uma página inicial personalizada após o login.
- [ ] **Consulta de Protocolos:** Permitir que o cidadão abra e consulte o andamento de protocolos.
- [ ] **Agendamento de Serviços:** Integrar um sistema para agendar atendimentos em secretarias municipais.
- [ ] **Notícias e Comunicados:** Uma área para a prefeitura publicar informações importantes.
- [ ] **Perfil do Usuário:** Permitir que o usuário edite suas informações e altere sua senha.

## 🛠️ Tecnologias Utilizadas

*   **Frontend:** [Streamlit](https://streamlit.io/ ) - Para a criação da interface web interativa em Python.
*   **Backend e Banco de Dados:** [Supabase](https://supabase.com/ ) - Utilizado para autenticação de usuários e como banco de dados PostgreSQL.
*   **Linguagem:** [Python 3](https://www.python.org/ )
*   **Hospedagem:** [Streamlit Community Cloud](https://streamlit.io/cloud )

## ⚙️ Como Executar o Projeto Localmente

Para executar esta aplicação em seu ambiente local, siga os passos abaixo.

### Pré-requisitos

*   Python 3.8 ou superior
*   Conta no Supabase (para obter as chaves de API)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/volpifabio/NOME-DO-SEU-REPO.git
    cd NOME-DO-SEU-REPO
    ```
    *(Lembre-se de substituir `NOME-DO-SEU-REPO` pelo nome real do seu repositório )*

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Windows: .venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure suas chaves de API:**
    *   Crie uma pasta chamada `.streamlit` na raiz do projeto.
    *   Dentro dela, crie um arquivo chamado `secrets.toml`.
    *   Adicione suas chaves do Supabase ao arquivo:
        ```toml
        SUPABASE_URL = "SUA_URL_AQUI"
        SUPABASE_KEY = "SUA_CHAVE_ANON_PUBLIC_AQUI"
        ```

### Execução

Com tudo instalado e configurado, inicie a aplicação com o seguinte comando:

```bash
streamlit run main.py

### 🤝 Contribuições
Este é um projeto pessoal, mas feedbacks e sugestões são sempre bem-vindos! Sinta-se à vontade para abrir uma Issue para relatar um bug ou sugerir uma nova funcionalidade.

