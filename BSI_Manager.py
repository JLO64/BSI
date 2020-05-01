#Made by Julian Lopez(JLO64)
import os, terminalColor, settingsJson, boto3, sys
from os import path

#https://starcatcher.us/TPT/Download/Snapshot%20linux64.zip


#
#   All of the functions/variables related to installing configuring computers
#

SystemBSItoDownloadAPT = ["aptitude", "snap", "lynx", "vim", "blueman"]

def SystemBSI():
    terminalColor.printCyanString("Initializing System-BSI")
    
    #Upgrading sofware on computer via apt
    terminalColor.printCyanString("\nUpgrading software via apt") 
    os.system('sudo apt update')
    os.system('sudo apt upgrade -y')
    os.system('sudo apt autoremove -y')

    #Downloading sofware on computer via apt
    for i in SystemBSItoDownloadAPT:
        terminalColor.printCyanString("\nInstalling: " + i )
        os.system('sudo apt install ' + i + " -y")

    #Upgrading sofware on computer via snap
    terminalColor.printCyanString("\nUpgrading software via snap")
    os.system('sudo snap refresh')

    #Changes wallpaper
    terminalColor.printCyanString("\nChanging default wallpaper")
    folderLocation = path.dirname(__file__)
    os.system('sudo cp ' + folderLocation + '/System_Files/System-BSI_v1.png /usr/share/lubuntu/wallpapers/lubuntu-default-wallpaper.png')

def downloadSelectedBSIs(listOfSelectedBSI):
    #This is a placeholder for future internet features
    terminalColor.printRedString("\nunable to connect to BSI-Servers")

    #runs all BSIs in the list listOfSelectedBSI
    for i in listOfSelectedBSI:
        exec(str(i.replace(" ","") + "()" ))
    
    #Reminds user to apply all changes
    terminalColor.printCyanString("\nPlease restart the computer to apply all changes made")
    os.system('sleep 5s')

def BSISelector():
    #Initializing variables
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
                print("\n" + listOfAllBSI[intDecision-1] + listOfBSIComments[intDecision-1] + "\nInstalls: " + ', '.join(eval( str(listOfAllBSI[intDecision-1]).replace(" ","") + "toDownloadAPT" )) + listOfBSIChanges[intDecision-1] )
                if not(listOfAllBSI[intDecision-1] == "System BSI"):
                    
                    #Ask if wants to download BSI
                    print("\nDo You want to download this BSI?[Yes/No]")
                    userYesNo=str(input())
                    if(userYesNo.lower() == "yes") or (userYesNo.lower() == "y"):
                        if( not (listOfAllBSI[intDecision-1] in listOfSelectedBSI)): listOfSelectedBSI.append(listOfAllBSI[intDecision-1])
                    elif(userYesNo.lower() == "no") or (userYesNo.lower() == "n"):
                        if(listOfAllBSI[intDecision-1] in listOfSelectedBSI): listOfSelectedBSI.remove(listOfAllBSI[intDecision-1])
            elif( intDecision <= len(listOfCommands) + len(listOfAllBSI) ):
                commandSelection = intDecision-1-len(listOfAllBSI)

                #Install Selected BSIs
                if( commandSelection == 0 ):
                    downloadSelectedBSIs(listOfSelectedBSI)
                    hasSelectedBSIs = True
                #Reset Selection
                elif( commandSelection == 1 ):
                    listOfSelectedBSI=["System BSI"]
                
                #Cancel
                elif( commandSelection == 2 ):
                    hasSelectedBSIs = True
        except:
            terminalColor.printRedString("Invalid Input")

#
#   All of the functions related to application settings
#
def Settings():
    intDecision = 0
    settingsOptions = ["Update Software", "Cancel"]

    while ( ( (intDecision < 1) or (intDecision > len(settingsOptions)) ) ):
            try:
                #Display options
                print("\nWhat do you want to do?")
                for i in range( len(settingsOptions) ):
                    terminalColor.printBlueString( str(i+1) + ". " + settingsOptions[i] )
                
                #get user input
                intDecision = int(input())

                if ( (intDecision < 1) or (intDecision > len(settingsOptions)) ): terminalColor.printRedString("Invalid Input")
                elif ( settingsOptions[intDecision-1] == "Cancel"): break #Exit settings
                elif ( settingsOptions[intDecision-1] == "Update BSI-Manager"):
                    intDecision = 0   
                    os.system( path.dirname(__file__) + '/BSI-Installer.sh')
                    sys.exit()
                else:
                    intDecision = 0    
            except Exception as e:
                if e == SystemExit: sys.exit()
                intDecision = 0
                terminalColor.printRedString("Invalid Input")

#
#   The function that runs first when the program is run
#
if __name__ == "__main__":
    print("\nBSI(Bash Script Installer) Manager\nMade By: Julian Lopez\nVersion: " + settingsJson.version)
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
            except Exception as e:
                if e == SystemExit: sys.exit()
                intDecision = 0
                terminalColor.printRedString("Invalid Input")