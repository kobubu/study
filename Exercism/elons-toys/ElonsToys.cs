using System;
class RemoteControlCar
{
    int _charge;
    int _distance;

    public RemoteControlCar()
    {
        _charge = 100;
        _distance = 0;
    }
    public static RemoteControlCar Buy() => new();

    //method to return the distance as displayed on the LED display:
    public string DistanceDisplay()
    {
        return $"Driven {_distance} meters";
    }

    public string BatteryDisplay() =>
    _charge == 0 ? "Battery empty" : $"Battery at {_charge}%";

    public void Drive()
    {
        if (_charge <= 0) return;
        _charge--;
        _distance += 20;
    }
}


