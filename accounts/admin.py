from django.contrib import admin
from accounts.models import User, Location





class UserAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','email', 'phone', 'bloodgroup', 'is_staff')

	def is_staff(self, obj):
		return obj.discription
	#email.short_discription = 'hello'


admin.site.register(Location)
admin.site.register(User, UserAdmin)
admin.site.site_header = 'Suatainable Blood(Admin Panel)'