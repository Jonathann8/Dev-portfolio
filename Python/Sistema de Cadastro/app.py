import streamlit as st

st.title("Sistema de Cadastro")

nome = st.text_input("Digite o nome do cliente:")
endereco = st.text_input("Digite o endereço:")
dt_nasc = st.date_input("Escolha a data de nascimento:")
tipo_cliente = st.selectbox("Selecione o tipo de cliente:", ["Pessoa Física", "Pessoa Jurídica"])
Telefone = st.text_input("Digite o telefone do cliente:")
email = st.text_input("Digite o e-mail do cliente:")
CPF_CNPJ = st.text_input("Digite o CPF ou CNPJ do cliente:")

cadastrar = st.button("Cadastrar Cliente")

if cadastrar:
    with open("clientes.csv", "a", encoding="utf8") as arquivo:
        arquivo.write(f"{nome},{endereco},{dt_nasc},{tipo_cliente}\n")
        st.success("Cliente cadastrado com sucesso!")