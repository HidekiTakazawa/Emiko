from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import NurseRecord
from .forms import NurseRecordForm
# Create your views here.
def paginate_queryset(request, queryset, count):
    """Pageオブジェクトを返す。

    ページングしたい場合に利用してください。

    countは、1ページに表示する件数です。
    返却するPgaeオブジェクトは、以下のような感じで使えます。

        {% if page_obj.has_previous %}
          <a href="?page={{ page_obj.previous_page_number }}">Prev</a>
        {% endif %}

    また、page_obj.object_list で、count件数分の絞り込まれたquerysetが取得できます。

    """
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj
def nurse_list(request):
    nurses = NurseRecord.objects.all().order_by('-nurse_day')
    page_obj = paginate_queryset(request, nurses, 10)
    return render(request, 'emikoKanri/nurse_list.html', {'page_obj':page_obj})
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
            return redirect('emikoKanri:nurse_list')
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
            return redirect('emikoKanri:nurse_list')
    else:
        form = NurseRecordForm(instance=nurse)
    return render(request, 'emikoKanri/nurse_edit.html', {'form': form})

@login_required
def nurse_remove(request, pk):
    nurse = get_object_or_404(NurseRecord, pk=pk)
    nurse.delete()
    return redirect('emikoKanri:nurse_list')