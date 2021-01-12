# @rebootstr

import os
import traceback


def checkModules():
    if not os.path.exists("Modules"):
        os.mkdir("Modules")
        return False
    else:
        if not os.path.isdir("Modules"):
            print("Error: Found file \"Modules\", but it should be the directory")
            return False
    moduleNames = []
    for file in os.scandir("Modules/"):
        if file.is_dir():
            moduleNames.append(file.name)
    for name in moduleNames:
        # tmp = __import__("Modules", fromlist=moduleNames)
        moduleDict = {
            "name": name,
            "module": __import__("Modules." + name, fromlist=["main"]).main
        }
        modules.append(moduleDict)
    return True


if __name__ == '__main__':
    debug = False
    modules = []
    if not checkModules():
        print("Modules not found. Put the modules in directory named \"Modules\". Closing..")

    print("Select need module to run():")
    for moduleNum in range(len(modules)):
        moduleName = modules[moduleNum]['name']
        try:
            moduleName = modules[moduleNum]["module"].MODULE_CUSTOM_NAME
        except:
            pass
        print(f"  {moduleNum + 1}. {moduleName}")
    print("\n  0. Debug On/Off \n  ---------------")

    while True:
        try:
            select = int(input("$runner: "))
            if select == 0:
                debug = False if debug else True
                print("Debug mod " + ("On" if debug else "Off"))
            else:
                modules[select-1]["module"].run()
        except Exception as ex:
            print("Wrong number or execution fail")
            if debug:
                print("########")
                print(traceback.format_exc(), end="")
                print("########")
