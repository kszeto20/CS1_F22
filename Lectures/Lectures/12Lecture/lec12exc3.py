def find_min(LL):
    minu = LL[0][0]
    for i in range(len(LL)):
        for j in range(len(LL[i])):
            if LL[i][j] < minu:
                minu = LL[i][j]
    
    return minu

if __name__ == "__main__":
    v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
    print("Min of list v: {}".format(find_min(v)) )
    u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ], \
              [ 'rain', 'snow', 'sun' ] ]
    print("Min of list u: {}".format(find_min(u)) )