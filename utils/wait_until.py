from time import sleep
from datetime import datetime, timedelta
from typing import Callable, Union


def wait_until(condition: Callable[..., bool],
               timeout: Union[int, float] = 5,
               interval: Union[int, float] = 0.5):

    start = datetime.now()
    end = start + timedelta(seconds=timeout)
    while condition is False:
        sleep(interval)
        if datetime.now() > end:
            break
