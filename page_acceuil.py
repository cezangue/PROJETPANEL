import streamlit as st

# Définir la configuration de la page
st.set_page_config(page_title="Page d'Accueil", page_icon="🏠")

# Fonction pour afficher le fond et le contenu
def display_home_page():
    # Styles CSS pour le fond et le texte
    st.markdown(
        """
        <style>
        .stApp {
            background-color: orange; /* Fond orange */
            color: black; /* Couleur du texte noire pour contraste */
        }
        .scroll-text {
            overflow: hidden;
            white-space: nowrap;
            box-sizing: border-box;
            animation: scroll 20s linear infinite; /* Animation de défilement */
        }
        @keyframes scroll {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }
        .main {
            text-align: center; /* Centrer le texte */
            padding: 20px; /* Ajout de padding pour le contenu */
        }
        h2 {
            color: #ADD8E6; /* Couleur du titre */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Affichage du titre défilant
    st.markdown("<div class='scroll-text'><h1>Page d'Accueil: TAGNE TCHINDA vous souhaite la bienvenue dans l'espace d'analyse des effets du changement climatique en Afrique sub-saharienne</h1></div>", unsafe_allow_html=True)

    # Affichage de l'image
    st.image("pages de navigation/Changement_climatique.JPG", caption="Changement Climatique", use_container_width=True)

    # Contenu principal
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h2>Nous sommes disponibles via l'adresse mail: cezangue@gmail.com</h2>", unsafe_allow_html=True)
    st.write("Cette page, fruit du travail de TAGNE TCHINDA RINEL, nous vous propose une vue sur la base de données utilisée pour faire des analyses, la description des différentes chroniques retenues, et l'analyse de la stationnarité des chroniques.")
    st.write("Pour voir le contenu d'une section, il vous suffit de cliquer sur le nom correspondant pour y accéder.")
    st.markdown("</div>", unsafe_allow_html=True)

# Fonction pour créer des onglets
def display_tabs():
    tabs = ["Volet de visualisation des indicateurs", "Analyse des stationnarité des séries", "Modélisation en Panel"]
    selected_tab = st.selectbox("Choisissez une option :", tabs)

    # Mettre à jour l'état de la page en fonction de l'onglet sélectionné
    st.session_state.page = selected_tab

# Vérifier quelle page afficher
if 'page' not in st.session_state:
    st.session_state.page = "accueil"  # Page par défaut

# Appel de la fonction pour afficher les onglets
display_tabs()

# Logique pour afficher la page d'accueil ou les autres pages
if st.session_state.page == "Volet de visualisation des indicateurs":
    import Volet_de_visualisation_des_indicateurs as vvi
    vvi.display()
elif st.session_state.page == "Analyse des stationnarité des séries":
    import Analyse_des_stationnarite_des_series as ass
    ass.display()
elif st.session_state.page == "Modélisation en Panel":
    import Modelisation_en_Panel as mp
    mp.display()
else:
    display_home_page()  # Afficher la page d'accueil par défaut
