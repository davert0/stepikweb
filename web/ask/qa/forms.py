# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

class AskForm(forms.Form):
    title = forms.CharField(max_length=250)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.strip() == '':
            raise forms.ValidationError('Заполните поле заголовка', code='validation_error')
            return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '':
            raise forms.ValidationError('Введите текст вопроса', code='validation_error')
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '':
            raise forms.ValidationError('Введите текст ответа', code='validation_error')
        return text

    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise forms.ValidationError('Неправильный идентификатор вопроса', code='validation_error')
        return question

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Не указано имя пользователя')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Не указан пароль')
        return password

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Неверное имя пользователя или пароль")
        if not user.check_password(password):
            raise forms.ValidationError('Неверное имя пользователя или пароль')


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.strip() == '':
            raise forms.ValidationError('Введите имя пользователя', code='validation_error')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError("Имя пользователя занято")
        except User.DoesNotExist:
            pass
        return username


    def clean_email(self):
        email = self.cleaned_data['email']
        if email.strip() == '':
            raise forms.ValidationError("Заполните поле E-mail", code='validation_error')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if password.strip() == '':
            raise forms.ValidationError("Введите Ваш парооль", code='validation_error')
        self.raw_passwrd = password
        return make_password(password)

    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user
