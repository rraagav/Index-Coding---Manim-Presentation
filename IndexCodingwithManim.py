from manim import *
import numpy as np
import array as arr

class part1(Scene):
    def construct(self):
        self.wait(1)
        intro = Text("Necessity is the Mother of all Invention",font_size = 40).center()
        self.play(Write(intro),run_time=2)
        self.wait(2)#wait for 2 seconds.
        self.play(Unwrite(intro),run_time=1)
        self.wait(1)
        #ticking sound starts.

        distress = Text("Someone has decided to detonate a bomb,and you, the hero must defuse it.\n",font_size = 30).move_to(UP).align_on_border(LEFT)
        self.play(FadeIn(distress),run_time=1)
        self.wait(1)
        dis2 = Text("Some buttons lie on the bomb, maybe it's a place to input a\npassword? Maybe this decodes the bomb?\n",font_size = 30).next_to(distress,2.5*DOWN).align_on_border(LEFT)
        self.play(FadeIn(dis2),run_time=1)
        self.wait(2)
        self.play(FadeOut(distress),FadeOut(dis2),run_time=1)
        self.wait(2)
        calltoaction = Text("What will you do?!",font_size = 40, color = RED).center() #put some deep brass songs(dune) 
        self.play(Write(calltoaction),run_time=1)
        self.wait(2)
        self.play(FadeOut(calltoaction),run_time=0.5)

        box_of_instructions = Rectangle(height = 3.7, width = 12, fill_opacity=0.4,color=RED)
        box_of_instructions.center()
        instructions = Text("Instructions",font_size=40,color = YELLOW).to_edge(3.3*UP)
        self.play(DrawBorderThenFill(box_of_instructions))
        self.play(Write(instructions))
        self.wait(0.5)

        sentences = [
            "You must send information through codewords that you generate",
            "5 Receivers exist",
            "You must send codes such that they can be decoded in the shortest time possible",
            "If the code taken by all receivers is correct, then you defuse the bomb",
        ]

        text_objects = [
            Text(sentence, font_size=20)
            for sentence in sentences
        ]

        line_spacing = 3  # Adjust the line spacing factor as desired
        spaced_text_objects = []
        for text_obj in text_objects:
            empty_line = Text(" ", font_size=20)
            spaced_text_objects.append(VGroup(text_obj, empty_line))

        text_group = VGroup(*spaced_text_objects).arrange(DOWN, aligned_edge=LEFT).move_to(box_of_instructions.get_center())

        self.play(FadeIn(text_group), run_time = 1)
        self.wait(5)
        self.play(FadeOut(text_group),FadeOut(box_of_instructions),FadeOut(instructions),run_time=1)
        self.wait(2)
#20 seconds.

class part2(Scene):
    def construct(self):
        self.wait(1)#we now become the hero
        beginners = Text("What if I try 00000?",font_size = 40,color = YELLOW).center()
        #I want to create 5 small boxes, of unit length, and space them out equally. these act as transmitters
        self.play(Write(beginners),run_time=1)

        beginners_transformed = beginners.copy()
        self.play(Transform(beginners, beginners_transformed),run_time=0.5)
        beginners_transformed = beginners.copy().shift((4*LEFT + 3.6*UP)).scale(0.7)
        self.play(Transform(beginners, beginners_transformed),run_time=0.5)   
        
        tr = Rectangle(height=1, width=1, fill_opacity=0.2, color=BLUE).next_to(beginners_transformed,6*DOWN)
        tx = Tex(r"$TX$",font_size = 40).next_to(tr,LEFT)

        #I need these receivers to be on the extreme right side (opposing the transmitters), and in their line.)
        rx1 = Rectangle(height=1, width=1, fill_opacity=0.2, color=GREEN).next_to(tr,30*RIGHT + 2.8*UP)
        r1 = Tex(r"$RX_1$",font_size = 40).next_to(rx1,RIGHT)
        rx2 = Rectangle(height=1, width=1, fill_opacity=0.2, color=GREEN).next_to(rx1,1.2*DOWN)
        r2 = Tex(r"$RX_2$",font_size = 40).next_to(rx2,RIGHT)
        rx3 = Rectangle(height=1, width=1, fill_opacity=0.2, color=GREEN).next_to(rx2,1.2*DOWN)
        r3 = Tex(r"$RX_3$",font_size = 40).next_to(rx3,RIGHT)
        rx4 = Rectangle(height=1, width=1, fill_opacity=0.2, color=GREEN).next_to(rx3,1.2*DOWN)
        r4 = Tex(r"$RX_4$",font_size = 40).next_to(rx4,RIGHT)
        rx5 = Rectangle(height=1, width=1, fill_opacity=0.2, color=GREEN).next_to(rx4,1.2*DOWN)
        r5 = Tex(r"$RX_5$",font_size = 40).next_to(rx5,RIGHT)

        self.play(DrawBorderThenFill(tr),Write(tx),run_time=1)
        self.play(DrawBorderThenFill(rx1),DrawBorderThenFill(rx2),DrawBorderThenFill(rx3),DrawBorderThenFill(rx4),DrawBorderThenFill(rx5),run_time=1)
        self.play(Write(r1),Write(r2),Write(r3),Write(r4),Write(r5),run_time=0.5)
        #draw arrows connecting the transmitters to the receivers.
        ar1 = Arrow(start=tr.get_center(), end=rx1.get_center(), color=ORANGE, stroke_width=2.5)
        text1 = Text("0", font_size=48).move_to(tr.get_center())
        self.play(Create(ar1),FadeIn(text1),run_time=0.5)
        text1c = text1.copy().move_to(rx1.get_center())
        self.play(Transform(text1.copy(),text1c),run_time=1)
        self.wait(0.3)    

        ar2 = Arrow(start=tr.get_center(), end=rx2.get_center(), color=ORANGE, stroke_width=2.5)
        text2 = Text("0", font_size=48).move_to(tr.get_center())
        self.play(Create(ar2),FadeIn(text2),run_time=0.5)
        text2c = text2.copy().move_to(rx2.get_center())
        self.play(Transform(text2.copy(),text2c),run_time=1)
        self.wait(0.3)    


        ar3 = Arrow(start=tr.get_center(), end=rx3.get_center(), color=ORANGE, stroke_width=2.5)
        text3 = Text("0", font_size=48).move_to(tr.get_center())
        self.play(Create(ar3),FadeIn(text3),run_time=0.5)
        text3c = text3.copy().move_to(rx3.get_center())
        self.play(Transform(text3.copy(),text3c),run_time=1)
        self.wait(0.3)    


        ar4 = Arrow(start=tr.get_center(), end=rx4.get_center(), color=ORANGE, stroke_width=2.5)
        text4 = Text("0", font_size=48).move_to(tr.get_center())
        self.play(Create(ar4),FadeIn(text4),run_time=0.5)
        text4c = text4.copy().move_to(rx4.get_center())
        self.play(Transform(text4.copy(),text4c),run_time=1)
        self.wait(0.3)    


        ar5 = Arrow(start=tr.get_center(), end=rx5.get_center(), color=ORANGE, stroke_width=2.5)
        text5 = Text("0", font_size=48).move_to(tr.get_center())
        self.play(Create(ar5),FadeIn(text5),run_time=0.5)
        text5c = text5.copy().move_to(rx5.get_center())
        self.play(Transform(text5.copy(),text5c),run_time=1)
        self.wait(0.3)    
    
        self.wait(2)
        observations_for_zeros = Text("This way, there's a 50% chance of things working out.\n\nThis is good...right?",font_size = 30).next_to(rx5,0.7*DOWN).align_on_border(LEFT)
        self.play(FadeIn(observations_for_zeros),run_time=0.5)
        self.wait(4)
        #However, this codeword isn't optimal, and it could even be wrong. I need to find a better probability distribution. 
        
        self.play(FadeOut(ar1),FadeOut(ar2),FadeOut(ar3),FadeOut(ar4),FadeOut(ar5),run_time = 0.5)
        self.play(FadeOut(text1c),FadeOut(text2c),FadeOut(text3c),FadeOut(text4c),FadeOut(text5c),run_time = 0.5)
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3),FadeOut(text4),FadeOut(text5),run_time = 0.5)
        self.play(FadeOut(tx),FadeOut(r1),FadeOut(r2),FadeOut(r3),FadeOut(r4),FadeOut(r5),run_time=0.3)
        self.play(FadeOut(beginners),FadeOut(tr),FadeOut(rx1),FadeOut(rx2),FadeOut(rx3),FadeOut(rx4),FadeOut(rx5),run_time=0.5)
        self.play(FadeOut(observations_for_zeros),run_time=0.5)
        self.clear()

        narrator1 = Text("Sure this is fast, but it's too risky",font_size = 30,color=PURE_RED).next_to(beginners,DOWN).align_on_border(LEFT)
        narrator2 = Text("There's only a 50% chance per receiver that the correct bit is received",font_size = 30,color=PURE_RED).next_to(narrator1,DOWN).align_on_border(LEFT)
        narrator3 = Text("Let me think about this logically",font_size = 30).next_to(narrator2,DOWN).align_on_border(LEFT)
        
        shannon = Text("I could try Shannon's Source Coding Theorem?",font_size = 30,color=YELLOW).next_to(narrator3,2*DOWN).align_on_border(LEFT)
        #showing that entropy is lowest length for codeword.
        self.play(FadeIn(narrator1),FadeIn(narrator2),run_time=0.5)
        self.wait(3)
        self.play(FadeOut(narrator1),FadeOut(narrator2),FadeIn(narrator3),run_time=0.5)
        self.wait(2) #explanation about entropy and all.
        self.play(FadeIn(shannon),run_time=0.5)
        self.wait(3) #explanation
        s1 = Text("I can just take the entropy of the codeword I've sent.",font_size = 30,color=YELLOW).next_to(shannon,DOWN).align_on_border(LEFT)
        s2 = Text("It's the lower bound of my codeword after all",font_size = 30,color=YELLOW).next_to(s1,DOWN).align_on_border(LEFT)
        self.play(FadeOut(narrator3),FadeOut(shannon),FadeIn(s1),FadeIn(s2),run_time=0.5)
        self.wait(4) 
        entropy = Tex(r"H(X) = -$\sum_{i=1}^5$ $p_i$ $\log_2$ $p_i$, where each $p_i$ = 0.5",font_size = 40).next_to(s2,DOWN).align_on_border(LEFT)
        self.play(FadeIn(entropy),run_time=0.5)
        entropyans = Tex(r"Then, H(X) = 2.5",font_size = 40).next_to(entropy,1.5*DOWN).align_on_border(LEFT)
        self.play(FadeIn(entropyans),run_time=0.5)
        self.wait(4)

class sideinfo(Scene):
    def construct(self):
        better_2 = Text("Consider the bits x and y: ",font_size = 30).align_to(LEFT).move_to(3*UP)
        x = Tex(r"$x$")
        x.move_to(2 * LEFT).align_to(better_2,DOWN)
        
        fancy_X = Tex(r"$\mathcal{X}$")  # Fancy notation for X
        fancy_X.next_to(x, 2.5*RIGHT).align_to(better_2,DOWN)
        
        belongs_X = Tex(r"$\in$")  # "belongs to" symbol
        belongs_X.next_to(x, RIGHT).align_to(better_2,DOWN)

        y = Tex(r"$y$")
        y.move_to(belongs_X.get_center() + 2*RIGHT).align_to(better_2,2.2*DOWN)

        fancy_Y = Tex(r"$\mathcal{Y}$")  # Fancy notation for Y
        fancy_Y.next_to(y, 2.5*RIGHT).align_to(better_2,2.2*DOWN)
        
        belong_Y = Tex(r"$\in$")  # "belongs to" symbol
        belong_Y.next_to(y, 0.8*RIGHT).align_to(better_2,2.2*DOWN)
        
        xgroup = VGroup(x, fancy_X, belongs_X)
        ygroup = VGroup(y, fancy_Y, belong_Y)

        #move the equations in place.
        xgroup.align_data(ygroup)
        xgroup.move_to(0.3*UP)
        ygroup.move_to(0.3*DOWN)

        comb = VGroup(xgroup,ygroup)
        comb.move_to(2.8*UP + 5*LEFT)
        input = Text("Inputs",font_size = 30).next_to(xgroup,1.5*RIGHT)
        y_text = Text("Receiver gets information about x from y",font_size = 30).next_to(ygroup,1.5*RIGHT)
        # add more wait time to show XxY and L. 
        self.play(Write(xgroup),Write(ygroup),run_time=0.5)        
        self.play(Write(input),Write(y_text),run_time=0.5)

        #ensure the text afterwards is aligned well. 
        capture = Text(r"We isolate this x and y into a set L to get ",font_size = 30).next_to(comb,DOWN).align_to(comb,LEFT)
        xy = Tex(r"$(x,y)$").next_to(capture,RIGHT)
        self.play(Write(capture), Write(xy),run_time=1)
        self.wait(1)
        
        relation = Tex(r"$(x,y) \in \mathcal{X} \times \mathcal{Y}$").next_to(capture,DOWN).align_to(capture,LEFT)
        alphabet = Tex(r"$\mathcal{L} \subseteq (\mathcal{X} \times \mathcal{Y}) $").next_to(relation,2*DOWN).align_to(capture,LEFT)
        #put a box around this text:
        relation.add_background_rectangle(color=BLUE_D,opacity=0.3, buff=0.2)
        self.play(Transform(xy.copy(),relation), run_time=1)
        self.wait(1)
        alphabet.add_background_rectangle(color=BLUE_E,opacity=0.3, buff=0.2)
        self.play(Transform(xy.copy(),alphabet),run_time = 1)
        self.wait(1) #explain whats happening here.

        witsenhausen = Text("Witsenhausen considered zero-error codes with side information",font_size = 30).next_to(alphabet,DOWN).align_to(capture,LEFT)
        self.play(Write(witsenhausen),run_time=1)

        wit1 = Text("Clearly, this decreases the probabilities associated with each bit.",font_size = 30).next_to(witsenhausen,DOWN).align_to(capture,LEFT)
        self.play(Write(wit1),run_time=0.5)#align this lmao
        self.wait(0.5)

        wit2cont = Text("Entropy associated with each bit decreases",font_size = 30).next_to(wit1,DOWN).align_to(capture,LEFT)
        implies = Tex(r"$\implies$").next_to(wit2cont,RIGHT)
        self.play(Write(wit2cont),Write(implies),run_time=0.5)
        self.wait(0.5)

        wit3 = Text("We decode quicker",font_size = 25).next_to(implies,RIGHT)
        self.play(Write(wit3),run_time=0.5)
        self.wait(1)

