if __name__ == '__main__':
    N_M = raw_input().strip()
    N = int(N_M.split()[0].strip())
    M = int(N_M.split()[1].strip())
    # orig_dict = { x:0 for x in xrange(N)}
    op_list = []

    for i in xrange(M):
        a_b_k = raw_input().strip()
        a = int(a_b_k.split()[0].strip())
        b = int(a_b_k.split()[1].strip())
        k = int(a_b_k.split()[2].strip())

        op_list.append({
            's':a,
            'e':b,
            'v':k
        })
    op_list = sorted(op_list, key=lambda x:x['s'])
    max = -1
    for i in xrange(N):
        temp_max = 0
        for op in op_list:
            if i < op['s']:
                break
            if i >= op['s'] and i <= op['e']:
                temp_max +=op['v']
        if temp_max>max:
            max = temp_max
    print max




