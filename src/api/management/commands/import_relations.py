import os
import sys

from django.core.management import BaseCommand

from core.models import Relation


class Command(BaseCommand):
    help = "Imports list of relations to the system"

    def handle(self, *args, file=None, **options):
        path = os.path.join(os.path.abspath(os.curdir), "relations.txt")
        with open(path, "r", encoding="utf-8") as f:
            lines = f.read().strip().split("\n")

        relations = []
        for line in lines:
            relations.append(Relation(name=line))

        Relation.objects.bulk_create(relations, ignore_conflicts=True)
        print("finish")
