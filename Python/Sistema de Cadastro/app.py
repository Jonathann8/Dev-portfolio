import streamlit as st

st.title("Sistema de Cadastro")

nome = st.text_input("Digite o nome do cliente:")
endereco = st.text_input("Digite o endereço:")
dt_nasc = st.date_input("Escolha a data de nascimento:")