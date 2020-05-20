#Made by Julian Lopez(JLO64)
import os, terminalColor, settingsJson, boto3, sys
from os import path

#
#   All of the functions/variables related to installing configuring computers (BSIs)
#

BSI_Directory = ""

#System BSI Variables
SystemBSItoDownloadAPT = ["aptitude", "snap", "lynx", "vim", "blueman", "vlc", "gparted", "htop"]
SystemBSItoDownloadSnap = []
SystemBSItoDownloadFireFoxExtensions = ["https://addons.mozilla.org/firefox/downloads/file/3551054/ublock_origin-1.26.2-an+fx.xpi"]
SystemBSItoDownloadAdditional = ["uBlock Origin"]
SystemBSIComments = "This is the System BSI, it is automatically installed with all other BSIs. It includes some helpful tools but nothing else."
SystemBSIChanges = "Changes: Wallpaper"

#Game BSI Variables
GameBSItoDownloadAPT = ["steam-installer", "supertuxkart", "gnome-chess", "gnome-mines", "aisleriot"]
GameBSItoDownloadSnap = []
GameBSItoDownloadAdditional = ["Powder Toy"]
GameBSIComments = "This is the Game BSI. It contains many games and distractions for a person to please themselves with."
GameBSIChanges = "Changes: None"

#Wine BSI Variables
#https://blog.dexterhaslem.com/getting-wine-3-0-working-on-ubuntu-18-04
#https://forum.winehq.org/viewtopic.php?t=16162
#play on linux
WineBSItoDownloadAPT = ["wine", "mono-complete"]
WineBSItoDownloadSnap = []
WineBSItoDownloadAdditional = []
WineBSIComments = "This is the Wine BSI. Wine is a program that allows windows applications to be run on Linux systems."
WineBSIChanges = "Changes: Opens Wine automatically whenever an exe file is opened."

def SystemBSI():
    
    #Upgrading sofware on computer via apt
    terminalColor.printCyanString("\nUpgrading software via apt") 
    os.system('sudo apt update')
    os.system('sudo apt upgrade -y')
    os.system('sudo apt autoremove -y')
    os.system('sudo /usr/bin/lubuntu-upgrader --full-upgrade')

    #Downloading sofware on computer via apt
    for i in SystemBSItoDownloadAPT:
        terminalColor.printCyanString("\nInstalling: " + i )
        os.system('sudo apt install ' + i + " -y")

    #Upgrading sofware on computer via snap
    terminalColor.printCyanString("\nUpgrading software via snap")
    os.system('sudo snap refresh')

    terminalColor.printCyanString("\nInstalling Firefox extensions")
    #Installs Firefox Extensions
    for i in SystemBSItoDownloadFireFoxExtensions:
        os.system('sudo wget -P /tmp/BSI_Manager ' + i)
        os.system('timeout 15s firefox /tmp/BSI_Manager/' + i.split("/")[-1])

    #Changes wallpaper
    terminalColor.printCyanString("\nChanging default wallpaper")
    folderLocation = path.dirname(__file__)
    os.system('sudo cp ' + folderLocation + '/System_Files/System-BSI_v1.png /usr/share/lubuntu/wallpapers/lubuntu-default-wallpaper.png')

def GameBSI():

    #Downloading sofware on computer via apt
    for i in GameBSItoDownloadAPT:
        terminalColor.printCyanString("\nInstalling: " + i )
        os.system('sudo apt install ' + i + " -y")

    #Downloading Installing Powder Toy
    #os.system('sudo mkdir /usr/lib/PowderToy')
    os.system("sudo wget -O /tmp/BSI_Manager/PowderToy.zip https://starcatcher.us/TPT/Download/Snapshot%20linux64.zip ")
    os.system("sudo unzip /tmp/BSI_Manager/PowderToy.zip -d /usr/lib/PowderToy")
    os.system("timeout 1s /usr/lib/PowderToy/powder64")

    #move Powder Toy desktop file
    os.system("sudo cp " + BSI_Directory + "/System_Files/powdertoy.desktop /usr/share/applications" )
    
    #move Powder Toy icon
    os.system("sudo cp " + BSI_Directory + "/System_Files/powdertoy.desktop /usr/share/icons/hicolor/48x48/apps/powdertoy.png" )

def WineBSI():

    #Downloading sofware on computer via apt
    for i in WineBSItoDownloadAPT:
        terminalColor.printCyanString("\nInstalling: " + i )
        os.system('sudo apt install ' + i + " -y")    

    #move the wine .desktop file
    os.system("sudo cp " + BSI_Directory + "/System_Files/wine.desktop /usr/share/applications")

    #set wine as the default for .exe
    os.system('sudo bash -c "echo application/x-ms-dos-executable=wine.desktop >> /usr/share/applications/defaults.list"')

