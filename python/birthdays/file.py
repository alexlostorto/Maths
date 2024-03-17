import json
import random


class File:
    def __init__(self):
        self.path = 'data.json'
        self.table = Table()

    def create(self):
        with open(self.path, 'w') as file:
            data = [{'numPeople': random.randint(1, 100), 'trials': 0, 'matches': 0, 'countRepeats': False}]
            file.seek(0)
            json.dump(data, file, indent=4)

    def validate(self):
        try:
            with open(self.path, 'r+') as file:
                data = json.load(file)
                if len(data) == 0:
                    print("Data file is empty. Formatting file...")
                    self.create()
        except FileNotFoundError:
            print("Data file not found. Creating new file...")
            self.create()
        except IOError:
            print("Error reading or writing to the file!")
            exit()
        except Exception as e:
            print("Data file is corrupted. Formatting file...")
            self.create()

    def createSimulation(self):
        with open (self.path, 'r+') as file:
            while True:
                try:
                    numPeople = int(input("\nNumber of people: "))
                    if numPeople <= 1:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter a number greater than 1.")

            while True:
                try:
                    countRepeats = input("Count repeats (y/n): ")
                    if countRepeats.lower() in ['y', 'yes']:
                        countRepeats = True
                    elif countRepeats.lower() in ['n', 'no']:
                        countRepeats = False
                    else:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter y, yes, n, or no.")

            print("Creating new simulation...")
            data = json.load(file)
            data.append({'numPeople': numPeople, 'trials': 0, 'matches': 0, 'countRepeats': countRepeats})
            file.seek(0)
            json.dump(data, file, indent=4)
        
        return len(data) - 1, {'numPeople': numPeople, 'trials': 0, 'matches': 0, 'countRepeats': countRepeats}
    
    def loadSimulation(self):
        print()
        with open (self.path, 'r') as file:
            data = json.load(file)
            for i, simulation in enumerate(data):
                print(f"{i+1}) {simulation.get('numPeople')} people, {simulation.get('trials')} trials, {simulation.get('matches')} matches, count repeats: {simulation.get('countRepeats')}")

            while True:
                try:
                    saveLocation = int(input("Enter the number of the simulation you want to load: ")) - 1
                    if (saveLocation < 0) or (saveLocation >= len(data)):
                        raise ValueError
                    break
                except ValueError:
                    print(f"\nInvalid input. Please enter a number between 1 and {len(data)} inclusive.")
        print("\nLoading simulation...")

        return saveLocation, data[saveLocation]

    def display(self):
        table = [['No.', 'Num People', 'Trials', 'Probability', 'Count Repeats']]      
        with open (self.path, 'r') as file:
            data = json.load(file)          
            for i, simulation in enumerate(data):
                probability = round(simulation.get('matches') / simulation.get('trials') if simulation.get('trials') != 0 else 0, 5)
                table.append([i+1, simulation.get('numPeople'), simulation.get('trials'), probability, simulation.get('countRepeats')])
            print()
            self.table.print(table)

    def save(self, data, saveLocation: int):
        with open (self.path, 'r+') as file:
            jsonData = json.load(file)
            if len(jsonData) == 0:
                print("Data file is empty. Formatting file...")
                self.createFile()
            else:
                jsonData[saveLocation] = data
                file.seek(0)
                json.dump(jsonData, file, indent=4)


class Table:
    def print(self, table):
        column_widths = [max(len(str(item)) for item in column) for column in zip(*table)]
        for row in table:
            print(" | ".join(str(item).ljust(width) for item, width in zip(row, column_widths)))