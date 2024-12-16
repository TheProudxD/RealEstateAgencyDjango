from django.contrib import admin
from .models import Agent, Agreement, Message

class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'credit', 'agreement')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'credit')
    list_editable = ('agreement',)
    list_filter = ('id', 'name', 'agreement')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Agreement)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Message)