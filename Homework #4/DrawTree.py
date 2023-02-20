class DrawTree:
    def draw(parents, names):
        lines = [""] * len(parents)
        lineNum = 0

        def drawLeaf(root, depth):
            nonlocal lineNum

            for i in range(len(parents)):
                if parents[i] == root:
                    lines[lineNum] = ""
                    for j in range(depth):
                        lines[lineNum] += "  "

                    lines[lineNum] += "+-" + names[i]
                    pipeNum = lineNum - 1
                    while pipeNum >= 0 and lines[pipeNum][depth * 2] == ' ':
                        oldLeaf = lines[pipeNum]
                        lines[pipeNum] = ""
                        for j in range(len(oldLeaf)):
                            if j == depth * 2:
                                lines[pipeNum] += '|'
                            else:
                                lines[pipeNum] += oldLeaf[j]
                        pipeNum -= 1

                    lineNum += 1
                    drawLeaf(i, 1 + depth)

        drawLeaf(-1, 0)
        return lines
