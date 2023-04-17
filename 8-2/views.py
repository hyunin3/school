from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article


@api_view(['GET'])
def Article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)