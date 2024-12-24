from kivymd.app import MDApp #import kivymd app
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDFloatingActionButton
#from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
class KivyApp(MDApp):
    def build(self):
        
        self.theme_cls.primary_palette="Red"
        self.theme_cls.theme_style="Dark"
        """
        scr = Screen()
        label2 = MDLabel(text="Raveendra Varma's Project", pos_hint={"center_x":0.55,"center_y":0.7}, size_hint_x=None,width=500,theme_text_color="Custom", text_color=(1,0,0,1), font_style="H3")
        label = MDLabel(text="Hello!", pos_hint={"center_x":1.1,"center_y":0.5},theme_text_color="Custom", text_color=(0,1,0,1), font_style="Caption")
        icon = MDIcon(icon="android",pos_hint={"center_x":0.8,"center_y":0.5})
        btn = MDRectangleFlatButton(text="hello!", pos_hint={"center_x":0.5,"center_y":0.5})
        btn2 = MDFloatingActionButton(icon="language-python", pos_hint={"center_x":0.7,"center_y":0.5})
        inp = MDTextField(text="enter here! it is kivy MD MDTextfield's", pos_hint={"center_x":0.5,"center_y":0.4},size_hint_x=None, width=300)
        scr.add_widget(btn)
        scr.add_widget(label)
        scr.add_widget(label2)
        scr.add_widget(btn2)
        scr.add_widget(icon)
        scr.add_widget(inp)"""
        b = Builder.load_string("""
Screen:
    ScrollView:
        MDList:
            TwoLineListItem:
                id:li
                text:"hello"
                secondary_text:"hi hello how are you"
            
            
    MDLabel:
        text:"Raveendra Varma's Turtorial Project"
        pos_hint:{"center_x":0.6,"center_y":0.7}
        size_hint_x:None
        text_size:500,None
        font_style:"H3"
        color:(1,0,0,1)
    MDTextField:
        id:t
        hint_text:"enter Here!"
        helper_text:"you can type here anything! it is kivy builder's text field!"
        pos_hint:{"center_x":0.5,"center_y":0.3}
        size_hint_x:None
        icon_left:"language-python"
        width:300
        on_text_validate:app.show()
    MDRectangleFlatButton:
        text:"Send"
        pos_hint:{"center_x":0.5,"center_y":0.2}
        on_release:app.show()
    ScrollView:
        MDLabel:
            id:txt
            text:"hi Iam a app created by Raveendra Varma"
            pos_hint:{"center_x":0.5,"center_y":0.1}
            size_hint_x:0.3
            text_size:self.width,None
            
            color:(1,0,0,1)
    MDCard:
        size_hint:None, None
        size:200,200
        padding:20
        MDLabel:
            text:"hi"
        MDRectangleFlatButton:
            text:"hi"
        
    
        
    
""")
        
       # scr.add_widget(b)
        return b
    def show(self):

            
        t = self.root.ids.t
        if t.text == "":
            self.di3 = MDDialog(title="Type Somthing Else", text="", buttons=[MDRectangleFlatButton(text="CLOSE", on_release=self.dis3)])
            self.di3.open()
        else:
            print(f"typed:{t.text}")
            self.txt = self.root.ids.txt
            self.txt.text = f"you typed:{t.text}"
            self.txt.width=100
            self.di = MDDialog(title="You Typed:", text=t.text, buttons=[MDRectangleFlatButton(text="CLOSE", on_release=self.dis), MDRectangleFlatButton(text="MORE", on_release=self.more)])
            self.di.open()
            t.text=""
    def more(self, obj):
        self.di.dismiss()
        self.di2 = MDDialog(title="www.nikhilvarmaconstructions.com-About", text="Proudly we are NIKHIL VARMA CONSTRUCTIONS is a Proprietorship concern started in 2020,\nwe are a rapidly emerging for all kind of Civil works, Structure repairing & Water Proofing etc, in Bangalore.\n\n\n\nYoung and self-motivated directors Mr PRAVVEEN KUMAR is founder of this company. This Firm is the brainchild of our founder who has more than 20 years of vast Experience in Civil works & Structure repairing & Water proofing as an employee in multiple companies. Further due to vast experience and business expertise of our founder, we have survived in intense competition in industry.", buttons=[MDRectangleFlatButton(text="CLOSE", on_release=self.dis2)])
        self.di2.open()
    def dis(self, obj):
        self.di.dismiss()
    def dis2(self, obj):
        self.di2.dismiss()
    def dis3(self, obj):
        self.di3.dismiss()
        
if __name__ == "__main__":
    KivyApp().run() #run the app
