import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
import os
from collections import Counter

# Função para carregar dados do JSON
def load_data():
    if not os.path.exists('db.json'):
        return None
    with open('db.json', 'r') as f:
        try:
            data = json.load(f)
            return data.get("emotions", [])
        except json.JSONDecodeError:
            return []  # Retorna lista vazia se o JSON estiver malformado

# Função para contar emoções
def count_emotions(emotions):
    return Counter(emotions)

# limpar o banco de dados
def clear_data():
    if os.path.exists('db.json'):
        os.remove('db.json')
    # Cria um novo arquivo vazio
    with open('db.json', 'w') as f:
        json.dump({"emotions": []}, f)

# Título do aplicativo
st.title("Análise de Emoções")

# Botão para limpar o banco de dados
if st.button("Limpar Dados"):
    clear_data()
    st.success("Dados limpos com sucesso!")

# Carregar dados
emotions = load_data()

if emotions:
    # Contar emoções
    emotion_counts = count_emotions(emotions)

    # Criar DataFrame para o gráfico
    df = pd.DataFrame.from_dict(emotion_counts, orient='index').reset_index()
    df.columns = ['Emotion', 'Count']

    # Plotar gráfico de pizza
    fig, ax = plt.subplots()
    ax.pie(df['Count'], labels=df['Emotion'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig)
else:
    st.write("Nenhum dado de emoção disponível.")
