from django.contrib import admin

from core.models import Autor
from core.models import Categoria
from core.models import Editora
from core.models import Livro
from core.models import Compra


admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Compra)
