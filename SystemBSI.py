import os, terminalColor, settingsJson
from os import path

toDownloadAPT = ["aptitude", "snap", "lynx", "vim", "blueman"]

def SystemBSI():
    terminalColor.printCyanString("Initializing System-BSI")
    
    #This is a placeholder for future internet features
    terminalColor.printRedString("\nunable to connect to BSI-Servers")
    
    #Upgrading sofware on computer via apt
    terminalColor.printCyanString("\nUpgrading software via apt") 
    os.system('sudo apt update')
    os.system('sudo apt upgrade -y')
    os.system('sudo apt autoremove -y')

    #Downloading sofware on computer via apt
    for i in toDownloadAPT:
        terminalColor.printCyanString("\nInstalling: " + i )
        os.system('sudo apt install ' + i + " -y")

    #Upgrading sofware on computer via snap
    terminalColor.printCyanString("\nUpgrading software via snap")
    os.system('sudo snap refresh')

    #Changes wallpaper
    terminalColor.printCyanString("\nChanging default wallpaper")
    folderLocation = path.dirname(__file__)
    os.system('sudo cp ' + folderLocation + '/System_Files/System-BSI_v1.png /usr/share/lubuntu/wallpapers/lubuntu-default-wallpaper.png')