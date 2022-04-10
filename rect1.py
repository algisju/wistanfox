from manimlib import *
class ArrangeInGridTest(Scene):
    def construct(self):
        y = 20
        x = 30
        colors = [RED, GREEN, BLUE]
        dots = VGroup(*[Dot() for x in range(y * x)])
        dots.arrange_in_grid(y, x, buff=SMALL_BUFF)
        for i in range(0, y*x):
            dots[i].set_color(colors[i % 3])

        self.add(dots)
        self.wait()
