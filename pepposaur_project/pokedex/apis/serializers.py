from rest_framework import serializers

from pokedex.models import Pokemon

class GetClosestPokemonsSerializer(serializers.Serializer):
    hp = serializers.FloatField(label="Health points")
    attack = serializers.FloatField(label="Attack")
    defense = serializers.FloatField(label="Defense")
    sp_atk = serializers.FloatField(label="Special Attack")
    sp_def = serializers.FloatField(label="Special Defense")
    speed = serializers.FloatField(label="Speed")

    class Meta:
        fields = (
            "hp",
            "attack",
            "defense",
            "sp_atk",
            "sp_def",
            "speed",
        )

class PokemonSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Pokemon
        fields = (
            "name",
            "slug",
            "image",
            "typology_one",
            "typology_two",
            "total",
            "health_points",
            "attack",
            "defense",
            "special_attack",
            "special_defense",
            "speed",
            "is_legendary",
        )

    def get_image(self, obj):
        if obj and obj.image:
            return obj.image.url
        return ""