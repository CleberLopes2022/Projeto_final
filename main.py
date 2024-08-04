import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sn
import plotly.express as px
sn.set()

st.title('Índice de mortalidade no Brasil de 1979 a 2023')

st.header('Principais Métricas de mortalidade')

# Define the CSS style
link_style = """
<style>
a {
    color: blue; /* Mude a cor do texto aqui */
    text-decoration: none; /* Remove sublinhado, se desejar */
}
a:hover {
    color: blue; /* Cor quando o mouse está sobre o link */
}
</style>
"""

with st.sidebar:
    st.title('Análise de mortes no Brasil')
    st.image('estatistica.jpeg')
    st.write(" ")
    
    # Aplica o estilo
    st.markdown(link_style, unsafe_allow_html=True)
    st.markdown('[Ministério da Saúde - Covid-19 No Brasil](https://infoms.saude.gov.br/extensions/covid-19_html/covid-19_html.html)', unsafe_allow_html=True)
    st.write(" ")
    st.write('O conjunto de dados analisados foram retirados de 24 arquivos csv , contendo mais 46 milhoes de linhas no total de dados registrados.')
    st.write('Foram feitos vários tratamentos dos dados,como dados faltantes, colunas com nome diferente em cada arquivo e correção no formato de datas.')
    st.write('Através da biblioteca pandas, foi feito a análise e obtenção dos dados contidos neste site. Obrigado!')


col1, col2, col3 = st.columns(3)
col1.metric("Total de Mortes Geral", "46357857" , "Total Geral")
col2.metric("Por Sexo", "26574767", "Homens")
col3.metric("Por Sexo", "19740984", "Mulheres")

# Dados fornecidos
anos = [1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
numero_mortes = [711742, 750727,750276,741614,771203,809825,788231,811556,799621,834338,815774,817284,803836,827652,878106,887594,878106,908883,903516,931895,938658,946686,961492,982807,1002340,1024073,1006827,1031691,1047824,1077007,1103088,1136947,1170498,1181166,1210474,1227039,1264175,1309774,1312663,1316719,1349801,1556824,1832649,1544266,1400590]

# Criar DataFrame com os dados
data = pd.DataFrame({'Ano': anos, 'Número de Mortes': numero_mortes})

# Criação do gráfico de barras interativo usando Plotly
fig = px.bar(data, x='Ano', y='Número de Mortes', title='Número de Mortes por Ano')
fig.update_layout(xaxis_title='Ano', yaxis_title='Número de Mortes', xaxis_tickangle=-45)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)

st.subheader('Informação 1')
st.write('O ano de 2021 registrou o maior número de mortes no período, totalizando 1.832.649 óbitos.')
st.write('Os Homens representam aproximadamente 57.33% do total de mortes, enquanto as Mulheres representam aproximadamente 42.58% do total de mortes.')
st.write(' ')

st.subheader('Principais causas de mortalidade')

# Dados fornecidos
causas = ["Infarto", "AVC", "Pneumonia", "Covid-19", "Diabetes", "Cancer Pulmão", "Hipertensão"]
quantidade = [2071776, 1160686, 928800, 690115, 650078, 571562, 514144]

# Criar DataFrame com os dados
data = pd.DataFrame({'Causa': causas, 'Quantidade': quantidade})

# Criação do gráfico de barras interativo usando Plotly
fig = px.bar(data, x='Causa', y='Quantidade', title='Quantidade de Mortes por Causa')
fig.update_layout(xaxis_title='Causa', yaxis_title='Quantidade', xaxis_tickangle=-45)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)

st.subheader('Informação 2')
st.write("Podemos observar que o Infarto agudo do miocárdio é de longe a causa de morte mais comum no Brasil, conforme dados do ministério da saúde.")
st.markdown('[Ministério da Saúde - Infarto do Miocárdio](https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/i/infarto#:~:text=O%20Infarto%20Agudo%20do%20Mioc%C3%A1rdio,7%20casos%2C%20ocorra%20um%20%C3%B3bito.)', unsafe_allow_html=True)
st.subheader(' ')

# Dados
data = {
    "Ano": [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013],
    "Quantidade": [1400590, 1544266, 1832649, 1556824, 1349801, 1316719, 1312663, 1309774, 1264175, 1227039, 1210474],
    "Maior Causa": ["Infarto do Miocardio", "Infarto do Miocardio", "Covid-19", "Covid-19", "Infarto do Miocardio", "Infarto do Miocardio", "Infarto do Miocardio", "Infarto do Miocardio", "Infarto do Miocardio", "Infarto do Miocardio", "Infarto do Miocardio"],
    "Qt Maior Causa": [82915, 92151, 415935, 203429, 90355, 87286, 87800, 89989, 86674, 83746, 82514]
}

df = pd.DataFrame(data)

# Lista suspensa para selecionar o ano
ano_selecionado = st.selectbox("Selecione o ano e obterá a Maior causa de Morte e quantidade nesse ano:", df["Ano"])

# Filtra os dados para o ano selecionado
df_filtrado = df[df["Ano"] == ano_selecionado]

# Cria um gráfico de barras para a quantidade total e a quantidade da maior causa
df_melted = df_filtrado.melt(id_vars="Ano", value_vars=["Quantidade", "Qt Maior Causa"], var_name="Tipo", value_name="Valor")

fig = px.bar(
    df_melted,
    x="Tipo",
    y="Valor",
    title=f"Dados para o ano {ano_selecionado}"
)

# Exibe os dados detalhados e o gráfico
st.write(f"Ano: {ano_selecionado}")
st.write(f"Quantidade Total de Mortes: {df_filtrado['Quantidade'].values[0]}.")
st.write(f"A Maior Causa: {df_filtrado['Maior Causa'].values[0]}.")
st.write(f"Quantidade da Maior Causa: {df_filtrado['Qt Maior Causa'].values[0]}.")

# Exibe o gráfico
st.plotly_chart(fig)

st.subheader('Informação 3')
st.write("Podemos observar que os unicos anos que o infarto do miocárdio não foi a princiapa causa, foi em 2020 e 2021 com o pico da covid-19.")
st.write(" ")


st.subheader('Mortalidade fetal x não_fetal')
# Dados fornecidos
labels = ['Fetal', 'Não Fetal']
sizes = [25248, 46332609]
colors = ['#ff9999','#66b3ff']

# Criação do gráfico de pizza interativo usando Plotly
fig = px.pie(values=sizes, names=labels, title='Distribuição de Mortes Fetal vs Não Fetal', color_discrete_sequence=colors)
fig.update_traces(textposition='inside', textinfo='percent+label', pull=[0.1, 0])

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)


st.subheader('Informação 4')
st.write('Morte por tipo de obito fetal foi de 25248, o que representa 0,1% dos dos dados.')


st.write('A morte fetal é definida como o falecimento de um feto dentro do útero materno antes do nascimento. Geralmente, é diagnosticada quando não há batimentos cardíacos detectáveis no feto após a idade gestacional em que se espera que esses batimentos sejam claramente visíveis, que geralmente é por volta das 20 semanas de gestação. A causa pode variar e incluir complicações médicas, problemas com a placenta, infecções, anomalias genéticas ou malformações congênitas, entre outros fatores.')


