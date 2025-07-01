# Source Generated with Decompyle++
# File: main.pyc (Python 3.11)

from kivymd.uix.scrollview import MDScrollView
from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivymd.uix.toolbar import MDTopAppBar
import math

def itog_round(x):
    return math.ceil(x) if x % 1 == 0.5 else round(x)


class EduCalcApp(MDApp):
    
    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.theme_style = open('assets/theme/theme.txt', 'r').read()
        layout = MDBoxLayout(orientation = 'vertical', spacing = 20, padding = 20)
        top_bar = MDTopAppBar(title = 'EduCalc', left_action_items = [
            [
                'theme-light-dark',
                self.theme_edit]], right_action_items = [
            [
                'exit-to-app',
                self.exit_app]], size_hint = (1, 0.15))
        layout.add_widget(top_bar)
        self.labelItog = MDLabel(text = 'Итоговая оценка: ', text_size = (Window.width * 0.9, None), font_style = 'H5', size_hint = (1, 0.125), halign = 'center')
        layout.add_widget(self.labelItog)
        self.labelAnswer = MDLabel(text = 'Средняя оценка: ', font_style = 'H5', size_hint = (1, 0.125), text_size = (Window.width * 0.9, Window.height * 0.9), halign = 'center')
        layout.add_widget(self.labelAnswer)
        scroll_view = MDScrollView(size_hint = (1, 0.4))
        self.labelScores = MDLabel(text = 'Все оценки: ', text_size = (Window.width * 0.9, None), font_style = 'H5', halign = 'center')
        scroll_view.add_widget(self.labelScores)
        layout.add_widget(scroll_view)
        buttons_layout = MDBoxLayout(orientation = 'horizontal', spacing = 20, padding = 20, size_hint = (1, 0.1))
        scores_layout = MDBoxLayout(orientation = 'horizontal', spacing = 20, padding = 20, size_hint = (1, 0.1))
        btnBckSp = MDRoundFlatButton(text = '<--', font_size = Window.width / 9, size_hint = (0.5, None))
        btnBckSp.bind(on_press = self.btnbcksp_press)
        buttons_layout.add_widget(btnBckSp)
        btnErase = MDRoundFlatButton(text = 'Стереть', font_size = Window.width / 9, size_hint = (0.5, None))
        btnErase.bind(on_press = self.btnerase_press)
        buttons_layout.add_widget(btnErase)
        layout.add_widget(buttons_layout)
        button2 = MDRoundFlatButton(text = '2', font_size = Window.width / 9, text_color = 'red', size_hint = (0.2, None))
        button2.bind(on_press = self.button2_press)
        scores_layout.add_widget(button2)
        button3 = MDRoundFlatButton(text = '3', font_size = Window.width / 9, text_color = 'orange', size_hint = (0.2, None))
        button3.bind(on_press = self.button3_press)
        scores_layout.add_widget(button3)
        button4 = MDRoundFlatButton(text = '4', font_size = Window.width / 9, text_color = 'yellow', size_hint = (0.2, None))
        button4.bind(on_press = self.button4_press)
        scores_layout.add_widget(button4)
        button5 = MDRoundFlatButton(text = '5', font_size = Window.width / 9, text_color = 'green', size_hint = (0.2, None))
        button5.bind(on_press = self.button5_press)
        scores_layout.add_widget(button5)
        layout.add_widget(scores_layout)
        self.nums = ''
        return layout

    
    def btnbcksp_press(self, instance):
        pass
    # WARNING: Decompyle incomplete

    
    def btnerase_press(self, instance):
        self.labelScores.text = 'Все оценки: '
        self.labelAnswer.text = 'Средняя оценка: '
        self.nums = ''
        self.labelItog.text = 'Итоговая оценка: '

    
    def button2_press(self, instance):
        pass
    # WARNING: Decompyle incomplete

    
    def button3_press(self, instance):
        pass
    # WARNING: Decompyle incomplete

    
    def button4_press(self, instance):
        pass
    # WARNING: Decompyle incomplete

    
    def button5_press(self, instance):
        pass
    # WARNING: Decompyle incomplete

    
    def exit_app(self, instance):
        exit()

    
    def theme_edit(self, instance):
        if self.theme_cls.theme_style == 'Dark':
            self.theme_cls.theme_style = 'Light'
            open('assets/theme/theme.txt', 'w').write('Light')
            return None
        self.theme_cls.theme_style = None
        open('assets/theme/theme.txt', 'w').write('Dark')


EduCalcApp().run()
