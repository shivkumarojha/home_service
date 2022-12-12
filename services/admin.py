from django.contrib import admin
from . models import Enquiry, ServiceTypes, ContactInfo, Newsletter, Team, ClientQuotes, Tag,Project, Message


class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile_number', 'select_service', 'service_status','enquiry_date']
    
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'date', 'resolved']
    
admin.site.register(Enquiry, EnquiryAdmin)
admin.site.register(ServiceTypes)
admin.site.register(ContactInfo)
admin.site.register(Newsletter)
admin.site.register(Team, TeamAdmin)
admin.site.register(ClientQuotes)
admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(Message, MessageAdmin)