[app]

title = Nikhil Varma Constructions
package.name = nvc
package.domain = org.nvc
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
version.filename = %(source.dir)s/main.py
requirements = python3,kivy,kivymd,pygithub,requests,pillow
icon.filename = %(source.dir)s/assets/icon.png
orientation = portrait

[buildozer]

log_level = 2
warn_on_root = 1

[android]

android.permissions = android.permission.INTERNET,android.permission.WRITE_EXTERNAL_STORAGE
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.debug_artifact = apk
android.release_artifact = aab

# Remove any conflicting settings or old cached configurations before building
