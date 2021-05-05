""" Administradores de los modelos del modulo equipos """
import datetime

from django.contrib import admin
from equipos.models import Equipo, Evento, Tipo, Modelo, Marca


class EquipoAdmin(admin.ModelAdmin):
    """ Administrador del modelo equipo """
    fields = ["nombre", "tipo", "modelo", "marca", "ano", "serial",
    "ubicacion", "dimensiones", "riesgos", "descripcion"
    ]
    list_display = ["uuid", "nombre", "tipo", "modelo", "marca", "ano",
    "serial", "ubicacion", "dimensiones", "riesgos", "descripcion"
    ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.creado_por = request.user
            obj.ip_creacion = request.META.get("REMOTE_ADDR")
        if change:
            obj.modificado_por = request.user
            obj.fecha_modificacion = datetime.datetime.today()
            obj.ip_modificacion = request.META.get("REMOTE_ADDR")
        super().save_model(request, obj, form, change)   


class EventoAdmin(admin.ModelAdmin):
    """ Administrador del modelo Evento """
    fields = ["nombre", "notas", "categoria", "severidad", "actor_id", "actor_email", "actor_nombre", "anonimo",
    "propiedades", "origen", "target_id", "fecha_evento", "ip_origen", "meta_datos", "es_una_prueba", "equipo"
    ]
    list_display = ["uuid", "nombre", "notas", "categoria", "severidad", "actor_id", "actor_email", "actor_nombre",
    "anonimo", "propiedades", "origen", "target_id", "fecha_evento", "ip_origen", "meta_datos", "es_una_prueba", "equipo"
    ]
    list_filter = ["categoria", "severidad", "origen", "fecha_creacion", "fecha_modificacion", "es_una_prueba", "equipo"]
    search_fields = ["nombre", "propiedades"]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.creado_por = request.user
            obj.ip_creacion = request.META.get("REMOTE_ADDR")
        if change:
            obj.modificado_por = request.user
            obj.fecha_modificacion = datetime.datetime.today()
            obj.ip_modificacion = request.META.get("REMOTE_ADDR")
        super().save_model(request, obj, form, change)


class TipoAdmin(admin.ModelAdmin):
    """ Administrador del modelo tipo """
    fields = ["nombre"]
    list_display = ["nombre", "creado_por", "fecha_creacion", "ip_creacion", "modificado_por", "fecha_modificacion", "ip_modificacion"]
 
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.creado_por = request.user
            obj.ip_creacion = request.META.get("REMOTE_ADDR")
        if change:
            obj.modificado_por = request.user
            obj.fecha_modificacion = datetime.datetime.today()
            obj.ip_modificacion = request.META.get("REMOTE_ADDR")
        super().save_model(request, obj, form, change)
        

class ModeloAdmin(admin.ModelAdmin):
    """ Administrador del modelo Modelo """
    fields = ["nombre"]
    list_display = ["nombre", "creado_por", "fecha_creacion", "ip_creacion", "modificado_por", "fecha_modificacion", "ip_modificacion"]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.creado_por = request.user
            obj.ip_creacion = request.META.get("REMOTE_ADDR")
        if change:
            obj.modificado_por = request.user
            obj.fecha_modificacion = datetime.datetime.today()
            obj.ip_modificacion = request.META.get("REMOTE_ADDR")
        super().save_model(request, obj, form, change)    


class MarcaAdmin(admin.ModelAdmin):
    """ Administrador del modelo Marca """
    fields = ["nombre"]
    list_display = ["nombre", "creado_por", "fecha_creacion", "ip_creacion", "modificado_por", "fecha_modificacion", "ip_modificacion"]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.creado_por = request.user
            obj.ip_creacion = request.META.get("REMOTE_ADDR")
        if change:
            obj.modificado_por = request.user
            obj.fecha_modificacion = datetime.datetime.today()
            obj.ip_modificacion = request.META.get("REMOTE_ADDR")
        super().save_model(request, obj, form, change)


admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.site_header = 'Deport'