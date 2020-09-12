from manimlib.imports import *


class a1_Hareket_Denklemleri(Scene):
    def construct(self):
    
        baslik = TextMobject ("Sabit ivmeli hareket denklemleri", color=BLUE)
    
# Denklem Tanımları

        d1_en=TexMobject(
            r"v_f",         #0  
            r"=",           #1
            r"v_i",         #2
            "+",            #3
            "a",            #4
            "t"             #5
            )

        d1_tr=TexMobject(
            r"v_{son}",     #0  
            r"=",           #1
            r"v_0",         #2
            "+",            #3
            "a",            #4
            "t"             #5
            )
    

        d2_en=TexMobject(
            "\\Delta{x}",   #0
            "=",            #1
            "{v_{f}",       #2
            "+",            #3
            "v_i",          #4
            "\\over"        #5
            "2}",           #6
            "t"             #7
            )

        d2_tr=TexMobject(
            "\\Delta{x}",   #0
            "=",            #1
            "{v_{son}",     #2
            "+",            #3
            "v_0",          #4
            "\\over"        #5
            "2}",           #6
            "t"             #7
            )

        d3_en=TexMobject(
            "\\Delta{x}",   #0
            "=",            #1
            "v_i",          #2
            "t",            #3
            "+",            #4
            "{1",           #5
            "\\over",       #6
            "2}",           #7
            "a",            #8
            "t^2"           #9
            )

        d3_tr=TexMobject(
            "\\Delta{x}",   #0
            "=",            #1
            "v_0",          #2
            "t",            #3
            "+",            #4
            "{1",           #5
            "\\over",       #6
            "2}",           #7
            "a",            #8
            "t^2"           #9
            )

        d4_en=TexMobject(
            "v_f",          #0       
            "^2",           #1
            "=",            #2
            "v_i",          #3
            "^2",           #4
            "+",            #5
            "2",            #6
            "a",            #7
            "\\Delta{x}"    #8
            )
        d4_tr=TexMobject(
            "v_{son}",      #0       
            "^2",           #1
            "=",            #2
            "v_0",          #3
            "^2",           #4
            "+",            #5
            "2",            #6
            "a",            #7
            "\\Delta{x}"    #8
            )


# Satırları sırala
        baslik.to_edge(UP)

        d1_en.next_to(baslik, 3*DOWN)
        d2_en.next_to(d1_en, 3*DOWN)
        d3_en.next_to(d2_en, 3*DOWN)
        d4_en.next_to(d3_en, 3*DOWN)        
        d1_tr.next_to(baslik, 3*DOWN)
        d2_tr.next_to(d1_en, 3*DOWN)
        d3_tr.next_to(d2_en, 3*DOWN)
        d4_tr.next_to(d3_en, 3*DOWN)

#Animasyonları oynat
        self.play(Write(baslik))
        self.wait(6)

        self.play(Write(d1_en))
        self.play(Write(d2_en))
        self.play(Write(d3_en))
        self.play(Write(d4_en))

        self.wait(3)


        # d1_tr[0].set_color(YELLOW)
        # d1_tr[2].set_color(YELLOW)
        # d2_tr[2].set_color(YELLOW)
        # d2_tr[4].set_color(YELLOW)
        # d3_tr[2].set_color(YELLOW)
        # d4_tr[0].set_color(YELLOW)
        # d4_tr[3].set_color(YELLOW)
     


        self.play(Transform (d1_en,d1_tr))
        

        self.play(Transform (d2_en,d2_tr))
        

        self.play(Transform (d3_en,d3_tr))

        self.play(Transform (d4_en,d4_tr))
        


        self.wait(35)

        denk_group = VGroup(baslik, d1_tr, d2_tr, d3_tr, d4_tr, d1_en, d2_en, d3_en, d4_en)

        self.play(FadeOut(denk_group))
        self.wait()



class a2_Ek_Sahne_2(Scene):

    def construct(self):

        self.wait(1)

        START = (-3,2.5,0)
        END =   (3,2.5,0)
        arrow = Arrow(START,END, color=RED)

        a= TexMobject("a")
        x = TexMobject("x")

        x.next_to(arrow, RIGHT)
        a.next_to(arrow, UP)

        self.play(ShowCreation(arrow))
        self.play(Write(a))
        self.play(Write(x))        


        self.wait(5)

       
        self.play(
            Uncreate(arrow),
            Uncreate(a),
            Uncreate(x)
            )



        d3_example_x=TexMobject(
            "\\Delta{x}",   #0
            "=",            #1
            "v_{0x}",          #2
            "t",            #3
            "+",            #4
            "{1",           #5
            "\\over",       #6
            "2}",           #7
            "a_x",            #8
            "t^2",           #9
            color=GREEN
            )

       

        d3_example_y=TexMobject(
            "\\Delta{y}",   #0
            "=",            #1
            "v_{0y}",          #2
            "t",            #3
            "+",            #4
            "{1",           #5
            "\\over",       #6
            "2}",           #7
            "a_y",            #8
            "t^2",           #9
            color=TEAL
            )

        

        d3_example_z=TexMobject(
            "\\Delta{z}",   #0
            "=",            #1
            "v_{0z}",          #2
            "t",            #3
            "+",            #4
            "{1",           #5
            "\\over",       #6
            "2}",           #7
            "a_z",            #8
            "t^2",           #9
            color=BLUE

            )


        d3_example_x.next_to(d3_example_y, UP)
        d3_example_z.next_to(d3_example_y, DOWN)

        self.play(Write(d3_example_x))
        self.play(Write(d3_example_y))
        self.play(Write(d3_example_z))


        self.wait(15)

        self.play(
            Uncreate(d3_example_x),
            Uncreate(d3_example_y),
            Uncreate(d3_example_z)

            )





