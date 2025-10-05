def levenshtein(word1: str, word2: str) -> int:
    matrix: list[list[int]] = [[] for _ in range(len(word1) + 1)]

    for num in range(len(word2) + 1):
        matrix[0].append(num)

    for num in range(1, len(word1) + 1):
        matrix[num].append(num)

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            levens = 0

            if word1[i - 1] != word2[j - 1]:
                levens = (
                    min(
                        (
                            matrix[i - 1][j],  # top
                            matrix[i][j - 1],  # left
                            matrix[i - 1][j - 1],  # digonal
                        )
                    )
                    + 1
                )

            else:
                levens = matrix[i - 1][j - 1]

            matrix[i].append(levens)

    return matrix[len(word1)][len(word2)]


if __name__ == "__main__":
    print(levenshtein("kitten", "sitting"))
    print(levenshtein("flaw", "lawn"))
