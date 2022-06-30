from django.urls import path
from pokedex.apis import views as app_views


urlpatterns = [
    path("get-closest-pokemons/", app_views.GetClosestPokemonsAPIView.as_view(), name="get_closest_pokemon")
]