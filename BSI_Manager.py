#Made by Julian Lopez(JLO64)
import os, terminalColor, settingsJson, boto3, sys, json, datetime
from os import path

#
#   All of the functions/variables related to installing configuring computers (BSIs)
#

BSI_Directory = ""

#System BSI Variables
SystemBSItoDownloadAPT = ["aptitude", "snap", "lynx", "vim", "blueman", "vlc", "gparted", "htop"]
SystemBSItoDownloadSnap = []
SystemBSItoDownloadFireFoxExtensions = ["https://addons.mozilla.org/firefox/downloads/file/3551054/ublock_origin-1.26.2-an+fx.xpi", "https://addons.mozilla.org/firefox/downloads/file/3548609/firefox_multi_account_containers-6.2.5-fx.xpi"]
SystemBSItoDownloadAdditional = ["uBlock Origin"]
SystemBSIComments = "This is the System BSI, it is automatically installed with all other BSIs. It includes some helpful tools but nothing else."
SystemBSIChanges = "Changes: Wallpaper"

#Game BSI Variables
GameBSItoDownloadAPT = ["steam-installer", "supertuxkart", "gnome-chess", "gnome-mines", "aisleriot"]
GameBSItoDownloadSnap = []
GameBSItoDownloadAdditional = ["Powder Toy"]
GameBSIComments = "This is the Game BSI. It contains many games and distractions for a person to kill time with."
GameBSIChanges = "Changes: None"

#Wine BSI Variables
WineBSItoDownloadAPT = ["wine", "mono-complete", "playonlinux"]
WineBSItoDownloadSnap = []
WineBSItoDownloadAdditional = []
WineBSIComments = "This is the Wine BSI. Wine is a program that allows windows applications to be run on Linux systems."
WineBSIChanges = "Changes: Opens Wine automatically whenever an exe file is opened."

#Office BSI Variables
OfficeBSItoDownloadAPT = ["libreoffice", "ttf-mscorefonts-installer"]
OfficeBSItoDownloadSnap = []
OfficeBSItoDownloadAdditional = []
OfficeBSIComments = "This is the Office BSI. It contains many tools to help with productivity such as AN alternative to the Microsoft Office Suite."
OfficeBSIChanges = "Changes: Adds LibreOffice templates. Installs Microsoft fonts."

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
		#os.system('timeout 15s firefox /tmp/BSI_Manager/' + i.split("/")[-1])
		os.system('firefox /tmp/BSI_Manager/' + i.split("/")[-1])

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

	#download gecko dependencies
	os.system("sudo mdkir /usr/share/wine/gecko")
	os.system('sudo wget -P /usr/share/wine/gecko http://dl.winehq.org/wine/wine-gecko/2.47.1/wine-gecko-2.47.1-x86.msi')
	os.system('sudo wget -P /usr/share/wine/gecko http://dl.winehq.org/wine/wine-gecko/2.47.1/wine-gecko-2.47.1-x86_64.msi')

	#move the wine .desktop file
	os.system("sudo cp " + BSI_Directory + "/System_Files/wine.desktop /usr/share/applications")

	#set wine as the default for .exe
	os.system('sudo bash -c "echo application/x-ms-dos-executable=wine.desktop >> /usr/share/applications/defaults.list"')

def OfficeBSI():

	#Downloading sofware on computer via apt
	for i in OfficeBSItoDownloadAPT:
		terminalColor.printCyanString("\nInstalling: " + i )
		os.system('sudo apt install ' + i + " -y")    

	#moves template files into template folder
	os.system("sudo cp " + BSI_Directory + "*.od* " + os.path.expanduser('~') + "/Templates/")

def installSelectedBSIs(listOfSelectedBSI):
	#This is a placeholder for future internet features
	terminalColor.printRedString("\nunable to connect to BSI-Servers")

	writeInstalledBSIs(listOfSelectedBSI)

	#runs all BSIs in the list listOfSelectedBSI
	if not settingsJson.dummyBSIInstall:
		for i in listOfSelectedBSI:
			terminalColor.printGreenString("\nInitializing " + i +" BSI")
			exec(str(i + "BSI()" ))
	
	#Reminds user to apply all changes
	terminalColor.printRedString("\nPlease restart the computer to apply all changes made")
	os.system('sleep 5s')

