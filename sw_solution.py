from manim import *

class thunbnail(Scene):
    def construct(self):
        a=1

class opening(Scene):
    def construct(self):
        a=1

class PauseAndPonderSolution(Scene):
    def construct(self):
        
        bk = Tex("Bahnkurve",":")
        bkformula = MathTex(r"y(x)=", r"tan(\theta )x", r"-\frac{gx^{2}}{2v_{0}^{2}cos^{2}(\theta )}")
        ansatz = Tex("Ansatz",":")
        ansatzf = MathTex(r"y(x)=0")
        svn = Tex("Satz vom ", "Nullprodukt",":").to_corner(UL)
        svntxt = Tex("Ein ","Produkt"," ist genau dann ","0",",")
        svntxt2 = Tex("wenn mindestens ein ","Faktor 0"," ist.")
        svn[1].set_color(YELLOW)
        svntxt[1].set_color(YELLOW)
        svntxt[3].set_color(YELLOW)
        svntxt2[1].set_color(YELLOW)
        svnf1 = MathTex(r"x=0").to_corner(UL).shift(DOWN*0.7)
        svnf2 = MathTex(r"tan(\theta )", r"-\frac{g}{2v_{0}^{2}cos^{2}(\theta )}x",r"=0").to_corner(UL).shift(DOWN*1.3)

        bkf0 = MathTex(r"0=", r"tan(\theta )x", r"-\frac{gx^{2}}{2v_{0}^{2}cos^{2}(\theta )}").shift(DOWN)
        bkf1 = MathTex(r"0=", r"tan(\theta )x", r"-\frac{g}{2v_{0}^{2}cos^{2}(\theta )}x^{2}").shift(UP)
        bkf2 = MathTex(r"0=",r"x",r"\cdot (", r"tan(\theta )", r"-\frac{g}{2v_{0}^{2}cos^{2}(\theta )}x",r")").shift(UP)
        bkf3 = MathTex(r"0=",r"x")
        bkf4 = MathTex(r"0",r"=tan(\theta )",r"-",r"\frac{g}{2v_{0}^{2}cos^{2}(\theta )}x")
        bkf5 = MathTex(r"\frac{g}{2v_{0}^{2}cos^{2}(\theta )}",r"x=tan(\theta )",r"\div")
        bkf6 = MathTex(r"x=", r"tan(\theta ) ", r"\cdot \frac{2v_{0}^{2}cos^{2}(\theta )}{g}")

        bkf7 = MathTex(r"x=", r"tan(\theta )\cdot cos^{2}(\theta ) ", r"\cdot \frac{2v_{0}^{2}}{g}")
        bkf8 = MathTex(r"x=", r"tan(\theta )\cdot (cos\theta)^{2} ", r"\cdot \frac{2v_{0}^{2}}{g}")
        bkf9 = MathTex(r"x=", r"\frac{sin(\theta )}{cos(\theta)}\cdot (cos\theta)^{2} ", r"\cdot \frac{2v_{0}^{2}}{g}")

        bkf10 = MathTex(r"x=", r"\frac{sin(\theta )\cdot (cos\theta)^{2}}{cos(\theta)} ", r"\cdot \frac{2v_{0}^{2}}{g}")
        bkf11 = MathTex(r"x=", r"sin(\theta )\cdot cos(\theta )", r"\cdot \frac{2v_{0}^{2}}{g}")

        #Doppelwinkelidentität, double angle identity
        dai = Tex("Doppelwinkelidentität",":")
        dai[0].set_color(YELLOW)
        dai1 = MathTex(r"sin(2\theta)=2sin(\theta)cos(\theta)")
        dai2 = MathTex(r"\Leftrightarrow ",r"0.5sin(2\theta)=",r"sin(\theta)cos(\theta)")

        bkf12 = MathTex(r"x=", r"0.5sin(2 \theta)", r"\cdot \frac{2v_{0}^{2}}{g}")
        bkf13 = MathTex(r"x=", r"sin(2 \theta)", r"\cdot \frac{v_{0}^{2}}{g}")
        bkf14 = MathTex(r"R=", r"\frac{v_{0}^{2}}{g}", r"sin(2 \theta)")

        #Ansatz/Idee
        bk[0].set_color(YELLOW)
        ansatz[0].set_color(YELLOW)
        texts = VGroup(bk,bkformula,ansatz,ansatzf)
        ax = Axes(x_range=[0,9,1],x_length=9,y_range=[0,5,1],y_length=4)
        graph1 = ax.plot(lambda x: -0.198*(x-4.5)**2 + 4)
        labely = MathTex(r"y").align_to(ax,UL).shift(RIGHT*0.5)
        laabelx = MathTex(r"x").align_to(ax,DR).shift(UP*0.5+RIGHT*0.1)
        gstuff = VGroup(ax,graph1,labely,laabelx).shift(UP*1.5)
        vec1 = Vector([3.8,1.3,0],color=YELLOW).shift(DOWN*2 +0.5*RIGHT)
        vec2 = Vector([-3.8,1.3,0],color=YELLOW).shift(DOWN*2 -0.5*RIGHT)
        nulls = Tex("Nullstellen").shift(DOWN*1.3)
        txstuff = VGroup(vec1,vec2,nulls)

        bk.to_corner(UL)
        bkformula.to_corner(UL).shift(DOWN*0.4)
        ansatz.to_edge(UP).shift(RIGHT*2)
        ansatzf.to_edge(UP).shift(RIGHT*2.1 + DOWN*0.8)
        self.wait()
        self.play(Write(bk))
        self.play(Write(bkformula))
        self.wait(2)
        self.play(Write(ansatz))
        self.play(Write(ansatzf))
        self.wait()
        self.play(Write(bkf0))
        self.play(FadeOut(texts),bkf0.animate.to_edge(DOWN),Write(gstuff),Write(txstuff),run_time=1)
        self.wait(3)
        self.play(Unwrite(gstuff),Unwrite(txstuff),bkf0.animate.move_to([0,-1,0]),run_time=1)
        self.wait()

        #x^2 nach rechts umstellen
        self.play(Circumscribe(bkf0[2][2:4]))
        self.play(Indicate(bkf0[2][2:4]))
        self.play(TransformMatchingShapes(bkf0.copy(),bkf1))
        self.play(Circumscribe(bkf1[2][14:16]))
        self.play(Indicate(bkf1[2][14:16]))
        self.play(Unwrite(bkf0))
        self.play(bkf1.animate.shift(DOWN*2))
        self.wait(2)

        #x ausklammern
        self.play(Circumscribe(bkf1[2][14:16]))
        self.play(Indicate(bkf1[2][14:16]))
        self.play(Circumscribe(bkf1[1][6:7]))
        self.play(Indicate(bkf1[1][6:7]))
        self.play(TransformMatchingShapes(bkf1.copy(),bkf2))
        self.play(Circumscribe(bkf2[1][0:1]))
        self.play(Indicate(bkf2[1][0:1]))
        self.play(Indicate(bkf1[1]),run_time=2)
        self.play(Indicate(bkf2[3]),run_time=2)
        self.wait()
        self.play(Indicate(bkf1[2]),run_time=2)
        self.play(Indicate(bkf2[4][0:15]),run_time=2)
        self.play(Unwrite(bkf1))
        self.play(bkf2.animate.shift(DOWN*2),run_time=2)
        self.wait(4)

        #Satz vom Nullprodukt
        self.play(Write(svn))
        self.wait(3)
        self.play(Write(svntxt.next_to(svn,DOWN).to_edge(LEFT)))
        self.play(Write(svntxt2.next_to(svntxt,DOWN).to_edge(LEFT)))
        self.wait()
        self.play(FadeOut(svntxt),FadeOut(svntxt2))

        self.play(Indicate(bkf2[0:2]))
        self.play(TransformMatchingShapes(bkf2[0:2][0:2].copy(),svnf1))
        self.play(Indicate(bkf2[3:5]))
        self.play(TransformMatchingShapes(bkf2[3:6].copy(),svnf2))
        self.play(Unwrite(bkf2))
        self.wait()

        #graph reference
        ax = Axes(x_range=[0,9,1],x_length=9,y_range=[0,5,1],y_length=5)
        graph1 = ax.plot(lambda x: -0.198*(x-4.5)**2 + 4).set_color(YELLOW)
        labely = MathTex(r"y").align_to(ax,UL).shift(RIGHT*0.5)
        laabelx = MathTex(r"x").align_to(ax,DR).shift(UP*0.5+RIGHT*0.1)
        xoff = 4.5
        yoff = 1.5
        object = Dot(radius=0.15,color=YELLOW)
        vec = Vector(color=YELLOW).move_to(object).shift(DOWN)
        x = ValueTracker(-4.5)
        R = MathTex(r"R",r"=")
        R[0].set_color(YELLOW)
        rval = DecimalNumber(0,num_decimal_places=2)
        graphstuff = VGroup(ax,graph1,labely,laabelx)

        object.add_updater(lambda mob: mob.set_x(x.get_value()).set_y(-0.198*(x.get_value()-4.5+xoff)**2 + 4-yoff))
        vec.add_updater(lambda mob: mob.move_to(object).set_angle(np.atan(-0.396*(x.get_value()-0))).shift(0.5*RIGHT*np.cos(vec.get_angle())+0.5* UP*np.sin(vec.get_angle())))
        R.add_updater(lambda mob: mob.next_to(object,0.3*DR))
        rval.add_updater(lambda mob: mob.set_value(x.get_value()+4.5).next_to(R,RIGHT))

        self.play(AnimationGroup(
        svnf1.animate.to_edge(RIGHT),
        svnf2.animate.to_edge(RIGHT),
        Unwrite(svn),
        lag_ratio=0.3
        ))
        self.play(Write(graphstuff))
        self.play(svnf2.animate.shift(DOWN*4.5),graphstuff.animate.shift(UP))
        self.play(svnf1.animate.shift(DOWN*5.3 + LEFT*10.5))
        self.wait()
        self.play(Indicate(svnf1))
        self.play(AnimationGroup(FocusOn([-4.5,-1.5,0]),FocusOn([-4.5,-1.5,0]),lag_ratio=0.2),run_time=1.4)
        self.wait()
        self.play(Indicate(svnf2))
        self.play(AnimationGroup(FocusOn([4.5,-1.5,0]),FocusOn([4.5,-1.5,0]),lag_ratio=0.2),run_time=1.4)
        self.wait()
        self.play(FadeToColor(graph1,color=WHITE))
        self.add(object,vec,R,rval)
        self.play(x.animate.set_value(4.5),rate_func=linear,run_time=11)
        self.remove(vec,object,R,rval)
        bkf4.move_to(svnf2).shift(LEFT)
        self.play(Unwrite(graphstuff),Unwrite(svnf1),TransformMatchingShapes(svnf2,bkf4))
        self.play(bkf4.animate.move_to([0,0,0]))
        self.wait()

        #a solve for x unsimplified
        def connectpoints(l1,p1,p2):
            dx = p1.get_x() - p2.get_x()
            xmid = (p1.get_x() + p2.get_x())/2
            ymid = (p1.get_y() + p2.get_y())/2
            scalefactor = dx/np.sqrt(2)
            yoffset = scalefactor * (2-np.sqrt(2))/4
            l1.move_to([xmid,ymid + yoffset,0])
            l1.scale(scalefactor)

        q1 = Dot([0,0,0])
        q2 = Dot([0,0,0])
        l2 = Arc(angle=PI/2).rotate(PI/4)

        q1.set_x(bkf4[3].get_x())
        q2.set_x(-3.9)
        connectpoints(l2,q1,q2)

        self.add(bkf4)
        self.play(Indicate(bkf4[2:4]))
        self.play(MoveAlongPath(bkf4[3],l2),bkf4[0].animate.set_opacity(0),bkf4[2][0].animate.set_opacity(0),run_time=2)
        self.wait()
        bkf5[2].set_opacity(0)
        bkf5.shift(LEFT*2.3)
        self.play(TransformMatchingShapes(bkf4,bkf5))
        self.play(Indicate(bkf5[0]))
        self.wait()

        q1.set_x(bkf5[0].get_x())
        q2.set_x(1.5)
        l2 = Arc(angle=PI/2).rotate(PI/4)
        connectpoints(l2,q1,q2)
        self.play(MoveAlongPath(bkf5[0],l2),bkf5[2].animate.set_opacity(1),run_time=2)
        self.wait(4)

        self.play(Circumscribe(bkf5[2]))
        self.play(Circumscribe(bkf5[0]))
        self.play(TransformMatchingShapes(bkf5,bkf6))
        self.play(Circumscribe(bkf6[2][0]))
        self.play(Circumscribe(bkf6[2][1:]))

        # simplify trigs
        self.wait()
        self.play(Circumscribe(bkf6[2][5:12]))
        self.play(TransformMatchingShapes(bkf6,bkf7))
        self.wait(2)
        self.play(Circumscribe(bkf7[1][7:14]))
        self.wait(3)
        self.play(TransformMatchingShapes(bkf7,bkf8))
        self.wait(3)
        self.play(Circumscribe(bkf8[1][0:6]))
        self.wait(2)
        self.play(TransformMatchingShapes(bkf8,bkf9))
        self.wait(4)
        self.play(TransformMatchingShapes(bkf9,bkf10))
        self.wait(1)
        self.play(Indicate(bkf10[1][7:14]),Indicate(bkf10[1][15:21]),run_time=2)
        self.wait(1)
        self.play(TransformMatchingShapes(bkf10,bkf11))
        self.wait(5)
        self.play(bkf11.animate.to_corner(UR))
        self.wait()
        self.play(Write(dai.shift(UP)))
        self.play(Write(dai1.shift(UP*0)))
        dai2.set_opacity(0).move_to(dai1)
        self.wait(7)
        self.play(dai2.animate.shift(DOWN).set_opacity(1))
        self.play(AnimationGroup(
            dai.animate.to_edge(LEFT),
            dai1.animate.to_edge(LEFT),
            dai2.animate.to_edge(LEFT),
            lag_ratio=0.3
        ))
        self.play(FadeToColor(dai,color=WHITE))
        self.play(bkf11.animate.shift(DOWN*3 + LEFT*0.7))
        bkf12.move_to(bkf11)
        bkf12[1].set_opacity(0)

        box1 = SurroundingRectangle(bkf11[1], color=YELLOW)
        box2 = SurroundingRectangle(dai2[2], color=YELLOW)
        self.play(DrawBorderThenFill(box1))
        self.play(DrawBorderThenFill(box2))
        self.play(TransformMatchingShapes(bkf11,bkf12),FadeOut(box1),FadeOut(box2))
        self.play(AnimationGroup(
            TransformMatchingShapes(dai2[1].copy(),bkf12[1]),
            bkf12[1].animate.set_opacity(1),
            lag_ratio=0.3
        ),run_time=3)
        self.play(Unwrite(dai),Unwrite(dai1),Unwrite(dai2))
        self.play(bkf12.animate.move_to([0,0,0]))
        self.play(Indicate(bkf12[1][0:3]),Indicate(bkf12[2][1]),run_time=2)
        self.play(TransformMatchingShapes(bkf12,bkf13))
        self.wait(2)
        bkf14.shift(UP*2).scale(1.3)
        self.play(AnimationGroup(bkf13.animate.shift(DOWN*2).set_opacity(0),FadeIn(bkf14),bkf14.animate.move_to([0,0,0]).scale(1)),run_time=2)
        self.wait(4)
        self.play(FadeOut(bkf14))
        self.wait()





