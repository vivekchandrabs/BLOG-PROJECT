from django.contrib import admin
from blogger.models	import blogpost, comments

admin.site.register(blogpost)

admin.site.register(comments)
# Register your models here.
