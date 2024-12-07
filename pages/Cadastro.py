import streamlit as st
# Configuração da página
st.set_page_config(page_title="Cadastro de Paciente - Saúde")

with open("cadastro.css") as editor:
    st.markdown(f"<style>{editor.read()}</style>",unsafe_allow_html=True)

nm = []
dtNascimento = []
sx = []
eml = []
sn = []
telef = []



# Título da página
st.title("Cadastro de Paciente")
st.write('<p style="font-size:20px;color:black;text-align:center">Por favor, preencha os dados abaixo para o seu cadastro.</p>',unsafe_allow_html=True)
st.sidebar.image("img/png-transparent-health-care-public-health-medicine-hospital-health-logo-medical-care-mental-health-thumbnail-removebg-preview.png")
image_url = "https://img.freepik.com/premium-vector/white-abstract-background-design_1208459-106.jpg?semt=ais_hybrid"  # Exemplo: "imagens/fundo.jpg"

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
st.markdown("""
    <style>
        /* Cor do fundo do campo de texto */
        .stTextInput>div>div>input {
            background-color: #f0f8ff;  /* Cor de fundo (exemplo: Alice Blue) */
            color: #333333;
}
        .stTextInput>div>div>input::placeholder {
            color: #333333;
}
    </style>
""", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    /* Altera a borda do st.text_input */
    .stTextInput input {
        border: 2px solid cyan;  /* Cor da borda */
    }
    </style>
    """, 
    unsafe_allow_html=True
)
if "cadastro_realizado" in st.session_state and st.session_state["cadastro_realizado"]:
    st.write("ok")
else:
    with st.form("cadastro"):
        # Informações pessoais
        st.header("Informacoes Pessoais:")
        nome = st.text_input("Nome", placeholder = "Digite seu nome")
        data = st.date_input("Data de Nascimento")
        sexo = st.radio("Sexo", ["Masculino", "Feminino", "Outro"], index=["Masculino", "Feminino", "Outro"])
        email = st.text_input("Email", placeholder= "emailaqui@gmail.com")
        senha = st.text_input("Senha", placeholder= "******", type="password")
        telefone = st.text_input("Telefone", placeholder= "(**) *****-****")

        enviado = st.form_submit_button("Continue")


# Exibe mensagem após envio do formulário
    if enviado: 
        if nome and email and telefone and senha and len(senha) < 8:
            st.error("A senha deve ter no mínimo 8 caracteres.")
    else:
        st.error("Por favor, preencha todos os campos obrigatórios.")    

    if enviado:
        if nome:
            nm.append(nome)
        if data:
            dtNascimento.append(data)
        if sexo:
            sx.append(sexo)
        if email:
            eml.append(email)
        if senha:
            sn.append(senha)
        if telefone:
            telef.append(telefone)   
                               
        if nome and "@" in email and telefone and senha and len(senha) >= 8:
            st.switch_page("pages/Informações Pessoais.py")
        elif "@" not in email:
            st.ersror("Digite seu email corretamente")    