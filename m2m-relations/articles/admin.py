from django.contrib import admin

from .models import Article, Scope, Tag
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        uniq_is_main = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data.get('is_main', False):
                uniq_is_main +=1
        if uniq_is_main > 1:

            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            raise ValidationError('Основной раздел должен быть один')
        return super().clean()  # вызываем базовый код переопределяемого метода
class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

