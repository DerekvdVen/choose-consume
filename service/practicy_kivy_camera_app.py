from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture

class CameraApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Create a Camera widget
        self.camera = Camera(resolution=(640, 480), play=True)
        self.layout.add_widget(self.camera)

        # Create a button to capture a picture
        self.capture_button = Button(text="Capture")
        self.capture_button.bind(on_press=self.capture)
        self.layout.add_widget(self.capture_button)

        return self.layout

    def capture(self, instance):
        # Define a callback function to capture the picture
        def on_picture_taken(texture):
            # Save the captured image
            texture.save("captured_image.png")
            popup.dismiss()
            self.show_captured_image()

        # Capture a picture and set the callback
        texture = self.camera.texture
        if texture:
            popup = Popup(title='Capturing...', content=Label(text='Capturing image, please wait...'), auto_dismiss=False, size_hint=(None, None), size=(400, 200))
            popup.open()
            Clock.schedule_once(lambda dt: on_picture_taken(texture), 2)

    def show_captured_image(self):
        # Display the captured image
        self.layout.clear_widgets()
        image = Image(source='captured_image.png')
        self.layout.add_widget(image)

if __name__ == '__main__':
    CameraApp().run()