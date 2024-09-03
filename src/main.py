import imagemgmt
import os_mgmt
import barcodereader
import argparser
from pprint import pprint

if __name__ == "__main__": 
    ######################################################################
    #setting up main variables
    inimage = ""
    inimage = "../images/img4.jpg" #test default
    outimage = ""
    camnum = -1
    debuglevel = 0

    ######################################################################
    #parse arguments to define program flow and set-up
    parser = argparser.setupargs()

    args = parser.parse_args()

    if debuglevel > 0: pprint(args) #debug logging

    if args.input != None: inimage = args.input[0]
    
    
    if args.output != None:
        outimage = args.output[0]
    else:
        outimage ="../images/img4a.jpg"
    
    if args.camera != None:
        cam_num = args.output[0]
    else:
        cam_num = -1
    
    if args.debug != None:
        debuglevel = args.debug[0]
    else:
        debuglevel = 0

    ######################################################################
    #system checking for hardware and cam set-up
    
    
    #get the current OS running with version for compatability
    OS = os_mgmt.checkOS(debug=debuglevel)
    
    #configure hardware set-up.
    if OS == "chromebook":
        cam_num = -1   
    elif (OS == "unknown"):
        print("Unknown OS - Terminating")    
    else:
        print("cam configured")

    ######################################################################
    # run the analyser   
    if cam_num != -1: imagemgmt.takePicture(inimage, cam_num)

    barcodereader.readbarcode(inimage, outimage, debug=debuglevel) 