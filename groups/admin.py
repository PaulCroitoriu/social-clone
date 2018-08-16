from django.contrib import admin
from groups.forms import GroupForm
from . import models


# class GroupAdmin(admin.ModelAdmin):
#     form = GroupForm

admin.site.register(models.Group)
admin.site.register(models.GroupMember)
