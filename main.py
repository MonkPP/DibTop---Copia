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

Builder.load_string('''
#:import Snackbar kivymd.uix.snackbar.Snackbar


<LoginScreen>
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

<MainScreen>
    MDBoxLayout:
        orientation: 'vertical'
        radius: [25, 0, 0, 0]
        md_bg_color: 'white'

        MDTopAppBar:
            id: toolbar
            title: "DIBTOP"
            theme_text_color: "Custom"
            elevation: 0
            pos_hint: {'top': 1}
            md_bg_color: 0.19, 0.21, 0.22, 1
            text_color: "white"

        MDBoxLayout:
            orientation: 'horizontal'
            padding: 60, 40, 60, 40
            MDBoxLayout:
                orientation: 'vertical'
                spacing: 40
                #pos_hint: {"center_x": 0.46, "center_y": 0.52}
                MDRaisedButton:
                    id: alunobtn
                    text: "ALUNOS"
                    md_bg_color: "red"
                    padding: 60, 40, 60, 40
                    font_size: 40
                    on_release: root.crud()   

                MDRaisedButton:
                    id:turmabtn
                    text: "TURMAS"
                    md_bg_color: "blue"
                    padding: 60, 40, 60, 40
                    font_size: 39
                    on_release: root.crud() 
                    
                MDRaisedButton:
                    id: cursobtn    
                    text: "CURSOS"
                    md_bg_color: "green"
                    padding: 60, 40, 60, 40
                    font_size: 40 
                    on_release: root.crud() 
                    
            MDBoxLayout:
                orientation: 'vertical'
                MDRectangleFlatIconButton:
                    icon: "android"
                    text: "GRADE DE HORÁRIOS"
                    md_bg_color: "green"
                    theme_text_color: "Custom"
                    text_color: "black"
                    #line_color: "black"
                    theme_icon_color: "Custom"
                    icon_color: "black"
                    
                    
<CrudScreen>
    MDBoxLayout:
    BoxLayout:
        orientation: 'vertical'
        spacing: 30
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint: 0.5, 0.5

        MDFillRoundFlatButton:
            text: "CADASTRAR"
            pos_hint: {'center_x':0.5,'center_y':0.75}
            #size_hint_x: 0.45
            padding: 20, 10, 20, 10
            text_color: 1,1,1,1
            md_bg_color: 0.18,0.53,1,1
            font_size: 25
            on_release: root.cadastrar()

        MDFillRoundFlatButton:
            text: "CONSULTAR"
            pos_hint: {'center_x':0.5,'center_y':0.5}
            #size_hint_x: 0.45
            padding: 20, 10, 20, 10
            text_color: 1,1,1,1
            md_bg_color: 0.18,0.53,1,1
            font_size: 25
            on_release: root.consultar()

        MDFillRoundFlatButton:
            text: "EDITAR"
            pos_hint: {'center_x':0.5,'center_y':0.25}
            #size_hint_x: 0.45
            padding: 48, 10, 48, 10
            text_color: 1,1,1,1
            md_bg_color: 0.18,0.53,1,1
            font_size: 25
            
        MDTextButton:
            text: 'Cancelar'
            on_release: root.principal()
            #pos_hint: {'center_x': .5}


<CadastrarAluno>
    MDBoxLayout:
        orientation: 'vertical'
        spacing: 2
        #pos_hint: {"center_x": 0.46, "center_y": 0.52}
        
        BoxLayout:
            orientation: 'horizontal'
            spacing: 5
            MDTextField:
                id: idnome
                hint_text:"Nome"
                pos_hint: {'center_x':0.5,'center_y':0.8}
                size_hint_x: 0.75
                max_text_length: 25
                #line_color_normal: [0,1,1,1]
                #line_color_focus: [0,1,0,1]
                
            MDTextField:
                id: idcpf
                hint_text:"CPF"
                pos_hint: {'center_x':0.5,'center_y':0.8}
                size_hint_x: 0.75
                max_text_length: 25
                #line_color_normal: [0,1,1,1]
                #line_color_focus: [0,1,0,1]
            
        MDTextField:
            id: iddtnasc
            hint_text:"dt nasc."
            pos_hint: {'center_x':0.5,'center_y':0.8}
            size_hint_x: 0.75
            max_text_length: 25
            #line_color_normal: [0,1,1,1]
            #line_color_focus: [0,1,0,1]       
            
                 
        MDTextField:
            id: idend
            hint_text:"Endereço"
            pos_hint: {'center_x':0.5,'center_y':0.8}
            size_hint_x: 0.75
            max_text_length: 25
            #line_color_normal: [0,1,1,1]
            #line_color_focus: [0,1,0,1]
            
        MDTextField:
            id: idemail
            hint_text:"Email"
            pos_hint: {'center_x':0.5,'center_y':0.8}
            size_hint_x: 0.75
            max_text_length: 25
            #line_color_normal: [0,1,1,1]
            #line_color_focus: [0,1,0,1]            
            
        MDTextField:
            id: idtel
            hint_text:"Tel."
            pos_hint: {'center_x':0.5,'center_y':0.8}
            size_hint_x: 0.75
            max_text_length: 25
            #line_color_normal: [0,1,1,1]
            #line_color_focus: [0,1,0,1]     
            
        MDTextField:
            id: idnat
            hint_text:"Naturalidade"
            pos_hint: {'center_x':0.5,'center_y':0.8}
            size_hint_x: 0.75
            max_text_length: 25
            #line_color_normal: [0,1,1,1]
            #line_color_focus: [0,1,0,1]
            
            
        MDTextField:
            id: idnomemae
            hint_text:"Nome da Mãe"
            pos_hint: {'center_x':0.5,'center_y':0.8}
            size_hint_x: 0.75
            max_text_length: 25
            #line_color_normal: [0,1,1,1]
            #line_color_focus: [0,1,0,1]   
            
        MDTextField:
            id: idestcivil
            hint_text:"Estado Civil"
            pos_hint: {'center_x':0.5,'center_y':0.8}
            size_hint_x: 0.75
            max_text_length: 25
            #line_color_normal: [0,1,1,1]
            #line_color_focus: [0,1,0,1] 
                  
        MDTextField:
            id: idesc
            hint_text:"Escolaridade"
            pos_hint: {'center_x':0.5,'center_y':0.8}
            size_hint_x: 0.75
            max_text_length: 25
            #line_color_normal: [0,1,1,1]
            #line_color_focus: [0,1,0,1]    
                  
                  
        MDRaisedButton:
            text: "SALVAR"
            md_bg_color: "green"
            pos_hint: {'center_x':0.5}
            size_hint_x: 0.75
            font_size: 20 
            on_release: root.guardar_dados()
            
        MDRaisedButton:
            text: 'CANCELAR'
            md_bg_color: "red"
            pos_hint: {'center_x':0.5}
            size_hint_x: 0.75
            font_size: 20
            #pos_hint: {'center_x': .5}
            on_release: root.principal()
            
<ConsultarAluno>
    MDBoxLayout:
        orientation: 'vertical'
        spacing: 2
        #pos_hint: {"center_x": 0.46, "center_y": 0.52}
        
        BoxLayout:
            orientation: 'horizontal'
            spacing: 5
            MDTextField:
                id: idnome
                hint_text:"Nome"
                pos_hint: {'center_x':0.5,'center_y':0.8}
                size_hint_x: 0.75
                max_text_length: 25
                #line_color_normal: [0,1,1,1]
                #line_color_focus: [0,1,0,1]
                
''')


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
            toast("Login ou senha inválidos", duration=10)


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
