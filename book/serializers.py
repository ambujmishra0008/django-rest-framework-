from rest_framework import serializers
from .models import Book


class BookModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        exclude = ('desc',)
    
       
class BookListSerializer(serializers.ListSerializer):
    title = serializers.CharField(required=True, max_length=50)
    desc = serializers.CharField(required=False, max_length=400)

    
    def save(self, **kwargs):
        
        obj_list = []
        for data in self.validated_data:
            if data["title"] !="nit":
                obj_list.append(Book(**data))
        print(obj_list)
        return Book.objects.bulk_create(obj_list)
            
 
    
    

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=50)
    desc = serializers.CharField(required=False, max_length=400)
    
    class Meta:
        list_serializer_class = BookListSerializer
    
    
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def save(self):
        return Book.objects.create(**self.validated_data)

    

    
    # def validate_title(self, value):
    #     if "mishra" not in value:
    #         raise serializers.ValidationError("MISHRA should be present in title")
        
    #     return value
            
    # def validate(self, attrs):
    #     if "mishra" not in attrs["title"]:
    #         raise serializers.ValidationError("MISHRA should be present in title")
    #     return attrs


    # def create(self, validated_data):
    #     return Book.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data["title"]
    #     instance.save()
    #     return super().update(instance, validated_data)
    
    # def to_representation(self, instance):
    #     out_dict = super().to_representation(instance)
    #     out_dict["age"] = 25
    #     out_dict["title"] = out_dict["title"] + "_ambuj"
    #     return out_dict
    
    # def to_internal_value(self, data):
    #     data["age"] = 25
    #     data["title"] = data["title"]+ "_nothing"
    #     return data
        
        
    
        

   


















