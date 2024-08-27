using System;
using System.Linq;

class BirdCount
{
    private int[] birdsPerDay;

    public BirdCount(int[] birdsPerDay)
    {
        this.birdsPerDay = birdsPerDay;
    }

    public static int[] LastWeek()
    {
        return new int[] { 0, 2, 5, 3, 7, 8, 4 };
    }

    public int Today()
    {
        return birdsPerDay.Last();
    }

    public void IncrementTodaysCount()
    {
        {

            int[] newArray = birdsPerDay[^birdsPerDay.First()..^1];
            birdsPerDay[^1]++;
        }
    }

    public bool HasDayWithoutBirds() => birdsPerDay.Contains(0);

    public int CountForFirstDays(int numberOfDays) => birdsPerDay.Take(numberOfDays).Sum();

    public int BusyDays() => birdsPerDay.Count(day => day >= 5);
    //{
    //    var count = 0;
    //    for (int i=0; i<birdsPerDay.Length; i++) 
    //    {
    //        if (birdsPerDay[i] >= 5)
    //        {
    //            count++;
    //        }
    //    }
    //    return count;
    //}
}
