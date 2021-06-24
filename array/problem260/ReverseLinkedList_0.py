def reverseList(head):
    index = 0
    while index < len(head) / 2:
        tail = (len(head)) - 1 - index
        head[index], head[tail] = head[tail], head[index]
        index = index + 1
    return head


if __name__ == '__main__':
    print(reverseList(head=[1, 2, 3, 4, 5]))
