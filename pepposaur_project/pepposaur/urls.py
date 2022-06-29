from django.contrib import admin
from django.urls import include, path
from pokedex import views as pokedex_views
from django.conf.urls import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        pokedex_views.CheckThemAllTemplateView.as_view(),
        name="check_them_all_homepage",
    ),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
