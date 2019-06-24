from abc import ABC
from .models import *
from rest_framework import serializers


class ImageRelatedField(serializers.RelatedField, ABC):
    def to_representation(self, value: ItemImage):
        return value.image.url


class LocationField(serializers.ReadOnlyField, ABC):
    def to_representation(self, value: Location):
        return LocationSerializer(value).data


class SeriesField(serializers.ReadOnlyField, ABC):
    def to_representation(self, value: Series):
        return SeriesSerializer(value).data


class AuthorField(serializers.ReadOnlyField, ABC):
    def to_representation(self, value: Author):
        return AuthorSerializer(value).data


class CategoryField(serializers.ReadOnlyField, ABC):
    def to_representation(self, value: Category):
        return CategorySerializer(value).data


class PositionField(serializers.ReadOnlyField, ABC):
    def to_representation(self, value: DetailPosition):
        return DetailPositionSerializer(value).data


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
    class Meta:
        model = Location
        fields = ("id", "country", "city", "street", "building", "unit", "room_number")


class DetailPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailPosition
        fields = ("id", "position", "description")


class ItemImageSerializer(serializers.ModelSerializer):
    item_name = serializers.ReadOnlyField(source="item.name")

    class Meta:
        model = ItemImage
        fields = ("id", "image", "item", "item_name")


class ItemSerializer(serializers.ModelSerializer):
    # images = serializers.SlugRelatedField(slug_field="title", queryset=ItemImage.objects.all(), many=True)
    images = ImageRelatedField(many=True, read_only=True)
    author_name = AuthorField(source="author")
    series_name = SeriesField(source="series")
    category_name = CategoryField(source="category")
    location_name = LocationField(source="location")
    position_name = PositionField(source="detail_position")

    class Meta:
        model = Item
        fields = (
            "id", "name", "description", "created_time", "author_name", "series_name",
            "category_name", "price", "qr_code", "location_name", "position_name",
            "images", "column", "row")


class ItemAbstractSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source="author.name")
    series_name = serializers.ReadOnlyField(source="series.name")
    category_name = serializers.ReadOnlyField(source="category.name")
    position = serializers.ReadOnlyField(source="detail_position.position")

    class Meta:
        model = Item
        fields = ("id", "name", "description",
                  "author_name", "category_name",
                  "series_name", "column", "row",
                  "position")
