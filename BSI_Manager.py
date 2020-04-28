import os, terminalColor, settingsJson, boto3
import SystemBSI

def BSISelector():
    listOfAllBSI = ["System BSI"]
    listOfBSIComments = ["\nThis is the base BSI, it is automatically installed with all other BSIs. It includes some helpful tools but nothing else."]
    listOfBSIChanges = ["\nChanges: Wallpaper"]
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
            elif( intDecision <= len(listOfAllBSI) ):#Has selected a BSI
                #Display info on selected BSI
                print("\n" + listOfAllBSI[intDecision-1] + listOfBSIComments[intDecision-1] + "\nInstalls: " + ', '.join(eval( str(listOfAllBSI[intDecision-1]).replace(" ","") + ".toDownload" )) + listOfBSIChanges[intDecision-1] )
                if not(listOfAllBSI[intDecision-1] == "System BSI"):
                    #Ask if wants to download BSI
                    print("\nDo You want to download this BSI?[Yes/No]")
                    userYesNo=str(input())
                    if(userYesNo.lower() == "yes") or (userYesNo.lower() == "y"):
                        if( not (listOfAllBSI[intDecision-1] in listOfSelectedBSI)): listOfSelectedBSI.append(listOfAllBSI[intDecision-1])
                    elif(userYesNo.lower() == "no") or (userYesNo.lower() == "n"):
                        if(listOfAllBSI[intDecision-1] in listOfSelectedBSI): listOfSelectedBSI.remove(listOfAllBSI[intDecision-1])
            elif( intDecision <= len(listOfCommands) + len(listOfAllBSI) ):#Has selected a command
                commandSelection = intDecision-1-len(listOfAllBSI)
                if( commandSelection == 0 ): #Install Selected
                    for i in listOfSelectedBSI:
                        exec(str(i.replace(" ","") + "()"))
                elif( commandSelection == 1 ): #Reset Selection
                    listOfSelectedBSI=["System BSI"]
                elif( commandSelection == 2 ): #Cancel
                    hasSelectedBSIs = True
        except:
            terminalColor.printRedString("Invalid Input")

def Settings():
    intDecision = 0
    settingsOptions = ["Update Software", "Cancel"]

    while ( ( (intDecision < 1) or (intDecision > len(settingsOptions)) ) ):
            try:
                print("\nWhat do you want to do?")
                for i in range( len(settingsOptions) ):
                    terminalColor.printBlueString( str(i+1) + ". " + settingsOptions[i] )
                intDecision = int(input())
                if ( (intDecision < 1) or (intDecision > len(settingsOptions)) ): terminalColor.printRedString("Invalid Input")
                elif ( settingsOptions[intDecision-1] == "Cancel"): break #Exit settings
                elif ( settingsOptions[intDecision-1] == "Set up a new computer"):
                    intDecision = 0   
                    BSISelector()
                else:
                    intDecision = 0    
            except:
                intDecision = 0
                terminalColor.printRedString("Invalid Input")

if __name__ == "__main__":
    print("BSI(Bash Script Installer) Manager\nMade By: Julian Lopez\nVersion: " + settingsJson.version)
    intDecision = 0
    listOfOptions = ["Set up a new computer","Settings","Exit"]

    while ( ( (intDecision < 1) or (intDecision > len(listOfOptions)) ) ):
            try:
                print("\nWhat do you want to do?")
                for i in range( len(listOfOptions) ):
                    terminalColor.printBlueString( str(i+1) + ". " + listOfOptions[i] )
                intDecision = int(input())
                if ( (intDecision < 1) or (intDecision > len(listOfOptions)) ): terminalColor.printRedString("Invalid Input")
                elif ( listOfOptions[intDecision-1] == "Exit"): break #Exit program
                elif ( listOfOptions[intDecision-1] == "Set up a new computer"):
                    intDecision = 0   
                    BSISelector()
                elif ( listOfOptions[intDecision-1] == "Settings"):
                    intDecision = 0   
                    Settings()
                else:
                    intDecision = 0    
            except:
                intDecision = 0
                terminalColor.printRedString("Invalid Input")