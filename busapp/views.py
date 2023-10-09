from django.shortcuts import render
from camera import VideoCamera
from django.shortcuts import render
from django.http.response import StreamingHttpResponse

# Create your views here.
def click_photo_enter(request):
    return render(request, 'index.html')



def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame
               + b'\r\n\r\n')

def video_feed(request):
    try :
        cam = VideoCamera()
        return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')
    except :
        pass
    return render(request, 'camera.html')


