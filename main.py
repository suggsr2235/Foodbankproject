'''
Application example using build() + return
==========================================
An application can be built if you return a widget on build(), or if you set
self.root.
'''
# an error occurred during configuration option use-feature invalid choice: 'content-addressable-pool' (choose from '2020-resolver', 'fast-deps' , 'truststore')
import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        # return a Button() as a root widget
        return Button(text='hello world!')

if __name__ == '__main__':
    TestApp().run()


# from bottle import route, run, template

# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)

# run(host='localhost', port=8080)