class part3(Scene):
    def construct(self):

        Block_erasure = Text("I'll assume block-level erasure:",font_size = 45,color = GREEN_A).center()
        self.play(Write(Block_erasure),run_time=1)
        self.play(Block_erasure.animate.shift(3*UP),run_time=0.5)
        
        What_is_it = Text("\nI must consider an entire error-free block or not at all.",font_size = 30).next_to(Block_erasure,DOWN).align_on_border(LEFT)
        conclude = Text("\n\nWith this assumption, let me consider each block as a single bit.",font_size = 30).next_to(What_is_it,DOWN).align_on_border(LEFT)
        
        self.play(Write(What_is_it),run_time=1)
        self.wait(1)
        self.play(Transform(What_is_it.copy(),conclude),run_time=1)
        self.wait(1)
        self.play(FadeOut(What_is_it),FadeOut(conclude),FadeOut(Block_erasure),run_time=0.5)
        self.wait(5)
        self.clear()

        FormalProblem = Text("We formalize the Source Coding with Side Information Problem as follows:",font_size = 30).center()
        FormalProblem.add_background_rectangle(color=PURPLE_E,opacity=0.5, buff=0.3)
        self.play(Write(FormalProblem),run_time=0.5)
        self.play(FormalProblem.animate.shift(3*UP),run_time=1)

        line1 = Tex(r"Consider a Sender who has an input (data) $x$ from a source",font_size = 45).next_to(FormalProblem,DOWN).align_on_border(LEFT)
        line4 = Tex(r"alphabet $\mathcal{X} \in \{0,1\}^{n}$",font_size = 45).next_to(line1, DOWN).align_on_border(LEFT)
        line2 = Tex(r"There are $n$ receivers, $R_1, R_2 \ldots R_n$, where for each $i$, $R_i$ is",font_size=45).next_to(line4, 2*DOWN).align_on_border(LEFT)
        line3 = Tex(r"interested in the bit (block) $x_i$",font_size=45).next_to(line2, DOWN).align_on_border(LEFT)
        
        self.play(Write(line1),Write(line4),run_time=1) 
        self.wait(4)
        self.play(Write(line2),Write(line3),run_time=1)
        self.wait(6)

        sideinfo = Tex(r"We obtain this side-information from a Graph directed on $\mathbb{N}$", font_size=45).next_to(line3, 2*DOWN).align_on_border(LEFT)
        self.play(Write(sideinfo),run_time=1)
        self.wait(2)
        sideinfoformula = Tex(r"Side Information of $R_i$ = $x[N($i$)]$", font_size=45).next_to(sideinfo, DOWN).align_on_border(LEFT)
        self.play(Write(sideinfoformula),run_time=1)
        self.wait(0.5)
        whatsN = Tex(r"$N(i)$ $\overset{\Delta}{=}$ \{$j \in V$ \right\vert $ (i,j)$ is an edge\}",font_size = 45).next_to(sideinfoformula,DOWN).align_on_border(LEFT)
        whatsN.add_background_rectangle(color=GRAY_A,opacity=0.3, buff=0.2)
        self.play(Write(whatsN),run_time=1)
        self.wait(3)

        self.play(FadeOut(line1),FadeOut(line3),FadeOut(line4),FadeOut(sideinfo),FadeOut(sideinfoformula),FadeOut(whatsN),FadeOut(FormalProblem),run_time=0.5)
        self.play(line2.animate.shift(3*UP).scale(0.7),run_time=0.5)
        #make boxes for transmitters and receivers, going up to i rx, and show that a directed graph is acting on them.
        
        tr = Rectangle(height=1, width=1, fill_opacity=0.2, color=BLUE).next_to(line2,7*DOWN + LEFT)
        tx = Tex(r"$TX$",font_size = 40).next_to(tr,LEFT)
        xi = Tex(r"$x_i$",font_size = 40).move_to(tr.get_center())
        
        #I need these receivers to be on the extreme right side (opposing the transmitters), and in their line.)
        rx1 = Rectangle(height=1, width=1, fill_opacity=0.2, color=GREEN).next_to(tr,20*RIGHT + 2.8*UP)
        r1 = Tex(r"$RX_1$",font_size = 40).next_to(rx1,1.2*RIGHT)
        bitr1 = Tex(r"$x_1$",font_size = 40).move_to(rx1.get_center())

        rx2 = Rectangle(height=1, width=1, fill_opacity=0.2, color=GREEN).next_to(rx1,1.2*DOWN)
        r2 = Tex(r"$RX_2$",font_size = 40).next_to(rx2,1.2*RIGHT)
        bitr2 = Tex(r"$x_2$",font_size = 40).move_to(rx2.get_center())

        rx3 = Rectangle(height=1, width=1, fill_opacity=0.2, color=GREEN).next_to(rx2,1.2*DOWN)
        r3 = Tex(r"$RX_3$",font_size = 40).next_to(rx3,1.2*RIGHT)
        bitr3 = Tex(r"$x_3$",font_size = 40).move_to(rx3.get_center())

        #make three dots between rx3 and rxi to show 'i' receivers.
        dr1 = Dot().move_to(rx3.get_center() + 0.5*DOWN)
        dr2 = Dot().move_to(rx3.get_center() + 1*DOWN)
        dr3 = Dot().move_to(rx3.get_center() + 1.5*DOWN)
        dr = VGroup(dr1,dr2,dr3)

        rxi = Rectangle(height=1, width=1, fill_opacity=0.2, color=GREEN).next_to(dr3,DOWN)
        ri = Tex(r"$RX_4$",font_size = 40).next_to(rxi,1.2*RIGHT)
        bitri = Tex(r"$x_i$",font_size = 40).move_to(rxi.get_center())

        self.play(DrawBorderThenFill(tr),Write(tx), Write(xi),run_time=1)
        self.play(DrawBorderThenFill(rx1),DrawBorderThenFill(rx2),DrawBorderThenFill(rx3),Create(dr),DrawBorderThenFill(rxi),run_time=1)
        self.play(Write(r1),Write(r2),Write(r3),Write(ri),run_time=0.5)
        
        ar1 = Arrow(start=tr.get_center(), end=rx1.get_center(), color=ORANGE, stroke_width=2.5)
        ar2 = Arrow(start=tr.get_center(), end=rx2.get_center(), color=ORANGE, stroke_width=2.5)
        ar3 = Arrow(start=tr.get_center(), end=rx3.get_center(), color=ORANGE, stroke_width=2.5)
        ari = Arrow(start=tr.get_center(), end=rxi.get_center(), color=ORANGE, stroke_width=2.5)
        
        #draw arrows:
        self.play(Create(ar1),Create(ar2),Create(ar3),Create(ari),run_time=1)
        self.wait(2)
        #explain fig wait time.
        #move all x1 to xi to rx(transform)
        self.play(Transform(xi.copy(),bitri),Transform(xi.copy(),bitr1),Transform(xi.copy(),bitr2),Transform(xi.copy(),bitr3),run_time=1)
        #draw the graphs:
        node1 = Circle(radius=0.5, color=PURPLE, fill_opacity = 0.5).next_to(r1,RIGHT)
        node2 = Circle(radius=0.5, color=PURPLE, fill_opacity = 0.5).next_to(r2,RIGHT)
        node3 = Circle(radius=0.5, color=PURPLE, fill_opacity = 0.5).next_to(r3,RIGHT)
        nodei = Circle(radius=0.5, color=PURPLE, fill_opacity = 0.5).next_to(ri,RIGHT)

        ndx1 = Tex(r"$x_1'$",font_size = 40).move_to(node1.get_center())
        ndx2 = Tex(r"$x_2'$",font_size = 40).move_to(node2.get_center())
        ndx3 = Tex(r"$x_3'$",font_size = 40).move_to(node3.get_center())
        ndxi = Tex(r"$x_{i}'$",font_size = 40).move_to(nodei.get_center())

        self.play(DrawBorderThenFill(node1),DrawBorderThenFill(node2),DrawBorderThenFill(node3),DrawBorderThenFill(nodei),run_time=1)
        self.play(Write(ndx1),Write(ndx2),Write(ndx3),Write(ndxi),run_time=0.5)
        self.wait(3)
        #draw arrows between the graphs.
        arrow1 = Arrow(start=node1.get_center(), end=node2.get_center(), color=YELLOW, stroke_width=2.5)
        arrow2 = Arrow(start=node2.get_center(), end=node3.get_center(), color=YELLOW, stroke_width=2.5)
        arrow3 = Arrow(start=node3.get_center(), end=dr1, color=YELLOW, stroke_width=2.5)
        arrow4 = Arrow(start=dr3, end=nodei.get_center(), color=YELLOW, stroke_width=2.5)
        
        self.play(Transform(ar1.copy(),arrow1),Transform(ar2.copy(),arrow2),Transform(ar3.copy(),arrow3),Transform(ari.copy(),arrow4),run_time=1)
        self.wait(3)

        self.play(FadeOut(node1),FadeOut(node2),FadeOut(node3),FadeOut(nodei),FadeOut(arrow1),FadeOut(arrow2),FadeOut(arrow3),FadeOut(arrow4),run_time=0.5) 
        self.play(FadeOut(ar1),FadeOut(ar2),FadeOut(ar3),FadeOut(ari),run_time=0.5)
        self.play(FadeOut(r1),FadeOut(r2),FadeOut(r3),FadeOut(ri),FadeOut(dr),run_time=0.5)
        self.play(FadeOut(xi),FadeOut(tx),FadeOut(tr),run_time=0.5)
        self.clear()
        self.wait(1)

