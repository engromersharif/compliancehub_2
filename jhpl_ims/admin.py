from django.contrib import admin

from .models import doc_controller, jhpl_ims_masterlist, notes
# Register your models here.
admin.site.register(doc_controller)
admin.site.register(jhpl_ims_masterlist)
admin.site.register(notes)
