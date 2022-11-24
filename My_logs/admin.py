from django.contrib import admin

# Register your models here.
from .models import Topic  # Імпортуємо модель, яку ми хочемо зареєструвати

admin.site.register(Topic)  # даємо знати django що треба керувати моделлю через інтерфейс адміністратора
