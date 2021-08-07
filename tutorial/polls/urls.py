from django.urls import path

from . import views

'''最後の name='post_list' は、
ビューを識別するために使われるURL の名前です。
これはビューと同じ名前にすることもできますが、
全然別の名前にすることもできます。 
プロジェクトでは名前づけされたURLを後で使うことになるので、
アプリのそれぞれのURLに名前をつけておくのは重要です。
また、URLの名前はユニークで覚えやすいものにしておきましょう。
'''

#pathの第1引数はルートurlの"/"までが省略されている
#例えば"root/post/"であればpath('post/',...)でok
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='poll_detail')
]