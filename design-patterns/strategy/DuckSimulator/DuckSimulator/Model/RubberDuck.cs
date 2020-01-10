using System;

namespace DuckSimulator
{
    public class RubberDuck : Duck
    {
        public RubberDuck()
        {
            _flyBehaviour = new FlyNoWay();
            _makeSound = new Squeak();
        }
        
        public override void Display()
        {
            Console.WriteLine("I'm a rubber duck");
        }
    }
}