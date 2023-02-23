from turtle import *
import colorsys

def main() -> None:
  speed(150)
  bgcolor("black")
  hue = 0
  for i in range(750):
    hue += 0.0018
    color(colorsys.hsv_to_rgb(hue, 1, 1))
    circle(i)
    lt(5)
  done()

  # bgcolor("black")
  # tracer(100)
  # pensize(1)
  # h = 0.5
  # for i in range(750):
  #   h += 0.0008
  #   c = colorsys.hsv_to_rgb(h, 1, 1)
  #   fillcolor(c)
  #   begin_fill()
  #   fd(i)
  #   lt(100)
  #   circle(30)
  #   end_fill()
  #   rt(109)
  #   fd(i)
  #   rt(109)

    # for y in range(2):
    #   fd(i*y)
    #   rt(50)
    #   end_fill()
  done()


  # color('red', 'yellow')
  # begin_fill()
  # fwd = 0
  # for _ in range(200):
  #   fwd += 2
  #   forward(fwd)
  #   left(10)

  #   # while True:
  #   #     forward(150)
  #   #     left(60)
  #   #     if abs(pos()) < 1:
  #   #         break
  #   # left(17)
  # end_fill()
  # done()


if __name__ == '__main__':
  main()