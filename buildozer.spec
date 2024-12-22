[app]

# (str) Title of your application
title = Nikhil Varma Constructions

# (str) Package name
package.name = nikhil_varma_constructions

# (str) Package domain (needed for android/ios packaging)
package.domain = org.kivy

# (str) Source code where the main.py is located
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to include (let empty to include all the files)
source.include_patterns = assets/*,data/*

# (str) Source directory
source.dir = .

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd,requests,pygithub

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/assets/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/assets/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) API key for Google Cloud Messaging (required for firebase notification)
android.firebase.gcm_sender_id = YOUR_GCM_SENDER_ID

# (list) Permissions
# Permissions required by the application
android.permissions = INTERNET

# (bool) Enable the creation of a debug (unecrypted) apk
debug = 1

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) Path to Android NDK
#android.ndk_path = /home/user/android-ndk-r23b

# (str) Path to Android SDK
#android.sdk_path = /home/user/android-sdk

# (str) Path to Android SDK
#android.gradle_path = /home/user/.gradle

# (str) Android entry point, default is ok for Kivy-based apps
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android's native code
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Additional Java dependencies to be added to the project
#android.add_jars = libs/android-support-v4.jar, libs/android-support-v7-recyclerview.jar

# (list) Android application meta-data to set
#android.meta_data =

# (list) Android libraries to include
#android.add_libraries =

# (list) Android AAR libraries to include
#android.gradle_dependencies = 

# (list) Android add python package requirements
#android.p4a_recommendations =

# (list) Android add requirements that are not python packages
#android.p4a_non_python_requirements =

# (str) Custom package names for the bootstrap (default is "sdl2")
#android.bootstrap = sdl2

# (list) Screens to include in the application
#android.screens = normal,large,xlarge

# (str) Presplash of the application
#android.presplash_color = #FFFFFF
