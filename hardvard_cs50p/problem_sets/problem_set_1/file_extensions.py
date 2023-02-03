def main() -> None:
  user_input = input("file name: ")
  print(file_extension(user_input))

def file_extension(file_name: str) -> str:
  file_name = file_name.strip().lower()
  extension = file_name.split(".")[1]
  match extension:
    case "gif":
      return "image/gif"
    case "jpg":
      return "image/jpeg"
    case "jpeg":
      return "image/jpeg"
    case "png":
      return "image/png"
    case "pdf":
      return "application/pdf"
    case "txt":
      return "text/plain"
    case "zip":
      return "application/zip"
    case _:
      return "application/octet-stream"

if __name__ == '__main__':
  main()