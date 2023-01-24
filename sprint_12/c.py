# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, idx):
    if idx == 0:
        return node.next_item
    counter = 0
    current_node = node
    while counter != idx:
        previous_node = current_node
        current_node = current_node.next_item
        counter += 1
    previous_node.next_item = current_node.next_item
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 2)
    assert new_head is node0
    assert new_head.next_item is node1
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3



test()
