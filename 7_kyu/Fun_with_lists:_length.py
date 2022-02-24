def length(head): 
    size = 0
    while(head != None):
        size += 1
        head = head.next
    return size