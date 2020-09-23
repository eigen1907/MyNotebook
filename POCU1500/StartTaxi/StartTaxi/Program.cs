using System;
using System.Threading;

namespace StartTaxi
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Put N that size of map(N, N)");
            int activeRange = int.Parse(Console.ReadLine());
            Console.WriteLine("Put M that number of passenger");
            int passengerCount = int.Parse(Console.ReadLine());
            Console.WriteLine("Put initial fuel mount");
            int reservedFuel = int.Parse(Console.ReadLine());

            int[,] map = new int[activeRange, activeRange];

            Console.WriteLine($"Map: ({activeRange} X {activeRange}), Panssenger: {passengerCount}, Fuel: {reservedFuel}L");
            Console.WriteLine("---------------------------------------------------------------");

            for (int i = 0; i < activeRange; i++)
            {
                for (int j = 0; j < activeRange; j++)
                {
                    map[i, j] = 0;
                }
            }

            Console.WriteLine("where is the walls?");
            while (true)
            {
                Console.WriteLine("put wall's row");
                int row = int.Parse(Console.ReadLine()) - 1;
                Console.WriteLine("put wall's column");
                int column = int.Parse(Console.ReadLine()) - 1;
                map[row, column] = 1;
                Console.WriteLine("Do you know other wall?  (Y, N)");
                string answer = Console.ReadLine();
                if (answer == "N")
                {
                    break;
                }
            }

            Console.WriteLine("Map has this shape! (empty space: 0, wall space: 1)");
            for (int i = 0; i < activeRange; i++)
            {
                for (int j = 0; j < activeRange; j++)
                {
                    Console.Write($"{map[i, j]}");
                }
                Console.WriteLine();
            }

            Console.WriteLine("---------------------------------------------------------------");

            Console.WriteLine("Where is the taxi driver? Put row");
            int driverRow = int.Parse(Console.ReadLine()) - 1;
            Console.WriteLine("Put column");
            int driverColumn = int.Parse(Console.ReadLine()) - 1;

            int[] passengerOriginRow = new int[passengerCount];
            int[] passengerOriginColumn = new int[passengerCount];
            int[] passengerDestinationRow = new int[passengerCount];
            int[] passengerDestinationColumn = new int[passengerCount];

            for (int i = 0; i < passengerCount; i++)
            { 
                Console.WriteLine($"Put passenger{i + 1}'s origin");
                Console.Write("Row: ");
                passengerOriginRow[i] = int.Parse(Console.ReadLine()) - 1;
                Console.Write("Column: ");
                passengerOriginColumn[i] = int.Parse(Console.ReadLine()) - 1;
                Console.WriteLine($"Put passenger{i + 1}'s destination");
                Console.Write("Row: ");
                passengerDestinationRow[i] = int.Parse(Console.ReadLine()) - 1;
                Console.Write("Column: ");
                passengerDestinationColumn[i] = int.Parse(Console.ReadLine()) - 1;
            }

            Console.WriteLine($"Taxi driver's Location: ({driverRow}, {driverColumn})");
            for (int i = 0; i < passengerCount; i++)
            {
                Console.WriteLine($"Passenger{i + 1}'s Origin: ({passengerOriginRow[i]}, {passengerOriginColumn[i]}), Destination: ({passengerDestinationRow[i]}, {passengerDestinationColumn[i]})");
            }
            Console.WriteLine("---------------------------------------------------------------");

        }
        int CalculateValue(int[] start, int[,] map, Move[] moves)
        {
            int[] location = start;
            int value = 0;
            foreach(Move move in moves)
            {
                switch (move)
                {
                    case Move.Up:
                        location[0] += 1;
                        if (map[location[0], location[1]] == 1)
                        {
                            value += 5000;
                        }
                        else
                        {
                            value += 1;
                        }
                        break;
                    case Move.Down:
                        location[0] -= 1;
                        if (map[location[0], location[1]] == 1)
                        {
                            value += 5000;
                        }
                        else
                        {
                            value += 1;
                        }
                        break;
                    case Move.Left:
                        location[1] -= 1;
                        if (map[location[0], location[1]] == 1)
                        {
                            value += 5000;
                        }
                        else
                        {
                            value += 1;
                        }
                        break;
                    case Move.Right:
                        location[1] += 1;
                        if (map[location[0], location[1]] == 1)
                        {
                            value += 5000;
                        }
                        else
                        {
                            value += 1;
                        }
                        break;
                }
            }
            return value;
        }

        Move[] FindPath(int[] start, int[] end)
        {

        }
    }
}
