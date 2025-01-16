import streamlit as st

# Définir la configuration de la page
st.set_page_config(page_title="Page d'Accueil", page_icon="🏠")

# Définir le titre de l'application
st.title("Page d'Accueil")

# Afficher l'image pour tester le chemin
st.image("pages de navigation/Changement_climatique.JPG", caption="Changement Climatique", use_container_width=True)

# Fonction pour créer des onglets
def display_tabs():
    tabs = ["Volet de visualisation des indicateurs", "Autre page 1", "Autre page 2"]
    selected_tab = st.selectbox("Choisissez une option :", tabs)

    if selected_tab == "Volet de visualisation des indicateurs":
        display_visualisation()
    elif selected_tab == "Autre page 1":
        st.write("Contenu de l'autre page 1")
    elif selected_tab == "Autre page 2":
        st.write("Contenu de l'autre page 2")

# Fonction pour afficher le contenu de la visualisation
def display_visualisation():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('./pages de navigation/Changement_climatique.JPG'); /* Chemin de l'image de fond */
            background-size: cover; /* Couvre toute la page */
            background-repeat: no-repeat; /* Ne pas répéter l'image */
            color: black; /* Couleur du texte noire pour contraste */
        }
        .main {
            background-color: rgba(255, 255, 255, 0.8); /* Fond blanc semi-transparent pour le contenu */
            padding: 20px; /* Ajout de padding pour le contenu */
            border-radius: 10px; /* Arrondir les coins */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<h1>Bienvenue dans l'espace d'analyse</h1>", unsafe_allow_html=True)

# Appel de la fonction pour afficher les onglets
display_tabs()
