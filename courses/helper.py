from django import template


register = template.Library()


@register.filter
def duration(td):
	total_seconds = int(td.total_seconds())
	hours = total_seconds // 3600
	minutes = (total_seconds % 3600) // 60

	return '{} hours {} min'.format(hours, minutes)


# def get_overtime_application_hours(start_time, end_time) -> int:
# 	difference = end_time - start_time
# 	hours = difference.seconds/3600
# 	print(hours)
# 	return hours 

# def duration(self):
# 	hours = get_overtime_application_hours(self.out, self._in)
# 	return round(hours)
