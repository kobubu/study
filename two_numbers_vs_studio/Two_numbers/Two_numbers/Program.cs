/*Задачка: Следующее число больше a и b и делится на b

Даны два числа a и b. Создайте функцию, которая возвращает следующее число, большее a и b и кратное b.
Примеры:
DivisibleByB(17, 8) ➞ 24
DivisibleByB(98, 3) ➞ 99
DivisibleByB(14, 11) ➞ 22s

Пишите ваши варианты в комментариях. Ответ будет в канале сегодня вечером.*/

namespace Two_Numbers;
internal class Program
{ 

    static void Main(string[] args)
    {
        Console.WriteLine(DivisibleByB(17, 8));
        Console.WriteLine(DivisibleByB(98, 3));
        Console.WriteLine(DivisibleByB(14, 11));
    }

    // private static int DivisibleByB(int a, int b) => b > a ? b * 2: b * 2 > a ? b * 2: DivisibleByB(a, b + 1);

    private static int DivisibleByB(int a, int b)
    {

        int number = a > b ? a + 1 : b + 1;

        while(true)
        {
            if (number % b == 0)
            {
                return number;
            }
            else
            { 
                number++;
            }
        }
    }
}
