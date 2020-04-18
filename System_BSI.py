import os, terminalColor
try:
    import boto3
except:
    os.system('pip3 install boto3')
    import boto3

print("SYSTEM BSI\nMade By: Julian Lopez\nVersion: Origin")
intDecision = 0
listOfOptions = ["Set up a new computer", "Exit"]

while ( ( (intDecision < 1) or (intDecision > len(listOfOptions)) ) ):
        try:
            print("\nWhat do you want to do?")
            for i in range( len(listOfOptions) ):
                terminalColor.printBlueString( str(i+1) + ". " + listOfOptions[i] )
            intDecision = int(input())
            if ( (intDecision < 1) or (intDecision > len(listOfOptions)) ): terminalColor.printRedString("Invalid Input")
            elif ( listOfOptions[intDecision-1] == "Exit"): break #Exit program
            else:
                intDecision = 0    
        except:
            intDecision = 0
            terminalColor.printRedString("Invalid Input")