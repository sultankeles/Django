from rest_framework import serializers

from .models import Path, Student

class StudentSerializer(serializers.ModelSerializer):
    
    born_year = serializers.SerializerMethodField()  # read_only
    path = serializers.StringRelatedField()  # read_only
    path_id = serializers.IntegerField()
    
    class Meta:
        model = Student
        fields = ["id","first_name", "last_name","number", "age", "born_year", "path", "path_id"]

        
    def get_born_year(self, obj):
        import datetime
        current_time = datetime.datetime.now()
        return current_time.year - obj.age
    
    
class PathSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Path
        fields = ["id", "path_name"]