class part4(Scene):
    def construct(self):
        #example 1 from paper. 
        example1 = Tex(r"Consider $x \in \{0,1\}^{n}$ Let n = 3",font_size = 45).move_to(3.5*UP)
        self.play(Write(example1),run_time=1)
        s1 = Square(side_length=0.8, fill_opacity=0.2, color=GREEN).next_to(example1,DOWN).align_on_border(LEFT)
        s2 = Square(side_length=0.8, fill_opacity=0.2, color=GREEN).next_to(s1,2*RIGHT)
        s3 = Square(side_length=0.8, fill_opacity=0.2, color=GREEN).next_to(s2,2*RIGHT)

        r1 = Tex(r"$R_1$",font_size = 40).next_to(s1,DOWN)
        r2 = Tex(r"$R_2$",font_size = 40).next_to(s2,DOWN)
        r3 = Tex(r"$R_3$",font_size = 40).next_to(s3,DOWN)

        x1 = Tex(r"$x_1$",font_size = 40).move_to(s1.get_center())
        x2 = Tex(r"$x_2$",font_size = 40).move_to(s2.get_center())
        x3 = Tex(r"$x_3$",font_size = 40).move_to(s3.get_center())

        self.play(DrawBorderThenFill(s1),DrawBorderThenFill(s2),DrawBorderThenFill(s3),run_time=0.5)
        self.play(Write(r1),Write(r2),Write(r3),Write(x1),Write(x2),Write(x3),run_time=0.5)
        self.wait(2)

        #create 3 circles, and label them as R1, R2, R3(put this text below them).
        c1 = Circle(radius=0.5, color=BLUE,fill_opacity = 0.5).move_to(LEFT)
        c2 = Circle(radius=0.5, color=BLUE,fill_opacity = 0.5).move_to(1.2*UP)
        c3 = Circle(radius=0.5, color=BLUE,fill_opacity = 0.5).move_to(RIGHT)
        
        #make copies of x1,x2,x3 and put it in the centre of the circles.
        x1c = x1.copy().move_to(c1.get_center())
        x2c = x2.copy().move_to(c2.get_center())
        x3c = x3.copy().move_to(c3.get_center())
                
        arr1 = Arrow(start=c1.get_center(), end=c2.get_center(), color=BLUE, stroke_width=3)
        arr2 = Arrow(start=c2.get_center(), end=c3.get_center(), color=BLUE, stroke_width=3)
        arr3 = Arrow(start=c3.get_center(), end=c1.get_center(), color=BLUE, stroke_width=3)

        cgroup = VGroup(c1,c2,c3,arr1,arr2,arr3,x1c,x2c,x3c)      
        cgroup.next_to(example1,RIGHT).align_on_border(RIGHT).shift(DOWN)

        self.play(DrawBorderThenFill(c1),DrawBorderThenFill(c2),DrawBorderThenFill(c3),run_time=1)
        
        self.play(Write(x1c),Write(x2c),Write(x3c),run_time=1)
        self.play(Create(arr1),run_time=0.5)
        self.play(Create(arr2),run_time=0.5)
        self.play(Create(arr3),run_time=0.5)
        self.wait(4)

        tex1 = Tex(r"Each bit $x_i$ is 'independant', i.e. each $x_i-1$ is independant of $x_i$",font_size = 33).next_to(r1,DOWN).align_on_border(LEFT)
        self.play(Write(tex1),run_time=1)
        self.wait(3)
        tex2 = Tex(r"To shorten the broadcast message, we can send the parities:",font_size = 33).next_to(tex1,DOWN).align_on_border(LEFT)
        tex12 = Tex(r"$x_1 \oplus x_2$",font_size = 33).next_to(tex2,DOWN).align_on_border(LEFT)
        tex23 = Tex(r" $x_2 \oplus x_3$",font_size = 33).next_to(tex12,3*RIGHT)
        tex12.add_background_rectangle(color=GREEN,opacity=0.3, buff=0.2)
        tex23.add_background_rectangle(color=GREEN,opacity=0.3, buff=0.2)
        self.play(Write(tex2),Write(tex12),Write(tex23),run_time=1)
        self.wait(5)

        recovery1 = Tex(r"For $i>1$, we recover $R_i$'s corresponding $x_i$ by taking ($x_i-1 \oplus x_i$) $\oplus$ ($x_i$)",font_size = 33).next_to(tex12,DOWN).align_on_border(LEFT)
        self.play(Write(recovery1),run_time=1)
        self.wait(2)
        r2 = Tex(r"Thus, $R_2$ can recover $x_2$ by taking (transmitted parity $\oplus$ $i^{th}$ bit)",font_size = 33).next_to(recovery1,DOWN).align_on_border(LEFT)
        self.play(Write(r2),run_time=1)
        self.wait(3)
        #bit at R2 finally is:
        r2bit = Tex(r"$x_2$ = $(x_1 \oplus x_2) \oplus x_2$",font_size = 33).next_to(r2,DOWN).align_on_border(LEFT)
        self.play(Transform(x2.copy(),r2bit),run_time=1)
        self.wait(2)
        #shrink and put it in R2.
        self.play(Transform(r2bit,x2),run_time=1)
        self.wait(3)
        self.play(Unwrite(example1),Uncreate(s1),Uncreate(s2),Uncreate(s3),Unwrite(r1),Unwrite(r2),Unwrite(r3),Unwrite(x1),Unwrite(x2),Unwrite(x3),run_time=0.5)
        self.play(FadeOut(cgroup), FadeOut(tex1),FadeOut(tex2),FadeOut(tex12),FadeOut(tex23),FadeOut(recovery1),FadeOut(r2),FadeOut(r2bit),run_time=0.5)
        self.clear()
        self.wait(1)

