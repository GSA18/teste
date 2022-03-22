from encodings import search_function
from re import search
from django.contrib import admin

# Register your models here.
from escola.models import Aluno, Curso


class AlunoConfigAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "rg", "cpf", "data_nascimento")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_per_page = 20


class CursoConfigAdmin(admin.ModelAdmin):
    list_display = ("id", "cod", "nome", "descricao")
    list_display_links = ("id", "cod")
    search_fields = ("cod",)


admin.site.register(Aluno, AlunoConfigAdmin)
admin.site.register(Curso, CursoConfigAdmin)