# Grafikleri 1


class b_Denklem_1(GraphScene):
    CONFIG = {
        "x_axis_label": "",
        "y_axis_label": "",
        "y_max" : 100,
        "y_min" : 0,
        "x_max" : 10,
        "x_min" : 0,
        "y_tick_frequency" : 20,
        "x_tick_frequency" : 2,
        "x_axis_width": 5,
        "y_axis_height": 5,
        "axes_color" : GRAY, 
    }

    def construct(self):
        self.graph_origin = 2.5   * DOWN + 6 * LEFT
        self.setup_axes(animate=True)
        accel_graph = self.get_graph(lambda x : 50, 
                                    color = GOLD_A,
                                    x_min = 0, 
                                    x_max = 8
                                    )
        
        self.graph_origin = 2.5 * DOWN + 1 * RIGHT
        self.setup_axes(animate=True)
        velo_graph = self.get_graph(lambda x : 5*x + 20, 
                                    color = BLUE_D,
                                    x_min = 0, 
                                    x_max = 8
                                    )
                                     
        label_a = TexMobject(r"a (m/s^2)")
        label_a.move_to(5.6*LEFT + 3 *UP)
  
        label_v = TexMobject(r"\upsilon (m/s)")
        label_v.move_to(1.4*RIGHT+ 3 *UP)
        label_t_a = TexMobject(r"t(s)")
        label_t_a.move_to(3   * DOWN + 1 * LEFT)
        label_t_v = TexMobject(r"t(s)")
        label_t_v.move_to(3   * DOWN + 6 * RIGHT)

        self.play(Write(label_a))
        self.play(Write(label_t_a))

        self.play(Write(label_v))
        self.play(Write(label_t_v))
        self.wait(8)

        label_at_t_0= TexMobject("0", color=YELLOW)
        label_at_t_0.move_to((3*DOWN + 6*LEFT))
       
        label_vt_t_0= TexMobject("0", color=YELLOW)
        label_vt_t_0.move_to((3*DOWN + 1*RIGHT))
       
        label_0_group = VGroup(label_at_t_0, label_vt_t_0)
        self.play(Write(label_0_group))

        self.wait(5)


        label_at_t= TexMobject("t", color=YELLOW)
        label_at_t.move_to((3*DOWN + 2*LEFT))
     
        label_vt_t= TexMobject("t", color=YELLOW)
        label_vt_t.move_to((3*DOWN + 5*RIGHT))
     
        label_t_group= VGroup(label_at_t, label_vt_t)      

        self.play(Write(label_t_group))
        self.wait(5)


        self.play(ShowCreation(accel_graph),run_time = 2,)
        self.wait(5)

        self.wait(4)

        label_v_0 = TexMobject(r"\upsilon_0", color=YELLOW)
        label_v_0.move_to(0.5*RIGHT+ 1.5 *DOWN)

        self.wait(5)

        self.play(Write(label_v_0))
        self.wait(3)


        self.play(ShowCreation(velo_graph),run_time = 2,)

        label_v_son = TexMobject(r"\upsilon_{son}", color=YELLOW)
        label_v_son.move_to(0.4*RIGHT+ 0.5*UP)

        START = (5,0.5,0)
        END =   (5,-2.5,0)
        line = DashedLine(START,END, color=RED)
        self.play(ShowCreation(line))

        

        self.wait(5)
        
        START2 = (5,0.5,0)
        END2 =   (1,0.5,0)
        line2 = DashedLine(START2,END2, color=RED)

        START2_1 = (5,-1.5,0)
        END2_1 =   (1,-1.5,0)
        line2_1 = DashedLine(START2_1,END2_1, color=RED)
        
        self.play(ShowCreation(line2))


        START3 = (5,0.5,0)
        END3 =   (5,-1.5,0)
        line3 = DashedLine(START3,END3, color=RED)



        self.play(Write(label_v_son))
        self.wait(10)

        self.play(TransformFromCopy(line2, line2_1))
        line2_1.set_color(TEAL)
        line2.set_color(GRAY)
        self.play(TransformFromCopy(line, line3))
        line3.set_color(TEAL)
        line.set_color(GRAY)
        self.wait(1)

        angle = math.radians(20)
        arc =  Arc(radius=1,angle=angle, color=RED)
        arc.move_to(1.335*DOWN + 1.7*RIGHT)
        self.play(ShowCreation(arc))
        sign_theta = TexMobject(r"\theta", color=RED)
        sign_theta.move_to(2.04*RIGHT + 1.25*DOWN)
        self.play(Write(sign_theta))


        self.wait(5)
        
        ivme_group = VGroup(label_at_t, label_a, label_at_t_0, label_t_a, accel_graph)
        velo_group = VGroup(label_v, label_v_0, label_v_son, label_t_v, label_vt_t_0, label_vt_t, velo_graph, arc, sign_theta, line, line2, line2_1, line3)
        

        line_group=VGroup(line, line2)
        # self.play(Uncreate(line_group))

        self.play(Uncreate(ivme_group))
       
       
        animation = ApplyMethod(velo_group.shift, 7*LEFT)
        self.play(animation)

        self.play(FadeOut(self.axes))



        self.wait(2)


