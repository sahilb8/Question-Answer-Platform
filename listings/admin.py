from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('listing_id','question_title','category')
    list_display_links = ('listing_id','question_title')
    list_filter = ('category',)
    search_fields = ('question_title',)
admin.site.register(Listing, ListingAdmin) 