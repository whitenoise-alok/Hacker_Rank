def add(list1, list2):
    l = []
    for l1, l2 in zip(list1, list2):
        l.append(l1+l2)
    return l
if __name__ == '__main__':
    N_M = raw_input().strip()
    N = int(N_M.split()[0].strip())
    M = int(N_M.split()[1].strip())
    orig_list = [0]*N

    for i in xrange(M):
        a_b_k = raw_input().strip()
        a = int(a_b_k.split()[0].strip())
        b = int(a_b_k.split()[1].strip())
        k = int(a_b_k.split()[2].strip())

        orig_list[(a-1):b] =add(orig_list[(a-1):b], [k]*(b-a+1) )


    print max(orig_list)