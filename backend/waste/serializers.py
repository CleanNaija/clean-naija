from rest_framework import serializers
from django.contrib.auth import get_user_model

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=('id', 'username', 'email', 'first_name', 'last_name', 'role', 'phone_number', 'address','password')
        extra_kwargs={
            'password':{
                'write_only':True # This is to ensure the password is write-only and not returned in the response
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password:
            user.set_password(password)  # This hashes the password
        
        user.save()
        return user
        
        def update(self,instance,validated_data):
            #Extract the password from the validated data 
            password=validated_data.pop('password',None)

            #Update the user instance with the remaining data 
            for attr,value in validated_data.items():
                setattr(instance,attr,value)

            #Hash the password and set it for the user if provided
            if password:
                instance.set_password(password)

            #Save the updated user to the database
            instance.save()
            return instance 
        

# serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UpdateProfileSerializer(serializers.ModelSerializer):
    """
    Serializer to update user profile information
    """
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'username']  # Add other fields you want to allow the user to update
        read_only_fields = ['username']  # If you don't want users to update their username, for example



from rest_framework import serializers
from .models import WasteBin, WasteCollectionRequest, WasteType, CollectionPoint, CollectionRequest, Report, WasteAnalytics
from django.contrib.auth import get_user_model

# WasteBin Serializer
class WasteBinSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteBin
        fields = '__all__'

# WasteCollectionRequest Serializer
class WasteCollectionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteCollectionRequest
        fields = '__all__'

# WasteType Serializer
class WasteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteType
        fields = '__all__'

# CollectionPoint Serializer
class CollectionPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionPoint
        fields = '__all__'

# CollectionRequest Serializer
class CollectionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionRequest
        fields = '__all__'

# Report Serializer
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

# WasteAnalytics Serializer
class WasteAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteAnalytics
        fields = '__all__'
