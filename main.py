import time

while True:
    UI = input('equation:')

    def num(x):
        return float(x)

    operation = UI.split(' ')[0]

    strnum = UI.split(' ')[1].split(',')
    nums = list(map(num,strnum))

    output = 0

    lprt = True

    if operation == 'sum' or operation == 'add':
        lprt = True
        for n in nums:
            output += n

    elif operation == 'subract':
        lprt = True
        for n in nums :
            output -= n

    elif operation == 'multiply' or operation == 'product':
        lprt = True
        output = 1
        for n in nums :
            output *= n

    elif operation == 'divide' or operation == 'over':
        output = nums[0]**2
        lprt = True
        for n in nums :
            output /= n

    elif operation == 'count':
        lprt = False
        r = range(int(nums[0]),int(nums[1]+1))

        for n in r:
            time.sleep(1)
            print(n)
            
    elif operation == 'square':
        lprt = True
        output = list(map(lambda x:x**2,nums))

    elif operation == 'sqrt':
        lprt = True
        output = list(map(lambda x:x**0.5,nums))

    if lprt:
        print(output)