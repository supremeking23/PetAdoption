from django.contrib import admin

from .models import Pet, Vaccine

#from django.utils.html import mark_safe

# Register your models here.


class PetAdmin(admin.ModelAdmin):
	list_display = ['pet_name','species','breed','age','sex','submitter']

	#fields = ['image_tag']
	search_fields = ['pet_name','submitter']

"""
	def image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.headshot.url,
			width=obj.headshot.width,
			height=obj.headshot.height,
		)
	)
"""

admin.site.register(Pet,PetAdmin)
admin.site.register(Vaccine)

