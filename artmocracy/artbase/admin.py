from django.contrib import admin
from artbase.models import UserProfile, Art, WinningArt

admin.site.register(UserProfile)
admin.site.register(Art)
admin.site.register(WinningArt)