# 1. Denklem

        delta_v_brace=Brace(line3,RIGHT)
        delta_v_text = TexMobject(r"\Delta{\upsilon}")
        delta_v_text.move_to(1*LEFT + 0.5*DOWN)


        delta_t_brace=Brace(line2_1, DOWN)
        delta_t_text = TexMobject(r"\Delta{t}")
        delta_t_text.move_to(4*LEFT + 2.2*DOWN)

       

        self.play(GrowFromCenter(delta_v_brace))
        self.wait(1)

        self.play(Write(delta_v_text))
        self.wait(1)
        self.play(GrowFromCenter(delta_t_brace))
        self.wait(1)
        self.play(Write(delta_t_text))
        self.wait(3)



    
        denklem_1a = TexMobject(
            r"a",               #0
            "=",                #1
            "{{{\Delta{v}}",    #2
            "\\over",           #3
            "{\Delta{t}}}",     #4
            "=",                #5
            "{\\upsilon_{son}", #6
            "-",                #7
            "\\upsilon_0",      #8
            "\\over",           #9
            "t",                #10
            "-",                #11
            "0}")               #12
        # text[0].set_color(RED)
        # text[1].set_color(BLUE)
        # text[2].set_color(GREEN)
        # text[3].set_color(ORANGE)
        # text[4].set_color("#DC28E2")
        denklem_1a.to_edge(UR)
        denklem_1a.shift(LEFT)
        denklem_1a.shift(0.5*DOWN)
       
        self.play(Write(denklem_1a[0]))
        self.play(Write(denklem_1a[1]))
        
        self.play(Write(denklem_1a[3]))
           

        self.play(ReplacementTransform(delta_v_text.copy(), denklem_1a[2]))
        self.play(ReplacementTransform(delta_t_text.copy(), denklem_1a[4]))
        self.wait(3)

        self.play(Write(denklem_1a[5]))
        self.play(Write(denklem_1a[9]))

        self.play(ReplacementTransform(label_v_son.copy(), denklem_1a[6]))  
        self.play(Write(denklem_1a[7]))  
        self.play(ReplacementTransform(label_v_0.copy(), denklem_1a[8]))
        self.wait(1)    
        self.play(ReplacementTransform(label_vt_t.copy(), denklem_1a[10])) 
        self.play(Write(denklem_1a[11]))  
        self.play(ReplacementTransform(label_vt_t_0.copy(), denklem_1a[12]))   

  
        self.wait(1)

        denklem_1b = TexMobject(
            r"a",               #0
            "=",                #1
            "{{{\Delta{v}}",    #2
            "\\over",           #3
            "{\Delta{t}}}",     #4
            "=",                #5
            "{\\upsilon_{son}", #6
            "-",                #7
            "\\upsilon_0",      #8
            "\\over",           #9
            "t}")               #10
        denklem_1b.to_edge(UR)
        denklem_1b.shift(LEFT)
        denklem_1b.shift(0.5*DOWN)


        self.play(Transform(denklem_1a[10:13], denklem_1b[10]))

        self.wait(5)

        denklem_1c = TexMobject(
            r"a",               #0
            "=",                #1
            "{\\upsilon_{son}", #2
            "-",                #3
            "\\upsilon_0",      #4
            "\\over",           #5
            "t}")               #6
        denklem_1c.next_to(denklem_1b, 3*DOWN)
        self.play(Transform(denklem_1b[0:2], denklem_1c[0:2]))
        self.play(Transform(denklem_1b[6:11], denklem_1c[2:7]))

        self.wait(3)

        denklem_1d = TexMobject(
            "a",                #0
            "t",                #1
            "=",                #2
            "{\\upsilon_{son}", #3
            "-",                #4
            "\\upsilon_0"       #5
            )
        denklem_1d.next_to(denklem_1c, 3*DOWN)

        self.play(ReplacementTransform(denklem_1c[0].copy(), denklem_1d[0]))
        self.play(ReplacementTransform(denklem_1c[6].copy(), denklem_1d[1]))
        self.play(ReplacementTransform(denklem_1c[1].copy(), denklem_1d[2])) 
        self.play(ReplacementTransform(denklem_1c[2].copy(), denklem_1d[3]))
        self.play(ReplacementTransform(denklem_1c[3].copy(), denklem_1d[4]))
        self.play(ReplacementTransform(denklem_1c[4].copy(), denklem_1d[5]))        

        self.wait(2)

        denklem_1e = TexMobject(
            "\\upsilon_0",                #0
            "+",                #1
            "at",                #2
            "=", #3
            "{\\upsilon_{son}",                #4
            )
        denklem_1e.next_to(denklem_1d, 3*DOWN)

        self.play(ReplacementTransform(denklem_1d[5].copy(), denklem_1e[0]))
        self.play(ReplacementTransform(denklem_1d[4].copy(), denklem_1e[1]))
        self.play(ReplacementTransform(denklem_1d[0:2].copy(), denklem_1e[2]))
        self.play(ReplacementTransform(denklem_1d[2].copy(), denklem_1e[3]))
        self.play(ReplacementTransform(denklem_1d[3].copy(), denklem_1e[4]))

        self.wait(1)


        denklem_1f = TexMobject(
            "{\\upsilon_{son}",         #0
            "=",                        #1
            "\\upsilon_0",              #2
            "+",                        #3
            "at",                       #4
            
            )
        denklem_1f.next_to(denklem_1e, 3*DOWN)

        self.play(ReplacementTransform(denklem_1e[4].copy(), denklem_1f[0]))
        self.play(ReplacementTransform(denklem_1e[3].copy(), denklem_1f[1]))
        self.play(ReplacementTransform(denklem_1e[0].copy(), denklem_1f[2]))
        self.play(ReplacementTransform(denklem_1e[1].copy(), denklem_1f[3]))
        self.play(ReplacementTransform(denklem_1e[2].copy(), denklem_1f[4]))


        self.play(FadeToColor(denklem_1f, RED))
        self.play(ScaleInPlace(denklem_1f, 1.5))

        self.wait(30)

