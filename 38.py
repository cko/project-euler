
for i in range (9100, 9999):
    v_1 = i
    v_2 = i*2
    v_str = str(v_1) + str(v_2)
    if len(v_str) == 9:
        n_set = set(v_str)
        if len(n_set) == 9:
            print v_str
