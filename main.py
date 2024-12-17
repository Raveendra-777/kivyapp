from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.card import MDCard
import hashlib
import os
from kivy.utils import platform
import webbrowser
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.properties import StringProperty
if platform != 'android':
    Window.size = (400, 700)

# Get the correct path for the database
if platform == 'android':
    from android.storage import app_storage_path
    db_path = os.path.join(app_storage_path(), 'users.db')
else:
    db_path = 'users.db'

app = """
ScreenManager:
    LoginScreen:
    SignupScreen:
    HomeScreen:
    ProjectsScreen:
    ServicesScreen:
    GalleryScreen:
    ContactScreen:
    AboutScreen:
    SettingsScreen:

<LoginScreen>:
    name: 'login'
    MDCard:
        size_hint: None, None
        size: 300, 400
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        elevation: 1
        padding: 25
        spacing: 25
        orientation: 'vertical'

        MDLabel:
            text: 'Nikhil Varma Constructions'
            font_style: 'H5'
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

        MDTextField:
            id: username
            hint_text: 'username'
            icon_right: "account"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {'center_x': 0.5}

        MDTextField:
            id: password
            hint_text: 'password'
            icon_right: "eye-off"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {'center_x': 0.5}
            password: True

        MDRoundFlatButton:
            text: 'LOG IN'
            pos_hint: {'center_x': 0.5}
            on_press: root.verify_credentials()

        MDTextButton:
            text: 'Create an account'
            pos_hint: {'center_x': 0.5}
            on_press: root.manager.current = 'signup'

<SignupScreen>:
    name: 'signup'
    MDCard:
        size_hint: None, None
        size: 300, 450
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        elevation: 1
        padding: 25
        spacing: 25
        orientation: 'vertical'

        MDLabel:
            text: 'Sign Up'
            font_style: 'H5'
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

        MDTextField:
            id: new_username
            hint_text: 'username'
            icon_right: "account"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {'center_x': 0.5}

        MDTextField:
            id: new_password
            hint_text: 'password'
            icon_right: "eye-off"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {'center_x': 0.5}
            password: True

        MDTextField:
            id: confirm_password
            hint_text: 'confirm password'
            icon_right: "eye-off"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {'center_x': 0.5}
            password: True

        MDRoundFlatButton:
            text: 'SIGN UP'
            pos_hint: {'center_x': 0.5}
            on_press: root.signup()

        MDTextButton:
            text: 'Already have an account'
            pos_hint: {'center_x': 0.5}
            on_press: root.manager.current = 'login'

<HomeScreen>:
    name: 'home'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Nikhil Varma Constructions'
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
            elevation: 2
            size_hint_y: None
            height: "56dp"

        ScrollView:
            size_hint_y: 5
            MDGridLayout:
                cols: 1
                spacing: 20
                padding: 20
                size_hint_y: None
                height: self.minimum_height

                # Logo Image
                FitImage:
                    source: "assets/nvc_logo.png"
                    size_hint: None, None
                    size: "300dp", "200dp"
                    pos_hint: {"center_x": .5}

                MDCard:
                    orientation: 'vertical'
                    size_hint_x: 0.9
                    size_hint_y: None
                    height: "200dp"
                    pos_hint: {"center_x": .5}
                    MDLabel:
                        text: 'Welcome to Nikhil Varma Constructions'
                        halign: 'center'
                        theme_text_color: "Primary"
                        font_style: 'H5'

                # Tagline Card
                MDCard:
                    orientation: 'vertical'
                    size_hint_x: 0.9
                    size_hint_y: None
                    height: "100dp"
                    pos_hint: {"center_x": .5}
                    padding: 16
                    MDLabel:
                        text: 'The business of our company shall encompass all types of construction, development work, structure repairing, and waterproofing, as well as any other activities incidental to the main business.'
                        halign: 'center'
                        theme_text_color: "Secondary"

                # Quick Actions
                MDGridLayout:
                    cols: 2
                    spacing: 10
                    size_hint_x: 0.9
                    size_hint_y: None
                    height: "60dp"
                    pos_hint: {"center_x": .5}

                    MDRoundFlatButton:
                        text: 'Our Projects'
                        size_hint_x: 0.45
                        on_press: root.manager.current = 'projects'

                    MDRoundFlatButton:
                        text: 'Contact Us'
                        size_hint_x: 0.45
                        on_press: root.manager.current = 'contact'

                # Featured Projects Card
                MDCard:
                    orientation: 'vertical'
                    size_hint_x: 0.9
                    size_hint_y: None
                    height: "250dp"
                    pos_hint: {"center_x": .5}
                    padding: 16

                    MDLabel:
                        text: 'Featured Projects'
                        theme_text_color: "Primary"
                        font_style: 'H6'
                        size_hint_y: None
                        height: "48dp"

                    MDLabel:
                        text: '• Luxury Villa Project in Banjara Hills\\n• Commercial Complex in Jubilee Hills\\n• Residential Apartments in Gachibowli\\n• Office Space in HITEC City'
                        theme_text_color: "Secondary"

                # Why Choose Us Card
                MDCard:
                    orientation: 'vertical'
                    size_hint_x: 0.9
                    size_hint_y: None
                    height: "300dp"
                    pos_hint: {"center_x": .5}
                    padding: 16

                    MDLabel:
                        text: 'Why Choose Us'
                        theme_text_color: "Primary"
                        font_style: 'H6'
                        size_hint_y: None
                        height: "48dp"

                    MDLabel:
                        text: '• 20+ Years of Excellence\\n• Expert Team of Professionals\\n• Quality Construction Materials\\n• Timely Project Delivery\\n• Transparent Pricing\\n• Customer Satisfaction Focus'
                        theme_text_color: "Secondary"

                # Services Overview Card
                MDCard:
                    orientation: 'vertical'
                    size_hint_x: 0.9
                    size_hint_y: None
                    height: "300dp"
                    pos_hint: {"center_x": .5}
                    padding: 16

                    MDLabel:
                        text: 'Our Services'
                        theme_text_color: "Primary"
                        font_style: 'H6'
                        size_hint_y: None
                        height: "48dp"

                    MDLabel:
                        text: '• Residential Construction\\n• Commercial Projects\\n• Interior Design\\n• Architecture & Planning\\n• Renovation Services\\n• Project Management'
                        theme_text_color: "Secondary"

                # Recent Projects Card
                MDCard:
                    orientation: 'vertical'
                    size_hint_x: 0.9
                    size_hint_y: None
                    height: "300dp"
                    pos_hint: {"center_x": .5}
                    padding: 16

                    MDLabel:
                        text: 'Recent Projects'
                        theme_text_color: "Primary"
                        font_style: 'H6'
                        size_hint_y: None
                        height: "48dp"

                    MDLabel:
                        text: '• Modern Apartment Complex\\n  Location: Financial District\\n\\n• Corporate Office Building\\n  Location: Madhapur\\n\\n• Luxury Villas\\n  Location: Kokapet'
                        theme_text_color: "Secondary"

                # Client Testimonials Card
                MDCard:
                    orientation: 'vertical'
                    size_hint_x: 0.9
                    size_hint_y: None
                    height: "300dp"
                    pos_hint: {"center_x": .5}
                    padding: 16

                    MDLabel:
                        text: 'Client Testimonials'
                        theme_text_color: "Primary"
                        font_style: 'H6'
                        size_hint_y: None
                        height: "48dp"

                    MDLabel:
                        text: '"Exceptional quality and professional service. Highly recommended for any construction needs."\\n\\n- Raj Kumar, Hyderabad\\n\\n"Outstanding work on our villa project. The team was very responsive and delivered on time."\\n\\n- Priya Reddy, Banjara Hills'
                        theme_text_color: "Secondary"

                # Contact Info Card
                MDCard:
                    orientation: 'vertical'
                    size_hint_x: 0.9
                    size_hint_y: None
                    height: "200dp"
                    pos_hint: {"center_x": .5}
                    padding: 16

                    MDLabel:
                        text: 'Get In Touch'
                        theme_text_color: "Primary"
                        font_style: 'H6'
                        size_hint_y: None
                        height: "48dp"

                    MDLabel:
                        text: 'Phone: +91 9844052227\\nEmail: nikhilvarmaconstructions09@gmail.com\\nLocation: Banglore, Karnataka'
                        theme_text_color: "Secondary"

                MDRoundFlatButton:
                    text: 'Visit Our Website'
                    size_hint_x: 0.9
                    pos_hint: {'center_x': 0.5}
                    padding: [20, 20]
                    on_press: root.open_website()

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)
            md_bg_color: [0.1, 0.1, 0.1, 1] if app.theme_cls.theme_style == "Dark" else [1, 1, 1, 1]
            
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                # User Profile Section
                MDCard:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: "120dp"
                    padding: "8dp"
                    md_bg_color: [0.15, 0.15, 0.15, 1] if app.theme_cls.theme_style == "Dark" else [0.9, 0.9, 0.9, 1]

                    MDIcon:
                        icon: "account-circle"
                        font_size: "64dp"
                        pos_hint: {"center_x": .5}
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color

                    MDLabel:
                        id: username_label
                        text: root.username_text
                        halign: "center"
                        size_hint_y: None
                        height: "40dp"
                        theme_text_color: "Primary"
                        font_style: "H6"

                MDSeparator:
                    height: "1dp"
                
                MDList:
                    md_bg_color: [0.1, 0.1, 0.1, 1] if app.theme_cls.theme_style == "Dark" else [1, 1, 1, 1]
                    OneLineIconListItem:
                        text: 'Home'
                        theme_text_color: "Primary"
                        on_press: 
                            root.manager.current = 'home'
                            nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: 'home'
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color

                    OneLineIconListItem:
                        text: 'Projects'
                        theme_text_color: "Primary"
                        on_press: 
                            root.manager.current = 'projects'
                            nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: 'office-building'
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color

                    OneLineIconListItem:
                        text: 'Services'
                        theme_text_color: "Primary"
                        on_press: 
                            root.manager.current = 'services'
                            nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: 'tools'
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color

                    OneLineIconListItem:
                        text: 'Gallery'
                        theme_text_color: "Primary"
                        on_press: 
                            root.manager.current = 'gallery'
                            nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: 'image'
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color

                    OneLineIconListItem:
                        text: 'Contact'
                        theme_text_color: "Primary"
                        on_press: 
                            root.manager.current = 'contact'
                            nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: 'phone'
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color

                    OneLineIconListItem:
                        text: 'About'
                        theme_text_color: "Primary"
                        on_press: 
                            root.manager.current = 'about'
                            nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: 'information'
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color

                    OneLineIconListItem:
                        text: 'Settings'
                        theme_text_color: "Primary"
                        on_press: 
                            root.manager.current = 'settings'
                            nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: 'cog'
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color

                    OneLineIconListItem:
                        text: 'Logout'
                        theme_text_color: "Primary"
                        on_press: 
                            root.logout()
                            nav_drawer.set_state("close")
                        IconLeftWidget:
                            icon: 'logout'
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color

<ProjectsScreen>:
    name: 'projects'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Our Projects'
            left_action_items: [["arrow-left", lambda x: setattr(root.manager, 'current', 'home')]]
        
        ScrollView:
            MDGridLayout:
                cols: 1
                spacing: 20
                padding: 20
                size_hint_y: None
                height: self.minimum_height

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "320dp", "200dp"
                    pos_hint: {"center_x": .5}
                    padding: 16

                    MDLabel:
                        text: 'Residential Projects'
                        theme_text_color: "Primary"
                        font_style: 'H6'

                    MDLabel:
                        text: '• Luxury Villas\\n• Apartments\\n• Independent Houses'
                        theme_text_color: "Secondary"

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "320dp", "200dp"
                    pos_hint: {"center_x": .5}
                    padding: 16

                    MDLabel:
                        text: 'Commercial Projects'
                        theme_text_color: "Primary"
                        font_style: 'H6'

                    MDLabel:
                        text: '• Office Buildings\\n• Shopping Complexes\\n• Industrial Structures'
                        theme_text_color: "Secondary"

<ServicesScreen>:
    name: 'services'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Our Services'
            left_action_items: [["arrow-left", lambda x: setattr(root.manager, 'current', 'home')]]
        
        ScrollView:
            MDGridLayout:
                cols: 1
                spacing: 20
                padding: 20
                size_hint_y: None
                height: self.minimum_height

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "320dp", "150dp"
                    pos_hint: {"center_x": .5}
                    padding: 16

                    MDLabel:
                        text: 'Construction Services'
                        theme_text_color: "Primary"
                        font_style: 'H6'
                        
                    MDLabel:
                        text: '• Residential Construction\\n• Commercial Construction\\n• Renovation'
                        theme_text_color: "Secondary"

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "320dp", "150dp"
                    pos_hint: {"center_x": .5}
                    padding: 16

                    MDLabel:
                        text: 'Design Services'
                        theme_text_color: "Primary"
                        font_style: 'H6'
                        
                    MDLabel:
                        text: '• Architectural Design\\n• Interior Design\\n• 3D Visualization'
                        theme_text_color: "Secondary"

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "320dp", "150dp"
                    pos_hint: {"center_x": .5}
                    padding: 16

                    MDLabel:
                        text: 'Consulting Services'
                        theme_text_color: "Primary"
                        font_style: 'H6'
                        
                    MDLabel:
                        text: '• Project Planning\\n• Cost Estimation\\n• Site Analysis'
                        theme_text_color: "Secondary"

<GalleryScreen>:
    name: 'gallery'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Our Projects Gallery'
            left_action_items: [["arrow-left", lambda x: setattr(root.manager, 'current', 'home')]]
            elevation: 2

        ScrollView:
            MDGridLayout:
                cols: 2
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height
                width: self.minimum_width
                adaptive_height: True

                # Project Images
                MDCard:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: "250dp"
                    padding: dp(8)
                    FitImage:
                        source: "assets/gallery1.jpg"
                        radius: [10, 10, 0, 0]
                    MDLabel:
                        text: "Foundation Work"
                        halign: "center"
                        size_hint_y: None
                        height: dp(30)

                MDCard:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: "250dp"
                    padding: dp(8)
                    FitImage:
                        source: "assets/gallery2.jpg"
                        radius: [10, 10, 0, 0]
                    MDLabel:
                        text: "Steel Structure"
                        halign: "center"
                        size_hint_y: None
                        height: dp(30)

                MDCard:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: "250dp"
                    padding: dp(8)
                    FitImage:
                        source: "assets/gallery3.jpg"
                        radius: [10, 10, 0, 0]
                    MDLabel:
                        text: "Compound Wall"
                        halign: "center"
                        size_hint_y: None
                        height: dp(30)

                MDCard:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: "250dp"
                    padding: dp(8)
                    FitImage:
                        source: "assets/gallery4.jpg"
                        radius: [10, 10, 0, 0]
                    MDLabel:
                        text: "Foundation Layout"
                        halign: "center"
                        size_hint_y: None
                        height: dp(30)

                MDCard:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: "250dp"
                    padding: dp(8)
                    FitImage:
                        source: "assets/gallery5.jpg"
                        radius: [10, 10, 0, 0]
                    MDLabel:
                        text: "Arch Structure"
                        halign: "center"
                        size_hint_y: None
                        height: dp(30)

                MDCard:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: "250dp"
                    padding: dp(8)
                    FitImage:
                        source: "assets/gallery6.jpg"
                        radius: [10, 10, 0, 0]
                    MDLabel:
                        text: "Commercial Building"
                        halign: "center"
                        size_hint_y: None
                        height: dp(30)

        

<ContactScreen>:
    name: 'contact'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Contact Us'
            left_action_items: [["arrow-left", lambda x: setattr(root.manager, 'current', 'home')]]
        
        ScrollView:
            MDGridLayout:
                cols: 1
                spacing: 20
                padding: 20
                size_hint_y: None
                height: self.minimum_height

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "320dp", "200dp"
                    pos_hint: {"center_x": .5}
                    padding: 16

                    MDLabel:
                        text: 'Contact Information'
                        theme_text_color: "Primary"
                        font_style: 'H6'

                    MDLabel:
                        text: 'Phone: +91 98744052227\\nEmail: nikhilvarmaconstructions09@gmail.com\\nAddress: Banglore, Karnataka'
                        theme_text_color: "Secondary"

                MDRoundFlatButton:
                    text: 'Visit Website'
                    pos_hint: {'center_x': 0.5}
                    on_press: root.open_website()

<AboutScreen>:
    name: 'about'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'About Us'
            left_action_items: [["arrow-left", lambda x:setattr(root.manager, 'current', 'home')]]
            elevation: 2

        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: dp(20)
                spacing: dp(20)

                MDCard:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: title.height + content.height + dp(40)
                    padding: dp(20)
                    
                    MDLabel:
                        id: title
                        text: "ABOUT US"
                        size_hint_y: None
                        height: self.texture_size[1]
                        halign: 'center'
                        theme_text_color: "Primary"
                        font_style: "H5"
                        bold: True
                        padding: [0, 0, 0, dp(20)]

                    MDLabel:
                        id: content
                        text: "Proudly we are NIKHIL VARMA CONSTRUCTIONS is a Proprietorship concern started in 2020,\\nwe are a rapidly emerging for all kind of Civil works, Structure repairing & Water Proofing etc, in Bangalore.\\n\\n\\nYoung and self-motivated directors Mr PRAVVEEN KUMAR is founder of this company. This Firm is the brainchild of our founder who has more than 20 years of vast Experience in Civil works & Structure repairing & Water proofing as an employee in multiple companies. Further due to vast experience and business expertise of our founder, we have survived in intense competition in industry."
                        size_hint_y: None
                        height: self.texture_size[1]
                        halign: 'left'
                        theme_text_color: "Secondary"
                        font_style: "Body1"

<SettingsScreen>:
    name: 'settings'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Settings'
            left_action_items: [["arrow-left", lambda x: setattr(root.manager, 'current', 'home')]]
        
        ScrollView:
            MDGridLayout:
                cols: 1
                spacing: 20
                padding: 20
                size_hint_y: None
                height: self.minimum_height

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "320dp", "400dp"
                    pos_hint: {"center_x": .5}
                    padding: 16

                    MDLabel:
                        text: 'Account Settings'
                        theme_text_color: "Primary"
                        font_style: 'H6'
                        size_hint_y: None
                        height: "48dp"

                    MDSeparator:
                        height: "1dp"

                    MDList:
                        OneLineIconListItem:
                            text: "Change Password"
                            on_press: root.show_change_password_dialog()
                            IconLeftWidget:
                                icon: "key"

                        OneLineIconListItem:
                            text: "Notification Settings"
                            on_press: root.show_notification_settings()
                            IconLeftWidget:
                                icon: "bell"

                        OneLineIconListItem:
                            text: "Theme"
                            on_press: root.show_theme_settings()
                            IconLeftWidget:
                                icon: "palette"

                        OneLineIconListItem:
                            text: "Privacy"
                            on_press: root.show_privacy_settings()
                            IconLeftWidget:
                                icon: "shield-account"

                MDCard:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: "320dp", "200dp"
                    pos_hint: {"center_x": .5}
                    padding: 16
                    md_bg_color: [0.1, 0.1, 0.1, 1] if app.theme_cls.theme_style == "Dark" else [1, 1, 1, 1]

                    MDLabel:
                        text: 'App Information'
                        theme_text_color: "Primary"
                        font_style: 'H6'
                        size_hint_y: None
                        height: "48dp"

                    MDSeparator:
                        height: "1dp"

                    MDList:
                        OneLineIconListItem:
                            text: "Version 1.0.0"
                            IconLeftWidget:
                                icon: "information"

                        OneLineIconListItem:
                            text: "Check for Updates"
                            on_press: root.check_updates()
                            IconLeftWidget:
                                icon: "update"

"""

class ChangePasswordContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = "12dp"
        self.size_hint_y = None
        self.height = "200dp"
        self.padding = ["24dp", "0dp", "24dp", "0dp"]
        
        self.current_password = MDTextField(
            hint_text="Current Password",
            password=True,
        )
        self.new_password = MDTextField(
            hint_text="New Password",
            password=True,
        )
        self.confirm_password = MDTextField(
            hint_text="Confirm New Password",
            password=True,
        )
        
        self.add_widget(self.current_password)
        self.add_widget(self.new_password)
        self.add_widget(self.confirm_password)

class NotificationContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = "12dp"
        self.size_hint_y = None
        self.height = "120dp"
        self.padding = ["24dp", "0dp", "24dp", "0dp"]

        # Push Notifications Row
        push_box = MDBoxLayout(orientation="horizontal", adaptive_height=True)
        push_label = MDLabel(
            text="Push Notifications",
            theme_text_color="Primary",
            size_hint_y=None,
            height="48dp"
        )
        self.push_switch = MDSwitch()
        push_box.add_widget(push_label)
        push_box.add_widget(self.push_switch)

        # Email Notifications Row
        email_box = MDBoxLayout(orientation="horizontal", adaptive_height=True)
        email_label = MDLabel(
            text="Email Notifications",
            theme_text_color="Primary",
            size_hint_y=None,
            height="48dp"
        )
        self.email_switch = MDSwitch()
        email_box.add_widget(email_label)
        email_box.add_widget(self.email_switch)

        self.add_widget(push_box)
        self.add_widget(email_box)

class ThemeContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = "12dp"
        self.size_hint_y = None
        self.height = "120dp"
        self.padding = ["24dp", "0dp", "24dp", "0dp"]

        # Theme Mode Row
        theme_box = MDBoxLayout(orientation="horizontal", adaptive_height=True)
        theme_label = MDLabel(
            text="Dark Mode",
            theme_text_color="Primary",
            size_hint_y=None,
            height="48dp"
        )
        self.theme_switch = MDSwitch()
        # Set initial state based on current theme
        app = MDApp.get_running_app()
        self.theme_switch.active = app.theme_cls.theme_style == "Dark"
        
        theme_box.add_widget(theme_label)
        theme_box.add_widget(self.theme_switch)
        self.add_widget(theme_box)

class LoginScreen(Screen):
    def verify_credentials(self):
        username = self.ids.username.text
        password = self.ids.password.text
        
        if not username or not password:
            self.show_error_dialog("Please fill in all fields")
            return
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Hash the password for comparison
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, hashed_password))
        user = cursor.fetchone()
        
        conn.close()
        
        if user:
            app = MDApp.get_running_app()
            app.current_user = username
            print(f"Logged in as: {username}")  # Debug print
            
            # Update username immediately
            home_screen = self.manager.get_screen('home')
            home_screen.username_text = username
            print(f"Set home screen username to: {username}")  # Debug print
            
            self.manager.current = 'home'
        else:
            self.show_error_dialog("Invalid username or password")

    def show_error_dialog(self, error_text):
        dialog = MDDialog(
            title="Error",
            text=error_text,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

class SignupScreen(Screen):
    def signup(self):
        username = self.ids.new_username.text
        password = self.ids.new_password.text
        confirm_password = self.ids.confirm_password.text
        
        if not username or not password or not confirm_password:
            self.show_dialog("Error", "Please fill in all fields")
            return
            
        if password != confirm_password:
            self.show_dialog("Error", "Passwords do not match")
            return
            
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        
        c.execute('''CREATE TABLE IF NOT EXISTS users
                    (username TEXT PRIMARY KEY, password TEXT)''')
        
        try:
            c.execute('''INSERT INTO users (username, password)
                        VALUES (?, ?)''', (username, hashed_password))
            conn.commit()
            self.show_dialog("Success", "Account created successfully")
            self.manager.current = 'login'
        except sqlite3.IntegrityError:
            self.show_dialog("Error", "Username already exists")
        
        conn.close()
    
    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

class HomeScreen(Screen):
    username_text = StringProperty("")
    
    def on_enter(self):
        app = MDApp.get_running_app()
        if app.current_user:
            self.username_text = app.current_user
            print(f"Set username_text to: {self.username_text}")

    def update_username(self, username):
        if username:
            self.username_text = username
            print(f"Updated username_text to: {username}")

    def logout(self, *args):
        app = MDApp.get_running_app()
        app.current_user = None
        self.username_text = ""
        self.manager.current = 'login'

    def open_website(self):
        webbrowser.open('http://www.nikhilvarmaconstructions.com')

class ProjectsScreen(Screen):
    pass

class ServicesScreen(Screen):
    pass

class GalleryScreen(Screen):
    pass

class ContactScreen(Screen):
    def open_website(self):
        webbrowser.open('http://www.nikhilvarmaconstructions.com')

class AboutScreen(Screen):
    pass

class SettingsScreen(Screen):
    def show_change_password_dialog(self):
        content = ChangePasswordContent()
        self.dialog = MDDialog(
            title="Change Password",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_release=lambda x: self.dialog.dismiss()
                ),
                MDRaisedButton(
                    text="SAVE",
                    on_release=lambda x: self.change_password(content)
                ),
            ],
        )
        self.dialog.open()

    def change_password(self, content):
        current_password = content.current_password.text
        new_password = content.new_password.text
        confirm_password = content.confirm_password.text
        
        if not current_password or not new_password or not confirm_password:
            self.show_error_dialog("Please fill in all fields")
            return
            
        if new_password != confirm_password:
            self.show_error_dialog("New passwords do not match")
            return
            
        # Hash the passwords for comparison
        hashed_current = hashlib.sha256(current_password.encode()).hexdigest()
        hashed_new = hashlib.sha256(new_password.encode()).hexdigest()
        
        # Get username from app class
        app = MDApp.get_running_app()
        username = app.current_user
        
        if not username:
            self.show_error_dialog("Please log in again")
            self.dialog.dismiss()
            self.manager.current = 'login'
            return
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        try:
            # Verify current password
            cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, hashed_current))
            user = cursor.fetchone()
            
            if user:
                # Update password
                cursor.execute('UPDATE users SET password=? WHERE username=?', (hashed_new, username))
                conn.commit()
                self.show_success_dialog("Password updated successfully")
            else:
                self.show_error_dialog("Current password is incorrect")
        except sqlite3.Error as e:
            self.show_error_dialog(f"Database error: {str(e)}")
        finally:
            conn.close()
            self.dialog.dismiss()

    def show_error_dialog(self, error_text):
        dialog = MDDialog(
            title="Error",
            text=error_text,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def show_success_dialog(self, message):
        dialog = MDDialog(
            title="Success",
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def show_notification_settings(self):
        content = NotificationContent()
        self.dialog = MDDialog(
            title="Notification Settings",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_release=lambda x: self.dialog.dismiss()
                ),
                MDRaisedButton(
                    text="SAVE",
                    on_release=lambda x: self.save_notification_settings(content)
                ),
            ],
        )
        self.dialog.open()

    def save_notification_settings(self, content):
        # Get the switch states
        push_enabled = content.push_switch.active
        email_enabled = content.email_switch.active
        
        # Get current user
        app = MDApp.get_running_app()
        username = app.current_user
        
        if not username:
            self.show_error_dialog("Please log in again")
            self.dialog.dismiss()
            self.manager.current = 'login'
            return
            
        # Here you can save the settings to a database or file
        # For now, we'll just show a success message
        self.show_success_dialog(
            f"Settings saved:\nPush Notifications: {'On' if push_enabled else 'Off'}\n"
            f"Email Notifications: {'On' if email_enabled else 'Off'}"
        )
        self.dialog.dismiss()

    def show_theme_settings(self):
        content = ThemeContent()
        self.dialog = MDDialog(
            title="Theme Settings",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_release=lambda x: self.dialog.dismiss()
                ),
                MDRaisedButton(
                    text="SAVE",
                    on_release=lambda x: self.save_theme_settings(content)
                ),
            ],
        )
        self.dialog.open()

    def save_theme_settings(self, content):
        # Get the theme state
        dark_mode = content.theme_switch.active
        
        # Update the theme
        app = MDApp.get_running_app()
        app.theme_cls.theme_style = "Dark" if dark_mode else "Light"
        
        # Show success message
        self.show_success_dialog(f"Theme changed to {'Dark' if dark_mode else 'Light'} mode")
        self.dialog.dismiss()

    def show_privacy_settings(self):
        dialog = MDDialog(
            title="Privacy Settings",
            text="Manage your privacy settings",
            buttons=[
                MDFlatButton(
                    text="CLOSE",
                    on_release=lambda x: dialog.dismiss()
                ),
            ],
        )
        dialog.open()

    def check_updates(self):
        dialog = MDDialog(
            title="Check for Updates",
            text="Your app is up to date!",
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                ),
            ],
        )
        dialog.open()

class MYApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        self.current_user = None
        return Builder.load_string(app)

    def on_start(self):
        print("App starting...")  # Debug print
        Clock.schedule_once(self.init_ui, 0.1)

    def init_ui(self, dt):
        print(f"Initializing UI with user: {self.current_user}")  # Debug print
        try:
            home_screen = self.root.get_screen('home')
            home_screen.update_username(self.current_user)
        except Exception as e:
            print(f"Error initializing UI: {e}")

if __name__ == '__main__':
    MYApp().run()
