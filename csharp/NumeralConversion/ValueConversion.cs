﻿using System;

Console.WriteLine("---Value Conversion---");

List<string> dataTypes = new() { "Binary", "Hexadecimal", "Denary" };
string dataType = dataTypes[displayChoices("Input datatype: ", dataTypes) - 1];

Console.Write("Value: ");
string? value = Console.ReadLine();
int output;

if (dataType == "Binary")
{
    output = binaryToDenary(value);
}
else if (dataType == "Hexadecimal")
{
    output = hexToDenary(value);
}
else
{
    output = Convert.ToInt32(value);
}

Console.WriteLine($"\nOutput: {output}");
preventConsoleClose();


static int charToInt(char character) {
    return Convert.ToInt32(Convert.ToString(character));
}


static int binaryToDenary(string input)
{
    char[] binary = input.ToCharArray();
    binary.Reverse();
    int multiplier = 1;
    int value = 0;

    for (var i = 0; i < binary.Length; i++)
    {
        value += charToInt(binary[i]) * multiplier;
        multiplier *= 2;
    }

    return value;
}


static int hexToDenary(string input)
{
    var hexDict = new Dictionary<string, int>
    {
        { "0", 0 },
        { "1", 1 },
        { "2", 2 },
        { "3", 3 },
        { "4", 4 },
        { "5", 5 },
        { "6", 6 },
        { "7", 7 },
        { "8", 8 },
        { "9", 9 },
        { "A", 10 },
        { "B", 11 },
        { "C", 12 },
        { "D", 13 },
        { "E", 14 },
        { "F", 15 }
    };

    char[] hex = input.ToCharArray();
    Array.Reverse(hex);
    int multiplier = 1;
    int value = 0;

    for (var i = 0; i < hex.Length; i++)
    {
        value += hexDict[Convert.ToString(hex[i])] * multiplier;
        multiplier *= 16;
    }


    return value;
}


static int displayChoices(string question, List<string> dataTypes)
{
    for (var i = 0; i < dataTypes.Count; i++)
    {
        Console.WriteLine($"{i+1}) {dataTypes[i]}");
    }

    Console.Write(question);
    string? userInput = Console.ReadLine();

    while (true)
    {
        if (!double.TryParse(userInput, out _) || Convert.ToInt32(userInput) < 1 || Convert.ToInt32(userInput) > dataTypes.Count) 
        {
            Console.WriteLine($"Input has to be a number 1-{dataTypes.Count}\n");
            Console.Write(question);
            userInput = Console.ReadLine();
            continue;
        } 
        else 
        {
            Console.WriteLine();
            Console.WriteLine($"You chose {dataTypes[Convert.ToInt32(userInput) - 1]}");
            return Convert.ToInt32(userInput);
        }
    }
}

static void preventConsoleClose()
{
    Console.ReadLine();
}