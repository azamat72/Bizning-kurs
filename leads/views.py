from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from . import models
from .forms import *



def index(request):
    leads  = models.Lead.objects.all()
    context = {
        "leads": leads  
    }
    return render(request, "index.html", context)

def about(request):
    users  = models.User.objects.all()
    context = {
         "users": users
    }
    return render(request, "about.html", context)


def leads_detail(request, pk):
    lead = get_object_or_404(models.Lead, id=pk)
    context = {
        "lead": lead
    }
    return render(request, "details.html", context)

def create(request):
    forms = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/about')
    context = {
       "forms": forms
    }
    return render(request, "create.html", context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance = lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance = lead)
        if form.is_valid():
            form.save()
            return redirect('/about')
    # if request.method == "POST":
    #     form = LeadForm(request.POST)
    #     if form.is_valid():
    #         familiyasi = form.cleaned_data["familiyasi"]
    #         ismi = form.cleaned_data["ismi"]
    #         yoshi = form.cleaned_data["yoshi"]
    #         lead.familiyasi = familiyasi
    #         lead.ismi = ismi
    #         lead.yoshi = yoshi
    #         lead.save()
    #         return redirect('/leads')
    context = {
        'form': form,
        'lead': lead
    }
    return render(request, "update.html", context)

def lead_delete(request, pk):
    lead = models.Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/')