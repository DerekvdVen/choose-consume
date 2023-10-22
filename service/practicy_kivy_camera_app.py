import kivy
kivy.require('2.2.1') # replace with your current kivy version !

from pyzbar.pyzbar import decode
import zxingcpp

import cv2
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time

Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
    Button:
        text: 'Nestle?'
        size_hint_y: None
        height: '48dp'
        on_press: root.find_barcode()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("./data/IMG_{}.png".format(timestr))
        print("Captured")

    def find_barcode(self):
        '''
        Function that takes an image to try to find the barcode
        '''
        print("Nestle?")
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        image_name = "./data/IMG_{}.png".format(timestr)

        camera.export_to_png(image_name)
        frame = camera.texture.pixels
        # print(frame)

        result_zbar = decode(cv2.imread(image_name))
        result_zxing = zxingcpp.read_barcodes(cv2.imread(image_name))
        print('zxing: ', result_zxing)
        print('zbar: ', result_zbar)

        # todo
        # use cv2 to detect the barcode
        # lookup barcode in barcode api in readme
        # return manufacturer code and see if it belongs to nestle in a lookup table
        # if it's nestle, inform user


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()