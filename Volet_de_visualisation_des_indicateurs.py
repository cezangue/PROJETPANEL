import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
import json

def display():
    st.title("Bienvenue sur la page de visualisation")  # Titre de la nouvelle page
    st.subheader("Volet de visualisation des indicateurs")

    # Onglet de sélection pour les types de visualisation
    visualization_type = st.sidebar.selectbox(
        "Choisissez le type de visualisation :",
        options=['Visualisation univariée des indicateurs', 'Visualisation bivariée des indicateurs', 'Autres analyses']
    )

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

    # Vérification des colonnes
    if 'Country' not in df.columns:
        st.warning("La colonne 'Country' n'est pas présente dans le fichier Excel.")
        return

    # Si l'utilisateur choisit 'Visualisation univariée des indicateurs'
    if visualization_type == 'Visualisation univariée des indicateurs':
        variable_col = st.sidebar.selectbox(
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

    # Si l'utilisateur choisit 'Visualisation bivariée des indicateurs'
    elif visualization_type == 'Visualisation bivariée des indicateurs':
        bivariate_option = st.sidebar.selectbox(
            "Choisissez le type de visualisation bivariée :",
            options=['Cartes bivariées', 'Matrice de corrélation']
        )

        # Cartes bivariées
        if bivariate_option == 'Cartes bivariées':
            st.sidebar.write("Sélectionnez deux variables pour la visualisation bivariée.")
            variable_col1 = st.sidebar.selectbox(
                "Sélectionnez la première variable :",
                options=[col for col in df.columns if col != 'Country'],
                index=0  # Par défaut, sélectionner la première variable
            )
            variable_col2 = st.sidebar.selectbox(
                "Sélectionnez la deuxième variable :",
                options=[col for col in df.columns if col != 'Country' and col != variable_col1],
                index=1  # Par défaut, sélectionner la deuxième variable
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

            # Vérifier si les variables sélectionnées existent après la fusion
            if variable_col1 not in merged_data.columns or variable_col2 not in merged_data.columns:
                st.warning(f"L'une des colonnes '{variable_col1}' ou '{variable_col2}' n'a pas été trouvée dans les données fusionnées.")
                return

            # Création de la carte choroplèthe bivariée
            fig = px.choropleth(
                merged_data,
                geojson=merged_data.geometry,
                locations=merged_data.index,
                color=variable_col1,
                hover_name="ADMIN",
                title=f'{variable_col1} et {variable_col2} en Afrique',
                color_continuous_scale="Viridis"
            )

            # Ajouter la couche de bulles
            merged_data[variable_col2] = merged_data[variable_col2].fillna(0)
            geojson_data = json.loads(merged_data.to_json())

            fig.add_scattergeo(
                geojson=geojson_data,
                locations=merged_data.index,
                lon=merged_data.geometry.centroid.x,
                lat=merged_data.geometry.centroid.y,
                text=merged_data['ADMIN'],
                mode="markers",
                marker=dict(
                    size=merged_data[variable_col2] / 5,
                    sizemode="area",
                    sizeref=2.*max(merged_data[variable_col2])/(40.**2),
                    sizemin=4,
                    color="green"  # Couleur des bulles
                ),
                name=variable_col2,  # Nom dans la légende
                showlegend=True  # Assurer que la légende est affichée
            )

            # Légende séparée pour la légende
            fig.add_scattergeo(
                geojson=geojson_data,
                locations=merged_data.index,
                lon=[None],
                lat=[None],
                text=[None],
                mode="markers",
                marker=dict(
                    size=[10, 20, 30],  # Tailles d'exemple pour la légende
                    sizemode="area",
                    sizeref=2.*max(merged_data[variable_col2])/(40.**2),
                    sizemin=4,
                    color="green",
                    opacity=0  # Rendre les marqueurs invisibles
                ),
                name=variable_col2,
                showlegend=True,
                legendgroup=variable_col2,
                visible="legendonly"  # Afficher uniquement dans la légende
            )

            # Déplacer la légende et changer la couleur de la police
            fig.update_layout(legend=dict(x=0, y=1, font=dict(color="black")))  # x=0 (gauche), y=1 (haut)

            # Affichage de la carte
            st.plotly_chart(fig)

        # Matrice de corrélation
        elif bivariate_option == 'Matrice de corrélation':
            st.write("Cette section affichera la matrice de corrélation.")
            # Vous pouvez ajouter ici le code pour afficher la matrice de corrélation si souhaité.

    # Si l'utilisateur choisit 'Autres analyses'
    elif visualization_type == 'Autres analyses':
        st.write("Cette section est réservée pour d'autres analyses.")

    st.write("Contenu de la visualisation des indicateurs.")
