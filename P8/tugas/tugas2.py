global facts
global is_changed

facts = [["A", 10000], ["B", 25]]
is_changed = True


def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True


while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "A" and A1[1] >= 10000:
            if ["C",  "College"] in facts:
                assert_fact(["E", True])
        if A1[0] == "B":
            if A1[1] > 22 and A1[1] < 30:
                assert_fact(["C", "College"])
        if A1[0] == "D" and A1[1] >= 40000:
            assert_fact(["F", True])
        if A1[0] == "B" and A1[1] < 30:
            if ["E", True] in facts:
                assert_fact(["F", True])
        if A1[0] == "F" and A1[1] == True:
            assert_fact(["G", True])

if ["G", True] in facts:
    print("Anda cocok investasi pada saham pertumbuhan dengan jenis saham IBM")
elif ["E", True] and ["F", False] in facts:
    print("Anda cocok investasi pada saham sekuritas")
else:
    print("Anda kurang beruntung")
