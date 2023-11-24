from manim import *

class IntegralStatement(Scene):
    def construct(self):
        title = Paragraph("Aproximaciones a π derivadas de", "integrales con integrandos no negativos", alignment="center")
        title.set_color(BLUE)

        equation1 = MathTex(r"\int_0^1 \frac{x^4(1-x)^4}{1+x^2} \, dx")
        equation1.next_to(title, DOWN)

        equation2 = MathTex(
            r"\int_{0}^{1}\frac{x^{4}(1-x)^{4}}{1+x^2}dx &= \int_{0}^{\pi/4}\frac{\tan^{4}\theta(1-\tan\theta)^{4}}{1+\tan^2 \theta} \sec^2 \theta d \theta",
            r"&= \int_{0}^{\pi/4} \tan^{4}\theta -4\tan^{5}\theta + 6\tan^{6}\theta -4\tan^{7}\theta + \tan^{8}\theta d \theta",
            r"&= \frac{1}{7} +5\int_{0}^{\pi/4} \tan^{6}\theta d \theta + \int_{0}^{\pi/4} \tan^{4}\theta d \theta",
            r"&= \frac{22}{7} - \pi",
            r"\text{entonces tenemos que } \frac{22}{7} > \pi"
        ).arrange(DOWN, aligned_edge=LEFT)

        inequalities = MathTex(
            r"x^{4}(1-x)^{4} = [x(1-x)]^{4}",
            r"x(1-x) \leq \frac{1}{4}",
            r"1+x^2 \geq 1",
            r"\text{para } x \text{ en el intervalo } [0, 1]"
        ).arrange(DOWN, aligned_edge=LEFT)

        new_inequalities = MathTex(
            r"\left(\frac{1}{4}\right)^4 \int_{0}^{1} dx &> \int_{0}^{1} \frac{x^4(1-x)^4}{1+x^2} dx",
            r"\frac{1}{256} &> \frac{22}{7} - \pi",
            r"\pi &> \frac{22}{7} - \frac{1}{256}",
            r"\text{o sea }",
            r"\frac{5625}{1792} = \frac{22}{7} - \frac{1}{256} < \pi < \frac{22}{7}"
        ).arrange(DOWN, aligned_edge=LEFT)

        new2_inequalities = MathTex(
            r"\text{Observando que } 1< 1+x^2< 2 \text{ en el intervalo } [0, 1] \text{ y que }",
            r"\int_{0}^{1} x^4(1-x)^4 dx = \frac{1}{630}",
            r"\text{por tanto, se tienen estas dos desigualdades }",
            r"\int_{0}^{1} \frac{x^4(1-x)^4}{1+x^2} dx = \frac{22}{7} < \frac{1}{630} = \int_{0}^{1} x^4(1-x)^4 dx",
            r"\int_{0}^{1} \frac{x^4(1-x)^4}{2} dx = \frac{1}{1260} < \frac{22}{7} = \int_{0}^{1} \frac{x^4(1-x)^4}{1+x^2} dx",
            r"\text{en conclusión }",
            r"\frac{1979}{630} = \frac{22}{7} - \frac{1}{630} < \pi < \frac{22}{7} - \frac{1}{1260} = \frac{3959}{1260}"
        ).arrange(DOWN, aligned_edge=LEFT)

        self.play(Write(title), run_time=10)
        self.play(Write(equation1), run_time=10)
        self.wait(10)  # 10 segundos de espera
        self.play(FadeOut(equation1, title), run_time=5)
        self.play(Write(equation2), run_time=20)
        self.wait(25)  # 25 segundos de espera
        self.play(FadeOut(equation2), run_time=3)
        self.play(Write(inequalities), run_time=10)
        self.wait(15)  # 10 segundos de espera
        self.play(FadeOut(inequalities), run_time=2)
        self.play(Write(new_inequalities), run_time=5)
        self.wait(5)  # 10 segundos de espera
        self.play(FadeOut(new_inequalities), run_time=2)
        self.play(Write(new2_inequalities), run_time=10)
        self.wait(20)  # 10 segundos de espera

IntegralStatement().render()

