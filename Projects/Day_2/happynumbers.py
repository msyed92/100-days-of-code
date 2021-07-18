def happy_number(n):
    p = n
    count = 0
    while p != 1:
        num = 0
        for i in str(p):
            num += int(i) ** 2
        p = num
        count += 1
        if count > 8:
            ans = f"{n} is not a happy number."
            break
        else:
            ans = f"{n} is a happy number. It took {count} iteration(s) to get to 1."
    return ans   
