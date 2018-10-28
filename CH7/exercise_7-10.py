places = []
activate = True
while activate:
    places.append(input("If you could visit one place in the world, where would you go?"))
    if input("Do you have other places to tell us?(Yes/No): ").lower() == "no":
        break
for place in places:
    print(place)