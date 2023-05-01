import monty_hall as mh


if __name__ == '__main__':

    hits_of_first = hits_of_second = 0
    total = 1000
    for _ in range(total):
        hit_of_first, hit_of_second = mh.monty_hall()
        if hit_of_first:
            hits_of_first +=1
        elif hit_of_second:
            hits_of_second+=1

    print(f"first: {hits_of_first}/{total} = {hits_of_first/total}")
    print(f"second: {hits_of_second}/{total} = {hits_of_second/total}")
