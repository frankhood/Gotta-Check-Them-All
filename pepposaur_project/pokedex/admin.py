from django.contrib import admin
from django.utils.safestring import mark_safe


from pokedex.models import Pokemon

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name", "is_legendary", "total")
    list_filter = ("is_legendary",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ["name"]}
    fieldsets = (
        ("Pokemon attributes", {"fields": (
            ("name", "slug"),
            ("image",),
            ("speed", "is_legendary"),
            ("health_points", "total"),
            ("attack", "special_attack"),
            ("defense", "special_defense"),
        )}),
    )