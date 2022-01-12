# V-Script (PY)
# Release Tag: 1.2
# Release Name: "Code Rewrite"

class Utility:
    class Out:
        def lnStr(curStr): print(curStr)
        def lnInt(curNum): print(curNum)

    class Version:
        def Check():
            curName = "V-Script"
            curTag ="1.2"
            tagName = "Code Rewrite"
            print("Name: " + curName + "\nVersion Tag: v" + curTag + "\nTag Name: " + tagName)

LocalUtil = Utility()

class Math:
    class Operations:
        def add(a, b): print(a+b)
        def subtract(a, b): print(a-b)
        def multiply(a, b): print(a*b)
        def divide (a, b): print(a/b)

ExtMath = Math()

class Main:

    def run():

        # Write Code
        
Main.run()
