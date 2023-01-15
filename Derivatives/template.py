from manim import *

def template(title):
    logo = Text("l-earn.academy", font="Arial", font_size=12, color=WHITE).to_edge(DR) 
    title = Tex(title, font_size=44, color=BLUE).to_edge(UL)
    g = Group(title,logo)
    return g

def transform(self,from_obj, to_obj,timeout):
        self.play(ReplacementTransform(from_obj,to_obj))
        self.wait(timeout)

def render_text_group(textItems):
    text = MathTex(*textItems, color=WHITE, font_size=90)
    group = Group(*text).arrange_in_grid(buff=2)
    return group

def greetings():
    greetings1 = Text("I hope you enjoyed it! ", font_size=22)
    greetings2 = Text("If you've liked this video give a thumbs up and subscribe to my channel! ", font_size=22)
    greetings3 = Text("Leave your suggestions in the comments.", font_size=22)
    greetings4 = Text("This video was realized using manim:  https://manim.community", font_size=15)
    greetings5 = Text("My GitHub Repo: https://github.com/HydraSevenEleven/l-earn.academy.git", font_size=15)
    group = Group(greetings1, greetings2, greetings3, greetings4, greetings5).arrange(DOWN, buff=.8) #.set_height(config.frame_height-LARGE_BUFF)
    return group