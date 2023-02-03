def main():
  name = input("what's your name? ")
  # hello(name)
  print(hello(name))

# def hello(name):
#   print("hello", name)

def hello(name=""):
  return "hello " + name

if __name__ == "__main__":
  main()