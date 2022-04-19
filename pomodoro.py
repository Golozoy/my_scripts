#!/usr/bin/python


import os
import time


def gen_notification(text: str='', title: str='Pomodoro')-> None:
    os.system(f'notify-send -t {5*60*1000} {title} {text}')

def main() -> None:
    counter = 0
    while True:
        try:
            gen_notification(text=f'{counter+1}_помидор_начался')
            time.sleep(25*60)
            counter += 1
            gen_notification(text=f'Перерыв_{"15" if counter % 4 == 0 else "5"}_минут')
            time.sleep(15*60 if counter % 4 == 0 else 5*60)
        except KeyboardInterrupt:
            gen_notification(text=f'Выполнено_{counter}_помидора')
            break

if __name__ == "__main__":
    main()
