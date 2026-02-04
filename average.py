# average.py
# def moyenne(liste):
#     if not liste:
#         return 0
#     return sum(liste) / len(liste)
def moyenne(liste):
    return sum(liste)  # bug : ne divise pas par len(liste)
