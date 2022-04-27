"""
Background image used in the application has been taken from: https://icons8.com
Dataset used in the application has been taken from: https://www.kaggle.com/datasets/mdhamani/goodreads-books-100k
"""

import pandas as pd
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

data = pd.read_csv("books.csv", encoding="UTF-8-sig")
data = data.dropna()

Window.size = dp(350), dp(600)


class Starting_Screen(Screen):

    def go_to_random_book_screen(self):
        self.manager.current = "random_book_screen"


class Random_Book_Screen(Screen):
    def on_enter(self, *args):
        self.load_text()

    def load_text(self):
        random_row = data.sample()
        random_image = (random_row["img"].values[0])
        random_image_title_subtitle = (random_row["title"].values[0])
        random_image_author = (random_row["author"].values[0])
        random_image_rating = (random_row["rating"].values[0])
        random_image_pages = (random_row["pages"].values[0])
        random_image_book_format = (random_row["bookformat"].values[0])
        random_image_reviews = (random_row["reviews"].values[0])
        random_image_desc_text = (random_row["desc"].values[0])
        self.ids['imagesource'].source = f'{random_image}'
        self.ids['book_title'].text = f'{random_image_title_subtitle}'
        self.ids['book_author'].text = f'{random_image_author}'
        self.ids['book_format_text'].text = f'{random_image_book_format}'
        self.ids['book_pages_text'].text = f'{random_image_pages}'
        self.ids['book_rating_text'].text = f'{random_image_rating}'
        self.ids['book_reviews_text'].text = f'{random_image_reviews}'
        self.ids['book_desc_text'].text = f'{random_image_desc_text}'

    def go_to_starting_screen(self):
        self.manager.current = "starting_screen"


class Window_Manager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        self.wm = Window_Manager(transition=FadeTransition())

        screens = [
            Starting_Screen(name="starting_screen"),
            Random_Book_Screen(name="random_book_screen")
        ]

        for screen in screens:
            self.wm.add_widget(screen)

        return self.wm


if __name__ == "__main__":
    MainApp().run()
