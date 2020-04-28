import os, terminalColor, settingsJson

toDownload = ["aptitude", "snap", "lynx", "vim", "blueman"]

def SystemBSI():
    terminalColor.printCyanString("Initializing System-BSI")
    terminalColor.printRedString("\nunable to connect to BSI-Servers") #This is a placeholder for future internet features
    
    terminalColor.printCyanString("\nUpgrading software") #Upgrading sofware on computer via apt
    os.system('sudo apt update')
    os.system('sudo apt upgrade -y')
    os.system('sudo apt autoremove -y')

    #Downloading sofware on computer via apt
    for i in toDownload:
        terminalColor.printCyanString("\nDownloading: " + i )
        os.system('sudo apt install ' + i + " -y")

    #Changes wallpaper
    terminalColor.printCyanString("\nChanging default wallpaper")
    os.system('sudo cp /usr/lib/BSI-Manager/System_Files/System-BSI_v1.png /usr/share/lubuntu/wallpapers/lubuntu-default-wallpaper.png')

    terminalColor.printCyanString("\nPlease restart the computer to apply all changes made")
    os.system('sleep 10s')