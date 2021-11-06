from django.contrib import admin
from main import models


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'checked')
    prepopulated_fields = {'slug': ('title',)}
