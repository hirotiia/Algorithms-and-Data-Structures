result = {
    'A': 28,
    'B': 45,
    'C': 76,
    'D': 11,
}
print(sorted(result, key=result.get, reverse=True))