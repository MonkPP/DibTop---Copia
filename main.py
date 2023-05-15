from kivy.lang import Builder
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.app import MDApp
from kaki.app import App
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.toolbar import toolbar
import psycopg2
from kivymd.toast import toast
from kivymd.uix.snackbar.snackbar import Snackbar
from datetime import datetime

Builder.load_file('interface.kv')
Builder.load_file('login.kv')
Builder.load_file('main.kv')
Builder.load_file('crud.kv')


def conectar():
    conn = psycopg2.connect(
        host="localhost",
        database="DIBTOP",
        user="postgres",
        password="postgres"
    )
    return conn


def validar_login(login, senha):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT * FROM funcionario WHERE login = %s AND senha = %s", (login, senha))
        resultado = cur.fetchone()
        if resultado:
            return True
        else:
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
            toast("Login e senha válidos", duration=2)
            self.manager.current = 'principal'
            # toast('Bem vindo', duration=3)
        else:
            toast("Login ou senha inválidos", duration=5)


class MainScreen(MDScreen):
    # Window.size = (700, 550)

    def crud(self):
        nome = self.ids.alunobtn.text
        toast(nome, duration=2)
        self.manager.current = 'crud'

    pass


class CrudScreen(MDScreen):
    def cadastrar(self):
        self.manager.current = 'cad_aluno'

    def consultar(self):
        self.manager.current = "con_aluno"

    # botão cancelar
    def principal(self):
        self.manager.current = 'principal'

    pass


class CadastrarAluno(MDScreen):
    def guardar_dados(self):
        try:
            nome = self.ids.idnome.text
            cpf = self.ids.idcpf.text
            dt_nasc = self.ids.iddtnasc.text
            endereco = self.ids.idend.text
            email = self.ids.idemail.text
            telefone = self.ids.idtel.text
            naturalidade = self.ids.idnat.text
            nome_mae = self.ids.idnomemae.text
            estado_civil = self.ids.idestcivil.text
            escolaridade = self.ids.idesc.text

            # Converte a string da data de nascimento para um objeto datetime
            dt_nasc = datetime.strptime(dt_nasc, '%d/%m/%Y')

            conn = conectar()
            cur = conn.cursor()
            print(nome, cpf, dt_nasc, endereco, email, telefone, naturalidade,
                  nome_mae, estado_civil, escolaridade)

            cur.execute("""INSERT into Aluno 
            (nome,cpf,dt_nasc,endereco,email,telefone,
            naturalidade,nome_mae,estado_civil,escolaridade) 
            Values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (nome, cpf, dt_nasc, endereco, email, telefone, naturalidade,
                  nome_mae, estado_civil, escolaridade))

            conn.commit()  # Confirma a transação
            toast("Salvo com sucesso", duration=2)

        except Exception as e:
            toast(f"Error ao inserir dados do Aluno: {e}", duration=2)
            # print(f"Error ao inserir dados do Aluno: {e}")
            return False

    def principal(self):
        self.manager.current = 'principal'

    pass


class ConsultarAluno(MDScreen):

    def principal(self):
        self.manager.current = 'principal'

    pass


class CadastrarTurma(MDScreen):

    def principal(self):
        self.manager.current = 'principal'

    pass


class CadastrarCurso(MDScreen):

    def principal(self):
        self.manager.current = 'principal'

    pass


class ConsultarTurma(MDScreen):

    def principal(self):
        self.manager.current = 'principal'

    pass


class ConsultarCurso(MDScreen):

    def principal(self):
        self.manager.current = 'principal'

    pass


class DibTopApp(MDApp, App):

    def build_app(self, **kwargs):
        Window.maximize()
        self.theme_cls.primary_palette = "Green"

        sm = ScreenManager()
        main_screen = MainScreen(name='principal')
        login_screen = LoginScreen(name='login')
        crud_screen = CrudScreen(name='crud')
        cadastrar_aluno = CadastrarAluno(name='cad_aluno')
        cadastrar_turma = CadastrarTurma(name='cad_turma')
        cadastrar_curso = CadastrarCurso(name='cad_curso')
        consultar_aluno = ConsultarAluno(name='con_aluno')
        consultar_turma = ConsultarTurma(name='con_turma')
        consultar_curso = ConsultarCurso(name='con_curso')
        sm.add_widget(login_screen)
        sm.add_widget(main_screen)
        sm.add_widget(crud_screen)
        sm.add_widget(cadastrar_aluno)
        sm.add_widget(cadastrar_turma)
        sm.add_widget(cadastrar_curso)
        sm.add_widget(consultar_aluno)
        sm.add_widget(consultar_turma)
        sm.add_widget(consultar_curso)

        return sm


if __name__ == "__main__":
    DibTopApp().run()
