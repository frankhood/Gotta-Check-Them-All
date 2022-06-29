from rest_framework import serializers

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