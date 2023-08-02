def find_closer(thing: str, diagram:int, fruits: list):
    ngram = {}
    uniques = {}
    results = []
    for fruit in fruits:
        list_ngram_fruits = []
        i = 0
        while i < len(fruit):
            gram = len(fruit[i:i+diagram])
            if gram == diagram:
                list_ngram_fruits.append(fruit[i:i+diagram])
            i += 1
        ngram[fruit] = list_ngram_fruits
        uniques[fruit] = list(dict.fromkeys(ngram[fruit]))
    
    for i in range(len(thing)):
        list_ngram_thing = []
        i = 0
        while i < len(thing):
            gram = len(thing[i:i+diagram])
            if gram == diagram:
                list_ngram_thing.append(thing[i:i+diagram])
            i += 1
        ngram[thing] = list_ngram_thing
        uniques[thing] = list(dict.fromkeys(ngram[thing]))

    for fruit in fruits:
        A = len(uniques[thing])
        B= len(uniques[fruit])
        C = len([value for value in uniques[thing] if value in uniques[fruit]])
        results.append(2*C/(A+B))
        print(thing, fruit, 2*C/(A+B))
    
    return results
    

fruits = ['abacate', 'abacaxi', 'abobora', 'abobrinha', 'ananás', 'maça', 'mamão',
        'manga', 'melancia', 'melão', 'mexerica', 'morango']

find_closer('acabati', 2, fruits)

