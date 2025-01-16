import streamlit as st

def set_background(opacity=0.5, color="#FFA500"):  # Modifiez la couleur ici pour orange
    """Définit la couleur de fond de l'application."""
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
            opacity: {opacity};
        }}
        .stApp h1, .stApp h2 {{
            color: white !important;
        }}
        .animated-title {{
            font-size: 2.5em;
            font-weight: bold;
            animation: text-animation 10s linear infinite;
            text-shadow: 2px 2px 4px #000000;
        }}
        @keyframes text-animation {{
            0% {{ transform: translateX(-100%); opacity: 0; }}
            10% {{ transform: translateX(0%); opacity: 1;}}
            90% {{ transform: translateX(0%); opacity: 1;}}
            100% {{ transform: translateX(100%); opacity: 0; }}
        }}
        .fade-in-out {{
            animation: fade 3s ease-in-out infinite alternate;
            color: #ADD8E6;
        }}
        @keyframes fade {{
            0% {{ opacity: 0.2; color: #ADD8E6;}}
            50% {{ opacity: 1; color: #87CEEB; }}
            100% {{ opacity: 0.2; color: #ADD8E8; }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():
    st.set_page_config(page_title="Visualisation des Données", page_icon="")
    
    # Définir la couleur de fond
    set_background(opacity=1.0, color="#FFA500")  # Appliquez la couleur orange ici

    st.markdown("""<h1 class="animated-title">TAGNE TCHINDA VOUS SOUHAITE LA BIENVENUE DANS L'ESPACE D'ANALYSE DES EFFETS DU CHANGEMENT CLIMATIQUE EN AFRIQUE SUB-SAHARIENNE</h1>""", unsafe_allow_html=True)
    st.markdown('<h2 class="fade-in-out">Bonne navigation</h2>', unsafe_allow_html=True)

    # Ajouter l'image du drapeau depuis le répertoire local
    st.image("Changement_climatique.JPG", caption="  ", use_container_width=True)

    st.title("Cette page, fruit du travail de TAGNE TCHINDA RINEL, nous vous proposons une vue sur la base de données utilisée pour faire des analyses, la description des différentes chroniques retenues, et l'analyse de la stationnarité des chroniques.")
    st.title("Pour voir le contenu d'une section, il vous suffit de cliquer sur le nom correspondant pour y accéder.")

if __name__ == '__main__':
    main()




<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visualisation des Données</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/leaflet.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/leaflet.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet.shapefile/1.0.0/leaflet.shapefile.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/xlsx/dist/xlsx.full.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        #map {
            height: 400px;
            width: 100%;
        }
        #chart {
            width: 100%;
            height: 400px;
        }
    </style>
</head>
<body>

    <h1>Options de Visualisation</h1>

    <h2>1. Graphiques de Type Carte</h2>
    <div id="map"></div>

    <h2>2. Évolutions Individuelles</h2>
    <canvas id="chart"></canvas>

    <script>
        // Initialisation de la carte
        var map = L.map('map').setView([0, 20], 3); // Vue centrée sur l'Afrique

        // Ajout d'une couche de carte
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
        }).addTo(map);

        // Chargement du shapefile
        fetch('shapefile_Afrique.shp')
            .then(response => response.arrayBuffer())
            .then(buffer => {
                const shapefileData = new Shapefile(buffer);
                L.shapefile(shapefileData).addTo(map);
            })
            .catch(err => console.error(err));

        // Fonction pour lire le fichier Excel
        function readExcel(file) {
            const reader = new FileReader();
            reader.onload = function(event) {
                const data = new Uint8Array(event.target.result);
                const workbook = XLSX.read(data, {type: 'array'});

                // Supposons que les données sont dans la première feuille
                const sheetName = workbook.SheetNames[0];
                const worksheet = workbook.Sheets[sheetName];
                const jsonData = XLSX.utils.sheet_to_json(worksheet);
                
                // Exemple d'utilisation de jsonData pour le graphique
                createChart(jsonData);
            };
            reader.readAsArrayBuffer(file);
        }

        // Exemple de création de graphique
        function createChart(data) {
            const labels = data.map(row => row['Variable']); // Remplacez 'Variable' par le nom de votre colonne
            const values = data.map(row => row['Valeur']); // Remplacez 'Valeur' par le nom de votre colonne

            const chartData = {
                labels: labels,
                datasets: [{
                    label: 'Données Excel',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    data: values,
                }]
            };

            const config = {
                type: 'line', // Type de graphique
                data: chartData,
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            };

            const myChart = new Chart(
                document.getElementById('chart'),
                config
            );
        }

        // Exemple pour lire le fichier Excel
        fetch('Panel7TOUT_fichier.xlsx')
            .then(response => response.blob())
            .then(blob => readExcel(blob))
            .catch(err => console.error(err));

    </script>

</body>
</html>

