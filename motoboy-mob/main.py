from collections import namedtuple, deque

import pytest


class Motoboy(namedtuple("Motoboy", "name price exclusive")):
    def can_deliver(self, store):
        if not self.exclusive:
            return True

        if self.exclusive == store:
            return True

        return False


Pedido = namedtuple("Pedido", "store amount commission")


class Cycle:
    def __init__(self, motoboys):
        self.motoboys = motoboys
        self.queue = deque()

    def ensure_queue(self):
        if not self.queue:
            self.queue = deque(self.motoboys)

    def prioritize(self, store):
        priorities = set()

        for m in self.queue:
            if m.exclusive == store:
                priorities.add(m)

        for m in priorities:
            self.queue.remove(m)
            self.queue.appendleft(m)


    def next(self, store):
        self.ensure_queue()
        self.prioritize(store)

        while True:
            self.ensure_queue()

            m = self.queue.popleft()
            if m.can_deliver(store):
                return m


def earnings(m, p):
    return m.price + p.amount * p.commission


def delivery(motoboys, pedidos):
    l = []

    iter = Cycle(motoboys)

    for p in pedidos:
        m = iter.next(p.store)
        l.append((m.name, p.store, earnings(m, p)))

    return l


def test_1_motoboy_loja1_com_1_pedido():
    assert delivery([Motoboy("M1", 2, [])], [Pedido("L1", 50, 0.05)]) == [
        ("M1", "L1", 4.5),
    ]


def test_1_motoboy_loja1_com_3_pedidos():
    pedidos = [
        Pedido("L1", 50, 0.05),
        Pedido("L1", 50, 0.05),
        Pedido("L1", 50, 0.05),
    ]
    assert delivery([Motoboy("M1", 2, [])], pedidos) == [
        ("M1", "L1", 4.5),
        ("M1", "L1", 4.5),
        ("M1", "L1", 4.5),
    ]


def test_2_motoboys_loja1_com_3_pedidos():
    pedidos = [
        Pedido("L1", 50, 0.05),
        Pedido("L1", 50, 0.05),
        Pedido("L1", 50, 0.05),
    ]

    motoboys = [
        Motoboy("M1", 2, []),
        Motoboy("M2", 3, [])
    ]

    assert delivery(motoboys, pedidos) == [
        ("M1", "L1", 4.5),
        ("M2", "L1", 5.5),
        ("M1", "L1", 4.5),
    ]


def test_5_motoboys_3_lojas_com_10_pedidos():
    pedidos = [
        Pedido("L1", 50, 0.05),
        Pedido("L1", 50, 0.05),
        Pedido("L1", 50, 0.05),
        Pedido("L2", 50, 0.05),
        Pedido("L2", 50, 0.05),
        Pedido("L2", 50, 0.05),
        Pedido("L2", 50, 0.05),
        Pedido("L3", 50, 0.15),
        Pedido("L3", 50, 0.15),
        Pedido("L3", 100, 0.15),
    ]

    motoboys = [
        Motoboy("M1", 2, ""),
        Motoboy("M2", 2, ""),
        Motoboy("M3", 2, ""),
        Motoboy("M4", 2, "L1"),
        Motoboy("M5", 3, ""),
    ]

    assert delivery(motoboys, pedidos) == [
        ("M4", "L1", 4.5),
        ("M1", "L1", 4.5),
        ("M2", "L1", 4.5),
        ("M3", "L2", 4.5),
        ("M5", "L2", 5.5),
        ("M1", "L2", 4.5),
        ("M2", "L2", 4.5),
        ("M3", "L3", 9.5),
        ("M5", "L3", 10.5),
        ("M1", "L3", 17.0),
    ]


def test_cycle():
    motoboys = [
        Motoboy("M1", 2, ""),
        Motoboy("M2", 2, ""),
        Motoboy("M3", 2, ""),
        Motoboy("M4", 2, "L1"),
        Motoboy("M5", 3, ""),
    ]

    c = Cycle(motoboys)

    assert c.next("L1").name == "M4"
    assert c.next("L1").name == "M1"
    assert c.next("L1").name == "M2"
    assert c.next("L2").name == "M3"
    assert c.next("L2").name == "M5"
    assert c.next("L2").name == "M1"
    assert c.next("L2").name == "M2"
    assert c.next("L3").name == "M3"
    assert c.next("L3").name == "M5"
    assert c.next("L3").name == "M1"


def test_cycle_2():
    motoboys = [
        Motoboy("M1", 2, ""),
        Motoboy("M2", 2, ""),
        Motoboy("M3", 2, ""),
        Motoboy("M4", 2, "L1"),
        Motoboy("M5", 3, "L1"),
    ]

    c = Cycle(motoboys)

    assert c.next("L1").name == "M5"
    assert c.next("L1").name == "M4"
    assert c.next("L1").name == "M1"
    assert c.next("L2").name == "M2"
    assert c.next("L2").name == "M3"
    assert c.next("L2").name == "M1"
    assert c.next("L2").name == "M2"
    assert c.next("L3").name == "M3"
    assert c.next("L3").name == "M1"
    assert c.next("L3").name == "M2"

if __name__ == "__main__":
    pytest.main(["-s", __file__])
