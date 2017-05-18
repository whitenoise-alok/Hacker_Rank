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

        orig_list[a-1] += k
        if b!=len(orig_list):
            orig_list[b] -= k
        # print orig_list

    max = -1
    for o_ind, o in enumerate(orig_list):
        if o_ind != 0:
            orig_list[o_ind] +=orig_list[o_ind-1]
            if max< orig_list[o_ind]:
                max = orig_list[o_ind]
    print max