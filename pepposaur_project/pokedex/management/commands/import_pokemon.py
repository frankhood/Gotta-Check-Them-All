import csv
from django.core.management.base import BaseCommand
import os
from pokedex.models import Pokemon
from slugify import slugify
from django.core.files import File


class Command(BaseCommand):
    help = "Import Pokemon"

    def add_arguments(self, parser) -> None:
        parser.add_argument("path_file_csv", type=str,
                            help="Insert path of csv file.")
        parser.add_argument("path_directory_images", type=str,
                            help="Insert the path of the folder containing the iamges.")

    def handle(self, *args, **options):
        path_file_csv = options['path_file_csv']
        path_directory_images = options['path_directory_images']
        file = open(f'{path_file_csv}', "r")
        reader = csv.reader(file)
        next(reader)  # ignoro la prima riga

        for idx, row in enumerate(reader):
            idx += 1
            id_image = row[0]
            for _, _, files in os.walk(path_directory_images):
                for file in files:
                    filename = file.split(".")[0]
                    if filename == id_image:
                        with open(f"{path_directory_images}/{file}", "rb") as f:
                            ##################### Gestione con Try Except #################
                            # try:
                            #     pokemon = Pokemon.objects.get(id=idx, slug=slugify(row[1]))
                            #     print(f"Pokemon {pokemon.name} già importato.")
                            # except Pokemon.DoesNotExist:
                            #     pokemon = Pokemon(
                            #         id = idx,
                            #         slug = slugify(row[1]),
                            #         name = row[1],
                            #         typology_one = row[2],
                            #         typology_two = row[3],
                            #         total = row[4],
                            #         health_points = row[5],
                            #         attack = row[6],
                            #         defense = row[7],
                            #         special_attack = row[8],
                            #         special_defense = row[9],
                            #         speed = row[10],
                            #         is_legendary = True if row[12] == "True" else False,
                            #         image=File(f, name=os.path.basename(f.name))
                            #     )
                            #     pokemon.save()
                            #     print(f"Pokemon {pokemon.name} importato.")
                            ############### Utilizzo del get_or_create di Django ######################
                            pokemon, created = Pokemon.objects.get_or_create(
                                id=idx,
                                slug=slugify(row[1]),
                                defaults={
                                    "name": row[1],
                                    "typology_one": row[2],
                                    "typology_two": row[3],
                                    "total": row[4],
                                    "health_points": row[5],
                                    "attack": row[6],
                                    "defense": row[7],
                                    "special_attack": row[8],
                                    "special_defense": row[9],
                                    "speed": row[10],
                                    "is_legendary": True if row[12] == "True" else False,
                                    "image": File(f, name=os.path.basename(f.name))
                                }

                            )
                            if created:
                                print(f"Pokemon {pokemon.name} importato.")
                            else:
                                print(f"Pokemon {pokemon.name} già importato.")
