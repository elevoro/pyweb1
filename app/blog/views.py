from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Note
from .serializers import NoteSerializer

# def index(request):
#     return HttpResponse("Привет, Лена")

def home(request):
    """ Использование Django шаблонов.  Метод обрабатывает запрос `/` """

    # Объект который будет передан в шаблон
    context = {
        'title': 'Добро пожаловать',
        'left': 'генератор списка',
        'right': 'записи из базы данных',
        'data': [{'id': i, 'name': f'Name {i}'} for i in range(3)],
        'notes': Note.objects.all()
    }

    # Рендеринг шаблона с последующим ответом клиенту
    return render(request, 'blog/index.html', context)


class BlogListView(APIView):
    """ BlogListView """
    def get(self, request):
        notes = Note.objects.filter(public=True)

        res = []
        for note in notes:
            res.append({
                'id': note.id,
                'title': note.title,
                'author': {
                    'id': note.author.id,
                    'username': note.author.username,
                }
            })

        return Response(res)


class BlogViewMix(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer