import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    class Mata:
        #降順にしたい場合は頭に-をつけます
        ordering = ['question_text']

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    #データのタイトルとしてquestion_textを表示させる
    #関数としては"str(classname)"で呼び出せるっぽい
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text