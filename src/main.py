import imagemgmt
import os_mgmt
import barcodereader
import argparser
import JSONdata
from PIL import Image
from datetime import datetime

from pprint import pprint

if __name__ == "__main__": 
    
    ######################################################################
    #setting up main variables
    inimage = ""                            #image to be read
    outimage = ""                           #image to save results to
    camnum = -1                             #camera to use ... -1 never exists
    debuglevel = 0
    availimage = 0                          #set to 1 for image being avail through camera or loading
    dupimage = 0                            #set to 1 if we are in danger of overwriting files
    dt = datetime.now()
    strdt = dt.strftime("%Y%m%d%H%M%S")     #timestamp for filenames if they arent provided
    barcodelist = ""                        #where the detected barcodes will go
    OCRlist = ""                            #where the detected text will go
    result = 0                              #used for function returns

    ######################################################################
    #parse arguments to define program flow and set-up
    parser = argparser.setupargs()          #build parser logic

    args = parser.parse_args()              #parse elements
    
    ###### Debug logging level set-up
    if args.debug != None: debuglevel = args.debug[0]
    
    if debuglevel > 0: pprint(args) #logging all input functions
    
    ###### set-up default input filename
    if args.input != None: 
        inimage = args.input[0]
        availimage = 1
    else:
        inimage = "../images/" + strdt + "-in.jpg"
    if debuglevel > 0: print("Input image name:", inimage)
    if os_mgmt.checkFileExists(inimage, debuglevel) != 0:
        availimage = 0

    ###### set-up default output filename
    if args.output != None:
        outimage = args.output[0]
    else:
        outimage = "../images/" + strdt + "-out.jpg"
    if debuglevel > 0: print("Output image name:", outimage)
    if os_mgmt.checkFileExists(outimage, debuglevel) == 0:
        dupimage = 1
        if debuglevel > 0: print("Image already exists: ", outimage, " exiting")

    ###### set-up camera to use
    if args.camera != None:
        cam_num = args.output[0]
        #system checking for cam set-up
    else:
        cam_num = -1
    if debuglevel > 0: print("Camera Number:", cam_num)
    if debuglevel > 0 and cam_num == -1: print("No camera selected")
    
    ######################################################################
    #get the current OS running with version for compatability
    OS = os_mgmt.checkOS(debug=debuglevel)
    
    #configure hardware set-up.
    if OS == "chromebook":
        cam_num = -1   
    elif (OS == "unknown"):
        print("Unknown OS - Terminating")
        cam_num = -1       
    else:
        print("cam configured?")
        #code to check the camera exists at the location

    ######################################################################
    # run the analyser   
    if cam_num != -1: 
        takepicture = imagemgmt.takePicture(inimage, cam_num)
        if takepicture != 0:
            availimage = 0

    if (availimage == 1 and dupimage == 0): 
        if debuglevel > 0: print("Running barcode analysis....")
        result, barcodelist = barcodereader.readbarcode(inimage, outimage, debug=debuglevel)
    else:
        if availimage !=1: print("no image to read, terminating....")
        if dupimage !=0: print("File exists... terminating")
    
    ######################################################################
    # output data to JSON  
    #if debuglevel > 0: pprint(barcodelist) 
    result, filename = JSONdata.outputJSON(barcodelist, strdt)
    if debuglevel > 0: print("data outputted to: ", filename) 
   