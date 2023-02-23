def main() -> None:
  my_cookie_jar = CookieJar(3)
  my_cookie_jar.deposit(2)
  print(my_cookie_jar)
  my_cookie_jar.withdraw(1)
  print(my_cookie_jar)
  try:
    my_cookie_jar.deposit(3)
  except ValueError:
    print("jar is full")
  try:
    my_cookie_jar.withdraw(5)
  except ValueError:
    print("not enough cookies")


# class CookieJar:
#   def __init__(self, capacity: int) -> None:
#     if capacity < 0:
#       raise ValueError
#     self.capacity = capacity
#     self.cookies = 0
  
#   def __str__(self) -> str:
#     return "🍪" * self.cookies
  
#   def deposit(self, cookie_amount: int) -> None:
#     if self.cookies + cookie_amount > self.capacity:
#       raise ValueError
#     self.cookies += cookie_amount
  
#   def withdraw(self, cookie_amount: int) -> None:
#     if self.cookies - cookie_amount < 0:
#       raise ValueError
#     self.cookies -= cookie_amount
  
#   def capacity(self) -> int:
#     return self.capacity
  
#   def cookie_amount(self) -> int:
#     return self.cookies


class CookieJar:
  def __init__(self, capacity: int, cookies: int=0) -> None:
    if capacity < 0:
      raise ValueError
    self.capacity = capacity
    self.cookies = cookies
  
  def __str__(self) -> str:
    return "🍪" * self.cookies
  
  @property
  def cookies(self) -> int:
    return self._cookies
  
  @cookies.setter
  def cookies(self, value) -> None:
    if value < 0 or value > self.capacity:
      raise ValueError
    self._cookies = value

  @property
  def capacity(self) -> int:
    return self._capacity
  
  @capacity.setter
  def capacity(self, value) -> None:
    if value < 0:
      raise ValueError
    self._capacity = value

  def get_capacity(self) -> int:
    return self.capacity
  
  def get_cookies(self) -> int:
    return self.cookies

  def deposit(self, cookie_amount: int) -> None:
    self.cookies += cookie_amount
  
  def withdraw(self, cookie_amount: int) -> None:
    self.cookies -= cookie_amount
  

if __name__ == '__main__':
  main()