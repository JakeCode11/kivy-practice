from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

from connected import Connected
import os

class Login(Screen):
    def login_op(self, uname, pwd):
        app = App.get_running_app()

        app.username = uname
        app.password = pwd

        # TODO need to implement login credential encryption
        if app.username == 'username' and app.password == 'password':
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'connected'

            app.config.read(app.get_application_config())
            app.config.write()
        else:
            print("Bad Creds")

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()
        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))

        return manager

    def get_application_config(self):
        if (not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if (not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
                '%s/config.cfg' % (conf_directory)
        )

if __name__ == '__main__':
    LoginApp().run()
