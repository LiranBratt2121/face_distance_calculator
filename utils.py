def focal_length_finder(measured_distance, real_width, width_in_rf_image):
    """"
    * Measured_distance: It is the distance from the camera to object while capturing the Reference image, Known_distance
    * Real_width: Its measure the width of an object in real-world, here we measure the width of the face which is around Known_width 
    * Width_in_rf_image: It is the width of the object in the image/frame it will be in pixels
    
    ## My results (not accurate)
    
    - Distance from camera = 32 cm
    - Face width = 442 px
    - Real face width = 16 cm

    ## Result:
    
    Focal_length = 884.0
    I changed my results a bit after :D It's still isn't perfect
    """
    
    focal_length = (width_in_rf_image * measured_distance) / real_width

    return focal_length

def distance_finder(face_width_in_frame, focal_Length=1150, real_face_width=20):
    distance = (real_face_width * focal_Length) / face_width_in_frame

    return distance

# print(focal_length_finder(measured_distance=32, real_width=16, width_in_rf_image=442))