﻿using System;

namespace ClassPractice
{
    class Program
    {
        static void Main(string[] args)
        {
            Warrior warrior = new Warrior("Chuck");

            warrior.Introduce();
            warrior.GetStatus();

            warrior.SwordStrike();
            warrior.UseWhirlwind();
            warrior.UseWhirlwind();
            warrior.UseWhirlwind();
            warrior.Rest();

            warrior.GetStatus();
            warrior.Health -= 200;

            warrior.GetStatus();
        }
    }
}
