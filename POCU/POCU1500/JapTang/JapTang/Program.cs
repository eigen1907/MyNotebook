using System;
using System.Collections.Generic;
using System.Runtime.ExceptionServices;
using System.Runtime.InteropServices;
using System.Threading.Tasks;

namespace JapTang
{
    class Program
    {
        static void Main(string[] args)
        {
            
        }
    }

    public static uint CalculateHash65599(string str)
    {
        uint hash = 0;

        for(int i = 0; i < str.Length; ++i)
        {
            hash = 65599 * hash + str[i];
        }

        return hash ^ (hash >> 16);
    }
}
