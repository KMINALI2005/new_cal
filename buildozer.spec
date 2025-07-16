[app]
# !!! تعديل مهم: اسم التطبيق الذي سيظهر للمستخدم
title = الحاسبة الذكية

# !!! تعديل مهم: اسم الحزمة يجب أن يكون فريداً وبأحرف إنجليزية صغيرة
package.name = smartcalculator
package.domain = com.mycompany.arabiccalc

# مجلد المصدر (لا تغيره)
source.dir = .

# !!! تعديل مهم جداً: إضافة امتداد ttf ليتم تضمين ملف الخط
source.include_exts = py,png,jpg,kv,atlas,ttf

# إصدار التطبيق
version = 1.0

# !!! تعديل مهم جداً: إضافة مكتبة pillow لدعم اللغة العربية
requirements = python3,kivy,pillow

# اتجاه الشاشة (عمودي)
orientation = portrait

# (اختياري) يمكنك إنشاء أيقونة بصيغة png بحجم 512x512 ورفعها لـ Colab
# icon.filename = %(source.dir)s/icon.png

#
# إعدادات أندرويد
#

# لا تجعل التطبيق بملء الشاشة (لإظهار شريط الحالة العلوي)
fullscreen = 0

# !!! تعديل مهم: تحديد صلاحيات الوصول للتخزين (مهمة لحفظ السجل)
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# !!! تعديل مهم: استخدام API حديث متوافق مع متطلبات جوجل بلاي
android.api = 33
android.minapi = 21

# المعالجات التي سيعمل عليها التطبيق (يغطي معظم الأجهزة)
android.archs = arm64-v8a, armeabi-v7a

# السماح بالنسخ الاحتياطي
android.allow_backup = true

# فلاتر لعرض سجل الأخطاء (مفيدة للمطورين)
android.logcat_filters = *:S python:D

[buildozer]
# مستوى عرض التفاصيل أثناء البناء (2 هو الأكثر تفصيلاً)
log_level = 2

# تحذير عند التشغيل بصلاحيات الجذر (طبيعي في Colab)
warn_on_root = 1