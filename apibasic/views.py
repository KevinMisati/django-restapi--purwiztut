from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Article
from .serilizers import ArticleSerilizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerilizer
    queryset = Article.objects.all()



""" class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerilizer
    queryset = Article.objects.all() """



""" class ArticleViewSet(viewsets.ViewSet):
    def list(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerilizer(articles, many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = ArticleSerilizer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset,pk=pk)
        serializer = ArticleSerilizer(article)
        return Response(serializer.data)
    
    def update (self,request,pk=None):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerilizer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     """
    














class GenericApiView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):

    serializer_class = ArticleSerilizer
    queryset = Article.objects.all()
    lookup_field = 'id'
    #authentication_class = [SessionAuthentication,BasicAuthentication]
    authentication_class = [TokenAuthentication]
    Permission_class = [IsAuthenticated]

    def get(self,request,id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    
    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id):
        return self.destroy(request,id)











class ArticleApiView(APIView):
    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerilizer(articles,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ArticleSerilizer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):
    def get_object(self,id):
        try:
            article = Article.objects.get(id=id)
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,repeat,id):
        article = self.get_object(id)
        serializer = ArticleSerilizer(article)
        return Response(serializer.data)

    def put(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerilizer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
























@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerilizer(articles,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        
        serializer = ArticleSerilizer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
    try:
        article = Article.objects.get(pk = pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerilizer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        
        serializer = ArticleSerilizer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)