# 2. Denklem


class c_Denklem_2(Scene):

    def construct(self):
        START = (-4,1,0)
        END =   (4,1,0)
        line = Line(START,END);
        self.play(ShowCreation(line))

        dot1 = Dot()
        dot2= Dot()
        dot1.move_to(1.5*UP + 3*LEFT)
        dot2.move_to(1.5*UP + 3*RIGHT)


        cisim = Square(side_length=1, color=RED)
        cisim.move_to(1.5*UP + 3*LEFT)
        cisim.set_fill(RED, opacity=0.1)
        self.play(
            ShowCreation(cisim),
            ShowCreation(dot1)
            )
        


        cisim_2 = Square(side_length=1, color=RED)
        cisim_2.move_to(1.5*UP + 3*RIGHT)
        cisim_2.set_fill(RED, opacity=0.1)

        cisim_v= TexMobject(r"\upsilon")
        cisim_v.next_to(cisim, LEFT)
        cisim_v2= TexMobject(r"\upsilon")
        cisim_v2.next_to(cisim_2, LEFT)



        t_0 = TexMobject("t=0")
        t_0.move_to(3*LEFT + 2.5*UP)

        t= TexMobject("t")
        t.move_to(3*RIGHT + 2.5*UP)


        x_0 = TexMobject ("x_0")
        x = TexMobject ("x")

        x_0.next_to(dot1, 2.5*DOWN)
        x.next_to(dot2, 2.5*DOWN)

        
        self.wait(10)
        
        self.play(Write(cisim_v))
        self.wait(2)

        self.play(Write(t_0))
        self.wait(1)


        self.play(Write(x_0))
        self.wait(5)
        


        self.play(
            ReplacementTransform(cisim.copy(), cisim_2),
            ReplacementTransform(dot1.copy(), dot2),
            ReplacementTransform(cisim_v.copy(), cisim_v2)
            )
       
        self.play(Write(t))
        self.wait(1)
        self.play(Write(x))
        self.wait(1)

        

        x_group = VGroup(x_0, x)
        dx_brace=Brace(x_group, DOWN)
        # dx_brace.next_to(line, DOWN)
        dx_text = TexMobject(
                        
            "x",            #0
            "-",            #1
            "x_0",          #2
            "=",            #3
            "\\Delta{x}"   #4
            )
       


        dx_text.next_to(dx_brace, DOWN)
        self.play(GrowFromCenter(dx_brace))
        self.wait(5)
        
        self.play(ReplacementTransform(x.copy(), dx_text[0]))
        self.play(Write(dx_text[1]))
        self.play(ReplacementTransform(x_0.copy(), dx_text[2]))
        self.wait(1)
        self.play(Write(dx_text[3:5]))

        self.wait(5)



        delta_x_denklemi_1 = TexMobject (
            "\\Delta{x}",       #0
            "=",                #1
            "v",        #2
            "\\Delta{t}",       #3

            )
        delta_x_denklemi_1.next_to(dx_text, 1.5*DOWN)

        self.play(ReplacementTransform(dx_text[4].copy(), delta_x_denklemi_1[0]))
        self.play(Write(delta_x_denklemi_1[1]))
        self.play(Write(delta_x_denklemi_1[2]))
        self.play(Write(delta_x_denklemi_1[3]))

        self.wait(1)

        delta_x_denklemi_2 = TexMobject (
            "\\Delta{x}",       #0
            "=",                #1
            "\\upsilon",        #2
            "t ",       #3
            )
        delta_x_denklemi_2.next_to(dx_text, 1.5*DOWN)

        self.play(
            ReplacementTransform(delta_x_denklemi_1[0], delta_x_denklemi_2[0]),
            ReplacementTransform(delta_x_denklemi_1[1], delta_x_denklemi_2[1]),
            ReplacementTransform(delta_x_denklemi_1[2], delta_x_denklemi_2[2]),
            ReplacementTransform(delta_x_denklemi_1[3], delta_x_denklemi_2[3])

            )

        self.wait(10)

        # delta_x_denklemi_3 kullanılmadı!!! #

        # delta_x_denklemi_3 = TexMobject (
        #     "\\Delta{x}",       #0
        #     "=",                #1
        #     r"\overline{\upsilon}",        #2
        #     "t ",       #3
        #     )
        # delta_x_denklemi_3.next_to(dx_text, DOWN)
        

        # v'leri v_0 v_son'a degistir

        v_0 = TexMobject ("v_0", color=YELLOW)
        v_son = TexMobject ("v_{son}", color=TEAL)
        v_0.next_to(cisim, LEFT)
        v_son.next_to(cisim_2, LEFT)

        self.wait(10)

        self.play(ReplacementTransform(cisim_v, v_0))
        scale_factors=[2,0.5]

        for scale_factor in scale_factors:
            self.play(ScaleInPlace(v_0, scale_factor))



        self.play(ReplacementTransform(cisim_v2,v_son))

        scale_factors=[2,0.5]

        for scale_factor in scale_factors:
            self.play(ScaleInPlace(v_son, scale_factor))
            
        self.wait(5)

        # v'yi v_ort'a donustur

        delta_x_denklemi_4 = TexMobject (
            "\\Delta{x}",       #0
            "=",                #1
            r"\upsilon_{ort}",        #2
            "t ",       #3
            )

        delta_x_denklemi_4[2].set_color(RED)
        delta_x_denklemi_4.next_to(dx_text, 1.5*DOWN)


        self.play(
            ReplacementTransform(delta_x_denklemi_2[0], delta_x_denklemi_4[0]),
            ReplacementTransform(delta_x_denklemi_2[1], delta_x_denklemi_4[1]),
            ReplacementTransform(delta_x_denklemi_2[2], delta_x_denklemi_4[2]),
            ReplacementTransform(delta_x_denklemi_2[3], delta_x_denklemi_4[3])

            )
        self.wait(10)


        denklem_2_final = TexMobject (
            "\\Delta{x}",       #0
            "=",                #1
            "\\left( ",                #2
            "{v_0",              #3
            "+",                #4
            "v_{son}",           #5
            "\\over",           #6
            "2}",               #7
            "\\right) " ,                #8
            "t"                 #9
            )

        denklem_2_final.next_to(delta_x_denklemi_4, 2*DOWN)


        self.play(ReplacementTransform(delta_x_denklemi_4[0].copy(), denklem_2_final[0]))
        self.play(ReplacementTransform(delta_x_denklemi_4[1].copy(), denklem_2_final[1]))
        self.wait(3)
        self.play(ReplacementTransform(v_0.copy(), denklem_2_final[3]))
        self.play(Write(denklem_2_final[4]))
        self.play(ReplacementTransform(v_son.copy(), denklem_2_final[5]))
        self.play(Write(denklem_2_final[6]))
        self.play(Write(denklem_2_final[7]))
        self.play(
            Write(denklem_2_final[2]), 
            Write(denklem_2_final[8]))
        self.wait(3)
        self.play(ReplacementTransform(delta_x_denklemi_4[3].copy(), denklem_2_final[9]))


        self.play(FadeToColor(denklem_2_final, RED))
        self.play(ScaleInPlace(denklem_2_final, 1.5))

        self.wait(30)


