from django import forms
from .models import Question, Answer


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
