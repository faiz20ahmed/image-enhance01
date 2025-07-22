
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
BoxLayout:
    orientation: 'vertical'
    spacing: dp(10)
    padding: dp(20)

    MDLabel:
        text: "Image Enhance01"
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H5"

    MDRaisedButton:
        text: "Select Image"
        pos_hint: {"center_x": .5}
        on_release: app.select_image()

    Image:
        id: image_preview
        source: ""
        allow_stretch: True

    MDRaisedButton:
        text: "Enhance Image"
        pos_hint: {"center_x": .5}
        on_release: app.enhance_image()
'''

class ImageEnhanceApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def select_image(self):
        print("Select image logic here")

    def enhance_image(self):
        print("Enhance logic here")

ImageEnhanceApp().run()
