def solve(shows, durations, k):
    p1 = 0
    p2 = 0
    n_dict = {}
    while p1 < len(shows):
        if shows[p1] not in n_dict:
            n_dict[shows[p1]] = durations[p2]
            p1 += 1
            p2 += 1
        else:
            n_dict[shows[p1]] += durations[p2]
            p1 += 1
            p2 += 1
    ans = 0
    for i in range(k):
        Keymax = max(n_dict, key=n_dict.get)
        ans += n_dict[Keymax]
        del n_dict[Keymax]
    return ans
if __name__ == "__main__":
    shows = ["Top Gun", "Aviator", "Top Gun", "Roma", "Logan"]
    durations = [5, 3, 5, 13, 4]
    k = 2
    print(solve(shows, durations, k))