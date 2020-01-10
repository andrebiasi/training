using System;

namespace DuckSimulator
{
    public class FlyWithWings : IFlyBehaviour
    {
        public void Fly()
        {
            Console.WriteLine("I'm flying");
        }
        
    }
}