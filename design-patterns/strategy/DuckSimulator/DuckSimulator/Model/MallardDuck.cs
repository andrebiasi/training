using System;

namespace DuckSimulator
{
    public class MallardDuck : Duck
    {
        public MallardDuck()
        {
            _flyBehaviour = new FlyWithWings();
            _makeSound = new Quack();
        }
        
        public override void Display()
        {
            Console.WriteLine("I'm a MallardDuck");
        }
    }
}