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
