using System;
using System.Collections.Generic;

namespace taller_2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Buenos dias!");
            Console.WriteLine(" ");

            HashSet<double> conjuntoA = new HashSet<double>();


            for (int i = 1; i < 30; i++)
            {
                conjuntoA.Add(i);
            }

            Console.WriteLine(" ");

            HashSet<double> conjuntoB = new HashSet<double>();


            for (int i = 1; i <= 25; i++)
            {
                if (i % 2 == 0)
                {
                    conjuntoB.Add(i);
                }

            }

            Console.WriteLine(" ");

            HashSet<double> conjuntoC = new HashSet<double>();

            conjuntoC.Add(0);
            conjuntoC.Add(3);
            conjuntoC.Add(6);
            conjuntoC.Add(9);
            conjuntoC.Add(12);
            conjuntoC.Add(15);
            conjuntoC.Add(18);
            conjuntoC.Add(20);

            Console.WriteLine(" ");

            HashSet<double> conjuntoD = new HashSet<double>();

            conjuntoD.Add(2);
            conjuntoD.Add(3);
            conjuntoD.Add(5);
            conjuntoD.Add(7);
            conjuntoD.Add(11);
            conjuntoD.Add(13);
            conjuntoD.Add(17);
            conjuntoD.Add(19);
            conjuntoD.Add(23);
            conjuntoD.Add(29);
            conjuntoD.Add(31);
            conjuntoD.Add(37);
            conjuntoD.Add(41);
            conjuntoD.Add(43);


            Console.WriteLine(" ");
            HashSet<double> conjuntoZ = new HashSet<double>();
            HashSet<double> conjuntoY = new HashSet<double>();
           
            conjuntoZ = difSim((inter(conjuntoA, conjuntoB)), conjuntoC);
            resultado(conjuntoZ);
            Console.WriteLine("--------------");

            conjuntoY = dif((union(conjuntoA, conjuntoC)), conjuntoB);
            resultado(conjuntoY);
            Console.WriteLine("--------------");

            conjuntoZ = union((difSim(conjuntoC, conjuntoD)), conjuntoA);
            resultado(conjuntoZ);
            conjuntoZ.Clear();
        }
        static HashSet<double> union(HashSet<double> a, HashSet<double> b)
        {
            HashSet<double> c = new HashSet<double>(a);
            c.UnionWith(b);
            return c;
        }
        static HashSet<double> inter(HashSet<double> a, HashSet<double> b)
        {
            HashSet<double> c = new HashSet<double>(a);
            c.IntersectWith(b);
            return c;
        }
        static HashSet<double> dif(HashSet<double> a, HashSet<double> b)
        {
            HashSet<double> c = new HashSet<double>(a);
            c.ExceptWith(b);
            return c;
        }
        static HashSet<double> difSim(HashSet<double> a, HashSet<double> b)
        {
            HashSet<double> c = new HashSet<double>(a);
            c.SymmetricExceptWith(b);
            return c;
        }
        static void resultado(HashSet<double> a)
        {
            foreach (double x in a)
            {
                Console.Write(" " + x + " ");
            }
            Console.WriteLine();
        }

    }
}