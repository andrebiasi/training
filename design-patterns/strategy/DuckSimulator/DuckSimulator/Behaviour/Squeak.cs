using System;

namespace DuckSimulator
{
    public class Squeak : IMakeSoundBehaviour
    {
        public void MakeSound()
        {
            Console.WriteLine("Squeak");
        }
    }
}