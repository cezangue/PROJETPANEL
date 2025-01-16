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

    # Assurez-vous que les noms de colonnes correspondent
    # Vérifiez que 'Country' et 'GDP per Capita (Current Prices)' sont bien présents
    if 'Country' not in df.columns or 'GDP per Capita (Current Prices)' not in df.columns:
        st.warning("Les colonnes 'Country' ou 'GDP per Capita (Current Prices)' ne sont pas présentes dans le fichier Excel.")
        return

    # Fusionner les données avec le GeoDataFrame
    try:
        merged_data = africa.merge(df, left_on='ADMIN', right_on='Country', how='left')
    except KeyError as e:
        st.error(f"Erreur lors de la fusion des DataFrames : {e}")
        return
    except Exception as e:
        st.error(f"Une erreur inattendue est survenue : {e}")
        return

    # Vérifier si la colonne 'GDP per Capita (Current Prices)' existe après la fusion
    if 'GDP per Capita (Current Prices)' not in merged_data.columns:
        st.warning("La colonne 'GDP per Capita (Current Prices)' n'a pas été trouvée dans les données fusionnées.")
        return

    # Création de la carte choroplèthe
    fig = px.choropleth(
        merged_data,
        geojson=merged_data.geometry,
        locations=merged_data.index,
        color="GDP per Capita (Current Prices)",
        color_continuous_scale="OrRd",
        hover_name="ADMIN",
        projection="mercator",
        title='GDP per Capita in Africa'
    )

    # Mettre à jour les géos
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 0, "t": 50, "l": 0, "b": 0})

    # Affichage de la carte
    st.plotly_chart(fig)

    st.write("Contenu de la visualisation des indicateurs.")