class part5(Scene):
    def construct(self):
        #Index Codes
        IndexCodes = Text("Index Codes",font_size = 45,color = GREEN_A).center()
        self.play(Write(IndexCodes),run_time=0.5)
        self.play(IndexCodes.animate.shift(3*UP),run_time=0.5)
        
        idx1 = Tex(r"Index Codes $\mathcal{C}$ are deterministic for $ \{0,1\}^{n}$, where n is the",font_size = 40).next_to(IndexCodes,DOWN).align_on_border(LEFT)
        idx2 = Tex(r"number of nodes in the given graph $\mathcal{G}$",font_size = 40).next_to(idx1,DOWN).align_on_border(LEFT)
        self.play(Write(idx1),Write(idx2),run_time=1)
        self.wait(1)        

        set_enc = Tex(r"It forms $\{0,1\}^{l}$, a set with encoding and decoding functions.",font_size = 40).next_to(idx2,2*DOWN).align_on_border(LEFT)
        self.play(Write(set_enc),run_time=1)
        self.wait(1)

        enc_dec = Tex(r"They simply need an encoding function E, and a set of decoding functions",font_size = 40).next_to(set_enc,DOWN).align_on_border(LEFT)
        self.play(Write(enc_dec),run_time=1)
        self.wait(1)
        enc = Tex(r"$E: \{0,1\}^{n} \rightarrow \{0,1\}^{l}$, maps the input space to possible codewords.",font_size = 35).next_to(enc_dec, 2*DOWN).align_on_border(LEFT)
        dec = Tex(r"Each receiver $R_i$ has decoding function $D_i$, capable of recovering $x_i$ for every $i$",font_size = 35).next_to(enc,DOWN).align_on_border(LEFT)
        self.play(Write(enc),Write(dec),run_time=1)
        self.wait(2)
        understand = Tex(r"The receivers won't be able to $\textit{understand}$ the received bits without",font_size = 35).next_to(dec,DOWN).align_on_border(LEFT)
        und2 = Tex(r"knowing the side-information graph $\mathcal{G}$ and the encoding scheme used.",font_size = 35).next_to(understand,DOWN).align_on_border(LEFT)
        und3 = Tex(r"We need to ensure that these are sent.",font_size = 35).next_to(und2,DOWN).align_on_border(LEFT)
        und3.add_background_rectangle(color=GREEN,opacity=0.3, buff=0.2)
        self.play(Write(understand),Write(und2),run_time=1)
        self.wait(2)
        self.play(Write(und3),run_time=1)
        self.wait(1)
        self.play(FadeOut(enc_dec),FadeOut(enc),FadeOut(dec),FadeOut(idx1),FadeOut(idx2),FadeOut(set_enc),FadeOut(IndexCodes),run_time=1)
        self.play(FadeOut(understand),FadeOut(und2),FadeOut(und3),run_time=1)
        self.wait(1)
        #refer ppt for why better.
