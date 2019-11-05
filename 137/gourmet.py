#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""
import itertools
from collections import Counter
import operator

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]


def _similarity(a, b):
    def letter_counter(item):
        c = Counter()
        for char in item.lower():
            c[char] += 1
        return c

    ac = letter_counter(a)
    bc = letter_counter(b)

    def score(a, b):
        d = dict()
        for k, v in a.items():
            if k in b.keys():
                d[k] = min(v, b[k])
        return sum(d.values())

    return score(ac, bc) / (1 + abs(len(a) - len(b)) ** 2)


def best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    if wine_type == "all":
        wine_it = itertools.chain(RED_WINES, WHITE_WINES, SPARKLING_WINES)
    elif wine_type == "white":
        wine_it = iter(WHITE_WINES)
    elif wine_type == "red":
        wine_it = iter(RED_WINES)
    elif wine_type == "sparkling":
        wine_it = iter(SPARKLING_WINES)
    else:
        raise ValueError

    output = ["wine", "cheese", 0]

    for wine in wine_it:
        for cheese in CHEESES:
            similarity_score = _similarity(wine, cheese)
            if similarity_score > output[2]:
                output[0] = wine
                output[1] = cheese
                output[2] = similarity_score

    return tuple(output)


def match_wine_5cheeses():
    """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """
    pairs = list()
    for wine in itertools.chain(WHITE_WINES, RED_WINES, SPARKLING_WINES):
        cheese_list = list()
        for cheese in CHEESES:
            cheese_list.append((cheese, _similarity(wine, cheese)))
        cheese_list.sort(key=lambda x: x[0])
        cheese_list.sort(key=lambda x: x[1], reverse=True)
        cheeses = [cheese_list[i][0] for i in range(0, 5)]
        pairs.append((wine, cheeses))
    return sorted(pairs, key=lambda x: x[0])
