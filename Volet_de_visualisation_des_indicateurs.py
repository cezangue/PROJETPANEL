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

    # Chargement des données (remplacez par votre DataFrame réel)
    # Exemple : df = pd.read_csv("path_to_your_data.csv")
    # Assurez-vous que df contient les colonnes appropriées
    df = pd.DataFrame({
        "Country": ["Algeria", "Nigeria", "Kenya", "South Africa"],
        "GDP per Capita (Current Prices)": [4000, 3000, 2000, 12000]
    })

    # Fusionner les données avec le GeoDataFrame
    try:
        merged_data = africa.merge(df, left_on='ADMIN', right_on='Country', how='left')
    except KeyError as e:
        st.error(f"Erreur lors de la fusion des DataFrames : {e}")
        return
    except Exception as e:
        st.error(f"Une erreur inattendue est survenue : {e}")
        return

    # Vérifier si la colonne 'GDP per Capita (Current Prices)' existe
    if 'GDP per Capita (Current Prices)' not in merged_data.columns:
        st.warning("La colonne 'GDP per Capita (Current Prices)' n'a pas été trouvée. Veuillez vérifier vos noms de colonnes.")
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
