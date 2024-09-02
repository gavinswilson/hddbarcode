import cv2

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


