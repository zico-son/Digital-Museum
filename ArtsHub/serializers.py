from rest_framework import serializers
from ArtsHub.models import Hall, ArtObject, ArtStory, Chariot, Painting, Other, Holding, BorrowedCollection, PermanentCollection, ArtObjectImage


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = ['id', 'name']

class ArtStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtStory
        fields = ['title', 'description']

class ChariotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chariot
        fields = ['object_number', 'origin','chassis_number']

class PaintingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['artist_name']

class OtherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Other
        fields = ['origin']

class HoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holding
        fields = ['material']

class BorrowedCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedCollection
        fields = ['date_of_borrowing', 'date_of_return']

class PermanentCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermanentCollection
        fields = ['date_of_acquisition']

class ArtObjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtObjectImage
        fields = ['image']

class ArtObjectSerializer(serializers.ModelSerializer):
    hall = HallSerializer(read_only=True)
    art_story = ArtStorySerializer(read_only=True)
    images = ArtObjectImageSerializer(many=True, read_only=True)
    type = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    status_info = serializers.SerializerMethodField()
    class Meta:
        model = ArtObject
        fields = ['id', 'name', 'epoch', 'description', 'hall','images', 'art_story', 'created_at', 'updated_at','active', 'highlighted', 'type','content' ,'status', 'status_info']

    def get_type(self, obj):
        try:
            if obj.chariot:
                return 'chariot'
        except:
            try:
                if obj.painting:
                    return 'painting'
            except:
                try:
                    if obj.other:
                        return 'other'
                except:
                    return 'holdings'


    def get_content(self, obj):
        try:
            if obj.chariot:
                return ChariotSerializer(obj.chariot).data
        except:
            try:
                if obj.painting:
                    return PaintingSerializer(obj.painting).data
            except:
                try:
                    if obj.other:
                        return OtherSerializer(obj.other).data
                except:
                    return HoldingSerializer(obj.holdings, many = True).data

    def get_status(self, obj):
        try:
            if obj.borrowed_collection:
                return 'borrowed'
        except:
            return 'Permanent'

    def get_status_info(self, obj):
        try:
            if obj.borrowed_collection:
                return BorrowedCollectionSerializer(obj.borrowed_collection).data
        except:
            return PermanentCollectionSerializer(obj.permanent_collection).data