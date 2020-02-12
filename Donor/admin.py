from django.contrib import admin
from .models import Event, Bloodbank, Feedback
# Register your models here.



class EventAdmin(admin.ModelAdmin):
	list_display = ('title','organizer','location','anouncedate')

	def is_staff(self, obj):
		return obj.discription


class BloodbankAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'loaction')

	def is_staff(self, obj):
		return obj.discription


class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('name','subject','email','comment')

	def is_staff(self, obj):
		return obj.discription


admin.site.register(Event, EventAdmin)
admin.site.register(Bloodbank, BloodbankAdmin)
admin.site.register(Feedback, FeedbackAdmin)