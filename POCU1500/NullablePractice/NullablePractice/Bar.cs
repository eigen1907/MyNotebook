using System;
using System.Collections.Generic;
using System.Text;

namespace NullablePractice
{
    public struct Bar
    {
        public Bar(int number)
        {
            Number = number;
        }
        
        public int Number { get; private set; }
    }
}
