import tabulate as tb

n = int(input('Enter No.Of Processes (Ideal CPU): '))
quanta = int(input('Enter Time Quantum : '))
brst_tyms, arrv_tyms = {}, {}
for i in range(1, n + 1):
    brst_tyms[f'P{i}'] = int(input(f'Enter Burst Time For Prc{i}   : '))
    arrv_tyms[f'P{i}'] = int(input(f'Enter Arrival Time For Prc{i} : '))
brst_tyms_temp = brst_tyms.copy()
arrv_tyms = {k: v for k, v in sorted(arrv_tyms.items(), key=lambda x: x[1])}
tym = arrv_tyms[list(arrv_tyms.keys())[0]]
completed = 0
ready_queue = []
cmplt_tyms = {}


def queueUpdation():
    for k, v in arrv_tyms.items():
        if v <= tym and brst_tyms[k] != 0 and k not in ready_queue:
            ready_queue.append(k)
            # print(tym, ready_queue)


while completed != n:
    queueUpdation()
    if len(ready_queue):
        proc = ready_queue[0]
        if brst_tyms[proc] > quanta:
            for i in range(quanta):
                brst_tyms[proc] -= 1
                tym += 1
                queueUpdation()
            ready_queue.pop(0)
        else:
            temp = brst_tyms[proc]
            for i in range(temp):
                brst_tyms[proc] -= 1
                tym += 1
                queueUpdation()
            ready_queue.pop(0)
            cmplt_tyms[proc] = tym
            completed += 1
            # print(proc)
            # print(completed)
    else:
        tym += 1
# print(arrv_tyms, brst_tyms, cmplt_tyms)

trn_around_tyms, wting_tyms = {}, {}
for i in range(1, n+1):
    trn_around_tyms[f'P{i}'] = cmplt_tyms[f'P{i}'] - arrv_tyms[f'P{i}']
    wting_tyms[f'P{i}'] = trn_around_tyms[f'P{i}'] - brst_tyms_temp[f'P{i}']

header = ['Process', 'Arrival Tym', 'Burst Tym', 'Cmpltn Tym',
          'Trn Around Tym', 'Waiting Tym']
helper = []
trn_around_time = 0
waiting_time = 0
for i in range(1, n + 1):
    temp = [f'P{i}', arrv_tyms[f'P{i}'], brst_tyms_temp[f'P{i}'], cmplt_tyms[f'P{i}'],
            trn_around_tyms[f'P{i}']]
    trn_around_time += trn_around_tyms[f'P{i}']
    temp.append(wting_tyms[f'P{i}'])
    waiting_time += wting_tyms[f'P{i}']
    helper.append(temp)
print(tb.tabulate(helper, headers=header, tablefmt='pretty'))
print('Total Turn Around Time :', trn_around_time)
print('Average Turn Around Time :', trn_around_time / n)
print('Total Waiting Time :', waiting_time)
print('Average Waiting Time :', waiting_time / n)
