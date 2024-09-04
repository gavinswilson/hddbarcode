import imagemgmt
import os_mgmt
import barcodereader
import argparser
from PIL import Image
from datetime import datetime

from pprint import pprint

if __name__ == "__main__": 
    ######################################################################
    #setting up main variables
    inimage = ""
    inimage = "../images/img4.jpg" #test default
    outimage = ""
    camnum = -1
    debuglevel = 0
    availimage = 0
    dupimage = 0
    dt = datetime.now()
    strdt = dt.strftime("%Y%m%d%H%M%S")

    ######################################################################
    #parse arguments to define program flow and set-up
    parser = argparser.setupargs()

    args = parser.parse_args()
    
    if args.debug != None:
        debuglevel = args.debug[0]
    else:
        debuglevel = 0

    if debuglevel > 0: pprint(args) #logging all input functions

    if args.input != None: 
        inimage = args.input[0]
        availimage = 1
    else:
        inimage = "../images/" + strdt + "-in.jpg"

    if debuglevel > 0: print("Input image name:", inimage)
    
    if os_mgmt.checkFileExists(inimage, debuglevel) != 0:
        availimage = 0

    if args.output != None:
        outimage = args.output[0]
    else:
        outimage = "../images/" + strdt + "-out.jpg"
    if debuglevel > 0: print("Output image name:", outimage)
    if os_mgmt.checkFileExists(outimage, debuglevel) == 0:
        dupimage = 1
        if debuglevel > 0: print("Image already exists: ", outimage, " exiting")
    
    if args.camera != None:
        cam_num = args.output[0]
    else:
        cam_num = -1
    
    if debuglevel > 0: print("Camera Number:", cam_num)

    

    ######################################################################
    #system checking for hardware and cam set-up
    
    
    #get the current OS running with version for compatability
    OS = os_mgmt.checkOS(debug=debuglevel)
    
    #configure hardware set-up.
    if OS == "chromebook":
        cam_num = -1   
    elif (OS == "unknown"):
        print("Unknown OS - Terminating")
        cam_num = -1       
    else:
        print("cam configured")
        #code to check the camera exists at the location

    ######################################################################
    # run the analyser   
    if cam_num != -1: 
        takepicture = imagemgmt.takePicture(inimage, cam_num)
        if takepicture != 0:
            availimage = 0
    
    

    if (availimage == 1 and dupimage == 0): 
        if debuglevel > 0: print("Running barcode analysis....")
        barcodereader.readbarcode(inimage, outimage, debug=debuglevel)
    else:
        if availimage !=1: print("no image to read, terminating....")
        if dupimage !=0: print("File exists... terminating")
    

   