# storing prev value as greedy method
def main(pattern):
    matched = 0
    # print(pattern)
    prev = []
    deleted_last = ''
    deleted = ''
    for i in pattern: #O(n)
        # print(f'{prev}  and {i} and deleted_last={deleted_last} and matched={matched}')
        if not prev:
            prev.append(i)
        elif prev[-1] == i:
            prev.append(i)
        elif prev[-1] != i:
            # if deleted_last == 'LR' :
            #     matched=matched+1
            deleted = i
            prev = prev[:len(prev) - 1]
        if not prev:
            matched = matched + 1
            deleted_last = deleted
    return matched


if __name__ == '__main__':
    with open(file='input.txt') as f , open(file='output.txt',mode='w') as out:
        for line in f.readlines():
            out.writelines(str(main(line.strip()))+'\n')
