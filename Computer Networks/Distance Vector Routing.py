class Node:
    def __init__(self):
        self.Dist = [0 for _ in range(10)]
        self.From = [0 for _ in range(10)]


def distanceVectorRouting():
    count = 0
    rt = [Node() for _ in range(10)]
    nodes = int(input('Enter the number of nodes :'))
    costmat = [[0 for _ in range(nodes)] for _ in range(nodes)]
    print(costmat)
    l = list(map(int, input('Enter cost matrix :').split()))
    lst = [l[i:i + nodes] for i in range(0, len(l), nodes)]
    print(lst)
    for i in range(nodes):
        for j in range(nodes):
            costmat[i][j] = lst[i][j]
            costmat[i][i] = 0
            rt[i].Dist[j] = costmat[i][j]
            rt[i].From[j] = j

    while True:
        for i in range(nodes):
            for j in range(nodes):
                for k in range(nodes):
                    if rt[i].Dist[j] > costmat[i][k] + rt[k].Dist[j]:
                        rt[i].Dist[j] = rt[i].Dist[k] + rt[k].Dist[j]
                        rt[i].From[j] = k
                        count += 1
        if count != 0:
            break

    for i in range(nodes):
        print(f'For router {i + 1} :')
        for j in range(nodes):
            print(f'   Node {j + 1} via {rt[i].From[j] + 1} Distance {rt[i].Dist[j]}')


if __name__ == '__main__':
    # INPUT : 0 2 7 2 0 1 7 1 0
    distanceVectorRouting()
