using System;

namespace DuckSimulator
{
    public abstract class Duck
    {
        protected IFlyBehaviour _flyBehaviour;
        protected IMakeSoundBehaviour _makeSound;
        
        public Duck()
        {
        }

        public void PerformFly()
        {
            _flyBehaviour.Fly();
        }

        public void PerformMakeSound()
        {
            _makeSound.MakeSound();
        }
        
        public void Swim()
        {
            Console.WriteLine("I'm swimming... All ducks float");
        }
        
        public abstract void Display();
    }
}