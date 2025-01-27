from django.contrib import admin

# Register your models here.
# userName: mohamad
# PassWord: 123123
from .models import User

admin.site.register(User)