# 3. ve 4. Denklemlerin türetilmesi


class d_Denklem_3(Scene):

    def construct(self):

        d1_tr=TexMobject(
            r"v_{son}",     #0  
            r"=",           #1
            r"v_0",         #2
            "+",            #3
            "a",            #4
            "t"             #5
            )

        d2_tr=TexMobject(
            "\\Delta{x}",   #0
            "=",            #1
            "{v_{son}",     #2
            "+",            #3
            "v_0",          #4
            "\\over",       #5
            "2}",           #6
            "t"             #7
            )


        d1_to_d2 =TexMobject(
            "\\Delta{x}",   #0
            "=",            #1
            "{v_0",         #2
            "+",            #3
            "a",            #4
            "t",            #5
            "+",            #6
            "v_0",          #7
            "\\over",        #8
            "2}",           #9
            "t"             #10
            )

        d1_to_d2[2:6].set_color(YELLOW)

            


        d1_tr.to_edge(UP)
        d2_tr.next_to(d1_tr, 2*DOWN)
        d1_to_d2.next_to(d2_tr, 2*DOWN)

        self.play(Write(d1_tr))
        self.wait(2)
        self.play(FadeToColor(d1_tr[2:6], YELLOW))
        self.wait(7)


        self.play(Write(d2_tr))
        self.wait(8)
        self.play(FadeToColor(d2_tr[2], RED))
        self.wait(1)

        
        



        self.play(ReplacementTransform(d2_tr[0].copy(), d1_to_d2[0]))
        self.play(ReplacementTransform(d2_tr[1].copy(), d1_to_d2[1]))
        self.play(
            ReplacementTransform(d1_tr[2].copy(), d1_to_d2[2]),
            ReplacementTransform(d1_tr[3].copy(), d1_to_d2[3]),
            ReplacementTransform(d1_tr[4].copy(), d1_to_d2[4]),
            ReplacementTransform(d1_tr[5].copy(), d1_to_d2[5])
            )
        self.play(
            ReplacementTransform(d2_tr[3].copy(), d1_to_d2[6]),
            ReplacementTransform(d2_tr[4].copy(), d1_to_d2[7])
            )
        self.play(
            ReplacementTransform(d2_tr[5].copy(), d1_to_d2[8]),
            ReplacementTransform(d2_tr[6].copy(), d1_to_d2[9])
            )
        self.play(ReplacementTransform(d2_tr[7].copy(), d1_to_d2[10]))

        

        self.wait(1)



        d3_duzenle_1 = TexMobject(
            "\\Delta{x}",   #0
            "=",            #1
            "{2",           #2
            "v_0",          #3
            "+",            #4
            "a",            #5
            "t",            #6
            "\\over",       #7
            "2}",           #8
            "t"             #9

            )
        d3_duzenle_1.next_to(d1_to_d2, 2*DOWN)

        self.play(ReplacementTransform(d1_to_d2[0:2].copy(), d3_duzenle_1[0:2]))
        
        self.play(
            ReplacementTransform(d1_to_d2[2].copy(), d3_duzenle_1[3]),
            ReplacementTransform(d1_to_d2[7].copy(), d3_duzenle_1[3]),
            Write(d3_duzenle_1[2])
            )

        

        self.play(
            ReplacementTransform(d1_to_d2[3].copy(), d3_duzenle_1[4]),
            ReplacementTransform(d1_to_d2[4].copy(), d3_duzenle_1[5]),
            ReplacementTransform(d1_to_d2[5].copy(), d3_duzenle_1[6])
            )




        self.play(
            ReplacementTransform(d1_to_d2[8].copy(), d3_duzenle_1[7]),
            ReplacementTransform(d1_to_d2[9].copy(), d3_duzenle_1[8])
            )
        self.play(ReplacementTransform(d1_to_d2[10].copy(), d3_duzenle_1[9]))
        


        d3_tr=TexMobject(
            "\\Delta{x}",   #0
            "=",            #1
            "v_0",          #2
            "t",            #3
            "+",            #4
            "{1",           #5
            "\\over",       #6
            "2}",           #7
            "a",            #8
            "t",            #9
            "^2"            #10
            )

        d3_tr.next_to(d3_duzenle_1, 2* DOWN)


        self.play(ReplacementTransform(d3_duzenle_1[0:2].copy(), d3_tr[0:2]))
        self.play(
            ReplacementTransform(d3_duzenle_1[3].copy(), d3_tr[2]),
            ReplacementTransform(d3_duzenle_1[2].copy(), d3_tr[2]),
            ReplacementTransform(d3_duzenle_1[8].copy(), d3_tr[2]),
            ReplacementTransform(d3_duzenle_1[7].copy(), d3_tr[2]),
            ReplacementTransform(d3_duzenle_1[9].copy(), d3_tr[3]),
            ReplacementTransform(d3_duzenle_1[9].copy(), d3_tr[3])
                       

            )
        self.play(ReplacementTransform(d3_duzenle_1[4].copy(), d3_tr[4]))
        self.play(
            ReplacementTransform(d3_duzenle_1[5].copy(), d3_tr[5]),
            ReplacementTransform(d3_duzenle_1[7].copy(), d3_tr[6]),
            ReplacementTransform(d3_duzenle_1[8].copy(), d3_tr[7]),
            )

        self.play(
            ReplacementTransform(d3_duzenle_1[5].copy(), d3_tr[8]),
            ReplacementTransform(d3_duzenle_1[6].copy(), d3_tr[9])
            )

        self.play(ReplacementTransform(d3_duzenle_1[9].copy(), d3_tr[10]))

        self.play(FadeToColor(d3_tr, RED))
        self.play(ScaleInPlace(d3_tr, 1.5))

        self.wait(30)


