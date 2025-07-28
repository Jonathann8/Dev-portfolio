import streamlit as st
import pandas as pd
import datetime

ARQUIVO = "clientes.csv"

def carregar_dados():
    try:
        df = pd.read_csv(ARQUIVO, header=None, encoding="utf-8", encoding_errors="ignore",
                         names=["Nome", "Endereço", "Data Nasc.", "Tipo", "Telefone", "Email", "CPF/CNPJ", "Observações"])
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["Nome", "Endereço", "Data Nasc.", "Tipo", "Telefone", "Email", "CPF/CNPJ", "Observações"])

def salvar_dados(df):
    df.to_csv(ARQUIVO, index=False, header=False, encoding="utf-8")

def limpar_arquivo_csv():
    try:
        with open(ARQUIVO, "r", encoding="utf8", errors="ignore") as f:
            linhas = f.readlines()
        linhas_validas = [linha for linha in linhas if linha.count(",") == 7]
        with open(ARQUIVO, "w", encoding="utf8") as f:
            f.writelines(linhas_validas)
    except FileNotFoundError:
        pass

# ---- TÍTULO ----
st.title("Sistema de Cadastro de Clientes")

# ---- FORMULÁRIO DE CADASTRO ----
with st.form("cadastro_cliente"):
    st.subheader("Cadastrar novo cliente")
    nome = st.text_input("Nome:")
    endereco = st.text_input("Endereço:")
    dt_nasc = st.date_input(
        "Data de nascimento:",
        min_value=datetime.date(1900, 1, 1),
        max_value=datetime.date.today(),
        value=datetime.date(2000, 1, 1)
    )
    tipo_cliente = st.selectbox("Tipo de cliente:", ["Pessoa Física", "Pessoa Jurídica"])
    telefone = st.text_input("Telefone:")
    email = st.text_input("E-mail:")
    cpf_cnpj = st.text_input("CPF ou CNPJ:")
    observacoes = st.text_area("Observações:")

    cadastrar = st.form_submit_button("Cadastrar")

    if cadastrar:
        with open(ARQUIVO, "a", encoding="utf8") as arquivo:
            arquivo.write(f"{nome},{endereco},{dt_nasc},{tipo_cliente},{telefone},{email},{cpf_cnpj},{observacoes}\n")
        st.success("Cliente cadastrado com sucesso!")

# ---- VISUALIZAÇÃO + EDIÇÃO/APAGAR ----
st.subheader("Clientes cadastrados")

limpar_arquivo_csv()
df = carregar_dados()

if df.empty:
    st.info("Nenhum cliente cadastrado.")
else:
    editar_index = st.session_state.get("editar_index", None)

    for i, row in df.iterrows():
        col1, col2, col3 = st.columns([4, 1, 1])
        with col1:
            st.markdown(f"**{row['Nome']}** | {row['Email']} | {row['Tipo']}")
        with col2:
            if st.button("Editar", key=f"editar_{i}"):
                st.session_state["editar_index"] = i
        with col3:
            if st.button("Apagar", key=f"apagar_{i}"):
                df = df.drop(i).reset_index(drop=True)
                salvar_dados(df)
                st.success("Cliente removido com sucesso.")
                st.experimental_rerun()

    # FORMULÁRIO DE EDIÇÃO
    if editar_index is not None and editar_index in df.index:
        st.write("---")
        st.subheader(f"Editar cliente: {df.loc[editar_index, 'Nome']}")
        nome_edit = st.text_input("Nome", value=df.loc[editar_index, "Nome"])
        endereco_edit = st.text_input("Endereço", value=df.loc[editar_index, "Endereço"])
        dt_nasc_edit = st.date_input("Data de nascimento", value=pd.to_datetime(df.loc[editar_index, "Data Nasc."]))
        tipo_edit = st.selectbox("Tipo", ["Pessoa Física", "Pessoa Jurídica"], index=0 if df.loc[editar_index, "Tipo"] == "Pessoa Física" else 1)
        telefone_edit = st.text_input("Telefone", value=df.loc[editar_index, "Telefone"])
        email_edit = st.text_input("Email", value=df.loc[editar_index, "Email"])
        cpf_cnpj_edit = st.text_input("CPF/CNPJ", value=df.loc[editar_index, "CPF/CNPJ"])
        obs_edit = st.text_area("Observações", value=df.loc[editar_index, "Observações"])

        if st.button("Salvar alterações"):
            df.loc[editar_index] = [
                nome_edit, endereco_edit, dt_nasc_edit, tipo_edit,
                telefone_edit, email_edit, cpf_cnpj_edit, obs_edit
            ]
            salvar_dados(df)
            st.success("Dados atualizados com sucesso.")
            st.session_state["editar_index"] = None
            st.experimental_rerun()
