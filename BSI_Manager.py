import os, terminalColor, settingsJson, boto3

def SetupNewComputer():
    terminalColor.printRedString("\nunable to connect to FATIMA")
    terminalColor.printGreenString("Initiallizing System-BSI")
    os.system('sudo apt update')
    os.system('sudo apt upgrade')
    toDownload = ["aptitude", "snap", "lynx", "vim"]
    for i in toDownload:
        os.system('sudo apt install ' + i + " -y")

if __name__ == "__main__":
    print("BSI(Bash Script Installer) Manager\nMade By: Julian Lopez\nVersion: " + settingsJson.version)
    intDecision = 0
    listOfOptions = ["Set up a new computer","Browse Database","Exit"]

    while ( ( (intDecision < 1) or (intDecision > len(listOfOptions)) ) ):
            try:
                print("\nWhat do you want to do?")
                for i in range( len(listOfOptions) ):
                    terminalColor.printBlueString( str(i+1) + ". " + listOfOptions[i] )
                intDecision = int(input())
                if ( (intDecision < 1) or (intDecision > len(listOfOptions)) ): terminalColor.printRedString("Invalid Input")
                elif ( listOfOptions[intDecision-1] == "Exit"): break #Exit program
                elif ( listOfOptions[intDecision-1] == "Set up a new computer"):
                    SetupNewComputer()
                else:
                    intDecision = 0    
            except:
                intDecision = 0
                terminalColor.printRedString("Invalid Input")