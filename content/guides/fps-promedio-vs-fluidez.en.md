It happened to you, or to a friend — guaranteed. You upgrade your setup, turn on the FPS counter in the corner, and there it is: 280, 300, sometimes spikes of 340. A number you used to only see in lab benchmark configs. You should be living the smoothest gaming experience of your life.

And yet something's wrong. The game feels choppy. Micro-stutters appear out of nowhere, especially in intense moments: a big explosion, a sharp camera turn, the exact second you need to react fast or die. You glance at the counter — 290 FPS — and think: "how can this feel bad when the number is sky-high?"

Welcome to one of the biggest lies benchmark culture sold us: that average FPS equals smoothness. It doesn't. Understanding why will completely change how you evaluate your PC's performance.

## Average is statistical makeup

Think of average FPS like average salary at a company. If nine people earn normal wages and one (the owner) earns a fortune, the office "average" looks high and misleading. It doesn't represent most workers' reality.

Average FPS works the same. If your game runs at 400 FPS in quiet moments (staring at a wall, standing in spawn) and drops to 60 FPS in real action (combat, lots of effects, explosions), the final average can still show something like 290 FPS — even though the experience when it actually matters (when you're really playing, not staring at a wall) is much worse than that number suggests.

Average lies because it mixes easy-to-render with hard-to-render, letting the easy stuff "cover" the hard stuff.

| Metric | What it measures | Reflects real smoothness? |
|--------|------------------|---------------------------|
| **Average FPS** | Session mean | **No** — hides valleys |
| **1% low** | Worst 1% of frames | **Yes** — your worst moments |
| **0.1% low** | Worst 0.1% of frames | **Yes** — extreme micro-hitches |
| **Frame time (ms)** | Milliseconds per frame | **Yes** — what you feel moving the camera |

## The real hero: 1% low

**1% low** (and its stricter cousin **0.1% low**) doesn't measure overall average — it measures **performance in the worst 1% of frames you generated**. Instead of "how did you do overall?" it asks "how bad were your worst moments?"

This metric is far more honest about how playing *feels*, because your brain doesn't perceive session average. It perceives peaks and valleys. A half-second hitch the exact moment you were about to react to an enemy costs you the round — not the fact that two seconds earlier you were running at 350 FPS staring at the sky.

Concrete example: two PCs, same game.

**PC A**: 240 average FPS. 55 FPS 1% low.

**PC B**: 165 average FPS. 130 FPS 1% low.

On paper, PC A "wins" by a huge margin if you only look at average. But playing, PC B feels dramatically more consistent, predictable, smoother in critical moments. PC A has spectacular peaks followed by sharp drops that feel like tripping. PC B keeps a much higher floor even though its ceiling is lower.

Almost any competitive player, blind-testing both without seeing numbers, would pick PC B as "smoother" despite the smaller average.

## Why do dips happen if hardware is powerful?

Several typical causes — each with a different fix:

**1. Shader compilation stutter.**

Many modern games compile shaders the first time an effect appears on screen, not beforehand. That causes micro-stutters when a new effect shows up (an explosion with particles you hadn't seen this session) — no matter how powerful your hardware. Some games precompile shaders at launch; others don't.

**2. Lack of RAM or VRAM headroom at spikes.**

As we covered in **your RAM isn't "full", it's working**, when the system must reorganize memory suddenly (loading many new effects in a big explosion), that reorganization causes a perceptible pause — even if your overall FPS average is sky-high.

**3. Background processes waking at the worst moment.**

Scheduled antivirus scan, Windows Update downloading, Discord processing an image notification — short resource competition in the most intense game moment won't tank your average much, but it destroys 1% low.

**4. CPU limits in scenes with lots of simultaneous logic.**

A big explosion isn't just visual: physics, hitboxes, positional audio, AI reacting. That load spike can drop frames even when your CPU is idle the rest of the time.

| Cause of dip | Typical symptom | What to try |
|--------------|-----------------|-------------|
| Uncompiled shaders | Hitch first time you see an effect | Precompile shaders / warmup round |
| Tight RAM/VRAM | Combat stutter + active disk | Close apps, free standby, more RAM/VRAM |
| Background | Random hitches unrelated to game | Game mode, close overlays, defer updates |
| CPU limit | GPU with headroom, low 1% in crowds | Better CPU or lower logic-heavy settings |

## The mistake of "optimizing for the number"

Here's the heart of the paradox. Many people obsess over raising average FPS: lower settings, performance mods — all to see a bigger number in the corner. Sometimes they succeed: average goes from 220 to 280.

But if those changes don't fix the real cause of point dips (uncompiled shaders, no memory margin, background competing), 1% low stays bad or gets worse — now more "easy" frames statistically cover the same "hard" frames as before.

It's like improving a runner's average speed on flat sections without fixing falling into every pothole. Average speed looks better on paper. Running that course with potholes intact still feels awful.

Related: enabling DLSS to boost average without improving lows is the same trap in reverse — sometimes upscaling improves both; sometimes it only inflates numbers in easy scenes. See our guide on **DLSS and FSR vs native resolution** (linked at the bottom).

## What should you watch instead of average?

If you want an experience that actually *feels* smooth, not just "measures well" in a screenshot with an FPS counter, prioritize:

**1. 1% low as main reference**, not average. MSI Afterburner, CapFrameX, or many game overlays show this directly.

**2. Frame time consistency** over raw numbers. A relatively flat frame-time graph beats spiky highs and deep valleys even if averages match.

**3. How it feels in the game's most demanding real moments**, not the main menu or spawn. Go straight to the most chaotic combat zone and evaluate there.

### Quick checklist before blaming hardware

1. Measure **1% low** in real combat, not menus
2. Precompile shaders if the game allows
3. Close heavy background; **Optimus game mode** before ranked
4. Check RAM and VRAM at peak (Task Manager / Afterburner)
5. Up-to-date GPU drivers

To understand what limits your PC (CPU, GPU, RAM, disk), see our guide on **how RAM, GPU, CPU and storage affect gaming** (linked at the bottom).

## Frequently asked questions

**What's a "good" 1% low?** Depends on game and monitor refresh. Rule of thumb: 1% low shouldn't fall much below ~80% of refresh (e.g. at 144 Hz, ideally lows >115 FPS). At 60 Hz, stable lows >50 FPS already feel fine.

**Does capping at 141 FPS help smoothness?** Sometimes: FPS cap can stabilize frame pacing in some titles. Try with V-Sync off + cap in Afterburner.

**More FPS always = less input lag?** Generally yes up to a point, but if lows are garbage, input feels inconsistent despite high average.

**Does Optimus raise 1% low?** It doesn't overclock. It frees RAM and reduces background noise — useful if lows come from memory or competing processes, not pure GPU limits.

**Does Frame Generation (DLSS 3) improve lows?** Boosts perceived FPS but can add latency; in competitive play prioritize real lows without frame generation.

## The real lesson

A big number in the corner is addictive, easy to compare with friends, easy to sell in GPU marketing. But it's not what your brain reads as "playing well." Your brain reads consistency. That when you turn the camera, the image responds without surprises. That at the exact moment of an explosion, the game doesn't betray you with half a second of pause when you need to react fastest.

Next time you evaluate whether your PC "runs well" or needs an upgrade, stop looking only at average. Look at your worst moments, not your best. In games as in life, you don't remember the average of a night. You remember the exact instant something went wrong.

And that instant isn't measured by average FPS. It's measured by 1% low.
