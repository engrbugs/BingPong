import time
import os
from wonderwords import RandomWord


def generate():
    r = RandomWord()
    for i in range(40):
        word = r.word(include_parts_of_speech=["nouns"])
        print(word)
        os.system(f"start microsoft-edge:https://www.bing.com/news/search?q={word}"
                  f"+news&form=hdrsc6")
        time.sleep(3)


if __name__ == '__main__':
    generate()
