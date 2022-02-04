from django.contrib import admin

from .models import Box, Drug, DrugBox

admin.site.register(Box)
admin.site.register(Drug)
admin.site.register(DrugBox)
