import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

def display():
    st.title("Bienvenue sur la page de visualisation")  # Titre de la nouvelle page
    st.subheader("Volet de visualisation des indicateurs")

    # Chargement du shapefile
    try:
        africa = gpd.read_file("pages de navigation/ne_110m_admin_0_countries.shp")
    except Exception as e:
        st.error(f"Erreur lors du chargement du shapefile : {e}")
        return

    # Chargement des données depuis le fichier Excel
    try:
        df = pd.read_excel("Panel7TOUT_fichier.xlsx")  # Assurez-vous que le chemin est correct
    except Exception as e:
        st.error(f"Erreur lors du chargement du fichier Excel : {e}")
        return

    # Afficher les colonnes du DataFrame pour vérification
    st.write("Colonnes disponibles dans le fichier Excel :", df.columns)

    # Vérification des colonnes
    if 'Country' not in df.columns:
        st.warning("La colonne 'Country' n'est pas présente dans le fichier Excel.")
        return

    # Sélecteur pour choisir la variable à visualiser
    variable_col = st.selectbox(
        "Sélectionnez la variable à visualiser :",
        options=[col for col in df.columns if col != 'Country'],
        index=0  # Par défaut, sélectionner la première variable
    )

    # Fusionner les données avec le GeoDataFrame
    try:
        merged_data = africa.merge(df, left_on='ADMIN', right_on='Country', how='left')
    except KeyError as e:
        st.error(f"Erreur lors de la fusion des DataFrames : {e}")
        return
    except Exception as e:
        st.error(f"Une erreur inattendue est survenue : {e}")
        return

    # Vérifier si la variable sélectionnée existe après la fusion
    if variable_col not in merged_data.columns:
        st.warning(f"La colonne '{variable_col}' n'a pas été trouvée dans les données fusionnées.")
        return

    # Création de la carte choroplèthe
    fig = px.choropleth(
        merged_data,
        geojson=merged_data.geometry,
        locations=merged_data.index,
        color=variable_col,
        color_continuous_scale="OrRd",
        hover_name="ADMIN",
        projection="mercator",
        title=f'{variable_col} en Afrique'
    )

    # Mettre à jour les géos
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 0, "t": 50, "l": 0, "b": 0})

    # Affichage de la carte
    st.plotly_chart(fig)

    st.write("Contenu de la visualisation des indicateurs.")
