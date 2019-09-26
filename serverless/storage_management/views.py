from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from .serializers import *
from .models import *
from django.db.models import Q
import json


class GetAllSettingsViewSet(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer()

    def retrieve(self, request, *args, **kwargs):
        categories = Category.objects.all()
        series = Series.objects.all()
        author = Author.objects.all()
        location = Location.objects.all()
        position = DetailPosition.objects.all()
        return Response({
            "categories": CategorySerializer(categories, many=True).data,
            "series": SeriesSerializer(series, many=True).data,
            "authors": AuthorSerializer(author, many=True).data,
            "locations": LocationSerializer(location, many=True).data,
            "positions": DetailPositionSerializer(position, many=True).data
        })


class GetByQR(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemAbstractSerializer()

    def retrieve(self, request, *args, **kwargs):
        data = None
        try:
            data = Item.objects.filter(
                Q(uuid=request.query_params['qr'])).first()
        except Exception:
            # print(e)
            data = Item.objects.filter(Q(qr_code=request.query_params['qr'])).first()
        finally:
            if data:
                return Response(ItemAbstractSerializer(data).data)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DetailPositionViewSet(viewsets.ModelViewSet):
    queryset = DetailPosition.objects.all()
    serializer_class = DetailPositionSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request, *args, **kwargs):
        query = Item.objects.all()
        serializer = ItemAbstractSerializer(query, many=True)
        return Response(serializer.data)


class ItemImageViewSet(viewsets.ModelViewSet):
    queryset = ItemImage.objects.all()
    serializer_class = ItemImageSerializer


class ItemFileViewSet(viewsets.ModelViewSet):
    queryset = ItemFile.objects.all()
    serializer_class = ItemFileSerializer

    def create(self, request, *args, **kwargs):
        files: [ItemFile] = request.data

        valid = True
        s = []
        for file in files:
            serialized = ItemFileSerializer(data=file)
            if not serialized.is_valid():
                valid = False
                break
            s.append(serialized)

        if valid:
            [se.save() for se in s]
            return Response(data=[se.data for se in s], status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
