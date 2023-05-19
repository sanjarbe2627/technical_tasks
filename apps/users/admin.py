from django.contrib import admin
from apps.users.models import User, Sponsor

admin.site.register(User)
admin.site.register(Sponsor)
