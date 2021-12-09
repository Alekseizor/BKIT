import unittest
import sys, os

sys.path.append(os.getcwd())
from music import *


class Test_task_1(unittest.TestCase):
    def test_First_letter(self):
        one_to_many = [(m.surname, m.salary, o.name) for o in orchestras for m in musicians if m.orchestra_id == o.id]
        self.assertEqual(task_1(one_to_many), [('Абрамов', 'Российский национальный оркестр'),
                                               ('Ахтамбаев', 'Лондонский симфонический оркестр')])


class Test_task_2(unittest.TestCase):
    def test_min_many_everyone_department(self):
        one_to_many = [(m.surname, m.salary, o.name) for o in orchestras for m in musicians if m.orchestra_id == o.id]
        self.assertEqual(task_2(one_to_many),
                         [('Российский национальный оркестр', 250000), ('Лондонский симфонический оркестр', 315000),
                          ('Королевский филармонический оркестр', 343000)])


class Test_task_3(unittest.TestCase):
    def test_worker_many_departments(self):
        many_to_many_temp = [(o.name, r.orchestra_id, r.musician_id) for o in orchestras for r in musorc if
                             o.id == r.orchestra_id]
        many_to_many = [(m.surname, o_name) for o_name, orchestra_id, musician_id in many_to_many_temp for m in
                        musicians if
                        m.id == musician_id]
        self.assertEqual(task_3(many_to_many),
                         [('Абрамов', ['Российский национальный оркестр', 'Российский национальный оркестр(другой)']), (
                             'Ахтамбаев',
                             ['Лондонский симфонический оркестр', 'Лондонский симфонический оркестр(другой)']),
                          ('Зорькин',
                           ['Королевский филармонический оркестр', 'Королевский филармонический оркестр(другая)']), (
                              'Некрасов',
                              ['Королевский филармонический оркестр', 'Королевский филармонический оркестр(другая)']), (
                              'Прошкина',
                              ['Королевский филармонический оркестр', 'Королевский филармонический оркестр(другая)'])])
