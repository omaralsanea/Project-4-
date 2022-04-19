from django.contrib import admin
from .models import *

# Register your models here.


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'level')


# Tell Django we want to edit these models in the admin area
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Level)
admin.site.register(Muscle)
