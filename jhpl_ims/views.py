from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.shortcuts import redirect, get_object_or_404
from jhpl_ims.forms import CommentForm, MasterListForm
from jhpl_ims.owner import OwnerDeleteView
# Create your views here.
from . models import jhpl_ims_masterlist, notes
from django.contrib.auth import get_user_model
from django.contrib.humanize.templatetags.humanize import naturaltime


class index(LoginRequiredMixin, View):
    def get(self, request):
        master_list = jhpl_ims_masterlist.objects.all()
        show_edit_link = False

        if request.user.username in ["admin", "ali"]:
            show_edit_link = True

        ctx = {'master_list': master_list, 'show_edit_link': show_edit_link}
        return render(request, 'jhpl_ims/index.html', ctx)


class procedures(LoginRequiredMixin, View):
    def get(self, request, pk):
        master_list = jhpl_ims_masterlist.objects.filter(ims_masterlist_id=pk)
        notes_list = notes.objects.filter(
            jhpl_ims_masterlist_key=pk).order_by('-updated_at')
        comment_form = CommentForm()
        ctx = {'master_list': master_list,
               'notes_list': notes_list, 'comment_form': comment_form}
        if pk == 1:
            return render(request, 'jhpl_ims/sop_one.html', ctx)
        elif pk == 2:
            return render(request, 'jhpl_ims/sop_two.html', ctx)
        elif pk == 3:
            return render(request, 'jhpl_ims/sop_three.html', ctx)
        elif pk == 4:
            return render(request, 'jhpl_ims/sop_four.html', ctx)
        elif pk == 5:
            return render(request, 'jhpl_ims/sop_five.html', ctx)


# class MasterUpdateView(LoginRequiredMixin, View):
#     model = jhpl_ims_masterlist
#     fields = ['doc_num', 'doc_title', 'rev_num', 'issue_date', 'status','approved_by','approved_date','reviewed_by','reviewed_date','control_copy_num']
#     fields_exclude = ['ims_masterlist_id', 'owner', 'created_at', 'updated_at']

class MasterUpdateView(LoginRequiredMixin, View):
    model = jhpl_ims_masterlist
    success_url = reverse_lazy('jhpl_ims/index.html')
    template = 'jhpl_ims/jhpl_ims_masterlist_form.html'

    def get(self, request, pk):
        masterlist = get_object_or_404(self.model, pk=pk)
        form = MasterListForm(instance=masterlist)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        masterlist = get_object_or_404(self.model, pk=pk)
        form = MasterListForm(request.POST, instance=masterlist)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)


class NotesCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        key = get_object_or_404(jhpl_ims_masterlist, ims_masterlist_id=pk)
        Notes = notes(
            large_text_body=request.POST['comment'], owner=request.user, jhpl_ims_masterlist_key=key)
        Notes.save()
        return redirect(reverse('jhpl_ims:procedures', args=[key.pk]))


class NotesDeleteView(OwnerDeleteView):
    model = notes
    template_name = "jhpl_ims/notes_delete.html"

    def get_success_url(self):
        jhpl_ims_masterlist_key = self.object.jhpl_ims_masterlist_key
        return reverse('jhpl_ims:procedures', args=[jhpl_ims_masterlist_key.ims_masterlist_id])
