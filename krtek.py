import json
import random

class Lokalita:
    def __init__(self):
        self.bobri = [] 
        self.nory = [] 
        self.prirazeni = {}

    def nacti_bobry(self, file_path):
        with open(file_path, 'r') as f:
            self.bobri = json.load(f)

    def nacti_nory(self, file_path):
        with open(file_path, 'r') as f:
            self.nory = json.load(f)

    def prirad_nory(self):
        if len(self.bobri) > len(self.nory):
            raise ValueError("Neni dostatek nor pro vsechny bobry")
        random.shuffle(self.nory)
        for bobr in self.bobri:
            nora = self.nory.pop()
            self.prirazeni[bobr] = nora

    def __str__(self):
        result = "Prideleni:\n"
        for bobr, nora in self.prirazeni.items():
            result += f"{bobr} bydli v {nora}.\n"
        return result

bobri_data = ["bobr A", "bobr B", "bobr C", "bobr D"]
nory_data = ["nora 1", "nora 2", "nora 3", "nora 4"]

with open('bobri.json', 'w') as f:
    json.dump(bobri_data, f)

with open('nory.json', 'w') as f:
    json.dump(nory_data, f)

lokalita = Lokalita()

lokalita.nacti_bobry('bobri.json')
lokalita.nacti_nory('nory.json')

lokalita.prirad_nory()

print(lokalita)
