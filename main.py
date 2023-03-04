import Maths
import Area_of_Shapes
import Volume_of_Shapes
import Conversion
import inspect


modules = [
    Maths,
    Conversion,
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

    def formatParam(paramName, parameters, param):
        if paramName == '':
            parameters[0].append(param)
        else:
            parameters[1][paramName] = param
        return parameters

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

    function = getInput(function, functions, "Choose which function you want to call: ")

    params = [str(param) for param in inspect.signature(functions[function-1]).parameters.values()]

    print("--PARAMETERS--")
    positional = []
    keyword = {}
    parameters = [positional, keyword]
    for param in params:
        if '=' in param:
            paramName = param.split('=')[0]
        else:
            paramName = ''

        while True:
            param = input(f"{param}: ")
            if param.lstrip('-').isdigit():
                parameters = formatParam(paramName, parameters, int(param))
                break
            elif param.isnumeric():
                parameters = formatParam(paramName, parameters, float(param))
                break
            elif param.lower() == 'true':
                parameters = formatParam(paramName, parameters, True)
                break
            elif param.lower() == 'false':
                parameters = formatParam(paramName, parameters, False)
                break
            elif param == '':
                if not paramName == '':
                    break
                else:
                    print("Don't leave me empty. Try again.")
            elif param.startswith('[') and param.endswith(']'):
                if ', ' in param:
                    parameters = formatParam(paramName, parameters, param[1:-1].split(', '))
                    break
                elif ',' in param:
                    parameters = formatParam(paramName, parameters, param[1:-1].split(','))
                    break
                elif ' ' in param:
                    parameters = formatParam(paramName, parameters, param[1:-1].split(' '))
                    break
                else:
                    print("Invalid list. Try again.")
            else:
                parameters = formatParam(paramName, parameters, param)
                break

    print(f"\nRunning {functions[function-1].__name__}")

    functions[function-1](*parameters[0], **parameters[1])


if __name__ == '__main__':
    main()
