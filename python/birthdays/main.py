import random
import time
from file import File
from graph import Graph


class Birthdays:
    def __init__(self):
        self.numPeople = 0
        self.trials = 0
        self.matches = 0
        self.countRepeats = False
        self.graph = Graph()
        self.file = File()
        self.saveLocation = 0
        self.file.validate()
        self.menu()

    def menu(self):
        while True:
            try:
                print()
                print("1. Create Simulation")
                print("2. Load Simulation")
                print("3. Display Data")
                print("9. Exit")
                
                choice = input("Choose an option: ")
                match choice:
                    case '1':
                        self.load(*self.file.createSimulation())
                    case '2':
                        self.load(*self.file.loadSimulation())
                    case '3':
                        self.file.display()
                    case '9':
                        print("\nGoodbye!")
                        exit()
                    case _:
                        print("Invalid choice. Please try again.")
            except KeyboardInterrupt:
                print("\n\nExiting gracefully...")
                exit()

    def load(self, saveLocation, data):
        self.saveLocation = saveLocation
        self.numPeople = data.get('numPeople')
        self.trials = data.get('trials')
        self.matches = data.get('matches')
        self.countRepeats = data.get('countRepeats')
        self.simulate()
    
    def simulate(self):
        print("\nSimulating...\n")
        startTime = time.time()
        timeCounter = 0
        try:
            while True:
                people = [random.randint(1, 365) for _ in range(self.numPeople)]
                uniquePeople = set(people)
                
                self.trials += 1
                if self.countRepeats:
                    self.matches += len(people) - len(uniquePeople)
                elif len(people) != len(uniquePeople):
                    self.matches += 1

                currentTime = time.time()

                if currentTime - startTime >= timeCounter * 5:
                    print(f"{self.matches} matches out of {self.trials} trials.")
                    timeCounter += 1
        except KeyboardInterrupt:
            print("\nSimulation interrupted. Saving data...")
            self.file.save({'numPeople': self.numPeople, 'trials': self.trials, 'matches': self.matches, 'countRepeats': self.countRepeats}, self.saveLocation)
            print("Data saved. Goodbye!")
            exit()


def main():
    Birthdays()


if __name__ == '__main__':
    main()