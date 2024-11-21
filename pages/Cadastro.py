import streamlit as st
# Configuração da página
st.set_page_config(page_title="Cadastro de Paciente - Saúde")

with open("cadastro.css") as editor:
    st.markdown(f"<style>{editor.read()}</style>",unsafe_allow_html=True)


# Título da página
st.title("Cadastro de Paciente")
st.write('<p style="font-size:20px;color:cyan">Por favor, preencha os dados abaixo para o seu cadastro.</p>',unsafe_allow_html=True)
st.sidebar.image("img/png-transparent-health-care-public-health-medicine-hospital-health-logo-medical-care-mental-health-thumbnail-removebg-preview.png")
image_url = "https://static.vecteezy.com/ti/vetor-gratis/p1/6712981-resumo-saude-medico-ciencia-saude-icone-tecnologia-digital-ciencia-conceito-moderno-inovacao-tratamento-medicina-em-hi-tech-futuro-fundo-azul-para-papel-de-parede-modelo-web-design-vetor.jpg"  # Exemplo: "imagens/fundo.jpg"

# Adicione a imagem de fundo com HTML e CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
# Formulário de cadastro
with st.form("cadastro"):
    # Informações pessoais
    st.header("Informacoes Pessoais:")
    nome = st.text_input("Nome completo", placeholder="Digite seu nome completo")
    data_nascimento = st.date_input("Data de nascimento")
    sexo = st.radio("Sexo", ["Masculino", "Feminino", "Outro"])

    # Contato
    st.header("Informacoes de Contato:")
    email = st.text_input("E-mail", placeholder="exemplo@vitally.com")
    senha = st.text_input("Senha", placeholder="Crie uma senha (min 8 dígitos)", type = 'password')
    telefone = st.text_input("Telefone", placeholder="(XX) XXXXX-XXXX")
    
    enviado = st.form_submit_button("Continue")
    

# Exibe mensagem após envio do formulário
if enviado:
    if nome and email and telefone and senha and len(senha) >= 8:
        st.switch_page("pages/Informações Pessoais.py")
    elif nome and email and telefone and senha and len(senha) < 8:
        st.error("A senha deve ter no mínimo 8 caracteres.")
    else:
        st.error("Por favor, preencha todos os campos obrigatórios.")    
