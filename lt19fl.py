K = [130, 106, 73, 60, 128, 7, 237, 17, 156, 2, 202, 218, 38, 65, 48, 202, 39, 252, 203]
C = [238, 30, 120, 5, 223, 97, 129, 120, 236, 114, 163, 133, 66, 32, 111, 172, 75, 147, 187]
FL = "".join([chr(k^c) for k, c in zip(K, C)])
EXP = "".join(
    [chr(i) for i in 
        [105, 99, 104, 32, 108, 97, 115, 115, 32, 100, 97, 115, 32, 106, 101, 116, 122, 116, 32, 115, 111]])
