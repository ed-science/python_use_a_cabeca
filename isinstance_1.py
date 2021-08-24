

# create lists in list of movies
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman",  ["Michael Palin", "John Cleese", "Terry Gilliam",
          "Eric Idle", "Terry Jones"]]]

# Processar a lista movies
for each_item in movies:
    # verificar se o item atual é uma lista
    if isinstance(each_item,list):
        # O loop interno precisa de identificador de destino, no caso nested_item
        # se for uma lista usar o loop for para processar a lista aninhada
        for nested_item in each_item:
            print(nested_item)
    # se o item atual anexado à lista não é uma lista, exibir na tela        
    else:
        print(each_item)



