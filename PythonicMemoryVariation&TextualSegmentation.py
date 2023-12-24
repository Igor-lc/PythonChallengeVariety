# ver without split
import sys

text = 'This Python course is unique ' * 1000
memory_without_split = sys.getsizeof(text.encode('utf-8'))

memory_without_split = sum(sys.getsizeof(word.encode('utf-8')) for word in text)
print(f"memory_without_split: {memory_without_split} bytes")  # вывод: 952000 bytes


# ver with split
import sys

text = 'This Python course is unique ' * 1000
memory_without_split = sys.getsizeof(text.encode('utf-8'))

memory_with_split = sum(sys.getsizeof((word + ' ').encode('utf-8')) for word in text.split())
print(f"memory_with_split: {memory_with_split} bytes")  # вывод: 160034 bytes


# how many objects
text = 'This Python course is unique ' * 1000
for word in text:
    print(f'{word}: id: {id(word)}, hash: {hash(word)}')
