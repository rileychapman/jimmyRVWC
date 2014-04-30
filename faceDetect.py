import cv

#HAAR_CASCADE_PATH = "/opt/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
#HAAR_CASCADE_PATH = "/usr/local/Cellar/opencv/2.4.8.2/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
HAAR_CASCADE_PATH = "/opt/ros/hydro/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
CAMERA_INDEX = 1

class Face:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h



def detect_faces(image):
    faces = []
    detected = cv.HaarDetectObjects(image, cascade, storage, 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))
    if detected:
        for (x,y,w,h),n in detected:
            face = Face(x,y,w,h)
            faces.append(face)
    return faces

if __name__ == "__main__":
    #cv.NamedWindow("Video", cv.CV_WINDOW_AUTOSIZE)

    cv.SetCaptureProperty(cv.CaptureFromCAM(CAMERA_INDEX), 15,0)
    capture = cv.CaptureFromCAM(CAMERA_INDEX)
    #capture = cv.CaptureFromCAM(CAMERA_INDEX)
    #capture.set(CV_CAP_PROP_AUTO_EXPOSURE, 0 );
    #print cv.GetCaptureProperty(capture, 15)
    storage = cv.CreateMemStorage()
    cascade = cv.Load(HAAR_CASCADE_PATH)
    faces = []

    i = 0
    while True:
        image = cv.QueryFrame(capture)


        # Only run the Detection algorithm every 5 frames to improve performance - changed to 1
        if i%1==0:
            faces = detect_faces(image)

        faces.sort(key=lambda face: face.y)

        for face in faces:
            cv.Rectangle(image, (face.x,face.y), (face.x+face.w,face.y+face.h), 255)
        if len(faces) != 0:
            face = faces[0]        
            #print "top face at:" + str(face.x) + ", "+ str(face.y)

        cv.ShowImage("w1", image)

        i += 1
