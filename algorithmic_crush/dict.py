

if __name__ == '__main__':
    N_M = raw_input().strip()
    N = int(N_M.split()[0].strip())
    M = int(N_M.split()[1].strip())
    orig_dict = {0:set(range(N))}

    for i in xrange(M):
        a_b_k = raw_input().strip()
        a = int(a_b_k.split()[0].strip())
        b = int(a_b_k.split()[1].strip())
        k = int(a_b_k.split()[2].strip())

        temp_set = set(range(a-1, b))
        count_set = set()
        for val,i_set in orig_dict.iteritems():
            if count_set == temp_set: break

            temp_common_set = temp_set.intersection(i_set)
            count_set = count_set.union(temp_common_set)

            if temp_common_set:
                if val+k in orig_dict:
                    orig_dict[val+k] = orig_dict[val+k].union(temp_common_set)
                else:
                    orig_dict[val + k] = temp_common_set

                orig_dict[val] = i_set - temp_set.intersection(i_set)

    max_value = max(orig_dict.keys())
    print max_value