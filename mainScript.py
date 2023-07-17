import DeveloperCredits
import GUI_login
import GUI_WorkLabel

def Start_GUI_Login():
    GUI_login.main()

def Start_GUI_WorkLabel():
    GUI_WorkLabel.main()

if __name__ == '__main__':
    DeveloperCredits.printCodeMaster()
    Start_GUI_Login()
    Start_GUI_WorkLabel()