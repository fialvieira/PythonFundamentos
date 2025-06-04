import pprint

filmsDict = {
    "Inception": {
        "yearRelease": 2010,
        "imdbRating": 8.8,
        "genre": ["Sci-Fi", "Action", "Thriller"]
    },
    "Interstellar": {
        "yearRelease": 2014,
        "imdbRating": 8.6,
        "genre": ["Sci-Fi", "Drama"]
    },
    "The Dark Knight": {
        "yearRelease": 2008,
        "imdbRating": 9.0,
        "genre": ["Action", "Drama", "Crime"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

# 1 - Buscar uma informação dentro de um dicionário aninhado
pp.pprint(filmsDict["Interstellar"]["genre"])

# 2 - Adicionar novo item
filmsDict["Inception"]["director"] = "Christopher Nolan"
pp.pprint(filmsDict["Inception"])

# 3 - Excluir um dicionário
del filmsDict["The Dark Knight"]
pp.pprint(filmsDict)