# Homework 6: Advanced Loops

for row in range(31):
    if row % 2 == 0:
        for column in range(1, 159):
            if column % 2 == 1:
                if column != 30:
                    print(" ", end="")
                else:
                    print(" ")
            else:
                print("|", end="")
        print(" | | ")
    else:
        print("-" * 162)
