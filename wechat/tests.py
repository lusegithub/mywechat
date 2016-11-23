import random

from django.test import TestCase

# Create your tests here.
from wechat.joke import getjoke

if __name__ == '__main__':
    jokes = getjoke()
    index = random.randint(0, len(jokes)-1)
    print(jokes[index])