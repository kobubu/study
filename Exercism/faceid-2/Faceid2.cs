using System;
using System.Collections.Generic;
public class FacialFeatures
{
    public string EyeColor { get; }
    public decimal PhiltrumWidth { get; }
    public FacialFeatures(string eyeColor, decimal philtrumWidth) =>
        (this.EyeColor, this.PhiltrumWidth) =
        (eyeColor, philtrumWidth);
    public override bool Equals(Object obj) =>
        ReferenceEquals(this, obj) ||
        Equals(obj as FacialFeatures);
    public bool Equals(FacialFeatures other) =>
        other != null &&
        this.EyeColor == other.EyeColor &&
        this.PhiltrumWidth == other.PhiltrumWidth;
    public override int GetHashCode() =>
        HashCode.Combine(this.EyeColor, this.PhiltrumWidth);
}
public class Identity
{
    public string Email { get; }
    public FacialFeatures FacialFeatures { get; }
    public Identity(string email, FacialFeatures facialFeatures) =>
        (this.Email, this.FacialFeatures) = (email, facialFeatures);
    public override bool Equals(Object obj) =>
        ReferenceEquals(this, obj) ||
        Equals(obj as Identity);

    public bool Equals(Identity other) =>
        other != null &&
        this.Email.Equals(other.Email) &&
        this.FacialFeatures.Equals(other.FacialFeatures);
    public override int GetHashCode() =>
        HashCode.Combine(this.Email, this.FacialFeatures);
}
public class Authenticator
{
    private HashSet<Identity> _registeredIdentities = new();

    public static bool AreSameFace(FacialFeatures faceA, FacialFeatures faceB) =>
        faceA.Equals(faceB);

    public bool IsAdmin(Identity identity) =>
        identity.Equals(_admin);

    public bool Register(Identity identity) =>
        !IsRegistered(identity) &&
        _registeredIdentities.Add(identity);

    public bool IsRegistered(Identity identity) =>
        _registeredIdentities.Contains(identity);

    public static bool AreSameObject(Identity identityA, Identity identityB) =>
        ReferenceEquals(identityA, identityB);

    #region Fixed values
    private static readonly Identity _admin = new Identity("admin@exerc.ism", new FacialFeatures("green", 0.9m));
    #endregion

}