def BSISelector():
	#Initializing variables
	listOfAllBSI = ["System", "Game", "Wine"]
	listOfCommands = ["Install Selected", "Reset Selection", "Cancel"]
	if "System" in settingsJson.installedBSIs: listOfSelectedBSI=[]
	else: listOfSelectedBSI=["System"]
	intDecision = 0
	hasSelectedBSIs = False

	while not hasSelectedBSIs:
		try:
			#Displays options for user to select
			print("\nWhat BSI(Bash Script Installer) packages do you want to install?")
			if settingsJson.dummyBSIInstall: terminalColor.printRedString("Dummy Install Mode is Active")
			for i in range( len(listOfAllBSI) ):
				if (listOfAllBSI[i] in settingsJson.installedBSIs ): terminalColor.printYellowString( str(i+1) + ". " + listOfAllBSI[i] + " BSI(v" + str(settingsJson.installedBSIVersions[i]) + " already installed on " + str(settingsJson.datesOfInstalls[i]) + ")" )
				elif (listOfAllBSI[i] in listOfSelectedBSI ): terminalColor.printGreenRegString( str(i+1) + ". " + listOfAllBSI[i] + " BSI" )                
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
				if not(listOfAllBSI[intDecision-1] == "System") and not(listOfAllBSI[intDecision-1] in settingsJson.installedBSIs) :
					
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
						installSelectedBSIs(listOfSelectedBSI)
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
	settingsOptions = ["Update Software", "Change Color Mode", "Developer Options", "Main Menu"]

	while ( ( (intDecision < 1) or (intDecision > len(settingsOptions)) ) ):
			try:
				#Display options
				print("\nWhat do you want to do?")
				for i in range( len(settingsOptions) ):
					terminalColor.printBlueString( str(i+1) + ". " + settingsOptions[i] )
				
				#get user input
				intDecision = int(input())

				if ( (intDecision < 1) or (intDecision > len(settingsOptions)) ): terminalColor.printRedString("Invalid Input")
				elif ( settingsOptions[intDecision-1] == "Main Menu"): writeSettings() #Exit settings
				elif ( settingsOptions[intDecision-1] == "Change Color Mode"):
					intDecision = 0
					if settingsJson.colorMode:
						print("\nCurrently Color Mode is ON\nDo you want to turn it off?[Yes/No]")
						userYesNo=str(input())
						if(userYesNo.lower() == "yes") or (userYesNo.lower() == "y"): settingsJson.colorMode = False
					else:
						print("\nCurrently Color Mode is OFF\nDo you want to turn it on?[Yes/No]")
						userYesNo=str(input())
						if(userYesNo.lower() == "yes") or (userYesNo.lower() == "y"): settingsJson.colorMode = True
				elif ( settingsOptions[intDecision-1] == "Update BSI-Manager"):
					intDecision = 0   
					os.system( path.dirname(__file__) + '/BSI-Installer.sh')
					sys.exit()
				elif ( settingsOptions[intDecision-1] == "Developer Options"):
					intDecision = 0   
					developerOptions()
				else:
					intDecision = 0    
			except Exception as e:
				if e == SystemExit: sys.exit()
				intDecision = 0
				terminalColor.printRedString("Invalid Input")

