import streamlit as st

# Définir la configuration de la page
st.set_page_config(page_title="Page d'Accueil", page_icon="🏠")

# Définir le titre de l'application
st.title("Page d'Accueil")

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
            background-color: orange; /* Fond orange */
            color: black; /* Couleur du texte noire pour contraste */
        }
        .main {
            background-size: cover; /* Couvre toute la section */
            background-repeat: no-repeat; /* Ne pas répéter l'image */
            background-position: top center; /* Positionner l'image en haut */
            height: 100vh; /* Hauteur de la section */
            padding: 20px; /* Ajout de padding pour le contenu */
            border-radius: 10px; /* Arrondir les coins */
        }
        h1 {
            font-size: 2.5em;
            font-weight: bold;
            text-shadow: 2px 2px 4px #000000;
        }
        h2 {
            color: #ADD8E6;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Affichage de l'image pour le dépannage
    st.image("pages de navigation/Changement_climatique.JPG", caption="Changement Climatique", use_container_width=True)

    # Contenu principal
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("""<h1>TAGNE TCHINDA VOUS SOUHAITE LA BIENVENUE DANS L'ESPACE D'ANALYSE DES EFFETS DU CHANGEMENT CLIMATIQUE EN AFRIQUE SUB-SAHARIENNE</h1>""", unsafe_allow_html=True)
    st.markdown('<h2>Bonne navigation</h2>', unsafe_allow_html=True)
    st.write("Cette page, fruit du travail de TAGNE TCHINDA RINEL, nous vous proposons une vue sur la base de données utilisée pour faire des analyses, la description des différentes chroniques retenues, et l'analyse de la stationnarité des chroniques.")
    st.write("Pour voir le contenu d'une section, il vous suffit de cliquer sur le nom correspondant pour y accéder.")
    st.markdown("</div>", unsafe_allow_html=True)

# Appel de la fonction pour afficher les onglets
display_tabs()
