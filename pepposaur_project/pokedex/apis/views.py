from pokedex.apis.serializers import PokemonSerializer
from pokedex.apis.serializers import GetClosestPokemonsSerializer
from pokedex.models import Pokemon
from pokedex.utils import df_get_k_neighbors
from rest_framework import status, generics
from rest_framework.response import Response
import pandas as pd


class GetClosestPokemonsAPIView(generics.GenericAPIView):
    
    serializer_class = GetClosestPokemonsSerializer

    def get_queryset(self):
        return Pokemon.objects.all()
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        our_pokemon_data = [
            serializer.data.get("hp"), 
            serializer.data.get("attack"), 
            serializer.data.get("defense"), 
            serializer.data.get("sp_atk"), 
            serializer.data.get("sp_def"), 
            serializer.data.get("speed")
        ]
        df_pokemon = pd.read_csv('../Gotta-Check-Them-All/pokemon.csv')
        pokemons = df_get_k_neighbors(df_pokemon, our_pokemon_data)
        response_serializer = PokemonSerializer(Pokemon.objects.filter(id__in=list(pokemons.index)), many=True)
        return Response(response_serializer.data, status=status.HTTP_200_OK)