import cv2


def gen():

    try:
        cam = cv2.VideoCapture(0)

        while True:
            ret,img = cam.read()
            frame=cv2.imencode(".jpeg",img)[1].tostring()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        del(cam)
    except:
        return None