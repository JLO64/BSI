import os, terminalColor, settingsJson, boto3

def SetupNewComputer():
    terminalColor.printCyanString("Initializing System-BSI")
    terminalColor.printRedString("\nunable to connect to BSI-Servers") #This is a placeholder for future internet features
    
    terminalColor.printCyanString("Upgrading software") #Upgrading sofware on computer via apt
    os.system('sudo apt update')
    os.system('sudo apt upgrade -y')
    os.system('sudo apt autoremove -y')
    terminalColor.printGreenString("Software upgrading complete")

    toDownload = ["aptitude", "snap", "lynx", "vim"]#Downloading sofware on computer via apt
    for i in toDownload:
        terminalColor.printCyanString("Downloading: " + i )
        os.system('sudo apt install ' + i + " -y")

    os.system('sudo reboot') #Reboots system to apply changes made

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