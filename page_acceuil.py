import streamlit as st
import Volet_de_visualisation_des_indicateurs
import Analyse_de_stationarité_des_indicateurs
import modelisation_de_panel# Assurez-vous que le nom du fichier est correct


# Définir la configuration de la page
st.set_page_config(page_title="Page d'Accueil", page_icon="🏠")

# Définir le titre de l'application
#st.markdown("<h1 style='text-align: center;'>Page d'Accueil: TAGNE TCHINDA vous souhaite la bienvenue dans l'espace d'analyse des effets du changement climatique en Afrique sub-saharienne</h1>", unsafe_allow_html=True)
st.markdown("<div class='scroll-text'><h1>Page d'Accueil: TAGNE TCHINDA vous souhaite la bienvenue dans l'espace d'analyse des effets du changement climatique en Afrique sub-saharienne</h1></div>", unsafe_allow_html=True)
st.markdown('<h2>Bonne navigation</h2>', unsafe_allow_html=True)
# Fonction pour créer des onglets
def display_tabs():
    tabs = ["Volet de visualisation des indicateurs", "Analyse des stationnarité des séries", "Modélisation en Panel"]
    selected_tab = st.selectbox("Choisissez une option :", tabs)

    #if selected_tab == "Volet de visualisation des indicateurs":
    #    display_visualisation()
   # elif selected_tab == "Analyse des stationnarité des séries":
 #       st.write("Contenu de l'analyse des stationnarité des séries")
  #  elif selected_tab == "Modélisation en Panel":
   #     st.write("Contenu de la modélisation en Panel")
    if selected_tab == "Volet de visualisation des indicateurs":
        Volet_de_visualisation_des_indicateurs.display()  # Appel à la fonction d'affichage
    elif selected_tab == "Analyse des stationnarité des séries":
#        st.write("Contenu de l'analyse des stationnarité des séries")
         Analyse_de_stationarité_des_indicateurs.display()  # Appel à la fonction d'affichage
    elif selected_tab == "Modélisation en Panel":
        modelisation_de_panel.display()
#        st.write("Contenu de la modélisation en Panel")

# Fonction pour afficher le contenu de la visualisation
def display_visualisation():
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
            background-size: cover; /* Couvre toute la section */
            background-repeat: no-repeat; /* Ne pas répéter l'image */
            background-position: top center; /* Positionner l'image en haut */
            height: 100vh; /* Hauteur de la section */
            padding: 20px; /* Ajout de padding pour le contenu */
            border-radius: 10px; /* Arrondir les coins */
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
    st.markdown("<h2 style='text-align: center;'>Nous sommes disponibles vie l'adresse mail: cezangue@gmail.com</h2>", unsafe_allow_html=True)
     #st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.write("Cette page, fruit du travail de TAGNE TCHINDA RINEL, nous vous proposons une vue sur la base de données utilisée pour faire des analyses, la description des différentes chroniques retenues, et l'analyse de la stationnarité des chroniques.")
    st.write("Pour voir le contenu d'une section, il vous suffit de cliquer sur le nom correspondant pour y accéder.")
    st.markdown("</div>", unsafe_allow_html=True)

# Appel de la fonction pour afficher les onglets
display_tabs()
