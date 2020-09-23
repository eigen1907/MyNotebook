using System;
using System.Collections.Generic;
using System.Xml;

namespace DictionaryCollectionPractice
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> list = new List<int>();

            Random random = new Random();

            for (int i = 0; i < 20; i++)
            {
                int number = random.Next(0, 10);
                list.Add(number);
            }

            Console.WriteLine($"[ {string.Join(", ", list)} ]");

            Dictionary<int, bool> dictionary = new Dictionary<int, bool>();

            for (int i = 0; i < list.Count; i++)
            {
                if (dictionary.ContainsKey(list[i]))
                {
                    list.Remove(list[i]);
                }
                else
                {
                    dictionary.Add(list[i], true);
                }
            }

            Console.WriteLine($"[ {string.Join(", ", list)} ]");

            int index = 0;
            foreach (KeyValuePair<int, bool> a in dictionary)
            {
                index++;
                Console.WriteLine($"Key : {a.Key}, Value: {a.Value}, Index: {index}");
            }

        }
    }
}