#PPT

class part6(Scene):
    def construct(self):
        our_contri = Text("Graph Functionals",font_size = 45).center()
        self.play(Write(our_contri),run_time=0.5)
        self.wait(0.5)
        self.play(our_contri.animate.shift(3*UP).scale(0.85),run_time=0.5)
        self.wait(0.5)
        gfunc = Tex(r"We can find the minimum length of a given codeword by utilizing a ",font_size = 40).next_to(our_contri,DOWN).align_on_border(LEFT)
        gfunc2 = Tex(r"graph functional called $minrank$, which is applicable for a wide variety",font_size = 40).next_to(gfunc,DOWN).align_on_border(LEFT)
        func3 = Tex(r"of codes and side information graphs",font_size = 40).next_to(gfunc2,DOWN).align_on_border(LEFT)
        self.play(Write(gfunc),Write(gfunc2),Write(func3),run_time=1)
        self.wait(3)
        minrk = Tex(r"What is $minrank$?",font_size = 40).move_to(our_contri.get_center())
        self.play(FadeOut(our_contri), Transform(gfunc2.copy(),minrk),FadeOut(gfunc),FadeOut(gfunc2),FadeOut(func3),run_time=1)
        self.wait(1)
        w1 = Tex(r"Consider a Directed Graph $\mathcal{G}$ with $n$ vertices",font_size = 35).next_to(minrk,DOWN).align_on_border(LEFT)
        self.play(Write(w1),run_time=0.5)
        self.wait(2)
        #we find a matrix that 'fits' this graph, given some constraints. 
        w2 = Tex(r"A binary matrix (0-1 matrix) $\mathcal{A}$ $\textit{fits}$ $\mathcal{G}$: $\forall$ $i,j \in \mathbb{N}$, when (i,j) is an edge in $\mathcal{G}$ ",font_size = 35).next_to(w1,2*DOWN).align_on_border(LEFT)
        self.play(Write(w2),run_time=1)
        self.wait(1)
        w3 = Tex(r"$\implies$ $a_{ij}$ = 1 for $i = j$, and zero otherwise for $\mathcal{G}$ ",font_size = 35).next_to(w2,DOWN).align_on_border(LEFT)
        self.play(Write(w3),run_time=0.5)
        self.wait(1)
        #clearly, we find the adjacency matrix for this graph.
        w4 = Tex(r"The Adjacency matrix is $\mathbb{A}-\mathbb{I}$ where $\mathbb{I}$ is the Identity Matrix. ",font_size = 32).next_to(w3,2*DOWN).align_on_border(LEFT)
        # The Adjacency matrix of the edge subgraph is
        self.play(Write(w4),run_time=1)
        self.wait(2)
        #then we find rank of this matrix.
        w5 = Tex(r"Let $rk_2(.)$ denote the 2-rank of $\mathbb{A}$ (or any 0-1 matrix)" ,font_size = 32).next_to(w4,2*DOWN).align_on_border(LEFT)
        self.play(Write(w5),run_time=1)

        w6 = Tex(r"Then, the minrank of $\mathbb{A}$ = $minrk_2$$(\mathcal{G})$ $\overset{\Delta}{=}$ min{$rk_2$($\mathbb{A}$) : $\mathbb{A}$ fits $\mathbb{G}$}",font_size = 32).next_to(w5,DOWN).align_on_border(LEFT)
        self.play(Write(w6),run_time=1)
        self.wait(2)

        self.play(FadeOut(w1),FadeOut(w2),FadeOut(w3),FadeOut(w4),FadeOut(w5),FadeOut(w6),FadeOut(minrk),run_time=1)
        self.clear()
        #example on ppt for this.

