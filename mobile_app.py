# --- START OF FILE mobile_app.py (CORRECTED VERSION) ---

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
حاسبة الجمع الذكية - تطبيق أندرويد
تطبيق محمول باستخدام Kivy لعمليات الجمع الذكية
"""

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import platform

# <<<--- إضافة: استيراد LabelBase لتسجيل الخطوط
from kivy.core.text import LabelBase

import json
import re
from datetime import datetime
from typing import List, Dict, Any
import os

# تعيين الحد الأدنى لإصدار Kivy
kivy.require('2.0.0')

class SmartCalculator:
    # ... (هذا الكلاس لا يحتاج أي تعديل) ...
    """حاسبة ذكية متطورة لعمليات الجمع - نسخة محمولة"""
    
    def __init__(self):
        self.decimal_precision = 10
    
    def parse_input(self, text_input: str) -> List[float]:
        """تحليل النص المدخل واستخراج الأرقام منه"""
        if not text_input or not text_input.strip():
            return []
        
        try:
            text_input = text_input.strip()
            number_pattern = r'-?\d+\.?\d*'
            matches = re.findall(number_pattern, text_input)
            
            numbers = []
            for match in matches:
                try:
                    if match and match != '.' and match != '-':
                        num = float(match)
                        numbers.append(num)
                except ValueError:
                    continue
            
            return numbers
            
        except Exception:
            return []
    
    def calculate_sum(self, numbers: List[float]) -> float:
        """حساب مجموع الأرقام مع دقة عالية"""
        if not numbers:
            return 0.0
        
        try:
            result = sum(numbers)
            return round(result, self.decimal_precision)
        except Exception:
            return 0.0
    
    def format_number(self, num: float) -> str:
        """تنسيق الأرقام لعرض أفضل"""
        try:
            if num == int(num):
                return f"{int(num):,}".replace(',', '٬')
            else:
                formatted = f"{num:.10f}".rstrip('0').rstrip('.')
                if '.' in formatted:
                    integer_part, decimal_part = formatted.split('.')
                    integer_part = f"{int(integer_part):,}".replace(',', '٬')
                    return f"{integer_part}.{decimal_part}"
                else:
                    return f"{int(float(formatted)):,}".replace(',', '٬')
        except:
            return str(num)

class CalculatorApp(App):
    """التطبيق الرئيسي للحاسبة الذكية"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.calculator = SmartCalculator()
        self.history = []
        
        # <<<--- إضافة: تسجيل الخط العربي. تأكد أن اسم الملف صحيح
        LabelBase.register(name='Arabic', fn_regular='arabic_font.ttf')
        
        self.load_history()
    
    def build(self):
        self.title = "🧮 حاسبة الجمع الذكية"
        
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
        
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title_label = Label(
            text='🧮 حاسبة الجمع الذكية',
            font_size='24sp',
            size_hint_y=None,
            height='60dp',
            color=[0.2, 0.6, 1, 1],
            bold=True,
            font_name='Arabic'  # <<<--- تعديل
        )
        main_layout.add_widget(title_label)
        
        input_section = self.create_input_section()
        main_layout.add_widget(input_section)
        
        self.result_section = self.create_result_section()
        main_layout.add_widget(self.result_section)
        
        control_section = self.create_control_section()
        main_layout.add_widget(control_section)
        
        history_section = self.create_history_section()
        main_layout.add_widget(history_section)
        
        return main_layout
    
    def create_input_section(self):
        section = BoxLayout(orientation='vertical', size_hint_y=None, height='200dp', spacing=10)
        
        input_label = Label(
            text='أدخل الأرقام (مفصولة بفواصل أو مسافات):',
            font_size='16sp',
            size_hint_y=None,
            height='30dp',
            color=[0.3, 0.3, 0.3, 1],
            font_name='Arabic'  # <<<--- تعديل
        )
        section.add_widget(input_label)
        
        self.input_field = TextInput(
            multiline=True,
            hint_text='مثال: 10, 20, 30.5 أو 15 25 35',
            font_size='16sp',
            size_hint_y=None,
            height='120dp',
            background_color=[0.95, 0.95, 0.95, 1],
            font_name='Arabic'  # <<<--- تعديل
        )
        section.add_widget(self.input_field)
        
        calculate_btn = Button(
            text='🚀 احسب النتيجة',
            font_size='18sp',
            size_hint_y=None,
            height='50dp',
            background_color=[0.2, 0.7, 0.3, 1],
            color=[1, 1, 1, 1],
            font_name='Arabic'  # <<<--- تعديل
        )
        calculate_btn.bind(on_press=self.calculate_result)
        section.add_widget(calculate_btn)
        
        return section
    
    def create_result_section(self):
        section = BoxLayout(orientation='vertical', size_hint_y=None, height='150dp', spacing=10)
        
        result_label = Label(
            text='النتيجة:',
            font_size='16sp',
            size_hint_y=None,
            height='30dp',
            color=[0.3, 0.3, 0.3, 1],
            font_name='Arabic'  # <<<--- تعديل
        )
        section.add_widget(result_label)
        
        self.result_display = Label(
            text='قم بإدخال أرقام واضغط احسب النتيجة',
            font_size='20sp',
            size_hint_y=None,
            height='60dp',
            color=[0.1, 0.5, 0.1, 1],
            bold=True,
            text_size=(None, None),
            font_name='Arabic'  # <<<--- تعديل
        )
        section.add_widget(self.result_display)
        
        self.info_display = Label(
            text='',
            font_size='14sp',
            size_hint_y=None,
            height='60dp',
            color=[0.5, 0.5, 0.5, 1],
            text_size=(None, None),
            font_name='Arabic'  # <<<--- تعديل
        )
        section.add_widget(self.info_display)
        
        return section
    
    def create_control_section(self):
        section = GridLayout(cols=3, size_hint_y=None, height='60dp', spacing=10)
        
        clear_btn = Button(
            text='🗑️ مسح', font_size='14sp', background_color=[0.8, 0.4, 0.4, 1],
            color=[1, 1, 1, 1], font_name='Arabic'  # <<<--- تعديل
        )
        clear_btn.bind(on_press=self.clear_input)
        section.add_widget(clear_btn)
        
        history_btn = Button(
            text='📚 التاريخ', font_size='14sp', background_color=[0.4, 0.4, 0.8, 1],
            color=[1, 1, 1, 1], font_name='Arabic'  # <<<--- تعديل
        )
        history_btn.bind(on_press=self.show_history)
        section.add_widget(history_btn)
        
        help_btn = Button(
            text='❓ مساعدة', font_size='14sp', background_color=[0.6, 0.6, 0.6, 1],
            color=[1, 1, 1, 1], font_name='Arabic'  # <<<--- تعديل
        )
        help_btn.bind(on_press=self.show_help)
        section.add_widget(help_btn)
        
        return section
    
    def create_history_section(self):
        section = BoxLayout(orientation='vertical', spacing=5)
        
        history_label = Label(
            text='آخر العمليات:',
            font_size='16sp',
            size_hint_y=None,
            height='30dp',
            color=[0.3, 0.3, 0.3, 1],
            font_name='Arabic'  # <<<--- تعديل
        )
        section.add_widget(history_label)
        
        self.history_scroll = ScrollView()
        self.history_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.history_layout.bind(minimum_height=self.history_layout.setter('height'))
        
        self.history_scroll.add_widget(self.history_layout)
        section.add_widget(self.history_scroll)
        
        self.update_history_display()
        
        return section
    
    def calculate_result(self, instance):
        # ... (الجزء المنطقي لا يتغير) ...
        input_text = self.input_field.text.strip()
        if not input_text:
            self.show_popup("خطأ", "الرجاء إدخال أرقام أولاً")
            return
        numbers = self.calculator.parse_input(input_text)
        if not numbers:
            self.show_popup("خطأ", "لم يتم العثور على أرقام صالحة في النص المدخل")
            return
        result = self.calculator.calculate_sum(numbers)
        formatted_result = self.calculator.format_number(result)
        self.result_display.text = f"النتيجة: {formatted_result}"
        count = len(numbers)
        min_num = min(numbers)
        max_num = max(numbers)
        avg = result / count if count > 0 else 0
        info_text = f"عدد الأرقام: {count}\n"
        info_text += f"أصغر رقم: {self.calculator.format_number(min_num)}\n"
        info_text += f"أكبر رقم: {self.calculator.format_number(max_num)}\n"
        info_text += f"المتوسط: {self.calculator.format_number(avg)}"
        self.info_display.text = info_text
        operation = {
            'timestamp': datetime.now().isoformat(), 'numbers': numbers,
            'result': result, 'count': count
        }
        self.history.append(operation)
        self.save_history()
        self.update_history_display()
        self.show_motivational_message(count, result)
        
    def clear_input(self, instance):
        self.input_field.text = ""
        self.result_display.text = "قم بإدخال أرقام واضغط احسب النتيجة"
        self.info_display.text = ""
    
    def show_history(self, instance):
        if not self.history:
            self.show_popup("التاريخ", "لا توجد عمليات سابقة")
            return
        content = BoxLayout(orientation='vertical', spacing=10)
        recent_history = self.history[-10:]
        for i, operation in enumerate(reversed(recent_history), 1):
            timestamp = datetime.fromisoformat(operation['timestamp'])
            time_str = timestamp.strftime('%H:%M:%S')
            history_text = f"{i}. النتيجة: {self.calculator.format_number(operation['result'])}\n"
            history_text += f"   عدد الأرقام: {operation['count']} - الوقت: {time_str}"
            history_label = Label(
                text=history_text, font_size='12sp', size_hint_y=None,
                height='60dp', text_size=(300, None), halign='right',
                font_name='Arabic'  # <<<--- تعديل
            )
            content.add_widget(history_label)
        close_btn = Button(text='إغلاق', size_hint_y=None, height='50dp', font_name='Arabic') # <<<--- تعديل
        popup = Popup(
            title='تاريخ العمليات', content=content, size_hint=(0.9, 0.8),
            title_font='Arabic'  # <<<--- تعديل لعنوان النافذة
        )
        close_btn.bind(on_press=popup.dismiss)
        content.add_widget(close_btn)
        popup.open()
    
    def show_help(self, instance):
        help_text = "..." # (النص كما هو)
        self.show_popup("المساعدة", help_text)
    
    def show_motivational_message(self, count, result):
        # ... (النص كما هو)
        if count <= 5: message = "عمل رائع! حساب دقيق ومتميز! 🌟"
        elif count <= 15: message = "مذهل! التعامل مع عدة أرقام بكل سهولة! 🚀"
        else: message = "استثنائي! التعامل مع البيانات الكبيرة بإتقان! 🏆"
        if result % 100 == 0 and result != 0: message += " النتيجة رقم مميز! 🎯"
        Clock.schedule_once(lambda dt: self.show_popup("تهانينا!", message), 0.5)
    
    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', spacing=10)
        message_label = Label(
            text=message, font_size='14sp', text_size=(300, None),
            halign='center', valign='middle', font_name='Arabic'  # <<<--- تعديل
        )
        content.add_widget(message_label)
        close_btn = Button(text='موافق', size_hint_y=None, height='50dp', font_name='Arabic') # <<<--- تعديل
        popup = Popup(
            title=title, content=content, size_hint=(0.8, 0.6),
            title_font='Arabic'  # <<<--- تعديل لعنوان النافذة
        )
        close_btn.bind(on_press=popup.dismiss)
        content.add_widget(close_btn)
        popup.open()
    
    def update_history_display(self):
        self.history_layout.clear_widgets()
        if not self.history:
            no_history = Label(
                text='لا توجد عمليات سابقة', font_size='12sp', size_hint_y=None,
                height='30dp', color=[0.6, 0.6, 0.6, 1], font_name='Arabic' # <<<--- تعديل
            )
            self.history_layout.add_widget(no_history)
            return
        recent_history = self.history[-5:]
        for operation in reversed(recent_history):
            timestamp = datetime.fromisoformat(operation['timestamp'])
            time_str = timestamp.strftime('%H:%M')
            history_text = f"النتيجة: {self.calculator.format_number(operation['result'])} ({operation['count']} أرقام) - {time_str}"
            history_item = Label(
                text=history_text, font_size='11sp', size_hint_y=None,
                height='25dp', color=[0.4, 0.4, 0.4, 1], text_size=(None, None),
                font_name='Arabic'  # <<<--- تعديل
            )
            self.history_layout.add_widget(history_item)
            
    def load_history(self):
        # <<<--- تعديل مهم: استخدام مسار آمن لا يحتاج تصاريح
        try:
            history_file = self.get_history_file_path()
            if os.path.exists(history_file):
                with open(history_file, 'r', encoding='utf-8') as f:
                    self.history = json.load(f)
        except Exception:
            self.history = []

    def save_history(self):
        # <<<--- تعديل مهم: استخدام مسار آمن لا يحتاج تصاريح
        try:
            history_file = self.get_history_file_path()
            if len(self.history) > 100: self.history = self.history[-100:]
            with open(history_file, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def get_history_file_path(self):
        # <<<--- تعديل مهم: استخدام مساحة التخزين الخاصة بالتطبيق (الأفضل والأكثر أماناً)
        return os.path.join(self.user_data_dir, 'smart_calculator_history.json')

if __name__ == '__main__':
    CalculatorApp().run()

# --- END OF FILE mobile_app.py (CORRECTED VERSION) ---