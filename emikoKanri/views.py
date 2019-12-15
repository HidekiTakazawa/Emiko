from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import NurseRecord
from .forms import NurseRecordForm
# Create your views here.
def nurse_list(request):
    nurses = NurseRecord.objects.all().order_by('-nurse_day')
    return render(request, 'emikoKanri/nurse_list.html', {'nurses':nurses})
def nurse_detail(request, pk):
    nurse = get_object_or_404(NurseRecord, pk=pk)
    return render(request, 'emikoKanri/nurse_detail.html', {'nurse': nurse})
@login_required
def nurse_new(request):
    if request.method == "POST":
        form = NurseRecordForm(request.POST)
        if form.is_valid():
            nurse = form.save(commit=False)
            nurse.author = request.user
            
            nurse.save()
            return redirect('nurse_list')
    else:
        form = NurseRecordForm()
    return render(request, 'emikoKanri/nurse_edit.html', {'form': form})
@login_required
def nurse_edit(request, pk):
    nurse = get_object_or_404(NurseRecord, pk=pk)
    if request.method == "POST":
        form = NurseRecordForm(request.POST, instance=nurse)
        if form.is_valid():
            nurse = form.save(commit=False)
            nurse.author = request.user
            
            nurse.save()
            return redirect('nurse_list')
    else:
        form = NurseRecordForm(instance=nurse)
    return render(request, 'emikoKanri/nurse_edit.html', {'form': form})

@login_required
def nurse_remove(request, pk):
    nurse = get_object_or_404(NurseRecord, pk=pk)
    nurse.delete()
    return redirect('nurse_list')