﻿using System;
using System.Collections.Generic;
using System.Text;

namespace ValueTypeVSReferenceType
{
    public class Vector
    {
        public Vector(int x, int y)
        {
            X = x;
            Y = y;
        }

        public int X { get; set; }

        public int Y { get; set; }
    }
}
