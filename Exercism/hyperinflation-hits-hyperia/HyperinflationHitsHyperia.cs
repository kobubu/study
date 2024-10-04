using System;

public static class CentralBank
{
    public static string DisplayDenomination(long @base, long multiplier)
    {
        try 
        {
        return checked(@base * multiplier).ToString();
        }
        catch 
        {
        return "*** Too Big ***";
        }
    }

    public static string DisplayGDP(float @base, float multiplier)
    {
        var product = @base * multiplier;
        
            return product != float.PositiveInfinity ? product.ToString() : "*** Too Big ***";
        
    }

    public static string DisplayChiefEconomistSalary(decimal salaryBase, decimal multiplier)
    {
        try
        {
            return checked(@salaryBase * multiplier).ToString();
        }
        catch (OverflowException e)
        {
            return "*** Much Too Big ***";
        }
    }
}
