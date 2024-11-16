from django.contrib import admin
from .models import Agent, Agreement

class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'credit', 'agreement')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'credit')
    list_editable = ('agreement',)
    list_filter = ('id', 'name', 'agreement')

admin.site.register(Agreement)
admin.site.register(Agent, AgentAdmin)