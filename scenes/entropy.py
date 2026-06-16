from manim import *
from templates.hooks import HookLibrary
from templates.captions import CaptionOverlay
from templates.transitions import FlashTransitions

class EntropyFlash(Scene):
    """
    30-second explainer: What is entropy?
    Format: Hook -> Visual Metaphor -> Formula -> Punchline
    """
    def construct(self):
        # Setup
        self.camera.background_color = "#0f0f23"
        captions = CaptionOverlay(self)
        
        # === SEGMENT 1: HOOK (0-3s) ===
        hook = HookLibrary.counterintuitive_question(
            self,
            "Why does your room\nalways get messy?",
            color="#e94560"
        )
        
        # === SEGMENT 2: VISUAL METAPHOR (3-12s) ===
        self.play(FadeOut(hook), run_time=0.5)
        
        # Ordered grid (clean room)
        ordered = VGroup(*[
            Dot(radius=0.08, color="#4ecca3").shift(
                np.array([x*0.35, y*0.35, 0])
            )
            for x in range(-4, 5) for y in range(-3, 4)
        ])
        
        # Disordered scatter (messy room)
        np.random.seed(42)
        disordered = VGroup(*[
            Dot(radius=0.08, color="#e94560").shift(
                np.array([
                    np.random.uniform(-2.5, 2.5),
                    np.random.uniform(-2, 2),
                    0
                ])
            )
            for _ in range(63)
        ])
        
        label_clean = Text("Ordered: 1 way", font_size=28, color="#4ecca3")
        label_clean.next_to(ordered, DOWN, buff=0.6)
        
        label_messy = Text("Disordered: MANY ways", font_size=28, color="#e94560")
        label_messy.next_to(disordered, DOWN, buff=0.6)
        
        self.play(FadeIn(ordered), FadeIn(label_clean), run_time=1.0)
        self.wait(0.5)
        self.play(
            Transform(ordered, disordered),
            Transform(label_clean, label_messy),
            run_time=2.0
        )
        self.wait(0.5)
        
        # === SEGMENT 3: CORE CONCEPT (12-22s) ===
        FlashTransitions.quick_fade(self, VGroup(ordered, label_clean), VGroup())
        
        formula = MathTex(
            r"S = k_B \ln \Omega",
            font_size=52,
            color="#ffffff"
        )
        formula.move_to(ORIGIN)
        
        concept_text = Text(
            "Entropy = measure of disorder", 
            font_size=30, 
            color="#f8f9fa"
        )
        concept_text.next_to(formula, DOWN, buff=0.8)
        
        self.play(Write(formula), run_time=1.5)
        self.play(FadeIn(concept_text), run_time=0.8)
        self.wait(2.0)
        
        # === SEGMENT 4: PUNCHLINE (22-28s) ===
        arrow = Arrow(LEFT*2, RIGHT*2, color="#e94560", buff=0.3, stroke_width=6)
        arrow.next_to(concept_text, DOWN, buff=0.8)
        
        punchline = Text(
            "Time flows toward disorder", 
            font_size=26, 
            color="#e94560",
            weight=BOLD
        )
        punchline.next_to(arrow, DOWN, buff=0.4)
        
        self.play(GrowArrow(arrow), run_time=1.0)
        self.play(FadeIn(punchline), run_time=0.8)
        self.wait(1.5)
        
        # === OUTRO (28-30s) ===
        brand = Text("@ConceptFlash", font_size=20, color="#666666")
        brand.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(brand), run_time=0.8)
        self.wait(1.0)
