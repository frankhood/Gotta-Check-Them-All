from pepposaur_project.pokedex.apis.serializers import GetClosestPokemonsSerializer
from pepposaur_project.pokedex.models import Pokemon
from pepposaur_project.pokedex.utils import df_get_k_neighbors
from rest_framework import views, status
from rest_framework.response import Response
import pandas as pd


class GetClosestPokemonsAPIView(views.APIView):
    
    serializer_class = GetClosestPokemonsSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Cosa deve stare in serializer.data
        # our_pokemon = [hp, attack, defense, sp_atk, sp_def, speed]
        # df_pokemon=pd.read_csv('pokemon.csv')
        # pokemons = df_get_k_neighbors(df_pokemon, serializer.data)
        # list(pokemons.index)
        # Pokemon.objects.filter(id__in=list(pokemons.index))
        return Response(serializer.data, status=status.HTTP_200_OK)