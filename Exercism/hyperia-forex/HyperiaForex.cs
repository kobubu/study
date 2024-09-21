using System;
public struct CurrencyAmount : IEquatable<CurrencyAmount>, IComparable<CurrencyAmount>
{
    private decimal _amount;
    private string _currency;

    public decimal Amount
    {
        get { return _amount; }
        set { _amount = value; }
    }

    public string Currency
    {
        get { return _currency; }
        set { _currency = value; }
    }


    public CurrencyAmount(decimal amount, string currency)
    {
        _amount = amount;
        _currency = currency;
    }

    public static bool operator ==(CurrencyAmount lhs, CurrencyAmount rhs) => lhs.Equals(rhs);
    public static bool operator !=(CurrencyAmount lhs, CurrencyAmount rhs) => !(lhs == rhs);

    public static bool operator >(CurrencyAmount lhs, CurrencyAmount rhs) => IsDifCurrency(lhs, rhs)? throw new ArgumentException() :
        lhs.Amount > rhs.Amount ? true : false;
    public static bool operator <(CurrencyAmount lhs, CurrencyAmount rhs) => IsDifCurrency(lhs, rhs) ? throw new ArgumentException() :
    lhs.Amount < rhs.Amount ? true : false;

    public static CurrencyAmount operator -(CurrencyAmount lhs, CurrencyAmount rhs) => IsDifCurrency(lhs, rhs) ? throw new ArgumentException() :
        new() { Currency = lhs.Currency, Amount = lhs.Amount - rhs.Amount };

    public static CurrencyAmount operator +(CurrencyAmount lhs, CurrencyAmount rhs) => IsDifCurrency(lhs, rhs) ? throw new ArgumentException() :
    new() { Currency = lhs.Currency, Amount = lhs.Amount + rhs.Amount };

    public static CurrencyAmount operator /(CurrencyAmount currencyAmount, decimal divisor) =>
     new(currencyAmount.Amount / divisor, currencyAmount.Currency);

    public static CurrencyAmount operator *(CurrencyAmount currencyAmount, decimal multiplier) =>
       new CurrencyAmount(currencyAmount.Amount * multiplier, currencyAmount.Currency);

    public static explicit operator double(CurrencyAmount currencyAmount) => (double)currencyAmount.Amount;
    public static implicit operator decimal(CurrencyAmount currencyAmount) => currencyAmount.Amount;

    public bool Equals(CurrencyAmount other)
    {
        if (_currency != other._currency)
            throw new ArgumentException();
        return CompareTo(other) == 0;
    }

    public int CompareTo(CurrencyAmount other)
    {
        if (_currency != other._currency)
            throw new ArgumentException();
        if (_amount == other._amount)
            return 0;
        if (_amount > other._amount)
            return 1;
        return -1;
    }

    private static bool IsDifCurrency(CurrencyAmount lhs, CurrencyAmount rhs) => lhs.Currency != rhs.Currency;
}
