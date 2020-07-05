import os

from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from .serializers import *
from .models import *
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
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

        data = Item.objects.filter(qr_code=request.query_params['qr']).first()
        if data:
            print("Get item By qr")
            return Response(ItemAbstractSerializer(data).data)

        data = Item.objects.filter(
            Q(uuid=request.query_params['qr'])).first()
        if data:
            print("Get item By uuid")
            return Response(ItemAbstractSerializer(data).data)

        p = DetailPosition.objects.filter(
            uuid=request.query_params['qr']).first()
        if p:
            print("Get item by position")
            items = Item.objects.filter(detail_position=p)
            print(items)
            if items:
                data = ItemAbstractSerializer(items, many=True)
                return Response(data=data.data, status=200)

        return Response(data=[], status=400)


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
    queryset = Item.objects.all().order_by('name')
    serializer_class = ItemSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'location', 'detail_position']

    def list(self, request, *args, **kwargs):
        self.serializer_class = ItemAbstractSerializer
        return super().list(request, *args, **kwargs)


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


class GetItemByLocationView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer()

    def retrieve(self, request, *args, **kwargs):
        pid = request.query_params['position_id']
        items = Item.objects.filter(detail_position=pid)
        print(items)
        if items:
            data = ItemSerializer(items, many=True)
            return Response(data=data.data, status=200)

        return Response(data=[], status=400)



