from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Tasks(BoxLayout):
	def __init__(self,tasks, **kwargs):
		super().__init__(**kwargs)
		for task in tasks:
			self.add_widget(Label(text=task))


class Test(App):
	def build(self):
		return Tasks(['Go gorcery shoppting', 'Finish article'])

Test().run()