from abc import ABC
from .models import *
from rest_framework import serializers


class ImageRelatedField(serializers.RelatedField, ABC):
    def to_representation(self, value: ItemImage):
        return value.image.url


class FileRelatedField(serializers.RelatedField, ABC):
    def to_representation(self, value: ItemFile):
        return value.file


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ("id", "name", "description")


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "name", "description")


class LocationSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj: Location):
        return f"{str(obj)}"

    class Meta:
        model = Location
        fields = ("id", "country", "city", "street",
                  "building", "unit", "room_number", "name")


class DetailPositionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj: DetailPosition):
        return f"{str(obj)}"

    class Meta:
        model = DetailPosition
        fields = ("id", "position", "description", "name", "uuid")


class ItemImageSerializer(serializers.ModelSerializer):
    item_name = serializers.ReadOnlyField(source="item.name")
    category = CategorySerializer(source="item.category", read_only=True)

    class Meta:
        model = ItemImage
        fields = ("id", "image", "item", "item_name", "category")


class ItemFileSerializer(serializers.ModelSerializer):
    # def __init__(self, *args, **kwargs):
    #     many = kwargs.pop('many', True)
    #     super(ItemFileSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = ItemFile
        fields = ("id", "file", "item")


class ItemSerializer(serializers.ModelSerializer):
    images = ImageRelatedField(many=True,
                               read_only=True)
    files = FileRelatedField(many=True,
                             read_only=True)
    files_objects = ItemFileSerializer(source="files",
                                       many=True,
                                       read_only=True)
    images_objects = ItemImageSerializer(source="images",
                                         many=True,
                                         read_only=True)
    author_name = AuthorSerializer(source="author",
                                   read_only=True)
    series_name = SeriesSerializer(source="series",
                                   read_only=True)
    category_name = CategorySerializer(source="category",
                                       read_only=True)
    location_name = LocationSerializer(source="location",
                                       read_only=True)
    position_name = DetailPositionSerializer(source="detail_position",
                                             read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source="author",
                                                   queryset=Author.objects.all(), write_only=True,
                                                   required=True)
    series_id = serializers.PrimaryKeyRelatedField(source="series",
                                                   queryset=Series.objects.all(), write_only=True,
                                                   required=True)
    category_id = serializers.PrimaryKeyRelatedField(source="category",
                                                     queryset=Category.objects.all(),
                                                     write_only=True,
                                                     required=True)
    location_id = serializers.PrimaryKeyRelatedField(source="location",
                                                     queryset=Location.objects.all(),
                                                     write_only=True,
                                                     required=True)
    position_id = serializers.PrimaryKeyRelatedField(source="detail_position",
                                                     queryset=DetailPosition.objects.all(),
                                                     write_only=True,
                                                     required=True)

    class Meta:
        model = Item
        fields = (
            "id", "name", "description", "price", "column", "row", "qr_code", "unit", "created_time", "author_name",
            "series_name",
            "category_name", "location_name", "position_name",
            "images", "files", "author_id", "series_id", "category_id", "location_id", "position_id",
            "uuid", "files_objects", "images_objects")


class ItemAbstractSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source="author.name")
    series_name = serializers.ReadOnlyField(source="series.name")
    category_name = serializers.ReadOnlyField(source="category.name")
    position = serializers.ReadOnlyField(source="detail_position.position")

    class Meta:
        model = Item
        fields = ("id", "uuid", "name", "description", "author",
                  "author_name", "category_name",
                  "series_name", "column", "row", "unit",
                  "position")
