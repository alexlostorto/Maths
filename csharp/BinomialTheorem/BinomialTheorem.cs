Console.OutputEncoding = System.Text.Encoding.Unicode;
Console.WriteLine("---Binomial Theorem---");
Console.WriteLine("Equation is in the form (x + y)ⁿ");

Console.Write("n: ");
int n = Convert.ToInt32(Console.ReadLine());

List<int> pascalRow = pascal(n);
string equation = expand(pascalRow);
Console.WriteLine($"\nExpansion: {equation}");

preventConsoleClose();


static string expand(List<int> row)
{
    List<string> equation = new() { };
    const string superscript = "⁰¹²³⁴⁵⁶⁷⁸⁹";

    for (int i = 0; i < row.Count; i++)
    {   
        string expression = "";
        char xExponent = superscript[row.Count - i - 1];
        char yExponent = superscript[i];

        if (row[i] != 1)
        {
            expression += row[i];
        }

        if (row.Count - i - 1 == 1)
        {
            expression += "x";
        } else if (row.Count - i > 1)
        {
            expression += "x" + xExponent;
        }

        if (i == 1)
        {
            expression += "y";
        }
        else if (i > 1)
        {
            expression += "y" + yExponent;
        }

        equation.Add(expression);
    }

    return String.Join(" + ", equation.ToArray());
}

static List<int> pascal(int rowNumber)
{
    List<int> row = new() { };
    List<int> tempRow = new() { };

    for (int i = 0; i < rowNumber; i++)
    {
        tempRow.Clear();

        for (int l = 0; l < (row.Count - 1); l++)
        {
            tempRow.Add(row[l] + row[l + 1]);
        }

        row = tempRow.ToList();
        row.Insert(0, 1);
        row.Add(1);
    }

    return row;
}

static void preventConsoleClose()
{
    Console.ReadLine();
}
