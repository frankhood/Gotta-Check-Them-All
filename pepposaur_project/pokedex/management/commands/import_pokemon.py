import csv
from django.core.management.base import BaseCommand
import os
from pokedex.models import Pokemon
from slugify import slugify
from django.core.files import File

class Command(BaseCommand):
    help = "Import Pokemon"

    def add_arguments(self, parser) -> None:
        parser.add_argument("path_file_csv", type=str, help="Insert path of csv file.")
        parser.add_argument("path_file_image", type=str, help="Insert the path of the folder containing the iamges.")

    def handle(self, *args, **options):
        path_file_csv = options['path_file_csv']
        path_file_image = options['path_file_image']
        file = open(f'{path_file_csv}', "r")
        reader = csv.reader(file)
        next(reader) # ignoro la prima riga

        for idx, row in enumerate(reader):
            id_image = row[0]
            for _, _, files in os.walk(path_file_image):
                for file in files:
                    filename = file.split(".")[0]
                    if filename == id_image:
                        with open(f"{path_file_csv}", "rb") as f:
                            pokemon, created = Pokemon.objects.get_or_create(
                                id=idx,
                                slug=slugify(row[1]),
                                defaults={
                                    "name":row[1],
                                    # typology_one:row[2],
                                    # typology_two:row[3],
                                    "total":row[4],
                                    "health_points":row[5],
                                    "attack":row[6],
                                    "defense":row[7],
                                    "special_attack":row[8],
                                    "special_defense":row[9],
                                    "speed":row[10],
                                    "is_legendary":True if row[12] == "True" else False,
                                    }
                                
                            )
                            if created:
                                # pokemon.image.save(content=f, name=f.name)
                                pokemon.image = File(f, name=os.path.basename(f.name)) # mette il file in memoria in modo tale da poter salvare il file
                                pokemon.save()
                                print(f"Pokemon {pokemon.name} importato.")
                            else:
                                print(f"Pokemon {pokemon.name} già importato.")

