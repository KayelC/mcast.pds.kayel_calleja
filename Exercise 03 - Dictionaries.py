game = {
    "title" : "Devil May Cry 3",
    "price" : "19.99",
    "platforms" : ["PC", "PlayStation 2"]
}

discount = float(game["price"]) * 0.9
print (discount)

game["rating"] = "9.9"
game["year_released"] = 2005

del(game["platforms"])

print (game)

print (game.keys())

game_list = list(game.values())
print(game_list)

game_additional = {
        "publisher" : "Capcom",
        "dlc_available" : "False"
}

game.update(game_additional)

print (game)