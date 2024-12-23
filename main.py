from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
import requests
import time as t
import random as r
from github import Github
import json
from kivymd.uix.dialog import MDDialog as mdd
from kivymd.uix.button import MDRectangleFlatButton
web_app_url = 'https://script.google.com/macros/s/AKfycbzOQnvvZze0rIl8F79wnR3DZ3qdtMw2DW3OzEMi7ZB3Vdz-oGH9IZ5_NjICzi9RaMUr/exec'



win=Window.size=(400,700)

kv = """
ScreenManager:
    Signin:
    Email:
    OTP:
    Signup:
    Home:
    Profile:
    Services:
    Gallery:
<Signin>:
    name:'in'
    MDLabel:
        text:"Nikhil Varma Constructions"
        halign:"center"
        pos_hint:{"top":1.4}
    MDCard:
        elevation:5
        padding: 25
        spacing: 25
        size_hint:None, None
        size:300,400
        orientation: 'vertical'
        padding: dp(10)
        pos_hint:{"center_x":0.5,"center_y":0.5}
        MDLabel:
            size_hint_y: None
            height: self.texture_size[1]
            halign: 'center'
            text:"SignIn"
            halign:"center"
            paddying_y:15
        MDTextField:
            id: username
            hint_text: 'username'
            icon_right: "account"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {'center_x': 0.5}
        MDTextField:
            id: pas
            hint_text: 'password'
            icon_right: "eye-off"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {'center_x': 0.5}
            password:True
        MDRectangleFlatButton:
            text:"SignIn"
            pos_hint: {'center_x': 0.5}
            on_release:root.signin()
        MDTextButton:
            text:"Don't Have Account? SignUp!"
            pos_hint: {'center_x': 0.5}
            on_press:
                root.manager.current = "up"
                

<Email>:
    name:'mail'
    MDLabel:
        text:"Nikhil Varma Constructions"
        halign:"center"
        pos_hint:{"top":1.4}
        paddying_y:10
    MDCard:
        elevation:5
        padding: 25
        spacing: 25
        size_hint:None, None
        size:250,300
        orientation: 'vertical'
        padding: dp(10)
        pos_hint:{"center_x":0.5,"center_y":0.5}
        MDLabel:
            text:"Verification"
            height: self.texture_size[1]
            halign: 'center'
            
            halign:"center"
            paddying_y:15
        MDTextField:
            id:em
            hint_text:"enter your email"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {'center_x': 0.5}
            
            icon_right:"numeric-0"
        MDRectangleFlatButton:
            text:"Send OTP"
            pos_hint:{"center_x":0.5}
            on_release:
                root.sotp()
                root.manager.current="otp"
        MDTextButton:
            text:"Go Back"
            pos_hint: {'center_x': 0.5}
            on_press:root.manager.current = "in"
        
<OTP>:
    name:"otp"
    MDLabel:
        text:"Nikhil Varma Constructions"
        halign:"center"
        pos_hint:{"top":1.4}
        paddying_y:10
    MDCard:
        elevation:5
        padding: 25
        spacing: 25
        size_hint:None, None
        size:250,350
        orientation: 'vertical'
        padding: dp(10)
        pos_hint:{"center_x":0.5,"center_y":0.5}
        MDLabel:
            text:"Verification"
            height: self.texture_size[1]
            halign: 'center'
            
            halign:"center"
            paddying_y:15
        MDTextField:
            id:ott
            hint_text:"enter OTP"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {'center_x': 0.5}
            password:True
            icon_right:"numeric-0"
        MDLabel:
            size_hint_y: None
            height: self.texture_size[1]
            halign: 'center'
            text:""
            id:vert
            halign:"center"
            paddying_y:15
        MDTextButton:
            text:"Resend OTP!"
            pos_hint: {'center_x': 0.5}
            color:(0,0,1,1)
            on_press:
                root.sotp2()
        MDRectangleFlatButton:
            text:"Verify OTP"
            pos_hint:{"center_x":0.5}
            on_release:
                root.ver()
        MDTextButton:
            text:"Go Back"
            pos_hint: {'center_x': 0.5}
            on_press:
                root.manager.current = "mail"
               
                
<Signup>:
    name:"up"
    MDLabel:
        text:"Nikhil Varma Constructions"
        halign:"center"
        pos_hint:{"top":1.4}
        paddying_y:10
    MDCard:
        elevation:5
        padding: 25
        spacing: 25
        size_hint:None, None
        size:300,450
        orientation: 'vertical'
        padding: dp(10)
        pos_hint:{"center_x":0.5,"center_y":0.5}
        MDLabel:
            size_hint_y: None
            height: self.texture_size[1]
            halign: 'center'
            text:"SignIn"
            halign:"center"
            paddying_y:15
        MDTextField:
            id: upusername
            hint_text: 'username'
            icon_right: "account"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {'center_x': 0.5}
        MDTextField:
            id: uppas
            hint_text: 'new password'
            icon_right: "eye-off"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {'center_x': 0.5}
            password:True
        MDTextField:
            id: uphipas
            hint_text: 'confrim password'
            icon_right: "eye-off"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {'center_x': 0.5}
            password:True
        MDRectangleFlatButton:
            text:"SignUp"
            pos_hint: {'center_x': 0.5}
            on_release:
                root.cre()
                
                
        MDTextButton:
            text:"Have an Account? SignIn!"
            pos_hint: {'center_x': 0.5}
            on_press:root.manager.current = "in"

<Home>:
    name:"home"
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title:"Nikhil Varma Constructions"
                        left_action_items:[["menu", lambda x:nav.set_state("open")]]
                        pos_hint:{"center_x":.5}
                   
                    
                    ScrollView:
                        halign:"center"
                        id:sc
                        padding: 25
                        spacing: 25
                            
                        size_hint: (1, 700)
                        orientation: 'vertical'
                        padding: dp(10)
                        pos_hint:{"center_x":0.5,"center_y":0.5}
                        BoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: self.minimum_height
                            MDCard:
                                halign: "center"
                                elevation: 5
                                padding: 25
                                spacing: 25
                                size_hint: None, None
                                size: 350, 300
                                orientation: 'vertical'
                                padding: dp(10)
                                pos_hint: {"center_x": 0.5}
                                Image:
                                    source:
                    
        MDNavigationDrawer:
            id:nav
            orientation:"vertical"
            MDCard:
                size_hint:None, None
                size:300,200
                elevation:2
                MDIcon:
                    font_size:"200dp"
                    halign:"center"
                    
                    icon:"account-circle"
            MDLabel:
                id:use
                
                size_hint_y:None
                text:""
                height: "60dp"
                halign: "center"
            ScrollView:
                MDList:

                    OneLineIconListItem:
                        text:"Company Profile"
                        on_release:
                            root.manager.current = 'pro'
                            nav.set_state("close")
                        IconLeftWidget:
                            icon:"face-man-profile"
                    OneLineIconListItem:
                        text:"Services"
                        on_release:
                            root.manager.current = 'ser'
                            nav.set_state("close")
                        IconLeftWidget:
                            icon:"tools"
                    OneLineIconListItem:
                        text:"Gallery"
                        on_release:
                            root.manager.current = 'gal'
                            nav.set_state("close")
                        IconLeftWidget:
                            icon:"image"
                    OneLineIconListItem:
                        text:"LogOut"
                        theme_text_color:"Error"
                        on_release:
                            root.manager.current = 'in'
                            nav.set_state("close")
                            root.clr()
                        IconLeftWidget:
                            icon:"logout"
                            theme_text_color:"Error"
<Profile>:
    name:'pro'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDTopAppBar:
                    title:"Company Profile"
                    left_action_items:[["arrow-left", lambda x:setattr(root.manager,'current','home')]]
                    pos_hint:{"top":1}
                Widget:
<Services>:
    name:"ser"
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDTopAppBar:
                    title:"Services"
                    left_action_items:[["arrow-left", lambda x:setattr(root.manager,'current','home')]]
                    pos_hint:{"top":1}
                Widget:
<Gallery>:
    name:"gal"
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDTopAppBar:
                    title:"Gallery"
                    left_action_items:[["arrow-left", lambda x:setattr(root.manager,'current','home')]]
                    pos_hint:{"top":1}
                Widget:
            
"""
import base64
token = ""
repo_name = "Raveendra-777/new"
def text_to_binary(text):
    binary_result = ''.join(format(ord(char), '08b') for char in text)
    return binary_result
