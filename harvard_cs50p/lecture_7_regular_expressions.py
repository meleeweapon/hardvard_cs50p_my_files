import re

def main() -> None:
  # validate()
  # format()
  twitter()

def validate():
  email = input("enter your email: ").strip()

  # if "@" in email:
  #   print("valid")
  # else:
  #   print("invalid")

  # if "@" in email and "." in email:
  #   print("valid")
  # else:
  #   print("invalid")

  # username, domain = email.split("@")
  # if username and "." in domain:
  #   print("valid")
  # else:
  #   print("invalid")

  # username, domain = email.split("@")
  # if username and domain.endswith(".com"):
  #   print("valid")
  # else:
  #   print("invalid")

  # if re.search("@", email):
  #   print("valid")
  # else:
  #   print("invalid")

  # if re.search(".+@.+", email):
  #   print("valid")
  # else:
  #   print("invalid")

  # # use raw string expression (r"") so python doesn't
  # # interpret the escape character, instead the regular
  # # expression should interpret backslash dot cuz
  # # instead of any character only dot is wanted
  # if re.search(r".+@.+\.edu", email):
  #   print("valid")
  # else:
  #   print("invalid")

  # if re.search(r"^.+@.+\.edu$", email):
  #   print("valid")
  # else:
  #   print("invalid")

  # if re.search(r"^[^@]+@[^@]+\.edu$", email):
  #   print("valid")
  # else:
  #   print("invalid")

  # if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
  #   print("valid")
  # else:
  #   print("invalid")

  # if re.search(r"^\w+@\w+\.edu$", email):
  #   print("valid")
  # else:
  #   print("invalid")

  if re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
    print("valid")
  else:
    print("invalid")

  # alternatively use a library


def format():
  name = input("what's your name: ").strip()

  # if "," in name:
  #   last_name, first_name = name.split(",")
  #   name = f"{first_name.strip()} {last_name.strip()}"
  # print(f"hello {name}")

  # # paranthesis is used for capturing
  # matches = re.search(r"^(.+), (.+)$", name)
  # if matches:
  #   last_name, first_name = matches.groups()
  #   name = f"{first_name.strip()} {last_name.strip()}"
  # print(f"hello {name}")

  # matches = re.search(r"^(.+), (.+)$", name)
  # if matches:
  #   last_name =  matches.group(1)
  #   first_name = matches.group(2)
  #   name = f"{first_name.strip()} {last_name.strip()}"
  # print(f"hello {name}")

  # matches = re.search(r"^(.+), ?(.+)$", name)
  # if matches:
  #   name = f"{matches.group(1).strip()} {matches.group(2).strip()}"
  # print(f"hello {name}")

  # matches = re.search(r"^(.+), *(.+)$", name)
  # if matches:
  #   name = f"{matches.group(1)} {matches.group(2)}"
  # print(f"hello {name}")

  if matches := re.search(r"^(.+), *(.+)$", name):
    name = f"{matches.group(1)} {matches.group(2)}"
  print(f"hello {name}")

# https://twitter.com/davidjmalan
def twitter():
  url = input("URL: ").strip()
  print("url is: " + url)

  # username = url.replace("https://twitter.com/", "")

  # username = url.removeprefix("https://twitter.com/")

  # username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

  # username = "not found"
  # if matches := re.search(r"^.*\.com/(.*)/?$", url):
  #   username = matches.group(1)

  username = "not found"
  # if matches := re.search(r"^.*(?:https?://)?(?:www\.)?twitter\.com/(.*)/?.*$", url, re.IGNORECASE):
  if matches := re.search(r"^.*(?:https?://)?(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)", url, re.IGNORECASE):
    username = matches.group(1)

  print("username is: " + username)


if __name__ == '__main__':
  main()