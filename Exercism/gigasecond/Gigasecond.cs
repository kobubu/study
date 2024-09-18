using System;

public static class Gigasecond
{
    const double GIGASECOND = 1E9;
    //Your task is to determine the date and time one gigasecond after a certain date.
    public static DateTime Add(DateTime birthday) => birthday.AddSeconds(GIGASECOND);
}