class e_Denklem_4(Scene):

    def construct(self):

        d1_tr=TexMobject(
            r"v_{son}",     #0  
            r"=",           #1
            r"v_0",         #2
            "+",            #3
            "a",            #4
            "t"             #5
            )
        d2_tr=TexMobject(
            "\\Delta{x}",   #0
            "=",            #1
            "{v_{son}",     #2
            "+",            #3
            "v_0",          #4
            "\\over",       #5
            "2}",           #6
            "t"             #7
            )
        d3_tr=TexMobject(
            "\\Delta{x}",   #0
            "=",            #1
            "v_0",          #2
            "t",            #3
            "+",            #4
            "{1",           #5
            "\\over",       #6
            "2}",           #7
            "a",            #8
            "t",            #9
            "^2"            #10
            )
        d4_tr=TexMobject(
            "v_{son}",      #0       
            "^2",           #1
            "=",            #2
            "v_0",          #3
            "^2",           #4
            "+",            #5
            "2",            #6
            "a",            #7
            "\\Delta{x}"    #8
            )


        d1_tr.to_edge(UP)
        d2_tr.next_to(d1_tr, 3 * DOWN)
        d3_tr.next_to(d2_tr, 2 * DOWN)


        self.play(
            Write(d1_tr),
            Write(d2_tr),
            Write(d3_tr)
            )


        denk_1 = TexMobject ("1.", color=YELLOW)
        denk_2 = TexMobject ("2.", color=YELLOW)
        denk_3 = TexMobject ("3.", color=YELLOW)
        denk_4 = TexMobject ("4.", color=YELLOW)

        denk_1.move_to(1*DOWN + 3*LEFT)
        denk_2.move_to(1.5*DOWN + 3*LEFT)
        denk_3.move_to(2*DOWN + 3*LEFT)
        denk_4.move_to(2.5*DOWN + 3*LEFT)
        