class part7(Scene):
    def construct(self):
        proofs = Text("Proofs on the Bounds of Linear Codes",font_size = 45).center()
        self.play(Write(proofs),run_time=0.5)
        self.play(proofs.animate.shift(3*UP).scale(0.85),run_time=0.5)
        self.wait(2)
        #we obtain a tight characterization of the length for these index codes. i.e. 
        #provide a precise and accurate description or representation of the minimum length of 
        #linear INDEX codes that can be achieved for any given side information graph
        p1 = Tex(r"For any side-information graph $\mathcal{G}$, $l_{min}$ = $minrk_2(\mathcal{G})$",font_size = 35).next_to(proofs,DOWN).align_on_border(LEFT)
        proof1 = Tex(r"Let A be the matrix that fits $\mathcal{G}$ whose 2-rank is the same as $minrk_2(\mathcal{G})$ $\overset{\Delta}{=}$ $k$",font_size = 35).next_to(p1,DOWN).align_on_border(LEFT)
        self.play(Write(p1),Write(proof1),run_time=1)
        self.wait(3)
        p2 = Tex(r"Assume WLOG, then, span($A_1,A_2,...,A_k$) equals span of all rows of A",font_size = 35).next_to(proof1,DOWN).align_on_border(LEFT)
        self.play(Write(p2),run_time=1)
        self.wait(2)
        p3 = Tex(r"Fix a receiver $R_i$ and let $A_i$ = $\sum_{j = 1}^{k}$ $\lambda_j$$A_j$",font_size = 35).next_to(p2,DOWN).align_on_border(LEFT)
        p4 = Tex(r"Using the k-bit encoding of x, $A_i$.$x$ = $\sum_{j = 1}^{k}$ $\lambda_j$$b_j$",font_size = 35).next_to(p3,2.5*DOWN).align_on_border(LEFT)
        p3.add_background_rectangle(color=GREEN,opacity=0.3, buff=0.2)
        p4.add_background_rectangle(color=GREEN,opacity=0.3, buff=0.2)
        self.play(Write(p3),Write(p4),run_time=1)
        self.wait(4)
        ci = Tex(r"Consider the vector $c_i = A_i - e_i$. Here, $e_i$ is the $i^{th}$ standard basis vector",font_size = 35).next_to(p4,DOWN).align_on_border(LEFT)
        ci2 = Tex(r"$c_i$'s non-zero entries correspond to its neighbours.",font_size = 35).next_to(ci,DOWN).align_on_border(LEFT)
        recovery = Tex(r" We can find $c_i$.$x$ using side information.",font_size = 35).next_to(ci2,DOWN).align_on_border(LEFT)

        self.play(Write(ci),run_time=1)
        self.play(Write(ci2),Write(recovery),run_time=1)
        self.wait(15)
        self.play(FadeOut(proofs),FadeOut(p1),FadeOut(p2),FadeOut(p3),FadeOut(p4),FadeOut(ci),FadeOut(ci2),FadeOut(recovery),FadeOut(proof1),run_time=1)
        recovery = Tex(r"$R_i$ uses this to recover $x_i$ via ($A_i$.$x$) - ($c_i$.$x$) = $e_i$.$x$ = $x_i$").center().move_to(3*UP)
        natofe = Tex(r"For every $i$, $e_i$ belongs to the span of S $\bigcup$ {$e_j$: j $\in N(i)$}",font_size = 35).next_to(recovery,DOWN).align_on_border(LEFT)
        self.play(Write(recovery),run_time=1)
        self.wait(8)
        self.play(Write(natofe),run_time=1)
        bycontr = Tex(r"Take some $i$, and let's assume $e_i \notin W$",font_size = 35).next_to(natofe,DOWN).align_on_border(LEFT)
        self.play(Write(bycontr),run_time=1)
        self.wait(9)
        dual = Tex(r"Consider the dual of W, a set of orthogoal vectors to all vectors in W.",font_size = 35).next_to(bycontr,DOWN).align_on_border(LEFT)
        dual2 = Tex(r"And taking the dual of (dual W) returns W itself. Thus, our assumption: $e_i \notin W$ is invalid.",font_size = 35).next_to(dual,DOWN).align_on_border(LEFT)
        self.play(Write(dual),Write(dual2),run_time=1)
        self.wait(10)

