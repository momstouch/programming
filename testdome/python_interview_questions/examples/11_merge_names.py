from collections import Counter
def unique_names(names1, names2):
    cnt = Counter(names1 + names2)
    return list(cnt.keys())

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
