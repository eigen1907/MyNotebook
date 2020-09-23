using System;
using System.Collections.Generic;
using System.Text;

namespace PartialClassPractice
{
    public partial class Robot
    {
        public void Nuke()
        {
            Console.WriteLine($"{Name}: Nuclear launched detected!");
        }
    }
}
