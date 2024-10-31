import os
import keyboard
import sys
import time
import asyncio
from rich.console import Console
console = Console()
def options():
    console.print('\nChoose your time unit', style="bold white")
    console.print('\n1. Hours', style="green")
    console.print('\n2. Minutes', style="light_green")
    console.print('\n3. Seconds', style="yellow")
    while True:
        if keyboard.is_pressed('1'):
            a = 60 * 60
            method = 'hours'
            console.print(f'Chose {method}', style="bold blue")
            break
        elif keyboard.is_pressed('2'):
            a = 60
            method = 'minutes'
            console.print(f'Chose {method}', style="bold blue")
            break
        elif keyboard.is_pressed('3'):
            a = 1
            method = 'seconds'
            console.print(f'Chose {method}', style="bold blue")
            break
    return a, method
def request(method):
    time_value = int(input("Shutdown in?:"))
    return time_value
def counter(a, method, time_value):
    seconds_to_shutdown = time_value * a
    os.system(f"shutdown -s -t {seconds_to_shutdown}")
    print(f"\nSystem will be shutdown in: {time_value} {method}")
def await_abort_request():
    console.print('\nAbort shutdown? Y/N', style="bold red")
    while True:
        if keyboard.is_pressed('Y'):
            console.print('\nShutdown aborted', style="bold white")
            time.sleep(2)
            os.system(f"shutdown -a")
            break
        if keyboard.is_pressed('N'):
            time.sleep(2)
            sys.exit()
a, method = options()
time.sleep(1)
time_value = request(method)
counter(a, method, time_value)
await_abort_request()

    

    