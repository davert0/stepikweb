# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Answer, User
from django.views.decorators.http import require_GET
from .forms import AskForm, AnswerForm, LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def void(request):
    raise Http404


@require_GET
def index(request, *args, **kwargs):
    questions = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'index.html', {
        'title': 'Список вопросов',
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


@require_GET
def popular(request, *args, **kwargs):
    questions = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'popular.html', {
        'title': 'Популярные вопросы',
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def question(request, id):
    question = get_object_or_404(id=id)
    answers = Answer.objects.filter(question=question).order_by('-added_at')
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            msg = 'Ваш ответ принят'
            form._user = request.user
            _ = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': question.id})
        return render(request, 'question.html', {
            'title': 'Страница вопроса',
            'question': question,
            'answers': answers,
            'form': form
        })


def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'title': 'Задать вопрос',
        'form': form,
    })


def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect(reverse('index'))


def log_out(request):
    if request.user is not None:
        logout(request)
    return HttpResponseRedirect(reverse('index'))


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.raw_passwrd
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            form = SignupForm()
        return render(request, 'signup.html', {
            'title': 'Регистрация пользователя',
            'form': form,
        })
