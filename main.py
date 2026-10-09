from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.07, 0.12, 1)

class ManoRoot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=40, spacing=20, **kwargs)
        
        title = Label(
            text='[b]MANO[/b]',
            markup=True,
            font_size='48sp',
            color=(0.0, 0.83, 1.0, 1),
            size_hint=(1, 0.3)
        )
        
        status = Label(
            text='AI Assistant\nReady to build',
            font_size='20sp',
            color=(0.8, 0.8, 0.8, 1),
            size_hint=(1, 0.3)
        )
        
        btn = Button(
            text='Tap Me',
            font_size='20sp',
            size_hint=(1, 0.2),
            background_color=(0.0, 0.83, 1.0, 1)
        )
        btn.bind(on_press=self.on_tap)
        
        self.add_widget(title)
        self.add_widget(status)
        self.add_widget(btn)
    
    def on_tap(self, instance):
        instance.text = 'Mano is coming soon...'

class ManoApp(App):
    def build(self):
        return ManoRoot()

if __name__ == '__main__':
    ManoApp().run()
