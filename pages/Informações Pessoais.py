import streamlit as st

st.title("Cadastro de Paciente - Saúde")
st.markdown("Por favor, preencha os dados abaixo para o seu cadastro.")
st.sidebar.image("img/png-transparent-health-care-public-health-medicine-hospital-health-logo-medical-care-mental-health-thumbnail-removebg-preview.png")
image_url = "https://img.freepik.com/free-vector/medical-healthcare-blue-color_1017-26807.jpg"  # Exemplo: "imagens/fundo.jpg"

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

with st.form("saúde"):
    st.header("Informações de Saúde")

    altura = st.number_input("Altura (cm)", min_value=50, max_value=250, step=1, value=170)
    peso = st.number_input("Peso (kg)", min_value=10, max_value=300, step=1, value=70)
    condições = st.text_area("Condições de Saúde", placeholder="Ex.: diabetes, hipertensão, etc.")
    
    enviado = st.form_submit_button("Enviar Cadastro")

if enviado:
    if altura and peso and condições:
        st.success("Cadastro realizado com sucesso! Seja Bem-Vindo(a).")
    else:
        st.error("Por favor, verifique se todos os campos estão preenchidos.")