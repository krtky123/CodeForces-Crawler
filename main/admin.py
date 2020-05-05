from django.contrib import admin
from .models import  languages, verdicts, levels

admin.site.register(languages)

admin.site.register(verdicts)
admin.site.register(levels)