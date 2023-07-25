from django import forms
from django.forms import ModelForm, Textarea
from jhpl_ims.models import jhpl_ims_masterlist
from tempus_dominus.widgets import DateTimePicker


class CommentForm(forms.Form):
    comment = forms.CharField()


class MasterListForm(forms.ModelForm):
    class Meta:
        model = jhpl_ims_masterlist
        exclude = ["owner"]

        widgets = {
            'doc_num': forms.TextInput(attrs={'class': 'form-control'}),
            'doc_title': forms.TextInput(attrs={'class': 'form-control'}),
            'rev_num': forms.NumberInput(attrs={'class': 'form-control'}),
            'issue_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'reviewed_by': forms.Select(attrs={'class': 'form-control'}),
            'reviewed_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'approved_by': forms.Select(attrs={'class': 'form-control'}),
            'approved_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'control_copy_num': forms.NumberInput(attrs={'class': 'form-control'}),
        }
