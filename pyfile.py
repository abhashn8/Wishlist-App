import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window


class WishListApp(App):
    '''class to create a Kivy app that manages a wishlist.'''

    def __init__(self, **kwargs):
        """
        To initialize the app and create an empty wishlist.
        """
        super(WishListApp, self).__init__(**kwargs)
        self.wish_list = {}

    def add_item(self, instance):
        """
        To add a new item to the wishlist and update it.

        """
        item_name = self.item_name_input.text
        item_note = self.item_note_input.text
        if item_name:
            self.wish_list[item_name] = item_note
            self.item_list_label.text = '\n'.join([f"{k} - {v}" for k, v in self.wish_list.items()])
            self.item_list_label.text = '\n'.join("")
            self.item_name_input.text = ""
            self.item_note_input.text = ""
            self.save_wish_list()

    def mark_as_purchased(self, instance):
        """
        To mark an item in the wishlist as purchased and update the output.

        """
        purchased_item = self.item_name_input.text.lower()
        if purchased_item in self.wish_list:
            del self.wish_list[purchased_item]
            self.item_list_label.text = '\n'.join([f"{k} - {v}" for k, v in self.wish_list.items()])
            self.item_name_input.text = ""
            self.item_note_input.text = ""
            self.save_wish_list()

    def load_wish_list(self):
        """
         To load the wishlist from a JSON file if the file exist.

        """
        try:
            with open('wishlist.json', 'r') as f:
                self.wish_list = json.load(f)
        except FileNotFoundError:
            pass

    def save_wish_list(self):
        """
        To save the wishlist to a JSON file.

        """
        with open('wishlist.json', 'w') as f:
            json.dump(self.wish_list, f)

    def view_list(self, instance):
        '''To display the items in the wishlist.'''
        self.load_wish_list()
        self.item_list_label.text = '\n'.join([f"#{k} - {v}" for k, v in self.wish_list.items()])
    
    def clear_list(self, instance):
        '''To clear the items in the wishlist.'''
        self.wish_list.clear()
        self.item_list_label.text = ''
        self.save_wish_list()


    def build(self):
            '''This is the method to create the GUI layout for the app.'''
            # Creating a GridLayout with one column and spacing of 10.
            layout = GridLayout(cols=1, spacing=10)

             # Setting the background color of the window to white.
            Window.clearcolor = (1, 1, 1, 1)
            # Adding an image to the background with 'y.jpg' as the source.
            bg_image = Image(source='y.jpg', allow_stretch=True, keep_ratio=False)
            Window.add_widget(bg_image)

            # To have some spaces on top.
            '''self.title_label = Label(text='  ')
            layout.add_widget(self.title_label)
            self.title_label = Label(text='   ')
            layout.add_widget(self.title_label)'''
            self.title_label = Label(text='   ')
            layout.add_widget(self.title_label)
            self.title_label = Label(text='   ')
            layout.add_widget(self.title_label)

            # Createing a BoxLayout for the input.
            item_name_box = BoxLayout(padding=(300, 10, 300,10))
            # Adding a TextInput widget for the user to enter the item name.
            self.item_name_input = TextInput(hint_text='Enter item name', multiline=False, size_hint_x=0.8, background_color=(0.85, 0.85, 0.85, 1))
            item_name_box.add_widget(self.item_name_input)
            layout.add_widget(item_name_box)

            item_note_box = BoxLayout(padding=(300, 10, 300,10))
            # Adding a TextInput widget for the user to enter note about the item.
            self.item_note_input = TextInput(hint_text='Note:', multiline=False, size_hint_x=0.8, background_color=(0.85, 0.85, 0.85, 1))
            item_note_box.add_widget(self.item_note_input)
            layout.add_widget(item_note_box)

             # Creating a BoxLayout for the buttons.
            button_layout = BoxLayout(orientation='horizontal',spacing=20, padding=(85, 0, 85, 0) )
            layout.add_widget(button_layout)

            # Creatting a button to add items to the list.
            self.add_button = Button(text='Add Item', size_hint=(0.1, 0.75), background_color=(0, 0.5, 0.5, 1))
            self.add_button.bind(on_press=self.add_item)
            button_layout.add_widget(self.add_button)

            # Creating a button to mark items as purchased.
            self.purchase_button = Button(text='Purchased', size_hint=(0.1, 0.75), background_color=(1, 0, 0, 1))
            self.purchase_button.bind(on_press=self.mark_as_purchased)
            button_layout.add_widget(self.purchase_button)

            # Creating a button to view the list of items.
            self.view_button = Button(text='View Your List', size_hint=(0.1, 0.75), background_color=(1, 0, 1, 1))
            self.view_button.bind(on_press=self.view_list)
            button_layout.add_widget(self.view_button)

            # Creating a button to clear the list of items.
            self.clear_button = Button(text='Clear List', size_hint=(0.1, 0.75), background_color=(0.5, 0.5, 0, 1))
            self.clear_button.bind(on_press=self.clear_list)
            button_layout.add_widget(self.clear_button)

            # Creating a Label widget to display the item list.
            self.item_list_label = Label(text='', font_size=24, halign='left', valign='middle', color=[0, 0, 0, 1])
            layout.add_widget(self.item_list_label)
            
            # Creating a label widget to display the number of items in the item list
            self.count_label = Label(text= f'{self.item_list_label.text} ', font_size=20)
            layout.add_widget(self.count_label)

            # Loading the wish list from the file system.
            self.load_wish_list()
            return layout

    

if __name__ == '__main__':
    WishListApp().run()