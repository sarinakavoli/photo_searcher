from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('fronted.kv')

class FirstScreen(Screen):
    def get_image_link(self):
        # Get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text
        # Get wikipedia page and the first image link.
        page = wikipedia.page(query)
        image_link = page.images[0]
        return image_link

    def download_image(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        # Download the image
        req = requests.get(self.get_image_link())
        imagepath = 'files/image.jpg'
        response = requests.get(self.get_image_link(), headers=headers)
        with open(imagepath, 'wb') as file:
            file.write(response.content)
        return imagepath
        # with open (imagepath, 'wb') as file:
        #     file.write(req.content)

    def set_image(self):
        #Set the image in the Image widget
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build (self):
        return RootWidget()


MainApp().run()


# url = 'https://upload.wikimedia.org/wikipedia/commons/9/9b/2009-Seaworld-Shamu.jpg'
# #url = 'https://upload.wikimedia.org/wikipedia/commons/a/ab/Crested_Caracara_eating_a_turtle_(16753759877).jpg'
#
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
# response = requests.get(image_link, headers= headers)
# with open(imagepath, 'wb') as file:
#     file.write(response.content)
# print("File downloaded successfully.")
# print(response.content[:100])
