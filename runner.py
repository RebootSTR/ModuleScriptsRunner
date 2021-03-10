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


def sortingModules():
    for module in modules:
        try:
            order = int(module["module"].ORDER)
        except:
            module["module"].ORDER = 0
    for i in range(0, len(modules)-1):
        for j in range(i, len(modules)):
            if modules[j]["module"].ORDER == 0:
                continue
            if modules[i]["module"].ORDER > modules[j]["module"].ORDER or modules[i]["module"].ORDER == 0:
                tmp = modules[j]
                modules[j] = modules[i]
                modules[i] = tmp


if __name__ == '__main__':
    debug = False
    modules = []
    if not checkModules():
        print("Modules not found. Put the modules in directory named \"Modules\". Closing..")

    sortingModules()

    print("Select need module to run():")
    for moduleNum in range(len(modules)):
        # Hiding checking
        try:
            if str(modules[moduleNum]["module"].HIDE) == "True":
                continue
        except:
            pass

        moduleName = modules[moduleNum]['name']
        moduleOrder = modules[moduleNum]["module"].ORDER

        # Custom name checking
        try:
            moduleName = modules[moduleNum]["module"].MODULE_CUSTOM_NAME
        except:
            pass

        print(f"  {moduleNum + 1:2}. {moduleName}({moduleOrder})")
    print("\n   0. Debug On/Off \n  ---------------")

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
