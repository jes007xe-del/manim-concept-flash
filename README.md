manim-concept-flash
  Concept Flash

Turn complex STEM ideas into 30-second LinkedIn videos — with code.**

Concept Flash is a Manim-based pipeline for creating cinematic, vertical-format explainers that make heavy concepts (entropy, gradient descent, neural networks) instantly digestible. Every scene is engineered for the 9:16 short-form format: 60fps, silent-caption friendly, and algorithm-optimized for LinkedIn engagement.

 Why This Exists

Short-form STEM content is underserved. Most explainers are either 10-minute lectures or oversimplified infographics. We bridge the gap: **cinematic depth at TikTok pacing.**

 What You Get

- Production-ready scenes** (entropy, gradient descent, neural networks, blockchain)
-  Template system** (hooks, captions, transitions) for consistent 30s structure
-  GitHub Actions CI/CD** — push code, get MP4
-  9:16 vertical config** pre-tuned for LinkedIn/Reels/TikTok
- Engagement-tested format**: Hook → Visual → Formula → Punchline

Perfect For

- ML engineers building personal brand
- STEM educators reaching new audiences
- Founders explaining technical moats
- Anyone who thinks 3Blue1Brown should have a TikTok account

 Quick Start

```bash
pip install -r requirements.txt
manim -pqh --config_file config/manim.cfg scenes/entropy_explainer.py EntropyFlash
