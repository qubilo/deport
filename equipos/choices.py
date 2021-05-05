# Core Django imports
from django.db import models
from django.utils.translation import gettext_lazy as _


class Severidad(models.TextChoices):
    """Es usado en el modelo Evento"""
    
    BAJA = "BAJA", _("BAJA")
    MEDIA = "MEDIA", _("MEDIA")
    ALTA = "ALTA", _("ALTA")  


class Categoria(models.TextChoices):
    """Es usado en el modelo Evento"""
    
    INFO = "INFO", _("INFO")
    WARNING = "WARNING", _("WARNING")
    ERROR = "ERROR", _("ERROR")  
    FATAL = "FATAL", _("FATAL")  
    SUCCESS = "SUCCESS", _("SUCCESS") 


class Origen(models.TextChoices):
    """Es usado en el modelo Evento"""
    
    EQUIPO_MEDICO = "EQUIPO_MEDICO", _("EQUIPO_MEDICO")
    USUARIO = "USUARIO", _("USUARIO")
    TERCERO = "TERCERO", _("TERCERO")
