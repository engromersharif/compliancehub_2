from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class index(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'jhpl_ims/index.html')


class sop_one(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'jhpl_ims/sop_one.html')


class sop_two(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'jhpl_ims/sop_two.html')


class sop_three(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'jhpl_ims/sop_three.html')


class sop_four(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'jhpl_ims/sop_four.html')


class sop_five(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'jhpl_ims/sop_five.html')
