from django import template
register = template.Library()

@register.filter
def has_attendance(lesson, student):
	has_attended = lesson.attendance_set.filter(student=student)
	if has_attended.exists():	
		return has_attended.first().status 
	return 'N'



