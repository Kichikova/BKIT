from operator import itemgetter
import unittest


class Comp:
    def __init__(self, id, name, ram, ssd, proc, os_id):
        self.id = id
        self.name = name
        self.ram = ram
        self.ssd = ssd
        self.proc = proc
        self.os_id = os_id


class OS:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class OSComp:
    def __init__(self, comp_id, os_id):
        self.comp_id = comp_id
        self.os_id = os_id


Comps = [
    Comp(1, 'Acer Aspire', 4, 128, 'Celeron J4025', 1),
    Comp(2, 'Dexp Atlas', 8, 240, 'Pentium Gold G6405', 2),
    Comp(3, 'Apple iMac 24"', 16, 512,'M1', 3),
    Comp(11, 'HP Pavilion Gaming', 16, 512, 'Ryzon 5 5600G', 4),
    Comp(22, 'Asus Tuf Gaming', 16, 512, 'Core i5', 1),
    Comp(33, 'Apple iMac 27"', 8, 256,'Core i5', 3),
    Comp(25, 'Dexp Mars', 8, 512, 'Core i5', 2)
]


OSs = [
    OS(1, 'Windows'),
    OS(2, 'Linux'),
    OS(3, 'Mac OS'),
    OS(4, 'Ubuntu')
]

OSCs = [
    OSComp(1, 1),
    OSComp(2, 2),
    OSComp(3, 3),
    OSComp(11, 4),
    OSComp(22, 1),
    OSComp(33, 3),
    OSComp(25, 2),
    OSComp(1, 3)
]

one_to_many = [(c.name, c.ssd, o.name)
                   for o in OSs
                   for c in Comps
                   if c.os_id == o.id]


many_to_many_temp = [(o.name, osc.os_id, osc.comp_id)
                         for o in OSs
                         for osc in OSCs
                         if o.id == osc.os_id]

many_to_many = [(c.name, c.proc, os_name)
                    for os_name, os_id, comp_id in many_to_many_temp
                    for c in Comps if c.id == comp_id]

class TestRK(unittest.TestCase):

    def test_b1(self):
        self.res_11 = sorted(one_to_many, key=itemgetter(1))
        ssds = [x[1] for x in self.res_11]
        rightssds = [128, 240, 256, 512, 512, 512, 512]
        self.assertEqual(ssds, rightssds)

    def test_b2(self):
        a = list(set([i.name for i in OSs]))
        self.res_12 = sorted([(i, len([j for j in many_to_many_temp if i == j[0]])) for i in a], key=itemgetter(1))
        self.assertEqual(self.res_12[2][1], self.res_12[1][1])
        self.assertEqual(self.res_12[0][0], 'Ubuntu')
        self.assertEqual(self.res_12[3][0], 'Mac OS')

    def test_b3(self):
        self.b = [j for j in many_to_many if j[1][-2:] == 'i5']
        self.res_13 = {j[2]: [i[0] for i in self.b if i[2] == j[2]] for j in self.b}
        self.assertTrue(x for x in self.b if x[1] == 'Core i5')


def main():
    """Основная функция"""

    print('Задание Б1')
    res_11 = sorted(one_to_many, key=itemgetter(1))
    print(res_11)

    print('\nЗадание Б2')
    a = list(set([i.name for i in OSs]))
    res_12 = sorted([(i, len([j for j in many_to_many_temp if i == j[0]])) for i in a], key=itemgetter(1))
    print(res_12)

    print('\nЗадание Б3')
    b = [j for j in many_to_many if j[1][-2:] == 'i5']
    res_13 = {j[2]: [i[0] for i in b if i[2] == j[2]] for j in b}
    print(res_13)


if __name__ == '__main__':
    main()