class Aber(Scene):
    def construct(self):
        self.add_sound(sound_file="MusicAber.wav",time_offset=2)
        
        aber = Tex("aber  ",".",".",".").scale(3).shift(LEFT*0.2)
        aber[1:].scale(2)

        #hinterfragen, andere möglichkeiten
        self.wait()
        self.play(FadeIn(aber[0]),rate_func=linear)
        self.play(DrawBorderThenFill(aber[1]))
        self.play(DrawBorderThenFill(aber[2]))
        self.play(DrawBorderThenFill(aber[3]))
        self.wait(2)
        self.play(FadeOut(aber),run_time=2)

        ax1 = Axes(x_range=[0,6,1],x_length=6,y_range=(0,5,1),y_length=4).shift(RIGHT*-3.5 +DOWN*1.5)
        plot1 = ax1.plot(lambda x: -0.45*(x-3)**2+4).set_color(YELLOW)
        ax2 = Axes(x_range=[0,6,1],x_length=6,y_range=(0,5,1),y_length=4).shift(RIGHT*3.5 +DOWN*1.5)
        plot2 = ax2.plot(lambda x: 0.5*x).set_color(YELLOW)
        label2x = MathTex(r"x").align_to(ax2,UL).shift(UP*0.5)
        label2t = MathTex(r"t").align_to(ax2,DR).shift(UP*0.5)
        label1y = MathTex(r"y").align_to(ax1,UL).shift(UP*0.5)
        label1t = MathTex(r"t").align_to(ax1,DR).shift(UP*0.5)

        xtformula = MathTex(r"x",r"(t)=",r"v_{0}cos(\theta)",r"t").align_to(label2x,LEFT).set_y(2.5)
        xtformula[0].set_color(RED)
        xtformula[2].set_color(RED)

        ytformula = MathTex(r"y",r"(t)=",r"v_{0}sin(\theta)",r"t-\frac{1}{2}gt^{2}").align_to(label1y,LEFT).set_y(2.5)
        ytf0 = MathTex(r"0",r"=",r"v_{0}sin(\theta)",r"t-\frac{1}{2}gt^{2}").move_to([-0.5,1.5,0])
        ytformula[0].set_color(GREEN)
        ytformula[2].set_color(GREEN)
        ytf0[2].set_color(GREEN)
        yt1t2 = MathTex(r"t=0\vee t=",r"\frac{2v_{0}}{g}sin(\theta )").move_to([-0.5,0.5,0])
        yt1t2[1][1:3].set_color(GREEN)
        yt1t2[1][5:].set_color(GREEN)

        graph = VGroup(ax1,ax2,plot1,plot2,label2x,label1t,label1y,label2t,xtformula,ytformula)
        yelements = VGroup(ax1,plot1,ytformula,label1t,label1y)
        xelements = VGroup(ax2,plot2,xtformula,label2t,label2x)
        ygraph = VGroup(ax1,plot1,label1t,label1y)
        xgraph = VGroup(ax2,plot2,label2t,label2x)
        ansatz = Tex("Ansatz",":")
        ansatz[0].set_color(YELLOW)
        ansatz2 = MathTex(r"y(t)=0").next_to(ansatz,DOWN).align_to(LEFT)
        ansatztxt = VGroup(ansatz,ansatz2)
        ansatz2[0][0].set_color(GREEN)
        nullpr = Tex("Nullprodukt").set_color(YELLOW).move_to([4.4,1.5,0])
        einsetzen = Tex("Einsetzen").set_color(YELLOW).move_to([4.4,0.5,0])
        vereinfach = Tex("Vereinfachen").set_color(YELLOW).move_to([4.4,2.5,0])
        dai = Tex("Doppelwinkelidentität").set_color(YELLOW).move_to([4.4,1.5,0])

        xt1 = MathTex(r"x(t)=",r"v_{0}cos(\theta )",r"(",r"\frac{2v_{0}}{g}sin(\theta ))")
        xt1[1].set_color(RED)
        xt1[3][1:3].set_color(GREEN)
        xt1[3][5:11].set_color(GREEN)
        xt2 = MathTex(r"R",r"=\frac{2v_{0}^{2}}{g}sin(\theta )cos(\theta)")
        xt2[0].set_color(YELLOW)
        xt3 = MathTex(r"R",r"=\frac{2v_{0}^{2}}{g}sin(2\theta )")
        xt3[0].set_color(YELLOW)
        hoch = Tex("Höhe von 0 nach der Zeit t").shift(UP*0.5 + RIGHT*3)
        vechoch = Vector([0,-3],color=YELLOW).shift(RIGHT*3)
        indi = VGroup(hoch,vechoch)

        #idee setzen, weg anzeigen
        self.play(Write(xelements),run_time=4)
        self.play(Write(yelements),run_time=4)
        self.wait(4)
        self.play(FadeOut(xelements),run_time=2)
        self.play(yelements.animate.shift(RIGHT*3.5),run_time=2)
        self.wait()
        self.play(AnimationGroup(FocusOn([3,-3.5,0]),FocusOn([3,-3.5,0]),lag_ratio=0.2),run_time=2)
        self.wait()
        self.play(FadeIn(indi))
        self.wait(2)
        self.play(FadeOut(indi))
        self.wait()
        self.play(ygraph.animate.to_edge(LEFT))
        self.wait(2)
        self.play(FadeIn(ansatztxt.next_to(ytformula,RIGHT,buff=1)))
        self.wait(3)
        self.play(FadeTransform(ytformula,ytf0),FadeTransform(ansatztxt,nullpr),run_time=2)
        self.wait(3)
        self.play(FadeTransform(ytf0,yt1t2),FadeTransform(nullpr,einsetzen),run_time=2)
        self.wait()

        #schema weiterführen
        xelements.move_to(ygraph).shift(UP*0.8)
        self.play(FadeTransform(ygraph,xelements))
        self.wait(4)
        xt1.move_to(xtformula).shift(RIGHT*4.5)
        self.play(yt1t2.animate.shift(UP*2).set_opacity(0),FadeTransform(xtformula,xt1),FadeTransform(einsetzen,vereinfach))
        self.wait(3)
        xt2.move_to(xt1).set_y(1.5).shift(LEFT*0.7)
        self.play(FadeTransform(xt1,xt2),FadeTransform(vereinfach,dai))
        self.wait()
        xt3.move_to(xt2).set_y(0.5)
        self.play(FadeTransform(xt2,xt3),dai.animate.shift(DOWN).set_opacity(0))
        self.wait(2)
        self.play(xgraph.animate.set_opacity(0),xt3.animate.move_to([0,0,0]).scale(2))
        self.wait(2)
        self.play(FadeOut(xt3))
        self.wait()





