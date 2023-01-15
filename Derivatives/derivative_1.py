from manim import *
from template import *

config.background_color = BLUE_E


class Derivative_1(Scene):
    def construct(self):
        #-------------------------------------------- FIRST SLIDE ---------------------------------------------#
        g = template(r"How do you solve this?")
        self.add(g)

        text1 = MathTex("f(x)=ax^n", color=WHITE, font_size=90)
        text2 = MathTex("\\frac{d}{dx} f(x)=?", color=WHITE, font_size=90)
        g2 = Group(text1,text2).arrange_in_grid(buff=2)
        
        self.add(g2)

        self.wait(5)

        #--------------------------------------------- SECOND SLIDE -------------------------------------------#
        slide2 = template(r"Some Examples of $ax^n$")
        transform(self,g,slide2,0)
        
        group1 = render_text_group(["f(x) = 2x^3", r"a=2\\n=3"])
        group2 = render_text_group(["f(x) = x", r"a=1\\n=1"])
        group3 = render_text_group(["f(x) = 5x^2", r"a=5\\n=2"])

        transform(self, g2, group1, 4)
        transform(self, group1, group2, 4)
        transform(self, group2, group3, 4)

        #--------------------------------------------- THIRD SLIDE --------------------------------------------#
        slide3 = template(r"The Rule")
        transform(self, slide2, slide3, 0)

        group4 = MathTex(r"f(x) = a x^n", r"\\ \frac{d}{dx} f(x) = n a x^{n-1}")
        transform(self, group3, group4, 5)

        self.wait(3)
        self.remove(group4)
        # -------------------------------------------- FOURTH SLIDE ------------------------------------------#
        slide4 = template(r"Proof")
        transform(self, slide3, slide4,0)
        text = MathTex(
            r"\frac{d}{dx}ax^n",
            r"&=a \lim_{\Delta x\to 0}",
            r"{(x+\Delta x)^n - x^n \over \Delta x}",
            r"= a \lim_{\Delta x\to 0}",
            r"{{\Sigma_{k=0}^n {\binom{n}{k} x^{n-k} \Delta x - x^n} \over \Delta x}", 
            color=WHITE, font_size=25).shift(2 * LEFT).shift(2*UP)
        
        f1=MathTex(
            r"= a",
            r"\lim_{\Delta x\to 0}",        
            r"{",                            
            r"x^n +",                        
            r"\binom{n}{1} x^{n-1}",         
            r"\Delta x",                     
            r"+ \binom{n}{2} x^{n-2} ",      
            r"\Delta x^2 ",                  
            r"+ ... + \binom{n}{n-1} x ",    
            r"\Delta x^{n-1} ",              
            r"+ \binom{n}{n} ",               
            r"\Delta x^n",                  
            r"-x^n",                        
            r"\over",                       
            r"\Delta x",                    
            r"}", font_size=25).align_to(text[1], LEFT)
        f2=MathTex(
            r"= a",
            r"\lim_{\Delta x\to 0}",       
            r"{",                          
            r"",                       
            r"\binom{n}{1} x^{n-1}",       
            r"\Delta x",                   
            r"+ \binom{n}{2} x^{n-2}",     
            r"\Delta x^2 ",                
            r"+ ... + \binom{n}{n-1} x ",  
            r"\Delta x^{n-1}",             
            r"+ \binom{n}{n} ",            
            r"\Delta x^n",                 
            r"",                           
            r"\over",                      
            r"\Delta x",                   
            r"}", font_size=25).align_to(text[1], LEFT)

        f3=MathTex(
            r"= a",
            r"\lim_{\Delta x\to 0}",                
            r"{",                                   
            r"",                                               
            r"\binom{n}{1} x^{n-1}",                
            r"",                                    
            r"+ \binom{n}{2} x^{n-2}",              
            r"\Delta x ",                           
            r"+ ... + \binom{n}{n-1} x ",           
            r"\Delta x^{n-2}",                      
            r"+ \binom{n}{n} ",                     
            r"\Delta x^{n-1}",                      
            r"",                                               
            r"",                                    
            r"",                                    
            r"}", font_size=25).align_to(text[1], LEFT)

        f4=MathTex(
            r"",                                        
            r"{",                                       
            r"",                                                   
            r"= a",                                                
            r" \binom{n}{1} x^{n-1} = a n x^{n-1}",                   
            r"",                                        
            r"",                                        
            r"",                                        
            r"",                                        
            r"",                                        
            r"",                                        
            r"",                                        
            r"",                                                    
            r"",                                        
            r"",                                        
            r"}", font_size=25).align_to(text[1], LEFT)
        
        self.add(text)
        self.wait(2)        
        self.add(f1)
        self.wait(5)
        framebox1 = SurroundingRectangle(f1[3], buff=.1, color=RED)
        framebox2 = SurroundingRectangle(f1[12], buff=.1, color=RED) 
        self.play(Create(framebox1))  # creating the frame 
        self.play(Create(framebox2))
        self.wait(3)

        self.play(
            ReplacementTransform(f1,f2),
            FadeOut(framebox1),
            FadeOut(framebox2)
        )
        
        self.wait(3)
        framebox3 = SurroundingRectangle(f2[4], buff=.1, color=RED)
        framebox4 = SurroundingRectangle(f2[6], buff=.1, color=RED)
        framebox5 = SurroundingRectangle(f2[8], buff=.1, color=RED)
        framebox6 = SurroundingRectangle(f2[10], buff=.1, color=RED) 
        framebox7 = SurroundingRectangle(f2[12], buff=.1, color=RED)
        self.play(Create(framebox3))  # creating the frame 
        self.play(Create(framebox4))
        self.play(Create(framebox5))  # creating the frame 
        self.play(Create(framebox6))
        self.play(Create(framebox7))  # creating the frame 
        
        self.wait(3)
        self.play(
            ReplacementTransform(f2,f3),
            FadeOut(framebox3),
            FadeOut(framebox4),
            FadeOut(framebox5),
            FadeOut(framebox6),
            FadeOut(framebox7)
        )

        self.wait(3)
        framebox8 = SurroundingRectangle(f3[1], buff=.1, color=RED)
        group = VGroup(f3[4], f3[5], f3[6], f3[7], f3[8], f3[9])
        brace = Brace(mobject=group, direction=DOWN, buff=.2, sharpness=1, background_stroke_color=RED)
        brace_text = brace.get_tex(r"=0")
        self.play(Create(framebox8))
        self.wait(2)
        self.play(
            Create(brace_text),
            GrowFromCenter(brace)
        )
        self.wait(2)
        self.play(
            FadeOut(brace_text),
            FadeOut(brace),
            ReplacementTransform(f3,f4),
            FadeOut(framebox8)
        )
        self.wait(5)
        self.remove(text, f4)
        slide5 = template(r"See you!")
        transform(self, slide4, slide5,0)
        self.add(greetings())
        self.wait(5)