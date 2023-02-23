import sys
import os
from PIL import Image
from PIL import ImageOps

def main() -> None:
  try:
    shirt_overlay_image = Image.open("shirt.png",)
  except FileNotFoundError:
    sys.exit("shirt overlay doesn't exist")

  argvs = sys.argv
  if len(argvs) < 3:
    sys.exit("too few arguments")
  elif len(argvs) > 3:
    sys.exit("too many arguments")
  
  target_file_path = argvs[1]
  destination_file_path = argvs[2]

  target_file_extension = os.path.splitext(target_file_path)[-1] # target_file_path.split(".")[-1]
  match target_file_extension:
    case ".png" | ".jpg" | ".jpeg":
      pass
    case _:
      sys.exit("path must end with .png, .jpg or .jpeg")
  if target_file_extension != os.path.splitext(destination_file_path)[-1]:
    sys.exit("target path extension and destination path extension must be same")

  try:
    target_image = Image.open(target_file_path,)
  except FileNotFoundError:
    sys.exit("file doesn't exist")
  
  resized_target_image = ImageOps.fit(target_image, shirt_overlay_image.size)
  resized_target_image.paste(shirt_overlay_image, shirt_overlay_image)
  resized_target_image.save(destination_file_path)


if __name__ == '__main__':
  main()