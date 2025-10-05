def levenshtein(word1: str, word2: str) -> int:
    matrix = [[] for _ in range(len(word1) + 1)]
    for num in range(len(word2) + 1):
        matrix[0].append(num)
    for num in range(1, len(word1) + 1):
        matrix[num].append(num)
    
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            leven = 0
            if word1[i - 1] != word2[j - 1]:
                leven = min(matrix[i - 1][j - 1], matrix[i - 1][j - 2], matrix[i][j - 2]) + 1
            matrix[i].append(leven)
            
    print(matrix)
    return leven
    
if __name__ == "__main__":
    print(levenshtein("house", "houes"))