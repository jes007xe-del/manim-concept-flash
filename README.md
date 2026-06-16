Concept Flash
A Manim-based animation engine for generating 30-second cinematic explainers of heavy STEM concepts. Each scene is a self-contained mathematical animation with explicit timing constraints, deterministic rendering, and a standardized structural grammar.
Architecture
Scene Lifecycle
plain
[0-3s]   Hook        : Attention arrest via counterintuitive premise
[3-12s]  Metaphor    : Visual abstraction of the concept
[12-22s] Core        : Mathematical formalism (equations, graphs, state transitions)
[22-28s] Punchline   : Synthesized takeaway
[28-30s] Outro       : Signature fade
Total runtime: 28-32 seconds at 60fps, 1080×1920 vertical canvas.
Module Structure
Table
Path	Function
scenes/	Scene implementations (one concept = one class)
templates/	Reusable animation primitives (hooks, captions, transitions)
config/manim.cfg	Global render configuration (resolution, framerate, color space)
.github/workflows/render.yml	CI pipeline for headless rendering on push
Dependencies
manim>=0.20.0 — Community edition rendering engine
numpy>=1.24.0 — Vector mathematics and random state control
ffmpeg — Video encoding (system dependency)
Usage
Local Render
bash
manim -pqh --config_file config/manim.cfg scenes/entropy_explainer.py EntropyFlash
Flags: -p preview, q quality (1440p), h high fidelity.
CLI Helper
bash
python utils/render_shortform.py scenes/gradient_descent.py GradientDescentFlash --quality qh
CI Render
Push to main or trigger workflow_dispatch with scene name parameter. Artifact retention: 7 days.
Scene Catalog
Table
Class	Concept	Mathematical Objects
EntropyFlash	Statistical entropy	State space, Boltzmann formula, arrow of time
GradientDescentFlash	Optimization dynamics	Loss landscape, parameter update rule, convergence path
NeuralNetworkForward	Inference computation	Layer-wise transformation, activation topology, output distribution
BlockchainConsensus	Distributed agreement	Proof-of-work vs. proof-of-stake state machines
Template API
templates/hooks.py
HookLibrary.counterintuitive_question(scene, question, color) — Renders a two-line challenge prompt with bold weighting
HookLibrary.bold_statement(scene, statement, color) — Centers a declarative claim with scale-in animation
HookLibrary.visual_puzzle(scene, setup, reveal) — Transforms a setup mobject into its resolution via Transform
templates/captions.py
CaptionOverlay.show(text, position, duration) — Auto-fading text with stroke outline for contrast against variable backgrounds
CaptionOverlay.persistent(text, position) — Caption remains until clear_all() invoked
CaptionOverlay.clear_all() — Batch fadeout of active caption stack
templates/transitions.py
FlashTransitions.quick_fade(scene, outgoing, incoming) — 0.8s crossfade, segment boundary standard
FlashTransitions.slide_wipe(scene, outgoing, incoming, direction) — 1.0s directional displacement
FlashTransitions.zoom_focus(scene, target, scale_factor) — 0.8s emphasis zoom with automatic snapback
Configuration
config/manim.cfg
ini
[CLI]
frame_rate = 60
pixel_height = 1920
pixel_width = 1080
background_color = #0f0f23

[custom_settings]
preview = False
write_to_movie = True
disable_caching = False
Canvas ratio: 9:16 vertical. Background: deep navy (#0f0f23). Accent palette: coral (#e94560) for tension states, mint (#4ecca3) for resolution states.
Adding Scenes
Implement Scene subclass in scenes/
Inherit timing constraints (28-32s total)
Use templates/ primitives for visual consistency
Register in .github/workflows/render.yml workflow_dispatch options
Append to scene catalog table in this README


 
