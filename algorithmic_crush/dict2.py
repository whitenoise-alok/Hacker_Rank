if __name__ == '__main__':
    N_M = raw_input().strip()
    N = int(N_M.split()[0].strip())
    M = int(N_M.split()[1].strip())
    # orig_dict = { x:0 for x in xrange(N)}
    orig_dict = {}
    for i in xrange(M):
        a_b_k = raw_input().strip()
        a = int(a_b_k.split()[0].strip())
        b = int(a_b_k.split()[1].strip())
        k = int(a_b_k.split()[2].strip())

        for j in range(a-1,b):
            if j in orig_dict:
                orig_dict[j] += k
            else:
                orig_dict[j] = 0

    print max(orig_dict.values())