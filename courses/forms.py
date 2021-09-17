from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('body', )

		labels = {'body': 'Comment:'}
		# widget = {

		# }

	
