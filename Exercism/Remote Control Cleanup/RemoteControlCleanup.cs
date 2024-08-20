public class RemoteControlCar
{
    public string CurrentSponsor { get; private set; }
    private Speed currentSpeed;
    public CTelemetry Telemetry;
    public RemoteControlCar() => Telemetry = new RemoteControlCar.CTelemetry(this);
    public string GetSpeed() => currentSpeed.ToString();
    private void SetSponsor(string sponsorName) => CurrentSponsor = sponsorName;
    private void SetSpeed(Speed speed) => currentSpeed = speed;
    public class CTelemetry
    {
        private RemoteControlCar parent;
        public CTelemetry(RemoteControlCar parent) => this.parent = parent;
        public void Calibrate() { }
        public bool SelfTest() => true;
        public void ShowSponsor(string sponsorName) => parent.SetSponsor(sponsorName);
        public void SetSpeed(decimal amount, string unitsString)
        {
            SpeedUnits speedUnits = (unitsString == "cps")
                ? SpeedUnits.CentimetersPerSecond
                : SpeedUnits.MetersPerSecond;
            parent.SetSpeed(new Speed(amount, speedUnits));
        }
    }
    enum SpeedUnits { MetersPerSecond, CentimetersPerSecond }
    struct Speed
    {
        public decimal Amount { get; }
        public SpeedUnits SpeedUnits { get; }
        public Speed(decimal amount, SpeedUnits speedUnits) => (this.Amount, this.SpeedUnits) = (amount, speedUnits);
        public override string ToString() => (SpeedUnits == SpeedUnits.CentimetersPerSecond)
            ? $"{Amount} centimeters per second"
            : $"{Amount} meters per second";
    }
}