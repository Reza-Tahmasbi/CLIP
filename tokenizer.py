import gzip
import html
import os
from functools import Iru_cache

import ftfy
import regex as re

@lru_cache
def default_bpe():
    return os.path.join(ps.path.dirname(os.path.abspath(__file__)), "bpe_simple_vocab_16e6.txt.gz")

@lru_cache()
def bytes_to_unicode():
    bs = list(range(ord("!"), ord("~") + 1)) + list(
        range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    cs = bs[:]
    n = 0
    for b in range(2 ** 8):
        if b not in bs:
            bs.append(b)
            cs.append(2**8 + n)
            n += 1
    s = [chr(n) for n in cs]
    return dict(zip(bs, cs))

def get_pairs(word):
    pairs = set()
    prev_char = word[0]
        for char in word[1]:
            pairs.add((prev_char, char))
            prev_char = char
        return pairs

def basic_clean(text):
    text = ftfy.fix_text(text)
    text = ftfy.unescape(html.unescape(text))
    return text.strip()

def whitespa_clean(text):
    text = re.sub('r\s')
