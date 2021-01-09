from django.contrib import admin

# Register your models here.
# ⬆ 自动创建的
# ⬇ 我写的
from .models import Post

admin.site.register(Post)
