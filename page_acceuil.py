import streamlit as st

# Définir la configuration de la page
st.set_page_config(page_title="Page d'Accueil", page_icon="🏠")

# Définir le titre de l'application
st.markdown("<div class='scroll-text'><h1>Page d'Accueil: TAGNE TCHINDA vous souhaite la bienvenue dans l'espace d'analyse des effets du changement climatique en Afrique sub-saharienne</h1></div>", unsafe_allow_html=True)
st.markdown('<h2>Bonne navigation</h2>', unsafe_allow_html=True)

# Fonction pour créer des onglets
def display_tabs():
    tabs = ["Volet de visualisation des indicateurs", "Analyse des stationnarité des séries", "Modélisation en Panel"]
    selected_tab = st.selectbox("Choisissez une option :", tabs)

    if selected_tab == "Volet de visualisation des indicateurs":
        import Volet_de_visualisation_des_indicateurs as vvi
        vvi.display()  # Appel à la fonction d'affichage du fichier correspondant
    elif selected_tab == "Analyse des stationnarité des séries":
        import Analyse_des_stationnarite_des_series as ass
        ass.display()  # Appel à la fonction d'affichage du fichier correspondant
    elif selected_tab == "Modélisation en Panel":
        import Modelisation_en_Panel as mp
        mp.display()  # Appel à la fonction d'affichage du fichier correspondant

# Appel de la fonction pour afficher les onglets
display_tabs()
