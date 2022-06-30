from django.contrib import admin

from pokedex.models import Pokemon


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name", "typology_one", "typology_two", "is_legendary", "total")
    list_filter = ("is_legendary", "typology_one", "typology_two")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ["name"]}
    fieldsets = (
        (
            "Pokemon attributes",
            {
                "fields": (
                    ("name", "slug"),
                    ("image",),
                    ("typology_one", "typology_two"),
                    ("speed", "is_legendary"),
                    ("health_points", "total"),
                    ("attack", "special_attack"),
                    ("defense", "special_defense"),
                )
            },
        ),
    )
