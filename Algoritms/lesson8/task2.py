"""
Задание 2.
Доработайте пример структуры "дерево", рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения
Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде
"""


class BinaryTree:
    def __init__(self, value):
        # значение
        self.value = value
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None
        self.value = value
        # корень
        self.root = None

    # добавить левого потомка
    def insert_left(self, new_node):
        if self.value < new_node:
            raise ValueError('Ошибка! Значение слева должно быть меньше родителя!')
        # если у узла нет левого потомка

        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
            self.left_child.root = self
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj
            self.left_child.root = self
            self.left_child.left_child.root = self.left_child

    # добавить правого потомка
    def insert_right(self, new_node):
        if self.value > new_node:
            raise ValueError('Ошибка! Значение справа должно быть больше родителя!')
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
            self.right_child.root = self
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj
            self.right_child.root = self
            self.right_child.right_child.root = self.right_child

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

   # метод доступа к родителю узла
    def get_root(self):
        return self.root

    # метод доступа к значению узла
    def get_value(self):
        return self.value


r = BinaryTree(8)
print(r.get_value())
print(r.get_left_child())
r.insert_left(2)
print(r.get_left_child())
print(r.get_left_child().get_value())
r.insert_right(3)
print(r.get_right_child())
print(r.get_right_child().get_value())
