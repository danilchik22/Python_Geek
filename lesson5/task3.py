# Задачу можно также решить через функцию генератора, но так код менее читабелен и придется каждый раз получать
# элемент по индексу, что очень затратно по времени:
# def generation (tutors, klasses):
#     index = 0
#     for tutor in tutors:
#         if index < len(klasses):
#             result = (tutor, klasses[index])
#             index += 1
#         else:
#             result = (tutor, None)
#         yield result
from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '8Б', '10А', '10Б', '9А', '4В', '3А'
]
# gen = generation(tutors, klasses)
if len(klasses) < len(tutors):
    gen = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses))
else:
    gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

