from django.db import models


class Pokemon(models.Model):
    name = models.CharField("Name", max_length=255)
    slug = models.CharField("Slug", max_length=255)
    image = models.ImageField("Image")
    typology_one = models.CharField(
        "Typology One", max_length=500, blank=True, default=""
    )
    typology_two = models.CharField(
        "Typology Two", max_length=500, blank=True, default=""
    )
    total = models.FloatField("Total", blank=True, null=True, default=None)
    health_points = models.FloatField("HP", blank=True, null=True, default=None)
    attack = models.FloatField("Attack", blank=True, null=True, default=None)
    defense = models.FloatField("Defense", blank=True, null=True, default=None)
    special_attack = models.FloatField(
        "Special attack", blank=True, null=True, default=None
    )
    special_defense = models.FloatField(
        "Special defense", blank=True, null=True, default=None
    )
    speed = models.FloatField("Speed", blank=True, null=True, default=None)
    is_legendary = models.BooleanField("Legendary", default=False)

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokedex"

    def __str__(self):
        return self.name
