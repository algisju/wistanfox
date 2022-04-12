from manimlib import *

class FirstScene(Scene):
    def construct(self):
        str = Text("Turlututu Chapeau Pointu ", font='Arial', stroke_widh=0)
        text = TexText("no integers (a,b,c) satisfy $a^n+b^n=c^n$, where $n > 2$")
        tex = Tex("x^n + y^n = z^n")
        group = VGroup(str, text, tex)
        group.arrange(DOWN)
        self.add(group)
        self.wait()