class parte1b(Scene):
    def construct(self):
       texto1b=Text("¿Otras integrales para aproximar?")\
          .to_edge(UP)
          eqn0=MathTex("\\int_{0}^{1}\\frac{x^{4}(1-x)^{4}}{1+x^2}dx")
          eqn1=MathTex("\\int_{0}^{1}\\frac{x^{4}(1-x)^{4}}{1+x^2}dx","=\\frac{22}{7}-\\pi")
          eqn2=MathTex("\\int_{0}^{1} ? dx","= ? -\\pi")
          eqn3=MathTex("\\int_{0}^{1}\\frac{x^{4}(1-x)^{4}}{1+x^2}dx=\\frac{22}{7}-\\pi")
          eqn4=MathTex("\\int_{0}^{1}\\frac{x^{4}(1-x)^{4}}{1+x^2}dx=\\frac{22}{7}-\\pi").move_to(UP*2).scale(0.5)
          eqn5=MathTex("x^{4}(1-x)^{4}").move_to(LEFT*2).scale(0.8)
          texto2b=Text("Funciona!! :)").move_to(RIGHT*2).scale(0.8)
          texto3b=Text("¿Funciona?").move_to(RIGHT*2 + DOWN*2).scale(0.8)
          #texto4b=Text("¿Funciona?").move_to(RIGHT + DOWN*2)
          eqn6=MathTex("x^{8}(1-x)^{8}").move_to(LEFT*2+DOWN*2).scale(0.8)
          eqn7=MathTex("x^{12}(1-x)^{12}").move_to(LEFT*2+DOWN*2).scale(0.8)
          #eqn6=MathTex("\\int_{0}^{1}\\frac{x^{8}(1-x)^{8}}{1+x^2}dx=?").move_to(DOWN*2)
          self.wait(2)
          self.play(Write(eqn0))
          self.play(Transform(eqn0,eqn1))
          self.wait(3)
          self.play(Write(texto1b))
          self.play(FadeOut(eqn0),Transform(eqn1,eqn2))
          self.wait(2)
          self.play(FadeOut(eqn1),Write(eqn3))
          self.wait(1)
          self.play(Transform(eqn3,eqn4))
          self.play(Write(eqn5))
          self.wait(3)
          self.play(Write(texto2b))
          self.wait(2)
          self.play(Write(eqn6))
          self.wait(2)
          self.play(Write(texto3b))
          self.wait(2)
          self.play(Transform(eqn6,eqn7))
          self.wait(2)

# manim -pqh Parte1b.py Parte2b

class Parte2b(Scene):
    def construct(self):
        texto4b=Text("Familia de integrales con integrandos no negativos").to_edge(UP).scale(0.7)
        eqn8=MathTex("I_{4n}")
        eqn9=MathTex("\\int_{0}^{1}\\frac{x^{4n}(1-x)^{4n}}{1+x^2}dx","=I_{4n}")
        eqn10=MathTex("\\int_{0}^{1}\\frac{x^{4n}(1-x)^{4n}}{1+x^2}dx","=I_{4n}").move_to(UP*2).scale(0.8)
        eqn11=MathTex("\\int_{0}^{1}\\frac{x^{4}(1-x)^{4}}{1+x^2}dx = I")
        eqn12=MathTex("I_{4}=I")
        eqn13=MathTex("\\frac{x^{4n}(1-x)^{4n}}{1+x^2}")
        eqn14=MathTex(r"\frac{x^{4n}(1-x)^{4n}}{x^2+1}&=(x^6-4x^5+5x^4-4x^2+4)\sum_{k=0}^{n-1}(-4)^{n-1-k}x^{4k}(1-x)^{4k} + \frac{(-4)^n}{1+x^2}").scale(0.7)
        texto5b=Text("Por inducción cae ;)").move_to(DOWN*2)
        eqn16=MathTex("\\int_{0}^{1}\\frac{x^{4n}(1-x)^{4n}}{1+x^2}dx")
        eqn17=MathTex(r"\int_{0}^{1}\frac{x^{4n}(1-x)^{4n}}{x^2+1}&=\int_{0}^{1}(x^6-4x^5+5x^4-4x^2+4)\sum_{k=0}^{n-1}(-4)^{n-1-k}x^{4k}(1-x)^{4k} + \frac{(-4)^n}{1+x^2}").scale(0.7)
        eqn18=MathTex("\\int_{0}^{1} x^m(1-x)^n dx","= \\frac{m!n!}{(m+n+1)!}").move_to(DOWN*2)
        eqn19=MathTex(r"\frac{(-1)^n}{4^{n-1}}\int_{0}^{1}\frac{x^{4n}(1-x)^{4n}}{x^2+1}dx&=\pi - \sum_{k=0}^{n-1}(-1)^k\frac{2^{4-2k}(4k)!(4k+3)!}{(8k+7)!}(820k^3+1533k^2+902k+165)").scale(0.5)
        eqn20=MathTex("n=2s +1").move_to(DOWN*2)
        eqn21=MathTex(r"\int_{0}^{1}\frac{x^{4}(1-x)^{4}}{x^2+1}dx&=\frac{22}{7}-\pi").move_to(LEFT)
        texto6b=Text("Para n = 1").move_to(RIGHT*3).scale(0.6)
        eqn22=MathTex(r"\frac{1}{4^2}\int_{0}^{1}\frac{x^{12}(1-x)^{12}}{x^2+1}dx&=\frac{431302721}{137287920}-\pi").move_to( LEFT + DOWN*2 ).scale(0.7)
        texto7b=Text("Para n = 3").move_to(RIGHT*3+DOWN*2).scale(0.5)
        self.wait(4)

        self.play(Write(texto4b))
        self.wait(3)
        self.play(Write(eqn9[0]))
        self.wait(1)
        self.play(Write(eqn9[1]))
        self.wait(4)
        self.play(Transform(eqn9,eqn10))
        self.play(Write(eqn11))
        self.wait(4)
        self.play(Transform(eqn11,eqn12))
        self.wait(3)
        self.play(FadeOut(eqn9),FadeOut(eqn11),FadeOut(eqn12))
        self.wait(3)
        self.play(Write(eqn13))
        self.wait(2)
        self.play(FadeOut(eqn13),Write(eqn14))
        self.play(Write(texto5b))
        self.wait(3)
        self.play(FadeOut(eqn14),FadeOut(texto5b))
        self.play(Write(eqn13))
        self.play(Transform(eqn13,eqn16))
        self.wait(3)
        self.play(FadeOut(eqn16),FadeOut(eqn13),Write(eqn17))
        self.wait(4)
        self.play(Write(eqn18), run_time = 5)
        self.wait(2)
        self.play(Transform(eqn17,eqn19))
        self.wait(2)
        self.play(FadeOut(eqn18))
        self.wait(8)
        self.play(Write(eqn20))
        self.wait(2)
        self.play(FadeOut(eqn17),FadeOut(eqn19),FadeOut(eqn20))
        self.wait(2)
        self.play(Write(eqn21),Write(texto6b))
        self.wait(2)
        self.play(Write(eqn22),Write(texto7b))
        self.wait(2)

