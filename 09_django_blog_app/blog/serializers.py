from rest_framework import serializers

from .models import Category, Blog


class BlogSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField() # Read Only
    category_id = serializers.IntegerField()

    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'content',
            'category',
            'category_id',
            'status',
            'created_date',
            'updated_date',
        )



class CategorySerializer(serializers.ModelSerializer):

    blogs = BlogSerializer(many = True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'blogs',
        )
