﻿using System;
using System.Transactions;

namespace EnumPractice
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("num1: ");
            string num1String = Console.ReadLine();
            int num1 = int.Parse(num1String);

            Console.Write("num2: ");
            string num2String = Console.ReadLine();
            int num2 = int.Parse(num2String);

            Console.Write("operation (+, -, *, /, %): ");
            string operationString = Console.ReadLine();
            char operationChar = operationString[0];

            EOperator operation = (EOperator)operationChar;


            switch (operation)
            {
                case EOperator.Plus:
                    Console.WriteLine($"{num1} + {num2} = {num1 + num2}");
                    break;
                case EOperator.Minus:
                    Console.WriteLine($"{num1} - {num2} = {num1 - num2}");
                    break;
                case EOperator.Multiply:
                    Console.WriteLine($"{num1} * {num2} = {num1 * num2}");
                    break;
                case EOperator.Divide:
                    Console.WriteLine($"{num1} / {num2} = {num1 / num2}");
                    break;
                case EOperator.Mod:
                    Console.WriteLine($"{num1} % {num2} = {num1 % num2}");
                    break;
                default: Console.WriteLine($"You entered wrong operator {operationChar}");
                    break;
            }

        }
    }
}
