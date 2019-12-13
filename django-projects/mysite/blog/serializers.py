from .models import Blog
from rest_framework import serializers
class BlogSerializers(serializers.ModelSerializer):
	class Meta:
		model = Blog
		fields = ('id','name','tagline')