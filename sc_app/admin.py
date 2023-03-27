from django.contrib import admin

from sc_app import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.Student_Register)
admin.site.register(models.Complaint)
admin.site.register(models.Notification)
