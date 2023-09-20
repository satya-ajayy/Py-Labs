class Process:
    def __init__(self, p_id, a, b):
        self.p_id = p_id
        self.ALLOCATED = a
        self.MAX_NEED = b
        self.NEED = None
        self.finished = False


class BankersAlgorithm:
    def __init__(self, processes, a, n):
        self.P = processes
        self.n = n
        self.completed = 0
        self.AVAILABLE = a
        self.safe_path = []

    def getNeed(self):
        for proc in self.P:
            zipper = zip(proc.MAX_NEED, proc.ALLOCATED)
            proc.NEED = [i - j for i, j in zipper]

    def getSafePath(self):
        print('Safe Sequence : ', end='')
        print('->'.join(self.safe_path))

    def findProcess(self):
        for proc in self.P:
            zipper = zip(proc.NEED, self.AVAILABLE)
            boolean = all([i <= j for i, j in zipper])
            if boolean and proc.finished is False:
                proc.finished = True
                self.completed += 1
                self.safe_path.append(f'P{proc.p_id}')
                zipper = zip(self.AVAILABLE, proc.ALLOCATED)
                self.AVAILABLE = [i + j for i, j in zipper]
                return proc

    def solveDeadLock(self):
        self.getNeed()
        while self.completed != self.n:
            if not self.findProcess():
                print('Danger!! Dead Lock Detected')
                break
        else:
            self.getSafePath()


if __name__ == '__main__':
    p0 = Process(0, [0, 1, 0], [7, 5, 3])
    p1 = Process(1, [2, 0, 0], [3, 2, 2])
    p2 = Process(2, [3, 0, 2], [9, 0, 2])
    p3 = Process(3, [2, 1, 1], [2, 2, 2])
    p4 = Process(4, [0, 0, 2], [4, 3, 3])
    prcs = [p0, p1, p2, p3, p4]
    solver = BankersAlgorithm(prcs, [3, 3, 2], 5)
    solver.solveDeadLock()
