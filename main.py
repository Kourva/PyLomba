#!/usr/bin/env python3

## Imports
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.actionbar import ActionBar, ActionView, ActionPrevious
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition

# KV File
with open("main.kv") as kv:
    Builder.load_string(kv.read())


# Main Class
class PyLombaApp(App):

    def run_text(self, *args):
        try:
            Input = self.TextInput.text
            Compiled_Text = eval(Input)
            self.ScrollView.ids.result.text = str(Compiled_Text)
        except Exception as E:
            Error = \
f"""
[color=#FFFFFF]# Error While Running Your Code[/color]
[color=#AA0000]{E}[/color]
.
.
.
.
.
.
[color=#FFFFFF]# Note[/color]
This app is for evaluate a string which contains [color=#AA0000]single expression[/color] and return the calculated value and only evaluates the single expression, not the complex logic code!
This app does not accept the source code which contains statements like[/color], [color=#AA0000]for[/color], [color=#AA0000]while[/color], [color=#AA0000]print[/color], [color=#AA0000]import[/color], [color=#AA0000]class[/color] and can not be used to [color=#AA0000]assign[/color] a value to variable


"""            
            self.ScrollView.ids.result.text = Error

    def clear_text(self, *args):
        self.TextInput.text = "# Python live evaluater - Start Coding\n\n"
        self.ScrollView.ids.result.text = "OutPut Here..."


    # Build Method
    def build(self):

        # Root
        root = Screen()

        # Action Bar
        self.ActionBar = ActionBar()

        # Text Input
        self.TextInput = TextInput()

        # Clear Button
        self.Clear = Button(
            pos_hint = {"bottom":1, "right":1},
            text = "Clear",
            on_press = self.clear_text
        )

        # Run It Button
        self.RunIt = Button(
            pos_hint = {"bottom":1, "left":1},
            text = "Eval",
            on_press = self.run_text
        )

        # Show Text
        self.ScrollView = ScrollView(
            pos_hint = {"center_x": 0.5, "center_y":0.4}
        )

        # Add Widgets
        root.add_widget(self.ActionBar) 
        root.add_widget(self.TextInput)
        root.add_widget(self.ScrollView)
        root.add_widget(self.Clear)
        root.add_widget(self.RunIt)

        # Return Root
        return root

# Run
PyLombaApp().run()


# Developer: Izolabela
