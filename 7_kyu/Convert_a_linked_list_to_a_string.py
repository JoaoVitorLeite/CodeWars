def stringify(node):
    if node == None:
        return 'None'
    aux = ''
    while node != None:
        aux += str(node.data)
        if node.next != None:
            aux += ' -> '
        else:
            aux += ' -> None'
        node = node.next
    return aux