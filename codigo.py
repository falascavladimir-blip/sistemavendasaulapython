# titulo - sistema de vendas
# secao cadastrar vendas
    # Campo Data
    # Campo Vendedor - ana, bruno, carla
    # Campo Produto - Notebook, Fone, Celular
    # Campo Qualidade
    # Campo Valor 
    # Botao Cadastrar Vendas 

# Secao Vendas Cadastradas 
    # tabela de vendas 

# Secao Dashboard
    # Card/Metrica -> Faturamento Total
    # Grafico Barra/Coluna -> Venda por vendedor
    # Grafico de Rosca 

import streamlit as st
import pandas as pd
import plotly.express as px

# carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

# Titulo do Formulário
st.write("## Sistema de Vendas VAF")

# secao de cadastro de vendas
st.sidebar.write("### Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruna", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Fone", "Celular"])
quantidade = st.sidebar.number_input("Quantidade", step=1, min_value=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Vendas")

# logica de cadastro
if botao_cadastrar:
    nova_venda = pd.DataFrame({
        "data": [data],
        "vendedor": [vendedor],
        "produto": [produto],
        "quantidade": [quantidade],
        "valor": [valor]
        
    })
    tabela_vendas = pd.concat([tabela_vendas, nova_venda], ignore_index=True)
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.sidebar.success("Venda cadastrada com sucesso!")     


# secao de visualizar as vendas
st.write("### Vendas Cadastradas")
st.dataframe(tabela_vendas)


# secao de dashboard
st.write("### Dashboard")

# card/metrica de faturamento total
faturamento = tabela_vendas["valor"].sum()
faturamento_formatado = f"R$ {faturamento:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
st.metric("Faturamento Total", faturamento_formatado)

# gráficos de barra/coluna -> Venda por Vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="vendedor", title="Vendas por Vendedor")
st.plotly_chart(grafico1)

# Gráficos de pizza -> Vendas por Produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", title="Vendas por Produto", hole=0.5)  
st.plotly_chart(grafico2)









