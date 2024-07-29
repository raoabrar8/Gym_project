from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from datetime import timedelta

# Create your views here.


def dashboard(request):
    members = MemberModel.objects.all()
    due_members = members.filter(fee_date__lt=timezone.now() - timezone.timedelta(days=28))
    context = {'members' : members, 'due_members' : due_members} 
    return render(request, 'dashboard.html', context)


def manage_members(request):
    members = MemberModel.objects.all()
    context = {'members' : members}
    return render(request, 'manage_members.html', context )


def member_details(request, id):
    member = get_object_or_404(MemberModel, id=id)
    context = {'member': member}
    return render(request, 'member_details.html', context)

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_members')
    else:
        form = MemberForm()
    return render(request, 'add_member.html', {'form':form})

def update_member(request, id):
    member = get_object_or_404(MemberModel, id=id)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('manage_members')
    else:
        form = MemberForm(instance=member)
    context = {'form': form, 'member': member}
    return render(request, 'update_member.html', context)

def delete_member(request, id):
    member = get_object_or_404(MemberModel, id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('manage_members')
    return render(request, 'delete_member.html', {'member': member})

def Reports(request):
    total_revenue = 0
    members = []
    
    if request.method == "GET" and 'start_date' in request.GET and 'end_date' in request.GET:
        start_date = request.GET['start_date']
        end_date = request.GET['end_date']
        members = MemberModel.objects.filter(fee_date__range=[start_date, end_date])
        total_revenue = sum(member.fee_amount for member in members)
        
        
    context = {'total_revenue' : total_revenue, 'members' : members}
        
    return render(request, 'reports.html', context)