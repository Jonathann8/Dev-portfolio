import streamlit as st
import datetime

st.title("Sistema de Cadastro")

nome = st.text_input("Digite o nome do cliente:")
endereco = st.text_input("Digite o endereço:")
dt_nasc = st.date_input(
    "Escolha a data de nascimento:",
    min_value=datetime.date(1900, 1, 1),
    max_value=datetime.date.today(),
    value=datetime.date(2000, 1, 1)
)
tipo_cliente = st.selectbox("Selecione o tipo de cliente:", ["Pessoa Física", "Pessoa Jurídica"])
Telefone = st.text_input("Digite o telefone do cliente:")
email = st.text_input("Digite o e-mail do cliente:")
CPF_CNPJ = st.text_input("Digite o CPF ou CNPJ do cliente:")
Observações = st.text_area("Observações adicionais:")

cadastrar = st.button("Cadastrar Cliente")

if cadastrar:
    with open("clientes.csv", "a", encoding="utf8") as arquivo:
        arquivo.write(f"{nome},{endereco},{dt_nasc},{tipo_cliente},{Telefone},{email},{CPF_CNPJ},{Observações}\n")
    st.success("Cliente cadastrado com sucesso!")
