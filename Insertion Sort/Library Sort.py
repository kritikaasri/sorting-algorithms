def isempty(e):
    return e == -1;


def prepareLibrarySort(epsilon, n, S):
    sLen = (1 + epsilon) * n
    for i in range(sLen):
        S[i] = -1
    return (sLen, S)


def searchFree(e, sortd, last):
    first, middle = 0, 0
    while last >= 0 and isempty(sortd[last]):
        last = last - 1
    while first <= last and isempty(sortd[first]):
        first = first + 1
    while first <= last:
        middle = (first + last) // 2
        if isempty(sortd[middle]):
            tmp = middle + 1
            while tmp < last and isempty(sortd[tmp]):
                tmp += 1
            if sortd[tmp] > e:
                tmp = middle - 1
                while middle > first and isempty(sortd[middle]):
                    middle = middle - 1
                if sortd[middle] < e:
                    return middle
                last = middle - 1
            else:
                first = tmp + 1
        elif sortd[middle] < e:
            first = middle + 1
        else:
            last = middle - 1
    if last >= 0 and isempty(sortd[last]):
        last = last - 1
    return last


def libSort(A, N, S, EPSILON):
    if N == 0:
        return
    goal = 1
    pos = 1

    S[0] = A[0]
    sLen = max((1 + EPSILON), goal + 1)

    while pos < n:

        for j in range(goal):
            insPos = searchFree(A[pos], S, sLen - 1)
            insPos = insPos + 1
            if not isempty(S[insPos]):
                nextFree = insPos + 1
                while not isempty(S[nextFree]):
                    nextfree = nextFree + 1
                if nextFree >= sLen:
                    insPos = insPos - 1
                    if not isempty(S[insPos]):
                        nextFree = insPos - 1
                        while not isempty(S[nextFree]):
                            nextFree = nextFree - 1
                        while nextFree < insPos:
                            S[nextFree] = S[nextFree + 1]
                            nextFree = nextFree + 1
                else:
                    while nextFree > insPos:
                        S[nextFree] = S[nextFree - 1]
                        nextFree = nextFree - 1
            elif insPos >= sLen:
                insPos -= 1
                nextFree = insPos - 1
                while not isempty(S[nextFree]):
                    nextFree = nextFree - 1
                while nextFree < insPos:
                    S[nextFree] = S[nextFree + 1]
                    nextFree = nextFree + 1
            S[insPos] = A[pos]
            pos = pos + 1

            if pos >= N:
                return
        j = sLen - 1
        k = min(goal * (2 + 2 * EPSILON), (1 + EPSILON) * N) - 1
        step = (k + 1) // (j + 1)
        while j >= 0:
            S[k] = S[j]
            S[j] = -1
            j = j - 1
            k -= step
        sLen = min(goal * (2 + 2 * EPSILON), N * (1 + EPSILON))
        goal <<= 1


def librarySort(A, n):
    epsilon = 2
    S = [-1] * 20000
    sLen, S = prepareLibrarySort(epsilon, n, S)
    libSort(A, n, S, epsilon)
    i = 0
    j = 0
    while i < sLen and j < n:
        if not isempty(S[i]):
            A[j] = S[i]
            j = j + 1
        i = i + 1
    return A


A = [4, 1, 2, 3, 1, 4, 9, 4]
print(A)
n = len(A)
print(librarySort(A, n))
