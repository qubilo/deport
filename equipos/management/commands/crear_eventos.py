import random

from django.core.management.base import BaseCommand
from equipos.models import Evento, Equipo
from equipos.choices import Severidad, Categoria, Origen


class Command(BaseCommand):
    help = 'Crea eventos en la base de datos'
    def handle(self, *args, **kwargs):
        Evento.objects.all().delete()
        nombres = ["FALLO INTERNO", "FALLA EN LA BATERIA", "FALLA EN LECTURA", "FALLO EN LA PANTALLA",
        "CAIDA DE ENERGIA", "SOBRE CALENTAMIENTO"]
        ips = ["172.16.4.205", "192.168.0.0", "136.0.0.11", "10.0.0.0", "1.0.0.205", "186.0.0.12", "192.0.0.15"]
        propiedades = [" PACS, HIS/RIS", "DR-D 20", "sistema de de procesamiento MÚSICA 2", "confort"]
        metadata = []
        notas = ["fácil manejo", "calidad de imagen excelente", "ofrece imágenes rápidas", "ofrece imágenes lentas", "dificil manejo", "calidad de imagne mala"]

        for n in range(100):
            Evento.objects.create(**{
                "nombre":  random.choice(nombres),
                "notas": random.choice(notas),
                "severidad": str(random.choice(Severidad.choices)[0]),
                "categoria": str(random.choice(Categoria.choices)[0]),
                "propiedades": random.choice(propiedades),
                "ip_origen": random.choice(ips),
                "meta_datos": random.choice(metadata),
                "equipo": Equipo.objects.order_by("?").first(),
                
            })
