movies = {}
colection = []
for c in range (1, 4, 1):
    movies["name"] = str(input("Enter with the name of the movie: "))
    movies["year"] = int(input("Enter with the year that the movie was release: "))
    movies["Director"] = str(input("Enter with the Director of the movie: "))
    colection.append(movies.copy())
print(f"colection = {colection}")
for c in colection:
    print(f"Questions: {c.keys()}")
    print(f"Aswers: {c.values()}")
print(f"Resume: {colection.items()}")