def binary_to_text(binary_str):
    # Split the binary string into 8-bit chunks
    binary_values = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    
    # Convert each binary value to the corresponding ASCII character
    text = ''.join([chr(int(bv, 2)) for bv in binary_values])
    
    return text

# Example usage


commit_message = "Append new data to user.json file"
g = Github(token)
file_path = "user.json"
repo = g.get_repo(repo_name)
class Signup(Screen):
    def cre(self):
        
        global file_path
        global repo
        
        
        # Replace with your GitHub token
        
        username = self.ids.upusername.text
        password = self.ids.uppas.text

        # Authenticate using the token
        
        

        # Get the file
        file = repo.get_contents(file_path, ref='main')
        ttb=text_to_binary(self.ids.uppas.text)
        sk = base64.b64encode(ttb.encode()).decode()
        # Load the existing JSON content
        content = json.loads(file.decoded_content.decode())
        file_content = repo.get_contents(file_path, ref='main')
        f = json.loads(file_content.decoded_content.decode()) 
        # Append the new content
        if "acc" not in content:
            content["acc"] = []
        content["acc"].append({
            "username": username,
            "password": sk
        })
        try:
        
            for user in f["acc"]:
                if username == user["username"]:
                    print("usename arleady Exists")
                    self.d6d = mdd(
                    title="This Username Arleady Exists! enter other username!",
                    buttons=[MDRectangleFlatButton(text="OK", on_release=self.di6)]
                        )
                    self.d6d.open()
                    return
            
            if self.ids.upusername.text =="" or self.ids.uppas.text=="" or self.ids.uphipas.text=="":
                self.ddd = mdd(
                title="Enter Your Credentials!",
                buttons=[MDRectangleFlatButton(text="OK", on_release=self.dis)]
                    )
                self.ddd.open()
            
            
                
            else:

            # Convert back to JSON string
            
                if password==self.ids.uphipas.text:
                    new_content = json.dumps(content, indent=2)
                    repo.update_file(file.path, commit_message, new_content, file.sha, branch='main')
                    print(f"File {file_path} updated successfully.")
                    self.d = mdd(
                    title="Account Created!",
                    buttons=[MDRectangleFlatButton(text="OK", on_release=self.ok)]
                        )
                    self.d.open()
                    
                elif password!=self.ids.uphipas.text:
                    print("password didnot match")
                    self.d = mdd(
                    title="password did not match!",
                    buttons=[MDRectangleFlatButton(text="OK", on_release=self.kk)]
                        )
                    self.d.open()
        except KeyError:
            return
            
        # Update the file
        

        # Get the updated file content
    def dis(self, obj):
        self.ddd.dismiss()
    def di6(self, obj):
        self.d6d.dismiss()
    def ok(self, obj):
        self.d.dismiss()
        self.manager.current='in'
    def kk(self, obj):
        self.d.dismiss()
        self.manager.current="up"
