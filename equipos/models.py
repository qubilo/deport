from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import choices


class TipoBase(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre


class Timestamped(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(null=True, blank=True)
    creado_por = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)s_creado_por",
        null=True,
        blank=True
    )
    modificado_por = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="%(class)s_modificado_por"
    )
    ip_creacion = models.GenericIPAddressField(blank=True, null=True, verbose_name=_('ip_creacion'))
    ip_modificacion = models.GenericIPAddressField(blank=True, null=True, verbose_name=_('ip_modificacion'))

    class Meta:
        abstract = True


class Tipo(TipoBase, Timestamped):
    pass


class Modelo(TipoBase, Timestamped):
    pass


class Marca(TipoBase, Timestamped):
    pass


class Equipo(Timestamped):
    uuid = models.UUIDField(unique=True, default=uuid4)
    nombre = models.CharField(max_length=30)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    ano = models.SmallIntegerField()
    serial = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=30)
    dimensiones = models.IntegerField(default=0)
    riesgos = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400)

    def __str__(self):
        return self.nombre


class Evento(Timestamped):
    """ Tabla para almacenar todos los eventos de los equipos """
    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=100, verbose_name=_('nombre'),db_index=True)
    notas = models.CharField(max_length=100, verbose_name=_('notas'))
    categoria = models.CharField(max_length=100, choices=choices.Categoria.choices, verbose_name=_('categoria'))
    severidad = models.CharField(max_length=100, choices=choices.Severidad.choices, verbose_name=_('severidad'))
    actor_id = models.CharField(blank=True, max_length=36, null=True,verbose_name=_('id_actor'))
    actor_email = models.EmailField(blank=True, max_length=100, null=True,verbose_name=_('email_actor'))
    actor_nombre = models.CharField(max_length=100, null=True, blank=True, db_index=True,verbose_name=_('nombre_actor'))
    anonimo = models.BooleanField(default=False, verbose_name=_('anonimo'))
    propiedades = models.TextField(blank=True, null=True,verbose_name=_('propiedades'))
    origen = models.CharField(max_length=20, blank=True, null=True, choices=choices.Origen.choices, verbose_name=_('origen'))
    target_id = models.CharField(blank=True, max_length=36, null=True)
    fecha_evento = models.DateTimeField(verbose_name=_('fecha_evento'), blank=True, null=True)
    ip_origen = models.GenericIPAddressField(blank=True, null=True,verbose_name=_('ip_origen'))
    meta_datos = models.TextField(blank=True, null=True,verbose_name=_('meta_datos'))
    es_una_prueba = models.BooleanField(default=False, verbose_name=_('es_prueba'))
    equipo = models.ForeignKey(
        Equipo,
        on_delete=models.CASCADE
    )
