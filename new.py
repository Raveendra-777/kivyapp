import cv2.data
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
import numpy as np

class CameraWidget(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.capture = cv2.VideoCapture(0)
        self.cas = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

        Clock.schedule_interval(self.update, 1.0/30.0)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # Process frame with OpenCV
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face = self.cas.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in face:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            # Convert to texture
            buf = cv2.flip(frame, 0).tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.texture = texture

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.camera = CameraWidget()
        layout.add_widget(self.camera)
        return layout

    def on_stop(self):
        self.camera.capture.release()

if __name__ == '__main__':
    MainApp().run()