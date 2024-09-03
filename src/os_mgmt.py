import platform
import os.path

def checkOS(debug=0):
    # print(platform.platform())
    # print(platform.system())
    # print(platform.release())
    # print(platform.version())
    # print(platform.architecture())
    # print(platform.machine())
    # print(platform.uname())
    # print(platform.node())
    if (platform.node() == "penguin"):
        if debug > 0: print("Chromebook detected - no webcam - load image\n")
        return "chromebook"
    else:
        return "unknown"

def checkFileExists(imagefile):
    if (os.path.isfile(imagefile)):
        return 1
    else:
        return 0
    # what do we do if the file doesnt exist?