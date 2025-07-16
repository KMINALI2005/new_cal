[app]
# اسم التطبيق
title = Smart Calculator
package.name = smartcalculator
package.domain = com.example.smartcalc

# إعدادات المصدر
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,txt
source.exclude_dirs = tests,bin,.buildozer
source.exclude_patterns = license,images/*/*.jpg

# إصدار التطبيق
version = 1.0
version.regex = __version__ = ['"]([^'"]*)['"]
version.filename = %(source.dir)s/main.py

# متطلبات Python
requirements = python3,kivy==2.1.0,pillow,android,pyjnius

# إعدادات التطبيق
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png
orientation = portrait
fullscreen = 0

# صلاحيات Android
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE

# إعدادات Android SDK/NDK
android.api = 30
android.minapi = 21
android.ndk = 23.2.8568313
android.sdk = 30
android.accept_sdk_license = True

# معمارية المعالج
android.archs = armeabi-v7a,arm64-v8a

# إعدادات Gradle
android.gradle_dependencies = 
android.add_java_dir = 
android.add_compile_options = 
android.add_gradle_repositories = 
android.gradle_repositories = google(), mavenCentral()
android.enable_androidx = False
android.compile_options = 1.8, 1.8

# تحسينات الأداء
android.add_jars = 
android.add_src = 
android.add_aars = 
android.gradle_dependencies = 
android.add_gradle_repositories = 
android.gradle_repositories = google(), mavenCentral()

# إعدادات التوقيع (اختيارية)
android.debug = 1
android.private_storage = True

# إعدادات التطبيق الإضافية
android.wakelock = False
android.manifest_placeholders = 
android.add_activities = 
android.add_permissions = 
android.add_features = 

[buildozer]
log_level = 2
warn_on_root = 1

# مسارات مخصصة (اختيارية)
# android.sdk_path = 
# android.ndk_path = 
# android.ant_path = 
# p4a.port = 
# p4a.hook = 
# p4a.bootstrap = sdl2
# p4a.local_recipes = 
# p4a.setup_py = 
# p4a.requirements = 

# إعدادات iOS (غير مطلوبة هنا)
# ios.kivy_ios_url = 
# ios.kivy_ios_branch = 
# ios.ios_deploy_url = 
# ios.ios_deploy_branch = 
# ios.codesign.debug = 
# ios.codesign.release =
