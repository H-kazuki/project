from django.db import models



class Category(models.Model):
	title = models.CharField('タイトル', max_length = 20)

	def __str__(self):
		return self.title



class Todo(models.Model):
	username = models.CharField('Username', max_length = 150, null = True)
	title = models.CharField('Title', max_length = 50)
	contents = models.TextField('Contents', max_length = 200)
	created_at = models.DateTimeField('Date', auto_now_add = True)
	category = models.ForeignKey(Category, on_delete = models.PROTECT)

	def __str__(self):
		return self.title + ':' + self.contents
		