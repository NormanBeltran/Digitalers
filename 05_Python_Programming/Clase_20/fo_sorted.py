def mi_orden(x):
    return len(x)

lista = ["a", "abcde", "z", "abcdef", "asd", "mmmm", "adfhkafhasfa"]

print(sorted(lista, key=mi_orden, reverse=True ))