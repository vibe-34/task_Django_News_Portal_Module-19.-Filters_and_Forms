import re

from django import template
from django.utils.safestring import mark_safe


register = template.Library()

# слова попадающие под цензуру
BAD_WORDS = ['волейбол', 'баскетбол', 'компания', 'успешный', 'добавлена', ]


@register.filter()  # декоратор, регистрирует функцию как фильтр (для применения его в шаблонах)
def censor(text):
    """Ищет слова в тексте совпадающие со списком BAD_WORDS
    заменяет их на символ * (кроме первого символа в слове)

    Компилируем слово из списка BAD_WORDS в его границах (для работы с полным совпадением), без учета регистра.
    Слова из списка BAD_WORDS маскируем символами *.
    При совпадении слов в тексте со словами из списка BAD_WORDS подменяем их
    """

    for el in BAD_WORDS:  # перебор списка слов и замена на *, при совпадении
        pattern = re.compile(r'\b{}\b'.format(el), re.IGNORECASE)
        censored_word = el[0] + '*' * (len(el) - 1)
        text = re.sub(pattern, censored_word, text)
    return text
