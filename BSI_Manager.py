import os, terminalColor, settingsJson, boto3

def BSISelector():
    listOfAllBSI = ["System BSI"]
    listOfBSIComments = ["\nThis is the base BSI, it is automatically installed with all other BSIs. It includes some helpful tools but nothing else.\nInstalls: aptitude, snap, lynx, vim\nChanges: Wallpaper"]
    listOfCommands = ["Install Selected", "Reset Selection", "Cancel"]
    listOfSelectedBSI=["System BSI"]
    intDecision = 0
    hasSelectedBSIs = False
    while not hasSelectedBSIs:
        try:
            #Displays options for user to select
            print("\nWhat BSI(Bash Script Installer) packages do you want to install?")
            for i in range( len(listOfAllBSI) ):
                if (listOfAllBSI[i] in listOfSelectedBSI ): terminalColor.printGreenRegString( str(i+1) + ". " + listOfAllBSI[i] )
                else: terminalColor.printBlueString( str(i+1) + ". " + listOfAllBSI[i] )
            for i in range( len(listOfCommands) ):
                terminalColor.printBlueString( str(i+1+len(listOfAllBSI) ) + ". " + listOfCommands[i] )
            #get user input
            intDecision = int(input())
            #find out what what user wanted
            if ( (intDecision < 1) or (intDecision > (len(listOfOptions) + len(listOfAllBSI) + 1 ) ) ): terminalColor.printRedString("Invalid Input")
            elif( intDecision <= len(listOfAllBSI) ):
                #Display info on selected BSI
                print("\n" + listOfAllBSI[intDecision-1] + listOfBSIComments[intDecision-1] )
                if not(listOfAllBSI[intDecision-1] == "System BSI"):
                    #Ask if wants to download BSI
                    print("\nDo You want to download this BSI?[Yes/No]")
                    userYesNo=str(input())
                    if(userYesNo.lower() == "yes") or (userYesNo.lower() == "y"):
                        if( not (listOfAllBSI[intDecision-1] in listOfSelectedBSI)):
                            listOfSelectedBSI.append(listOfAllBSI[intDecision-1])
                    elif(userYesNo.lower() == "no") or (userYesNo.lower() == "n"):
                        print(listOfAllBSI[intDecision-1])
                        if(listOfAllBSI[intDecision-1] in listOfSelectedBSI): listOfSelectedBSI.remove(listOfAllBSI[intDecision-1])
            elif( intDecision <= len(listOfCommands) ): print(listOfCommands[intDecision-1-len(listOfAllBSI)])
        except:
            terminalColor.printRedString("Invalid Input")

def SystemBSI():
    terminalColor.printCyanString("Initializing System-BSI")
    terminalColor.printRedString("\nunable to connect to BSI-Servers") #This is a placeholder for future internet features
    
    terminalColor.printCyanString("\nUpgrading software") #Upgrading sofware on computer via apt
    os.system('sudo apt update')
    os.system('sudo apt upgrade -y')
    os.system('sudo apt autoremove -y')

    toDownload = ["aptitude", "snap", "lynx", "vim"]#Downloading sofware on computer via apt
    for i in toDownload:
        terminalColor.printCyanString("\nDownloading: " + i )
        os.system('sudo apt install ' + i + " -y")

    #Changes wallpaper
    terminalColor.printCyanString("\nChanging default wallpaper")
    os.system('sudo cp /usr/lib/BSI-Manager/System_Files/System-BSI_v1.png /usr/share/lubuntu/wallpapers/lubuntu-default-wallpaper.png')

    terminalColor.printCyanString("\nPlease restart the computer to apply all changes made")
    os.system('sleep 10s')


if __name__ == "__main__":
    print("BSI(Bash Script Installer) Manager\nMade By: Julian Lopez\nVersion: " + settingsJson.version)
    intDecision = 0
    listOfOptions = ["Set up a new computer","Browse Database","Settings","Exit"]

    while ( ( (intDecision < 1) or (intDecision > len(listOfOptions)) ) ):
            try:
                print("\nWhat do you want to do?")
                for i in range( len(listOfOptions) ):
                    terminalColor.printBlueString( str(i+1) + ". " + listOfOptions[i] )
                intDecision = int(input())
                if ( (intDecision < 1) or (intDecision > len(listOfOptions)) ): terminalColor.printRedString("Invalid Input")
                elif ( listOfOptions[intDecision-1] == "Exit"): break #Exit program
                elif ( listOfOptions[intDecision-1] == "Set up a new computer"): BSISelector()
                else:
                    intDecision = 0    
            except:
                intDecision = 0
                terminalColor.printRedString("Invalid Input")