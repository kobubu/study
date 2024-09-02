using System;


public static class SimpleCalculator
{
    public static string Calculate(int operand1, int operand2, string operation) => operation switch
    {
        "+" => $"{operand1} + {operand2} = {operand1 + operand2}",
        "*" => $"{operand1} * {operand2} = {operand1 * operand2}",
        "/" => operand2 != 0 ? $"{operand1} / {operand2} = {operand1 / operand2}" : "Division by zero is not allowed.",
        "" => throw new ArgumentException(),
        null => throw new ArgumentNullException(),
        _ => throw new ArgumentOutOfRangeException()
    };
}
