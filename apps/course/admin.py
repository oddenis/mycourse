from django.contrib import admin
from .models import Course, Lectures, Material, Category
# Register your models here.

class LecturesInLine(admin.StackedInline):
    model = Lectures
    fields = ('title', 'desc', 'stage')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LecturesInLine,]

class MaterialInLine(admin.StackedInline):
    model = Material
    fields = ('title', 'text', 'file', 'type_file', 'stage')

@admin.register(Lectures)
class LecturesAdmin(admin.ModelAdmin):
    inlines = [MaterialInLine,]
    list_filter =('course__title',)

#admin.site.register(Lectures)
admin.site.register(Material)
admin.site.register(Category)