from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import Question
from .models import Choice

class QuestionResource(resources.ModelResource):
    # Modelに対するdjango-import-exportの設定
    class Meta:
        model = Question



class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(ImportExportModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('pk','question_text', 'pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    # django-import-exportsの設定
    resource_class = QuestionResource

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
