import time
import os
from wonderwords import RandomWord


def print_hi(name):
    r = RandomWord()
    for i in range(30):
        word = r.word(include_parts_of_speech=["nouns"])
        print(word)
        os.system(f"start microsoft-edge:https://www.bing.com/news/search?q={word}"
                  f"+news&form=hdrsc6")
        time.sleep(5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
