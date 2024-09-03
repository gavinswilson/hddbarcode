import imagemgmt
import os_mgmt
import barcodereader
import argparser
#import argparse

if __name__ == "__main__": 
    
    parser = argparser.setupargs()

    args = parser.parse_args()
    print(args)

    if args.read != None:
        inimage = args.read[0]
    else:
        inimage ="../images/img6.jpg"
    
    if args.output != None:
        outimage = args.output[0]
    else:
        outimage ="../images/img4a.jpg"
    
    if args.camera != None:
        cam_num = args.output[0]
    else:
        cam_num = 999
    
    OS = os_mgmt.checkOS()
    if OS == "chromebook":
        cam_num = 999   
    elif (OS == "unknown"):
        print("Unknown OS - Terminating")    
    else:
        imagemgmt.takePicture(inimage, cam_num)
       
    barcodereader.readbarcode(inimage, outimage) 