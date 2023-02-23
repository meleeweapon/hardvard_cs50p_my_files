import re

def main() -> None:
  test_cases = [
    ('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>', 'https://youtu.be/xvFZjo5PgG0'),
    ('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', 'https://youtu.be/xvFZjo5PgG0'),
    ('<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>', None),
  ]
  for case, expected_result in test_cases:
    if parse(case) != expected_result:
      print("failed", parse(case))
    else:
      print("success")


def get_embed_link(html: str) -> str:
  if type(html) != str:
    return None

  if match := re.search(r'<iframe.+src="(.*?)".*>.*</iframe>', html):
    return match.group(1)
  return None

def get_last_part_of_embed_link(link: str) -> str:
  if type(link) != str:
    return None

  if match := re.search(r'youtube\.com/embed/(.*)/?', link):
    return match.group(1)
  else:
    return None

def shorten_youtube_embed_link(last_part: str) -> str:
  if last_part == None:
    return None
  else:
    return f'https://youtu.be/{last_part}'

def parse(html: str) -> str:
  return shorten_youtube_embed_link(get_last_part_of_embed_link(get_embed_link(html)))

if __name__ == '__main__':
  main()