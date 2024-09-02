 
import cv2 # only needed for testing 
from pyzbar.pyzbar import decode 
import os_mgmt
   
# Read barcodes
def readbarcode(image): 

    if (os_mgmt.checkFileExists(image)):
        img = cv2.imread(image)  
        detectedBarcodes = decode(img) 
            
        if not detectedBarcodes: 
            print("Barcode Not Detected or your barcode is blank/corrupted!") 
        else: 
            print(detectedBarcodes) 
            for barcode in detectedBarcodes:    
                (x, y, w, h) = barcode.rect 
                #for testing breakout image 
                cv2.rectangle(img, (x-10, y-10), 
                            (x + w+10, y + h+10),  
                            (255, 0, 0), 2) 
                
                if barcode.data!="": 
                    print(barcode.data) 
                    print(barcode.type) 
        filename = "img4a.jpg"
        cv2.imwrite(filename, img)           
        cv2.imshow("Image", img)
        cv2.waitKey(0) 
        # cv2.destroyAllWindows() 
        print("Done")
    else:
        print("cannot open file - terminating")


