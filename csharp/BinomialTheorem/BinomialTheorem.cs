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
    string equation = "";
    string superscript = "⁰¹²³⁴⁵⁶⁷⁸⁹";

    for (int i = 0; i < row.Count; i++)
    {
        equation += " + " + row[i] + "x" + superscript[row.Count - i - 1] + "y" + superscript[i];
    }

    return equation;
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
