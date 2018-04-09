from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class appendOnApp(BoxLayout):
	pass

class Test(App):
	def build(self):
		return appendOnApp()

Test().run()
