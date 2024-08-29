using System;
using System.Globalization;

static class Appointment
{
    public static DateTime Schedule(string appointmentDateDescription) => DateTime.Parse(appointmentDateDescription);

    public static bool HasPassed(DateTime appointmentDate) => (appointmentDate < DateTime.Now);


    public static bool IsAfternoonAppointment(DateTime appointmentDate) => appointmentDate.Hour >=12 && appointmentDate.Hour <=17;


    public static string Description(DateTime appointmentDate) => $"You have an appointment on {appointmentDate}.";

    // => new DateTime(2023, 9, 15, 0, 0, 0)
    public static DateTime AnniversaryDate() => new DateTime(DateTime.Now.Year, 9, 15, 0, 0, 0); 

}
