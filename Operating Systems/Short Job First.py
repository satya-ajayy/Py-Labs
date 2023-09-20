import tabulate as tb


class Process:
    def __init__(self, p_id, a, b):
        self.p_id, self.at, self.bt = p_id, a, b
        self.ct, self.tt, self.wt = 0, 0, 0
        self.finished = False


class SJF:
    def __init__(self, processes, n):
        self.P = processes
        self.completed = 0
        self.cur_tym = 0
        self.n = n

    def findProcess(self):
        p = list(filter(lambda x: (x.at <= self.cur_tym and x.finished is False), self.P))
        p.sort(key=lambda x: x.bt)
        if len(p) == 0:
            return 0, False
        return p[0], True

    def schedule(self):
        while self.completed != self.n:
            p, flag = self.findProcess()
            if flag:
                start_tym = self.cur_tym
                p.ct = start_tym + p.bt
                p.tt = p.ct - p.at
                p.wt = p.tt - p.bt
                p.finished = True
                self.completed += 1
                self.cur_tym = p.ct
            else:
                self.cur_tym += 1

    def Show(self):
        header = ['Process', 'Arrival Tym', 'Burst Tym',
                  'Cmpltn Tym', 'Trn Around Tym', 'Waiting Tym']
        helper = []
        trn_around_time = 0
        waiting_time = 0
        for p in self.P:
            temp = [p.p_id, p.at, p.bt, p.ct, p.tt, p.wt]
            trn_around_time += p.tt
            waiting_time += p.wt
            helper.append(temp)
        print(tb.tabulate(helper, headers=header, tablefmt='pretty'))
        print('Total Turn Around Time :', trn_around_time)
        print('Average Turn Around Time :', trn_around_time / self.n)
        print('Total Waiting Time :', waiting_time)
        print('Average Waiting Time :', waiting_time / self.n)


if __name__ == '__main__':
    num = int(input('Enter No.Of Processes (Ideal CPU): '))
    s = 'Enter Burst and Arrival Times of P{} : '
    prcs = []
    for i in range(1, num + 1):
        bt, at = map(int, input(s.format(i)).split())
        prcs.append(Process(i, at, bt))
    scheduler = SJF(prcs, num)
    scheduler.findProcess()
    scheduler.schedule()
    scheduler.Show()
