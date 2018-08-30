from django.db import models

# Create your models here.

class blogpost(models.Model):
	title=models.CharField(max_length=20)
	body=models.TextField(max_length=200)
	datepublish=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class comments(models.Model):
	post=models.ForeignKey(blogpost,on_delete=models.CASCADE)
	text=models.TextField()
	timestamp=models.DateTimeField(auto_now_add=True)

	def __str__(self):

		return f"{self.post.title}|{self.text[:30]}"