def developerOptions():
	intDecision = 0
	devSettingsOptions = ["Dummy BSI Install Mode", "Delete BSI Install Data", "Exit"]

	while ( ( (intDecision < 1) or (intDecision > len(devSettingsOptions)) ) ):
			try:
				#Display options
				terminalColor.printRedString("\nWarning: these settings are not meant for regular users, they are mostly for testing purposes")
				print("What do you want to do?")
				for i in range( len(devSettingsOptions) ):
					terminalColor.printBlueString( str(i+1) + ". " + devSettingsOptions[i] )
				
				#get user input
				intDecision = int(input())

				if ( (intDecision < 1) or (intDecision > len(devSettingsOptions)) ): terminalColor.printRedString("Invalid Input")
				elif ( devSettingsOptions[intDecision-1] == "Exit"): pass
				elif ( devSettingsOptions[intDecision-1] == "Dummy BSI Install Mode"):
					intDecision = 0   
					terminalColor.printRedString("if enabled when installing a BSI nothing is downloaded/installed")
					if settingsJson.dummyBSIInstall:
						print("Currently this option is ENABLED. Do you want to disable it?[Yes/No]")
						userYesNo=str(input())
						if(userYesNo.lower() == "yes") or (userYesNo.lower() == "y"): settingsJson.dummyBSIInstall = False
					else: 
						print("Currently this option is DISABLED. Do you want to enable it?[Yes/No]")
						userYesNo=str(input())
						if(userYesNo.lower() == "yes") or (userYesNo.lower() == "y"): settingsJson.dummyBSIInstall = True
				elif ( devSettingsOptions[intDecision-1] == "Delete BSI Install Data"):
					terminalColor.printRedString("if you Delete your BSI Install Data you will not be able to tell what BSIs have been installed onto your computer")
					print("Are you absolutely certain you want to delete this data?[Yes/No]")
					userYesNo=str(input())
					if(userYesNo.lower() == "yes") or (userYesNo.lower() == "y"):
						try: os.remove(os.path.expanduser('~') + "/.BSI/computerInfo")
						except: pass
				else:
					intDecision = 0
			except:
				intDecision = 0
				terminalColor.printRedString("Invalid Input")

def checkForDirectory(programPath): #checks for "programPath" directory and creates it if not found
	if not os.path.exists(programPath):
		os.system('mkdir ' + programPath)
	return programPath

def writeInstalledBSIs(selectedBSIs):
	checkForDirectory(os.path.expanduser('~') + "/.BSI" )
	for i in selectedBSIs:
		settingsJson.installedBSIs.append(i)
		settingsJson.installedBSIVersions.append(settingsJson.version)
		settingsJson.datesOfInstalls.append(str(datetime.date.today()) )
	data = {}
	data["installedBSIs"] = settingsJson.installedBSIs
	data["installedBSIVersions"] = settingsJson.installedBSIVersions
	data["datesOfInstalls"] = settingsJson.datesOfInstalls
	writeJSONFile(data, os.path.expanduser('~') + "/.BSI/computerInfo")

def checkForFile(filePath): #checks for "filePath" file and returns boolean
	if os.path.exists(filePath):
		return True
	else: return False

def readInstalledBSIs():
	if checkForFile(os.path.expanduser('~') + "/.BSI/computerInfo"):
		BSIjsonData = readJSONFile(os.path.expanduser('~') + "/.BSI/computerInfo")
		settingsJson.installedBSIs = BSIjsonData["installedBSIs"]
		settingsJson.installedBSIVersions = BSIjsonData["installedBSIVersions"]
		settingsJson.datesOfInstalls = BSIjsonData["datesOfInstalls"]
	else:
		pass

def readJSONFile(fileLoc):
	if checkForFile(fileLoc):
		with open(fileLoc) as json_file:
			data = json.load(json_file)
			return data
	else:
		return {}

def writeJSONFile(data, filePath):
	with open(filePath, 'w') as outfile:
		json.dump(data, outfile)

def initializeSettings():
	if checkForFile(os.path.expanduser('~') + "/.BSI/settings"):
		settingsFile = readJSONFile(os.path.expanduser('~') + "/.BSI/settings")
		settingsJson.colorMode = settingsFile["colorMode"]
		settingsJson.dummyBSIInstall = settingsFile["dummyBSIInstall"]
	else: pass

def writeSettings():
	data = {}
	data["colorMode"] = settingsJson.colorMode
	data["dummyBSIInstall"] = settingsJson.dummyBSIInstall
	writeJSONFile(data, os.path.expanduser('~') + "/.BSI/settings")

	#
#   The function that runs first when the program is run
#

if __name__ == "__main__":
	BSI_Directory = os.path.dirname(os.path.realpath(__file__))
	checkForDirectory('mkdir /tmp/BSI_Manager')
	readInstalledBSIs()
	initializeSettings()

	print("BBB   SSS  III")
	print("B  B  S     I")
	print("BBB   SSS   I")
	print("B  B    S   I")
	print("BBB   SSS  III")

	print("\nBSI(Bash Script Installer) Manager\nMade By: Julian Lopez\nVersion: " + str(settingsJson.version) + settingsJson.versionName )
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