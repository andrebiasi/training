using System;

namespace DuckSimulator
{
    public class Quack : IMakeSoundBehaviour
    {
        public void MakeSound()
        {
            Console.WriteLine("Quack");
        }
    }
}