#1. satır
        v_0 = TexMobject("v_0", color=GREEN)
        v_son = TexMobject("v_{son}", color=GREEN)
        acc = TexMobject("a", color=GREEN)
        time = TexMobject("t", color=GREEN)
        delta_x = TexMobject("\\Delta{x}", color=RED)

        self.play(Write(denk_1))
        v_0.move_to(1*DOWN + 2*LEFT)
        v_son.move_to(1*DOWN + 1*LEFT)
        acc.move_to(1*DOWN )
        time.move_to(1*DOWN + 1*RIGHT)
        delta_x.move_to(1*DOWN + 2*RIGHT)


        self.wait(1)
        self.play(ReplacementTransform(d1_tr[2].copy(), v_0))
        self.play(ReplacementTransform(d1_tr[0].copy(), v_son))
        self.play(ReplacementTransform(d1_tr[4].copy(), acc))
        self.play(ReplacementTransform(d1_tr[5].copy(), time))

        self.wait(1)
        self.play(Write(delta_x))

        grup1 = VGroup(denk_1, v_0, v_son, time, delta_x, acc)

#2. satır
        v_0 = TexMobject("v_0", color=GREEN)
        v_son = TexMobject("v_{son}", color=GREEN)
        acc = TexMobject("a", color=RED)
        time = TexMobject("t", color=GREEN)
        delta_x = TexMobject("\\Delta{x}", color=GREEN)


        self.wait(2)
        self.play(Write(denk_2))
        v_0.move_to(1.5*DOWN + 2*LEFT)
        v_son.move_to(1.5*DOWN + 1*LEFT)
        acc.move_to(1.5*DOWN )
        time.move_to(1.5*DOWN + 1*RIGHT)
        delta_x.move_to(1.5*DOWN + 2*RIGHT)
        self.wait(1)

        self.play(ReplacementTransform(d2_tr[4].copy(), v_0))
        self.play(ReplacementTransform(d2_tr[2].copy(), v_son))
        self.play(ReplacementTransform(d2_tr[7].copy(), time))
        self.play(ReplacementTransform(d2_tr[0].copy(), delta_x))
        self.wait(2)
        
        self.play(Write(acc))

        grup2 = VGroup(denk_2, v_0, v_son, time, delta_x, acc)

#3. satır       
        v_0 = TexMobject("v_0", color=GREEN)
        v_son = TexMobject("v_{son}", color=RED)
        acc = TexMobject("a", color=GREEN)
        time = TexMobject("t", color=GREEN)
        delta_x = TexMobject("\\Delta{x}", color=GREEN)


        self.wait(1)
        self.play(Write(denk_3))
        v_0.move_to(2*DOWN + 2*LEFT)
        v_son.move_to(2*DOWN + 1*LEFT)
        acc.move_to(2*DOWN )
        time.move_to(2*DOWN + 1*RIGHT)
        delta_x.move_to(2*DOWN + 2*RIGHT)
        self.wait(1)

        self.play(ReplacementTransform(d3_tr[2].copy(), v_0))
        self.play(ReplacementTransform(d3_tr[8].copy(), acc))
        self.play(ReplacementTransform(d3_tr[9].copy(), time))
        self.play(ReplacementTransform(d3_tr[0].copy(), delta_x))
        self.wait(1)
        self.play(Write(v_son))

        grup3 = VGroup(denk_3, v_0, v_son, time, delta_x, acc)

        self.wait(23)

