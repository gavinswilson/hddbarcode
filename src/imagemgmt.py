import cv2

def takePicture(captimage, cam_num):
    # Tries to capture an image and returns a result
    # name of captured image to be saved is captimage
    # camera port is cam_num
    # Returns:
    #   0 for success
    #   2 for no image captured
    #   3 for invalid camera passed
    #   4 for no camera at address
    
    for x in range(5): #update to define actual cam num
        cam_port = x
        cam = cv2.VideoCapture(cam_port) 
        if cam is None or not cam.isOpened():
            print('Warning: unable to open video source: ', x)
            return 4
    
    if cam_num == -1:
        print("incorrect camera allocated")
        return 3

    result, image = cam.read() 
    if result: 

        cv2.imshow(image) 
        cv2.imwrite(captimage, image)  
        cv2.waitKey(0) 
        cv2.destroyWindow("GeeksForGeeks") 
        return 0
    
    else: 
        print("No image detected. Please! try again")
        return 2


