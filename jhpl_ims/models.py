from django.db import models
from django.conf import settings

class doc_controller(models.Model):
    doc_controller_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class jhpl_ims_masterlist(models.Model):
    ims_masterlist_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doc_num = models.IntegerField()
    doc_title = models.CharField(max_length=200, null=True, blank=True)
    rev_num = models.IntegerField()
    issue_date = models.DateTimeField()
    status = models.CharField(max_length=10)
    approved_by = models.ForeignKey("doc_controller", on_delete=models.CASCADE, related_name="jhpl_approved_by")
    approved_date = models.DateTimeField()
    reviewed_by = models.ForeignKey("doc_controller", on_delete=models.CASCADE, related_name="jhpl_reviewed_by")
    reviewed_date = models.DateTimeField()
    control_copy_num = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.doc_title


class notes(models.Model):
    notes_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    large_text_body = models.TextField()
    jhpl_ims_masterlist_key = models.ForeignKey("jhpl_ims_masterlist", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.large_text_body