#4. satır

        v_0 = TexMobject("v_0", color=GREEN)
        v_son = TexMobject("v_{son}", color=GREEN)
        acc = TexMobject("a", color=GREEN)
        time = TexMobject("t", color=RED)
        delta_x = TexMobject("\\Delta{x}", color=GREEN)

        self.play(Write(denk_4))
        v_0.move_to(2.5*DOWN + 2*LEFT)
        v_son.move_to(2.5*DOWN + 1*LEFT)
        acc.move_to(2.5*DOWN )
        time.move_to(2.5*DOWN + 1*RIGHT)
        delta_x.move_to(2.5*DOWN + 2*RIGHT)
        
        self.wait(1)

        self.play(Write(time))

        self.wait(5)
        self.play(Write(v_0))
        self.play(Write(v_son))
        self.play(Write(acc))
        self.play(Write(delta_x))

        grup4 = VGroup(denk_4, v_0, v_son, time, delta_x, acc)

        self.wait(2)

        self.play(
            Uncreate(d3_tr),
            Uncreate(grup1),
            Uncreate(grup2),
            Uncreate(grup3),
            Uncreate(grup4)
            )

        self.wait(11)



        self.play(
            FadeToColor(d1_tr[5], RED),
            FadeToColor(d2_tr[7], RED)
            )
        scale_factors=[2,0.5]

        for scale_factor in scale_factors:
            self.play(ScaleInPlace(d1_tr[5], scale_factor), ScaleInPlace(d2_tr[7], scale_factor))
            self.wait(0.3)

        
        self.wait(20)


        t_denk = TexMobject(
            "t",                 #0
            "=",                #1
            "{2",               #2
            "\\Delta{x}",       #3
            "\\over",           #4
            "{v_{son}",         #5
            "+",                #6
            "v_0}}"             #7
            
            
            )


        t_denk.next_to(d2_tr, DOWN)


        t_denk[0].set_color(RED)


        self.play(ReplacementTransform(d2_tr[7].copy(), t_denk[0]))
        self.play(ReplacementTransform(d2_tr[1].copy(), t_denk[1]))
        self.play(ReplacementTransform(d2_tr[6].copy(), t_denk[2]))
        self.play(ReplacementTransform(d2_tr[0].copy(), t_denk[3]))
        self.play(ReplacementTransform(d2_tr[5].copy(), t_denk[4]))
        self.play(ReplacementTransform(d2_tr[2:5].copy(), t_denk[5:8]))


        self.play(FadeToColor(t_denk[2:8], YELLOW))

        self.play(FadeToColor(d1_tr[5], YELLOW))
        scale_factors=[2,0.5]

        for scale_factor in scale_factors:
            self.play(ScaleInPlace(d1_tr[5], scale_factor))




        d1_replaced=TexMobject(
            "v_{son}",          #0  
            "=",                #1
            "v_0",              #2
            "+",                #3
            "a",                #4
            "\\left( ",         #5
            "{2",               #6
            "\\Delta{x}",       #7
            "\\over",           #8
            "{v_{son}",         #9
            "+",                #10
            "v_0}}",            #11
            "\\right) "         #12
            )

        
        d1_replaced.next_to(t_denk, DOWN)
        d1_replaced[5:13].set_color(YELLOW)

        self.play(ReplacementTransform(d1_tr[0:5].copy(), d1_replaced[0:5]))
        self.play(ReplacementTransform(t_denk[2:8].copy(), d1_replaced[5:13]))

        self.wait(2)



        d4_tr.next_to(d1_replaced, 3*DOWN)

        
        self.play(
            ReplacementTransform(d1_replaced[0].copy(), d4_tr[0:2]),
            ReplacementTransform(d1_replaced[9].copy(), d4_tr[0:2])

            )
        self.play(ReplacementTransform(d1_replaced[1].copy(), d4_tr[2]))

        self.play(
            ReplacementTransform(d1_replaced[2].copy(), d4_tr[3]),
            ReplacementTransform(d1_replaced[11].copy(), d4_tr[4])
            )

        self.play(ReplacementTransform(d1_replaced[3].copy(), d4_tr[5]))

        self.play(
            ReplacementTransform(d1_replaced[4].copy(), d4_tr[7]),
            ReplacementTransform(d1_replaced[6:8].copy(), d4_tr[6:9])
            )


     
        self.play(FadeToColor(d4_tr, RED))
        self.play(ScaleInPlace(d4_tr, 1.5))





        self.wait(30)



class z_son_sahne(Scene):
    def construct(self):
    
        baslik = TextMobject ("Sabit ivmeli hareket denklemleri", color=BLUE)
    
# Denklem Tanımları

       

        d1_tr=TexMobject(
            r"v_{son}",     #0  
            r"=",           #1
            r"v_0",         #2
            "+",            #3
            "a",            #4
            "t",             #5
            color=YELLOW
            )
    

       

        d2_tr=TexMobject(
            "\\Delta{x}",   #0
            "=",            #1
            "{v_{son}",     #2
            "+",            #3
            "v_0",          #4
            "\\over"        #5
            "2}",           #6
            "t",             #7
            color=TEAL
            )

        

        d3_tr=TexMobject(
            "\\Delta{x}",   #0
            "=",            #1
            "v_0",          #2
            "t",            #3
            "+",            #4
            "{1",           #5
            "\\over",       #6
            "2}",           #7
            "a",            #8
            "t^2",           #9
            color=BLUE
            )

        
        d4_tr=TexMobject(
            "v_{son}",      #0       
            "^2",           #1
            "=",            #2
            "v_0",          #3
            "^2",           #4
            "+",            #5
            "2",            #6
            "a",            #7
            "\\Delta{x}",    #8
            color=ORANGE
            )


# Satırları sırala
        

        d1_tr.to_edge(UP)
        d2_tr.next_to(d1_tr, 4*DOWN)
        d3_tr.next_to(d2_tr, 4*DOWN)
        d4_tr.next_to(d3_tr, 4*DOWN)

#Animasyonları oynat
        
        

        self.play(Write(d1_tr))
        self.play(Write(d2_tr))
        self.play(Write(d3_tr))
        self.play(Write(d4_tr))

        self.wait(60)


       

        denk_group = VGroup(d1_tr, d2_tr, d3_tr, d4_tr )

        self.play(FadeOut(denk_group))
        self.wait(2)



class z_Z_opening_scene(Scene):
    def construct(self):

        logo1 = TexMobject(
            "y",    #0
            "u",    #1
            "s",    #2
            "u",    #3
            "f",    #4
           
            "t",    #5
          
            "o",    #6
            "r",    #7
            "u",    #8
            "n",    #9
            )

        logo2 = TexMobject(
            
            "f",    #4
            "(",    #5
            "t",    #6
            ")",    #7
            
            )
        self.play(Write(logo1))
        self.wait(1)

        self.play(
            FadeOut(logo1[0:4]),
            FadeOut(logo1[6:10])
            )


        self.play(ReplacementTransform(logo1[4:6], logo2))
        self.wait(1)

        self.play(FadeOut(logo2))

       