#  manim -pqh Parte1b.py Parte3b
class Parte3b(Scene):
    def construct(self):
        texto8b = Text("Expansión en series :D").to_edge(UP)
        eqn23 = MathTex(
            r"\frac{(-1)^n}{4^{n-1}}\int_{0}^{1}\frac{x^{4n}(1-x)^{4n}}{x^2+1}dx&=\pi - \sum_{k=0}^{n-1}(-1)^k\frac{2^{4-2k}(4k)!(4k+3)!}{(8k+7)!}(820k^3+1533k^2+902k+165)").scale(
            0.5)
        eqn24 = MathTex("\\pi = \\sum_{m=0}^{\\infty}?")
        eqn25 = MathTex(
           r"\pi = \sum_{m=0}^{\infty}\sum_{k=0}^{n-1}(-4)^{-nm-k}\int_{0}^{1}(x^6-4x^5+5x^4-4x^2+4)x^{4(k+nm)}(1-x)^{4(k+nm)}dx").scale(                    0.6)
        eqn26 = MathTex(
            r"\pi \approx \sum_{m=0}^{3}\sum_{k=0}^{n-1}(-4)^{-nm-k}\int_{0}^{1}(x^6-4x^5+5x^4-4x^2+4)x^{4(k+nm)}(1-x)^{4(k+nm)}dx").scale(
            0.6)
        eqn27 = MathTex(
            r"\pi \approx \sum_{m=0}^{6}\sum_{k=0}^{n-1}(-4)^{-nm-k}\int_{0}^{1}(x^6-4x^5+5x^4-4x^2+4)x^{4(k+nm)}(1-x)^{4(k+nm)}dx").scale(
            0.6)
        texto9b = Text("Para n=2 y considerando los primeros 7 terminos de la serie tenemos:")
        eqn28 = MathTex(
            r"\frac{27866240172453844886325941887505217163994611104897858617}{8870099737663958700556100446465640958076561638241075200}").scale(
            0.7)
        eqn29 = MathTex(r"3.141592653589793238462643383279502884197169...").move_to(DOWN * 2).scale(0.7)
        eqn30 = MathTex(
            r"\pi \approx \sum_{m=0}^{6}\sum_{k=0}^{n-1}(-4)^{-nm-k}\int_{0}^{1}(x^6-4x^5+5x^4-4x^2+4)x^{4(k+nm)}(1-x)^{4(k+nm)}dx").move_to(
            UP * 2).scale(0.6)
        texto10b = Text("Gracias por ver :)").scale(0.8)
        texto11b = Text("Elaborado por:").to_edge(UP).scale(0.8)
        texto12b = Text("Juan José Medina González").scale(0.8)
        texto13b = Text("Brayan Nicolás Amortegui").move_to(DOWN * 2).scale(0.8)

            self.wait(2)
            self.play(Write(eqn23))
            self.wait(3)
            self.play(Write(texto8b))
            self.wait(1)
            self.play(Transform(eqn23, eqn24))
            self.wait(2)
            self.play(FadeOut(eqn23), Transform(eqn24, eqn25))
            self.wait(12)
            self.play(FadeOut(eqn24), Transform(eqn25, eqn26))
            self.wait(4)
            self.play(FadeOut(eqn25), Transform(eqn26, eqn27))
            self.wait(4)
            self.play(FadeOut(eqn26), FadeOut(eqn27), Write(eqn30))
            self.wait(2)
            self.play(Write(eqn28))
            self.wait(2)
            self.play(Write(eqn29))
            self.play(FadeOut(eqn28), FadeOut(eqn29), FadeOut(eqn30), FadeOut(texto8b))
            self.wait(4)
            self.play(Write(texto10b))
            self.play(FadeOut(texto10b), Write(texto11b))
            self.play(Write(texto12b), Write(texto13b))
            self.wait(2)
            self.play(FadeOut(texto11b), FadeOut(texto12b), FadeOut(texto13b))
            self.wait(2)