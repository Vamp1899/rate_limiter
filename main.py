import threading
import time
from functools import wraps
def rate_limiter(max_calls, period):
  def decorator(func):
    last_rest = time.time()
    count = 0
    lock = threading.Lock()
    @wraps(func)
    def wrapper(*args, **kwargs):
      nonlocal last_rest, count
      curr = time.time()
      with lock:
        if curr-last_rest>period:
          count = 0
          last_rest = curr
        if max_calls>count:
          count+=1
          return func(*args,**kwargs)
        else:
          raise ValueError("Terminated Limit reached")
    return wrapper
  return decorator

@rate_limiter(max_calls = 3, period = 15)
def func(x,y):
  print(x+y)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  while True:
    try:
      t = threading.Thread(target = func, args=(3,5))
      t.start()
    except:
      print("EXITED Program")
      break


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