class VisualEnding(Scene):
    def construct(self):
        
        #show results
        bkf14 = MathTex(r"R=", r"\frac{v_{0}^{2}}{g}", r"sin(2 \theta)")
        self.wait()
        self.add(bkf14)

        ax2 = Axes(x_range=[0,13,1],x_length=13,y_range=[0,7,1],y_length=7)
        axl1 = MathTex(r"y").align_to(ax2,UL).shift(RIGHT*0.5)
        axl2 = MathTex(r"x").align_to(ax2,DR).shift(UP*0.5)

        theta = ValueTracker(0.7)
        g = 9.81
        v0 = ValueTracker(11)
        rval = DecimalNumber(0,num_decimal_places=2)
        rval.add_updater(lambda mob: mob.set_value(v0.get_value()**2/g *np.sin(2*theta.get_value())).next_to(label,RIGHT,buff=0.1))
        v0val = DecimalNumber(0,num_decimal_places=1).scale(1.3)
        v0val.add_updater(lambda mob: mob.next_to(v0txt,RIGHT,buff=0.2).set_value(v0.get_value()))
        thetaval = DecimalNumber(0,num_decimal_places=1).scale(1.3)
        thetaval.add_updater(lambda mob: mob.next_to(v0theta,RIGHT,buff=0.2).set_value(theta.get_value()))

        f1 = ax2.plot(lambda x: 0)
        f1.add_updater(lambda mob: mob.become(ax2.plot(
            lambda x: np.tan(theta.get_value())*x - (g * x**2)/(2*v0.get_value()**2 * np.cos(theta.get_value())**2))))

        pointer = Vector(DOWN).set_y(-2.5)
        pointer.add_updater(lambda mob: mob.set_x(((v0.get_value()**2/g *np.sin(2*theta.get_value()))-6.5)))
        label = MathTex(r"R",r"=").add_updater(lambda m: m.next_to(pointer, UP).shift(LEFT*0.5))
        label[0].set_color(YELLOW)

        v0vector = Vector([5,0],color=YELLOW).align_to(ax2,DL).shift(UP*0.2+RIGHT*0.2)
        v0vector.add_updater(
            lambda mob: mob.set_angle((theta.get_value())).set_length(0.5*v0.get_value()).align_to(ax2,DL).shift(UP*0.2+RIGHT*0.2))
        
        v0angle = Arc(start_angle=0)
        v0angle.add_updater(lambda mob: mob.become(Arc(color=YELLOW,angle=theta.get_value(),radius=0.5*v0vector.get_length()).shift(6.5*LEFT+3.5*DOWN)))

        v0theta = MathTex(r"\theta=").scale(1.3)
        v0theta.add_updater(
            lambda mob: mob.set_x(0.6*v0vector.get_length()*np.cos(0.5*theta.get_value())).set_y(0.6*v0vector.get_length()*np.sin(0.5*theta.get_value())).shift(6*LEFT+3.5*DOWN))

        v0txt = MathTex(r"v_{0} =").scale(1.3)
        v0txt.add_updater(
            lambda mob: mob.move_to(v0vector).shift(0.6*UP*np.sin(theta.get_value())*v0vector.get_length() +0.6*RIGHT*np.cos(theta.get_value())*v0vector.get_length()))

        self.play(bkf14.animate.to_corner(UR))

        self.play(Write(ax2),Write(axl1),Write(axl2),Write(f1))
        self.play(Write(v0vector),Write(v0angle),Write(v0txt),Write(v0theta),Write(v0val),Write(thetaval))
        self.play(Write(pointer),Write(label),Write(rval))
        self.play(theta.animate.set_value(1.5))
        self.play(v0.animate.set_value(5))

class quellen(Scene):
    def construct(self):
        self.add_sound(sound_file="MusicAber.wav")
        self.wait(10)


class zusammenfassung(Scene):
    def construct(self):
        a=1