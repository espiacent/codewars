authors = ["Peter pan", "Elefant Man", "Isaak Asimov",
           "Michael meyers", "freddy Kruger", "david bowie", "rIcky GErVAIS"]

authors.sort(key=lambda name: name.split(" ")[-1].lower(), reverse=True)

print(authors)
