import streamlit as st
import plotly.graph_objects as go

def display():
    st.title("Bienvenue sur la page de visualisation")  # Titre de la nouvelle page
    st.subheader("Volet de visualisation des indicateurs")
    
    # Exemple de graphique
    fig = go.Figure(data=go.Scatter(y=[2, 3, 1], mode='lines+markers'))
    st.plotly_chart(fig)
    
    st.write("Contenu de la visualisation des indicateurs.")
