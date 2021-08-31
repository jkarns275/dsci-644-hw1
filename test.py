import pytest
import random
from linked_list import LinkedList, Node

def we(ll):
    return go(ll.list)

def go(n):
    return 1+(go(n.tail) if n.tail else 0)

def test_get_length():
    ll = LinkedList()
    assert ll.get_length() == 0
    for i in range(1, 100):
        ll = mklist(i)
        assert ll.get_length() == i

def mklist(length):
    node = None

    for i in range(length):
        node = Node(random.random(), node)
    
    ll = LinkedList()
    ll.list = node
    return ll

def test_head():
    with pytest.raises(Exception):
        ll = LinkedList()
        head = ll.head()

    ll = mklist(100)
    head = ll.head()
    
    assert head == 16

def test_get():
    with pytest.raises(Exception):
        ll = LinkedList()
        first = ll.get(0)

    ll = mklist(100)
    first = ll.get(0)
    assert first == 16

def test_set():
    with pytest.raises(Exception):
        ll = LinkedList()
        ll.set(0, 10)
    with pytest.raises(Exception):
        ll = LinkedList()
        ll.set(4, 10)
    ll = mklist(100)
    ll.set(2, 20)
    assert ll.list.tail.tail == 20

    with pytest.raises(Exception):
        ll = mklist(2)
        ll.set(2, 10)

def test_append():
    ll = LinkedList()
    ll.append(0)
    assert we(ll)==1

    assert ll.list.element == 0

    ll = mklist(100)
    ll.append(15)
    assert we(ll) == 101
    li = ll.list
    while li.tail:
        li = li.tail
    assert li.element == 15

def test_remove():
    with pytest.raises(Exception):
        ll = LinkedList()
        ll.remove(0)
    with pytest.raises(Exception):
        ll = mklist(10)
        ll.remove(10)

    ll = mklist(10)
    for i in reversed(range(10)):
        ll.remove(i)
    assert ll.list == None
