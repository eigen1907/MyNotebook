using System;

namespace OutParameter
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter \"true\" or \"false\":");
            string booleanstring = Console.ReadLine();

            bool b;
            if (bool.TryParse(booleanstring, out b))
            {
                Console.WriteLine($"Successfully parsed: {b}");
            }
            else
            {
                Console.WriteLine("Cannot be parsed to boolean");
            }

            Console.WriteLine("Enter an integer");
            string intString = Console.ReadLine();

            int number;
            if (int.TryParse(intString, out number))
            {
                Console.WriteLine($"Successfully parsed: {number}");
            }
            else
            {
                Console.WriteLine("Cannot be parsed to integer");
            }

            Console.WriteLine("what do you want random number bigger than this");
            string stringSomenumber = Console.ReadLine();
            int intSomeNumber = int.Parse(stringSomenumber);

            int randomNumber;
            if (TryGetIntegerGreaterThan(intSomeNumber, out randomNumber))
            {
                Console.WriteLine($"Great! {randomNumber} > {intSomeNumber}");
            }
            else
            {
                Console.WriteLine($"Failed to get an integer greater than {intSomeNumber}");
            }
        }

        static bool TryGetIntegerGreaterThan(int input, out int output)
        {
            var random = new Random();

            output = random.Next(0, 10);

            return output > input;
        }
    }
}
