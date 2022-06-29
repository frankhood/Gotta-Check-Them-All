import csv
from django.core.management.base import BaseCommand
import os
from pokedex.models import Pokemon
from slugify import slugify
from django.core.files import File

class Command(BaseCommand):
    help = "Import Pokemon"

    def add_arguments(self, parser) -> None:
        parser.add_argument("path_csv", type=str, help="Insert path of csv file.")
        parser.add_argument("path_image", type=str, help="Insert the path of the folder containing the iamges.")

    def handle(self, *args, **options):
        # ==========================
        # Pokemon
        # ==========================

        path_csv = options['path_csv']
        path_image = options['path_image']

        file = open(f'{path_csv}/pokemon.csv', "r")
        reader = csv.reader(file)

        for row in reader:
            id_image = row[0]
            for _, _, files in os.walk(path_image):
                for file in files:
                    filename = file.split(".")[0]
                    if filename == id_image:
                        with open(f"{path_image}/{file}", "rb") as f:
                            pokemon = Pokemon.objects.create(
                                id=row.index,
                                name=row[1],
                                slug=slugify(row[1]),
                                # typology_one=slugify(row[2]),
                                # typology_two=slugify(row[3]),
                                total=row[4],
                                health_points=row[5],
                                attack=row[6],
                                defense=row[7],
                                special_attack=row[8],
                                special_defense=row[9],
                                speed=row[10],
                                is_legendary=True if row[12] == "True" else False,
                            )
                            # pokemon.image.save(content=f, name=f.name)
                            pokemon.image = File(f, name=os.path.basename(f.name)) # mette il file in memoria in modo tale da poter salavere il file
                            pokemon.save()
                            print(f"Pokemon {pokemon.name} importato.")

