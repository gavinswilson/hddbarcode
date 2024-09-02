 
import cv2 # only needed for testing 
from pyzbar.pyzbar import decode 
import platform
   
# Read barcodes
def BarcodeReader(image): 
      
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

def takePicture(image):
    for x in range(5):
        cam_port = x
        cam = cv2.VideoCapture(cam_port) 
        if cam is None or not cam.isOpened():
            print('Warning: unable to open video source: ', x)
    
    
    result, image = cam.read() 
    if result: 

        cv2.imshow("GeeksForGeeks", image) 
        cv2.imwrite("GeeksForGeeks.png", image)  
        cv2.waitKey(0) 
        cv2.destroyWindow("GeeksForGeeks") 
    
    else: 
        print("No image detected. Please! try again") 

def checkOS():
    # print(platform.platform())
    # print(platform.system())
    # print(platform.release())
    # print(platform.version())
    # print(platform.architecture())
    # print(platform.machine())
    # print(platform.uname())
    # print(platform.node())
    if (platform.node() == "penguin"):
        print("Chromebook detected - no webcam - load image\n")
        return "chromebook"
    else:
        return "unknown"
    

if __name__ == "__main__": 
  # Take the image from user 
    image="img6.jpg"
    OS = checkOS()
    if OS == "chromebook":
        image = "img4.jpg"
        BarcodeReader(image) 
    elif (OS == "unknown"):
        print("Unknown OS - Terminating")    
    else:
        takePicture(image)
        BarcodeReader(image) 
    
