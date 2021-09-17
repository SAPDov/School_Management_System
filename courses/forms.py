from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('comment_name', 'body')

		labels = {"body": 'Comment:'}
		# widget = {

		# }
