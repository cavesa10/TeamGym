from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.user import User
from .models.planes import Planes
from .models.videos import Videos
from .models.imc import Imc
admin.site.register(User)
admin.site.register(Planes)
admin.site.register(Videos)
admin.site.register(Imc)