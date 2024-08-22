using System;

static class QuestLogic
{
    //Implement the (static) QuestLogic.CanFastAttack() method that takes a boolean value that indicates if the knight is awake.
    //This method returns true if a fast attack can be made based on the state of the knight. Otherwise, returns false:
    public static bool CanFastAttack(bool knightIsAwake)
    {
        if (knightIsAwake)
        {
            return false;
        }
        else
        {
            return true;
        }
    }

    public static bool CanSpy(bool knightIsAwake, bool archerIsAwake, bool prisonerIsAwake)
    {
        if (knightIsAwake || archerIsAwake || prisonerIsAwake)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    public static bool CanSignalPrisoner(bool archerIsAwake, bool prisonerIsAwake)
    {
        if (!archerIsAwake && prisonerIsAwake)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    //If Annalyn has her pet dog with her she can rescue the prisoner if the archer is asleep.
    //The knight is scared of the dog and the archer will not have time to get ready before Annalyn and the prisoner can escape.
    public static bool CanFreePrisoner(bool knightIsAwake, bool archerIsAwake, bool prisonerIsAwake, bool petDogIsPresent)
    {
        if (!archerIsAwake && petDogIsPresent)
        {
            return true;
        }
        else if (!knightIsAwake && !archerIsAwake && prisonerIsAwake && !petDogIsPresent)
        {
            return true;
        }
        else
        { 
            return false; 
        }
    }
}
