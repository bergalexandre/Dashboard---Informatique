from matplotlib import pyplot as plt
from utils import *

class Problemes():

    def __init__(self, specialty):
        self.specialty = specialty
        self.travail_effectue = {}
        for membre in self.specialty['membres'].keys():
            if membre not in self.travail_effectue.keys():
                self.travail_effectue[membre] = []
       

    def fetchData(self):
        # fetching data
        semaine_courante = df_formule['Date Actuel'][1]
        data = df_travail_effectue[['NOM', 'Nom Système', 'Problème']].dropna()[df_travail_effectue['Semaine'] == semaine_courante]
    
        # Heures taches de la semaine
        for i, objectif in data.iterrows():
            if objectif['NOM'] in self.travail_effectue.keys():
                self.travail_effectue[objectif['NOM']].append(objectif.values.tolist())

                

    def graphSave(self):
        
        column_headers = ['Membre', 'Nom Système', 'Problème']
        

        cell_text = []
        for membre in self.travail_effectue.keys():
            for row in self.travail_effectue[membre]:
                if bool(row):
                    cell_text.append(row)
        
        fig = plt.subplot()
        table = fig.table(cellText=cell_text, colColours=['g', 'g', 'g'], colLabels=column_headers, loc='center', cellLoc='center')
        fig.axis("off")
        #fig.set_size_inches(5, 8)
        #[t.auto_set_font_size(False) for t in [tab1, tab2]]
        #[t.set_fontsize(8) for t in [tab1, tab2]]

        table.auto_set_column_width(col=list(range(len(column_headers)))) # Provide integer list of columns to adjust
        plt.savefig('img/problemes.png', transparent=True, bbox_inches='tight', pad_inches=0, dpi=450)
