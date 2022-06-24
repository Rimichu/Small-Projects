using System;

namespace Console_Program
{
    class Program
    {
        static void Main(string[] args)
        {   
            int difficulty = 1;
            Random randint = new Random();
            int ans;
            int num1;
            int num2;
            int sign;
            char[] signs = {'+','-','*','/'};
            bool wrong = false;

            Console.WriteLine("Quick Tip, When dividing, give your answer to the nearest whole number :)");

            while (true){
                num1 = randint.Next(1,difficulty);
                num2 = randint.Next(1,difficulty);
                sign = randint.Next(signs.Length);
                Console.WriteLine("{0} {1} {2}", num1, signs[sign], num2);
                try{
                ans = Convert.ToInt16(Console.ReadLine());
                } 
                catch (Exception e){
                    Console.WriteLine("Please enter a number");
                    continue;
                }
                switch(sign){
                    case 0:
                        if (ans == (num1 + num2)){
                            Console.WriteLine("Correct, difficulty is now {0}", difficulty+1);
                            difficulty += 1;                 
                        } else {
                            wrong = true;
                        }
                        break;
                    case 1:
                        if (ans == (num1 - num2)){
                            Console.WriteLine("Correct, difficulty is now {0}", difficulty+1);
                            difficulty += 1;
                        } else {
                            wrong = true;
                        }
                        break;
                    case 2:
                        if (ans == (num1 * num2)){
                            Console.WriteLine("Correct, difficulty is now {0}", difficulty+1);
                            difficulty += 1;
                        } else {
                            wrong = true;
                        }
                        break;
                    case 3:
                        if (ans == Decimal.Round(num1 / num2)){
                            Console.WriteLine("Correct, difficulty is now {0}", difficulty+1);
                            difficulty += 1;
                        } else {
                            wrong = true;
                        }
                        break;
                }
                if (wrong == true){
                    break;
                }
            }

            Console.WriteLine("final difficulty was {0}", difficulty);
            

            Console.ReadKey();
        }
    }
}