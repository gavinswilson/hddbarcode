import imagemgmt
import os_mgmt
import barcodereader

if __name__ == "__main__": 
  # Take the image from user 
    image="img6.jpg"
    OS = os_mgmt.checkOS()
    if OS == "chromebook":
        image = "img4.jpg"
        barcodereader.readbarcode(image) 
    elif (OS == "unknown"):
        print("Unknown OS - Terminating")    
    else:
        imagemgmt.takePicture(image)
        barcodereader.readbarcode(image) 
    