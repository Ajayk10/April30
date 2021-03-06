from django.contrib import admin
from .models import *

# Register your models here.

class Q1(admin.ModelAdmin):
    list_display = ['i1','i2','i3','i4']

class Q2(admin.ModelAdmin):
    list_display = ['i5','i6','i7','i8']

class Q3(admin.ModelAdmin):
    list_display = ['i9','i10','i11','i12','i13']

class Q4(admin.ModelAdmin):
    list_display = ['i14','i15','i16','i17']


class Q5(admin.ModelAdmin):
    list_display = ['i18']


admin.site.register(Answers1,Q1)
admin.site.register(Answers2,Q2)
admin.site.register(Answers3,Q3)
admin.site.register(Answers4,Q4)
admin.site.register(Answers5,Q5)