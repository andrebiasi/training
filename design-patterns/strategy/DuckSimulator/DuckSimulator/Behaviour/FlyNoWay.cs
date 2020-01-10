using System;

namespace DuckSimulator
{
    public class FlyNoWay : IFlyBehaviour
    {
        public void Fly()
        {
            Console.WriteLine("I cannot fly");
        }
    }
}