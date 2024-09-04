 
import cv2 # only needed for testing 
from pyzbar.pyzbar import decode 
import os_mgmt
from pprint import pprint
   
# Read barcodes
def readbarcode(inputimage, outputimage, debug=0): 

    img = cv2.imread(inputimage)  
    detectedBarcodes = decode(img) 
    print("Analysing image: ", inputimage)    
    if not detectedBarcodes: 
        print("Barcode Not Detected or your barcode is blank/corrupted!") 
    else: 
        if debug > 0: pprint(detectedBarcodes) 
        for barcode in detectedBarcodes:    
            (x, y, w, h) = barcode.rect 
            #for testing breakout image 
            cv2.rectangle(img, (x-10, y-10), 
                        (x + w+10, y + h+10),  
                        (255, 0, 0), 2) 
            
            # if barcode.data!="": 
            #     print(barcode.data) 
            #     print(barcode.type) 
    #filename = "../images/img4a.jpg"
    cv2.imwrite(outputimage, img)
    if debug > 0: print("\nwriting barcode detected image:", outputimage)          
    # cv2.imshow("Image", img)
    # cv2.waitKey(0) 
    # # cv2.destroyAllWindows() 
    print("\nDone")
    return detectedBarcodes, 0

