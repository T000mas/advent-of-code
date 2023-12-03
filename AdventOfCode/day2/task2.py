def task_2():
    allCubesCollors = ["red", "green", "blue"]
    allCubesAbount = [12, 13, 14]

    with open("day2/dataset2.txt") as f:
        for line in f:
            isPossible = True
            game = line.split(":")
            gameNumber, cubeSets = game[0], game[1]
            for cubeSetsSemicolonSplit in cubeSets.split(";"):
                for cubeSetsCommaSplit in cubeSetsSemicolonSplit.split(","):
                    numberOfCubes, colorOfCubes = (
                        cubeSetsCommaSplit.split(" ")[1],
                        cubeSetsCommaSplit.split(" ")[2],
                    )
                    for (c, n) in (allCubesCollors, allCubesAbount):
                        if colorOfCubes == c:
                            if allCubesAbount > n:
                                isPossible = False
            if not isPossible:                
                print("not possible", game, cubeSets)