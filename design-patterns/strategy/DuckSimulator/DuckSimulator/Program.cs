using System;

namespace DuckSimulator
{
    class Program
    {
        static void Main(string[] args)
        {
            Duck mallardDuck = new MallardDuck();
            mallardDuck.Display();
            mallardDuck.Swim();
            mallardDuck.PerformMakeSound();
            mallardDuck.PerformFly();
            
            Console.WriteLine("----------------------------");
            
            Duck rubberDuck = new RubberDuck();
            rubberDuck.Display();
            rubberDuck.Swim();
            rubberDuck.PerformMakeSound();
            rubberDuck.PerformFly();

            Console.ReadLine();
        }
    }
}