use = ""
class Signin(Screen):
    def signin(self):
        global file_path
        global repo
        global use
        file_content = repo.get_contents(file_path, ref='main')
        f = json.loads(file_content.decoded_content.decode())
        username_entered = self.ids.username.text
        password_entered = self.ids.pas.text

        if username_entered == "" or password_entered == "":
            self.dd = mdd(
                title="Enter Username and Password!",
                buttons=[MDRectangleFlatButton(text="OK", on_release=self.di)]
            )
            self.dd.open()
            return
        
        for user in f["acc"]:
            up = user["password"]
            decoded_bytes = base64.b64decode(up)
            binary_string = ''.join(format(byte, '08b') for byte in decoded_bytes)
            b=binary_to_text(binary_string)
            txt = binary_to_text(b)
            if username_entered == user["username"] and password_entered == txt:
                use = username_entered 
                self.manager.current = 'home'
                return

        self.d5d = mdd(
            title="Incorrect Username or Password",
            buttons=[MDRectangleFlatButton(text="OK", on_release=self.di5)]
        )
        self.d5d.open()

    def di(self, obj):
        self.dd.dismiss()

    def di5(self, obj):
        self.d5d.dismiss()
ran=None
e = ""
class Email(Screen):
    def sotp(self):
        global ran
        global e
        ran = r.randint(1000,9999)
        data = {
    'email': f'{self.ids.em.text}',
    'subject': 'Verificationcode',
    'message': f'Verification code:{ran}'
}
        e = self.ids.em.text
        response = requests.post(web_app_url, json=data)
        print(response.text)
        