def downloadSelectedBSIs(listOfSelectedBSI):
    #This is a placeholder for future internet features
    terminalColor.printRedString("\nunable to connect to BSI-Servers")

    #runs all BSIs in the list listOfSelectedBSI
    for i in listOfSelectedBSI:
        terminalColor.printGreenString("\nInitializing " + i +" BSI")
        exec(str(i + "BSI()" ))
    
    #Reminds user to apply all changes
    terminalColor.printCyanString("\nPlease restart the computer to apply all changes made")
    os.system('sleep 5s')

def BSISelector():
    #Initializing variables
    listOfAllBSI = ["System", "Game", "Wine"]
    listOfCommands = ["Install Selected", "Reset Selection", "Cancel"]
    listOfSelectedBSI=["System"]
    intDecision = 0
    hasSelectedBSIs = False

    while not hasSelectedBSIs:
        try:
            #Displays options for user to select
            print("\nWhat BSI(Bash Script Installer) packages do you want to install?")
            for i in range( len(listOfAllBSI) ):
                if (listOfAllBSI[i] in listOfSelectedBSI ): terminalColor.printGreenRegString( str(i+1) + ". " + listOfAllBSI[i] + " BSI" )
                else: terminalColor.printBlueString( str(i+1) + ". " + listOfAllBSI[i] + " BSI" )
            for i in range( len(listOfCommands) ):
                terminalColor.printBlueString( str(i+1+len(listOfAllBSI) ) + ". " + listOfCommands[i])
            
            #get user input
            intDecision = int(input())
            
            #find out what what user wanted
            if ( (intDecision < 1) or (intDecision > (len(listOfOptions) + len(listOfAllBSI) + 1 ) ) ): terminalColor.printRedString("Invalid Input")
            elif( intDecision <= len(listOfAllBSI) ):#Has selected a BSI
                
                #Display info on selected BSI
                CurrentBSI = listOfAllBSI[intDecision-1] + "BSI"
                print("\n" + listOfAllBSI[intDecision-1] + " BSI" ) #Name of BSI
                print(eval( listOfAllBSI[intDecision-1] + "BSIComments" ) ) #BSI comments
                CurrentBSIComments = "Installs: "
                BSIDownloadSources = ["toDownloadAPT", "toDownloadSnap", "toDownloadAdditional"]
                for i in BSIDownloadSources:
                    currentDownloadList = eval( CurrentBSI + i) 
                    if len(currentDownloadList) > 0 and CurrentBSIComments == "Installs: " : CurrentBSIComments = CurrentBSIComments + ', '.join(currentDownloadList)
                    elif len(currentDownloadList) > 0: CurrentBSIComments = CurrentBSIComments + ", " + ', '.join(currentDownloadList)
                print( CurrentBSIComments ) #BSI downloads
                print(eval( listOfAllBSI[intDecision-1] + "BSIChanges" ) ) #BSI Changes
                if not(listOfAllBSI[intDecision-1] == "System"):
                    
                    #Ask if wants to download BSI
                    print("\nDo You want to install this BSI onto this computer?[Yes/No]")
                    userYesNo=str(input())
                    if(userYesNo.lower() == "yes") or (userYesNo.lower() == "y"):
                        if( not (listOfAllBSI[intDecision-1] in listOfSelectedBSI)): listOfSelectedBSI.append(listOfAllBSI[intDecision-1])
                    elif(userYesNo.lower() == "no") or (userYesNo.lower() == "n"):
                        if(listOfAllBSI[intDecision-1] in listOfSelectedBSI): listOfSelectedBSI.remove(listOfAllBSI[intDecision-1])
            elif( intDecision <= len(listOfCommands) + len(listOfAllBSI) ):
                commandSelection = intDecision-1-len(listOfAllBSI)

                #Install Selected BSIs
                if( commandSelection == 0 ):
                    print("\nDo You want to install these BSIs onto this computer?[Yes/No]")
                    for i in listOfSelectedBSI: terminalColor.printGreenRegString(i + " BSI")
                    userYesNo=str(input())
                    if(userYesNo.lower() == "yes") or (userYesNo.lower() == "y"):
                        downloadSelectedBSIs(listOfSelectedBSI)
                        hasSelectedBSIs = True
                #Reset Selection
                elif( commandSelection == 1 ):
                    listOfSelectedBSI=["System"]
                
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
    BSI_Directory = os.path.dirname(os.path.realpath(__file__))
    os.system('mkdir /tmp/BSI_Manager')
    print("BBB   SSS  III")
    print("B  B  S     I")
    print("BBB   SSS   I")
    print("B  B    S   I")
    print("BBB   SSS  III")

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