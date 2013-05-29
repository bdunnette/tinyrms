from django.shortcuts import render, get_object_or_404

from eval.models import CaseEvaluation

def index(request):
    latest_eval_list = CaseEvaluation.objects.order_by('-evaluation_date')[:5]
    context = {'latest_eval_list': latest_eval_list}
    return render(request, 'eval/index.html', context)

def detail(request, eval_id):
    eval = get_object_or_404(CaseEvaluation, pk=eval_id)
    return render(request, 'eval/detail.html', {'eval': eval})
