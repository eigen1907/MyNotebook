using System;
using System.Text;

namespace ExtensionMethod
{
    class Program
    {
        static void Main(string[] args)
        {
            string stringExample = "Hello String?";
            string a = stringExample.Reverse(6, 12);
            Console.WriteLine($"Before: {stringExample}, After: {a}");

        }
    }
}
