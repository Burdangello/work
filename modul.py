# Je set A podmnožinou setu B
fr_set_a = frozenset({"zena", "ruze", "kost", "pisen", "Lucie", "Matous"})
fr_set_b = frozenset({"zena", "ruze", "kost", "pisen",})
print(fr_set_a.isdisjoint(fr_set_b))
