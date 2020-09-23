using System;
using System.Collections.Generic;

namespace ListCollectionPractice
{
    class Program
    {
        static void Main(string[] args)
        {
            const int ELEMENT_COUNT = 10;

            List<int> list = new List<int>();
            for (int i = 0; i < ELEMENT_COUNT; i++)
            {
                list.Add(i);
            }
            Console.WriteLine($"[ {string.Join(", ", list)} ]");

            List<int> list2 = new List<int> { 1, 2, 3, 4, 5, 6 };

            Console.WriteLine($"[ {string.Join(", ", list2)} ]");

            Console.WriteLine($"First element is {list[0]}");
            Console.WriteLine($"Last element is {list[list.Count - 1]}");

            list.Insert(2, 2);

            Console.WriteLine($"[ {string.Join(", ", list)} ]");

            list.Remove(2);

            Console.WriteLine($"[ {string.Join(", ", list)} ]");

            bool bContains5 = list.Contains(5);

            Console.WriteLine($"Is list contains 5?: {bContains5}");

            bool bContains10 = list.Contains(10);

            Console.WriteLine($"Is list contains 10?: {bContains10}");

            int sum = 0;
            for (int i = 0; i < list.Count; i++)
            {
                sum += list[i];
            }

            Console.WriteLine($"Sum of list is : {sum}");
        }
    }
}
