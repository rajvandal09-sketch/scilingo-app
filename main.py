from kivy.app import App
from kivy.uix.label import Label

class ScilingoApp(App):
    def build(self):
        return Label(text="App is running successfully!")

if __name__ == '__main__':
    ScilingoApp().run()
