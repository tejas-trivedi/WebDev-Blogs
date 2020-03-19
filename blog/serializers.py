from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer): 
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=200)
    content=serializers.CharField()
    date_posted=serializers.DateTimeField()