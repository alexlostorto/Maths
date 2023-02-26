import Maths
import Area_of_Shapes
import Volume_of_Shapes
import inspect


modules = [
    Maths,
    Area_of_Shapes,
    Volume_of_Shapes
]


def main():
    def getInput(userInput, array, question):
        while True:
            # check input is acceptable
            if not userInput.isdigit() or int(userInput) < 1 or int(userInput) > len(array):
                print(f"Input has to be a number 1-{len(array)}")
                userInput = input(question)
                continue
            else:
                # chooses file
                userInput = int(userInput)
                print(f"You chose '{array[userInput-1].__name__}'\n")
                return userInput

    # Choose modules
    for i in range(len(modules)):
        print(f"{i+1}) {modules[i].__name__}")
    module = input("Choose which module you want to use: ")
    print()

    module = getInput(module, modules, "Choose which module you want to use: ")

    # Choose function
    functions = modules[module-1].__all__
    for i in range(len(functions)):
        print(f"{i+1}) {functions[i].__name__}")
    function = input("Choose which function you would like to call: ")
    print()

    function = getInput(function, functions,
                        "Choose which function you want to call: ")

    params = [str(param) for param in inspect.signature(
        functions[function-1]).parameters.values()]

    print("--PARAMETERS--")
    for index, param in enumerate(params):
        param = input(f"{param}: ")
        if param.isdigit():
            params[index] = int(param)
            print(f"{param} is an integer")
        elif param.isnumeric():
            params[index] = float(param)
            print(f"{param} is a float")
        else:
            params[index] = param

    print(f"\nRunning {functions[function-1].__name__}")

    functions[function-1](*params)


if __name__ == '__main__':
    main()
