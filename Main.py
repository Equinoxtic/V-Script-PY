# V-Script-PY
# Version: 1.0
# Released: X

import webbrowser

def OutputVersion(ReleaseName, ReleaseTag, IsReleased):
    strRelease = ""
    if IsReleased == True:
        strRelease = "Y"
    else:
        strRelease = "X";
        print("This version of V-Script (PY) has not been released yet.")
    print(
        "Name: " + ReleaseName +
        "\nVersion: " + ReleaseTag +
        "\nReleased: " + strRelease
        )
    if ReleaseTag != "1.0":
        print("You version of V-Script (PY) is outdated! \nPlease update to the latest version.")
        ReqUpdate()

def ReqUpdate():
    curOpt = ""
    print("Update to latest version of V-Script (PY)? [Y/N]: ")
    curOpt = input()
    def OpenUrl(CurUrl):
        print("Opening the V-Script (PY) Github page...")
        webbrowser.open(CurUrl)
    if curOpt == "Y" or curOpt == "y":
        OpenUrl("https://github.com/Equinoxtic/V-Script-PY/releases")
    elif curOpt == "N" or curOpt == "n":
        print("Update operation Cancelled.")

class Utility:
    class SysOut:
        def lnStr(curStr):
            print(curStr)
        def lnInt(curInt):
            print(curInt)

def Main():
    # Testing if this works
    Utility.SysOut.lnStr("Hello World!")
Main()
