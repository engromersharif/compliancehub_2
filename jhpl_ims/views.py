from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.shortcuts import redirect, get_object_or_404
# Create your views here.
from . models import jhpl_ims_masterlist, notes


class index(LoginRequiredMixin, View):
    def get(self, request):
        master_list = jhpl_ims_masterlist.objects.all()
        ctx = {'master_list': master_list}
        return render(request, 'jhpl_ims/index.html', ctx)


class procedures(LoginRequiredMixin, View):
    def get(self, request, pk):
        master_list = jhpl_ims_masterlist.objects.filter(ims_masterlist_id=pk)
        notes_list = notes.objects.filter(jhpl_ims_masterlist_key=pk)

        ctx = {'master_list': master_list, 'notes_list': notes_list}
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


class MasterUpdateView(UpdateView):
    model = jhpl_ims_masterlist
    fields = ['doc_num', 'doc_title', 'rev_num', 'issue_date', 'status']
    # This would make more sense
    fields_exclude = ['ims_masterlist_id', 'owner', 'created_at', 'updated_at']


class NotesCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        key = get_object_or_404(jhpl_ims_masterlist, id=pk)
        notes = notes(large_text_body=request.POST['comment'], owner = request.user, jhpl_ims_masterlist_key = key)
        notes.save()
        return redirect(reverse('jhpl_ims:procedures', args=[pk]))