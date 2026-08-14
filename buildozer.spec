[app] android.accept_sdk_license = True
# (str) Title of your application
title = Scilingo
# (str) Package name
package.name = scilingo
# (str) Package domain (needed for android/ios packaging)
package.domain = org.parsifal

# (str) Source code where the main.py lives
source.dir = .
# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2
warn_on_root = 1