class OTP(Screen):
    
        
    def ver(self):
        try:
            global ran
            if ran == int(self.ids.ott.text):
                print("verified")
                self.d2d = mdd(
                title="OTP Verified!",
                buttons=[MDRectangleFlatButton(text="OK", on_release=self.di2)]
                    )
                self.d2d.open()
                
                
            else:
                print("not Verifield")
                self.d3d = mdd(
                title="OTP Not Verified!",
                buttons=[MDRectangleFlatButton(text="OK", on_release=self.di3)]
                    )
                self.d3d.open()
        except ValueError as e:
                self.d4d = mdd(
                title=f"Enter a Valid OTP Number Please",
                buttons=[MDRectangleFlatButton(text="OK", on_release=self.di4)]
                    )
                self.d4d.open()
    def sotp2(self):
        global ran
        global e
        ran = r.randint(1000,9999)
        data = {
    'email': f'{e}',
    'subject': 'Verificationcode',
    'message': f'Verification code:{ran}'
}
        
        response = requests.post(web_app_url, json=data)
        print(response.text)
    def di2(self, obj):
        self.d2d.dismiss()
        self.manager.current='home'
    def di4(self, obj):
        self.d4d.dismiss()
    def di3(self, obj):
        self.d3d.dismiss()


class Home(Screen):
    global use
    global e
    def on_pre_enter(self, *args):
        uses = f"Hello, {use}\n email:{e}"
        self.ids.use.text = uses
        

    def clr(self):
        screen_manager = self.manager
        if 'mail' in screen_manager.screen_names:
            mail = screen_manager.get_screen('mail')
            mail.ids.em.text=""
        if 'otp' in screen_manager.screen_names:
            otp = screen_manager.get_screen('otp')
            otp.ids.vert.text=""
            otp.ids.ott.text=""
        # Clear fields in the 'in' screen (Signin screen)
        if 'in' in screen_manager.screen_names:
            signin_screen = screen_manager.get_screen('in')
            signin_screen.ids.username.text = ""
            signin_screen.ids.pas.text = ""

        # Clear fields in the 'up' screen (Signup screen)
        if 'up' in screen_manager.screen_names:
            signup_screen = screen_manager.get_screen('up')
            signup_screen.ids.upusername.text = ""
            signup_screen.ids.uppas.text = ""
            signup_screen.ids.uphipas.text = ""
class Profile(Screen):
    pass
class Services(Screen):
    pass
class Gallery(Screen):
    pass
sm = ScreenManager()
sm.add_widget(Signin(name='in'))
sm.add_widget(Signup(name='up'))
sm.add_widget(Email(name='mail'))
sm.add_widget(OTP(name='otp'))
sm.add_widget(Home(name='home'))
sm.add_widget(Profile(name='pro'))
sm.add_widget(Services(name='ser'))
sm.add_widget(Gallery(name='gal'))
class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)
if __name__ == "__main__":
    MyApp().run()
