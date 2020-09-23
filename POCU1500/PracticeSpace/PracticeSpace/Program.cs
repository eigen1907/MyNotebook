using System;

namespace PracticeSpace
{
    class Program
    {
        static void Main(string[] args)
        {
            int num;
            Console.WriteLine(int.TryParse(Console.ReadLine(), out num));
        }
    }
}
