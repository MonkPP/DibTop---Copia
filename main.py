from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.app import MDApp
from kaki.app import App
import psycopg2


Builder.load_string('''

<LoginScreen>:
    FloatLayout:
        MDTextField:
            id: idlogin
            hint_text:"Login"
            pos_hint: {'center_x':0.5,'center_y':0.8}
            size_hint_x: 0.75
            max_text_length: 25
            #line_color_normal: [0,1,1,1]
            #line_color_focus: [0,1,0,1]
        MDTextField:
            id: idsenha
            hint_text:"Senha"
            pos_hint: {'center_x':0.5,'center_y':0.6}
            size_hint_x: 0.75
            password: True
            #line_color_normal: [0,1,1,1]
            #line_color_focus: [0,1,0,1]
        MDTextButton:
            text: "Esqueci minha senha"
            pos_hint: {'center_x':0.5,'center_y':0.4}
            font_size: 15
        MDFillRoundFlatButton:
            text: "Entrar"
            pos_hint: {'center_x':0.5,'center_y':0.2}
            size_hint_x: 0.75
            text_color: 1,1,1,1
            md_bg_color: 0.18,0.53,1,1
            font_size: 20
            on_release: root.get_data()            

<MainScreen>:
    FloatLayout:
        MDTextField:
            id: idlogin
            hint_text:"Login"
            pos_hint: {'center_x':0.5,'center_y':0.8}
            size_hint_x: 0.75
            max_text_length: 25
        MDTextField:
            id: idsenha
            hint_text:"Senha"
            pos_hint: {'center_x':0.5,'center_y':0.6}
            size_hint_x: 0.75
            password: True
        MDTextButton:
            text: "Esqueci minha senha"
            pos_hint: {'center_x':0.5,'center_y':0.4}
            font_size: 15
        MDFillRoundFlatButton:
            text: "Entrar"
            pos_hint: {'center_x':0.5,'center_y':0.2}
            size_hint_x: 0.75
            text_color: 1,1,1,1
            md_bg_color: 1,0.53,1,1
            font_size: 20
            on_release: root.get_data()


''')


def conectar():
    conn = psycopg2.connect(
        host="localhost",
        database="DIBTOP",
        user="postgres",
        password="postgres"
    )
    print(conn)
    return conn


def validar_login(login, senha):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT * FROM funcionario WHERE login = %s AND senha = %s", (login, senha))
        resultado = cur.fetchone()
        if resultado:
            # login e senha valids
            print("t")
            return True
        else:
            print('f')
            # login e senha invalids
            return False
    except Exception as e:
        print(f"Error ao validar login: {e}")
        return False


class LoginScreen(MDScreen):
    # Window.size = (350, 275)

    def get_data(self):
        login = self.ids.idlogin.text
        senha = self.ids.idsenha.text
        if validar_login(login, senha):
            print("Login e senha válidos")
            self.manager.current = 'principal'
        else:
            print("Login ou senha inválidos")


class MainScreen(MDScreen):
    # Window.size = (700, 550)
    pass


class MainApp(MDApp, App):

    def build_app(self, **kwargs):
        Window.maximize()
        self.theme_cls.primary_palette = "Green"

        sm = ScreenManager()
        main_screen = MainScreen(name='principal')
        login_screen = LoginScreen(name='login')
        sm.add_widget(login_screen)
        sm.add_widget(main_screen)

        return sm


if __name__ == "__main__":
    MainApp().run()
