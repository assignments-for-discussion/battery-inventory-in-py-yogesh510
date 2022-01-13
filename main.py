def count_batteries_by_usage(cycles):
    lowCount = 0
    mediumCount = 0
    highCount = 0
    for i in range(len(cycles)):
        if cycles[i] < 400:
            lowCount += 1
        elif cycles[i] > 400 and cycles[i] < 919:
            mediumCount += 1
        elif cycles[i] > 920:
            highCount += 1

    return {
        "lowCount": lowCount,
        "mediumCount": mediumCount,
        "highCount": highCount}


def test():
    print("Counting batteries by usage cycles...\n");
    counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
    assert (counts["lowCount"] == 2)
    assert (counts["mediumCount"] == 3)
    assert (counts["highCount"] == 1)
    print("Done counting :)")


test()