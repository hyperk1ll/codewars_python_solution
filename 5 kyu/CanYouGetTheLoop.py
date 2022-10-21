# Can you get the loop ?


def loop_size(node):
    a = []

    while node not in a:
        a.append(node)
        node = node.next

    return len(a) - a.index(node)