# V-Script-PY
# Version: 1.1
# Released: /

from re import match
import webbrowser

# Very cool version checking
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
        "\nReleased: " + strRelease + "\n"
        )
    if ReleaseTag != "1.0":
        print("You version of V-Script (PY) is outdated! \nPlease update to the latest version.")
        ReqUpdate()

# Very cool update thing I can make
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

        # For printing strings
        def lnStr(curStr):
            print(curStr)

        # For printing integers
        def lnInt(curInt):
            print(curInt)

    # Yo, create some objects with this function
    def ObjectCreator():
        name = ""
        type = ""
        typeOpts = 0

        print("Input a name for your object: ")
        name = input()

        print("Select an object type:\n[1] String | [2] Integer\n")
        typeOpts = input()

        # :troll: time to nest these functions
        def InputStr():
            curStr = ""
            curStr = input()
            print("String: " + curStr)

        def InputInteger():
            curInt = 0
            curInt = input()
            print("Integer: " + curInt)

        # No wei python switch case :flushed:
        match (typeOpts):
            case 1:
                InputStr()
            case 2:
                InputInteger()

def Main():
    # Get the goddamn version
    OutputVersion("V-Script (PY)", "1.1", True)
    # Testing if this works
    Utility.SysOut.lnStr("Hello World!")
Main()
