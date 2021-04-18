from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Answer, User


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def void(request):
    raise Http404


def new(request, *args, **kwargs):
    questions = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'qa/new.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def popular(request):
    questions = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'qa/popular.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def question(request, id):
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404

    answers = Answer.objects.filter(question=question)
    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers,
    })
