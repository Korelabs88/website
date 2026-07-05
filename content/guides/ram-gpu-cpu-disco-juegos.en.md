## Quick answer: who affects what?

| Component | Mainly affects… | Typical in-game impact |
|-----------|-----------------|------------------------|
| **GPU** | FPS, visual quality, resolution | **Very high** |
| **CPU** | Minimum FPS, simulations, many NPCs | **High** (game-dependent) |
| **RAM** | Stuttering, crashes, Discord + game multitasking | **Medium** (if low or full) |
| **Storage** | Load times, texture streaming | **Low on FPS**; **high on loads** |

There's no single king: competitive 1080p may be **CPU-limited**; 4K AAA is often **GPU-limited**; 8 GB full RAM makes everything choppy regardless of graphics.

## GPU: the frame engine

The **graphics card** draws each frame: shaders, textures, effects. At 1440p/4K in modern titles, the GPU is usually the **first bottleneck** when you raise quality or FPS.

### What matters on GPU

- **VRAM**: 8 GB is often enough at 1080p/1440p with sensible settings; 12–16 GB helps at 4K and heavy mods. When VRAM fills, stutter and sharp FPS drops appear.
- **Raw power**: how many FPS you hold at a given resolution.
- **Updated drivers**: sometimes +10 % from a clean NVIDIA/AMD/Intel install.

### Signs GPU is the limit

- GPU ~95–100 % in-game, CPU lower
- Lower resolution or settings **boost FPS a lot**
- Monitoring shows GPU maxed, CPU with headroom

**Optimus** won't replace a better GPU, but **game mode** and freeing RAM help the CPU feed the GPU without junk processes competing.

## CPU: the conductor

The **processor** prepares the scene: physics, AI, animations, draw calls. **Single-thread** games want fast cores; strategy, MMOs and sims use **more cores**.

### When CPU limits more than GPU

- Competitive shooters at **high FPS 1080p** (CS2, Valorant, Fortnite)
- Dense cities in **Cyberpunk**, **Starfield**, **Cities: Skylines**
- Emulation, heavy mod Minecraft, local servers

### Signs of CPU bottleneck

- GPU at 60–70 % and **one core** at 100 %
- Bad 1 % lows while average FPS looks OK
- Raising graphics **barely lowers** FPS (GPU isn't the cap)

More cores don't always help: many titles still hammer 4–6 cores. **GHz**, recent architecture and memory latency matter.

## RAM: capacity, speed and "full memory"

**RAM** holds the game, textures in flight, Discord, browser, antivirus and Windows. It doesn't draw like the GPU, but **without free RAM** the system pages to disk and you get **hitches**.

### Comfortable capacity (2026)

| Use | Comfortable minimum |
|-----|---------------------|
| Casual gaming + Windows | 16 GB |
| AAA + Discord + browser | **32 GB** |
| 4K, mods, local streaming | 32–64 GB |

**8 GB** is tight or insufficient for many current titles.

### DDR speed (MT/s)

- DDR4 3200 vs 3600: often **1–5 %** FPS difference
- DDR5 5600+: slight edge in bandwidth-sensitive cases
- Usually **capacity** matters more than last MHz

### Full RAM vs standby

Windows keeps data in **standby** cache — normal. Before long sessions:

- Close unused tabs and launchers
- Purge standby if you're tight (**Optimus** uses native ops with before/after metrics)

### Signs of RAM problems

- Constant **>90 %** use with disk activity
- Unexpected closes ("out of memory")
- Open-world stutter while moving fast, GPU not saturated

## Storage: HDD, SATA SSD and NVMe

**Storage** rarely changes steady combat FPS once a level is loaded. It shows in:

| Type | Load times | Open-world streaming | Combat FPS |
|------|------------|----------------------|------------|
| **HDD** | Slow, late textures | Pops and hitches turning | Similar* |
| **SATA SSD** | Fast | Very good | Baseline |
| **NVMe Gen4/5** | Very fast | Excellent for streaming titles | ~same as SATA |

\*HDD open worlds may **stutter** from slow texture reads — hitches, not just "lower average FPS."

### Storage tips

- Install games on **SSD** (NVMe if available)
- Keep **20 %+ free** on system drive for cache and shaders
- Clean old temp files (**Optimus** deep cleanup, reversible)

Don't buy Gen5 NVMe for +3 FPS; buy it if you hate load screens or play heavy streaming worlds (Flight Simulator, some RPGs).

## How all four interact

Pipeline:

```
Disk → loads level and textures into RAM
RAM → CPU runs logic and feeds GPU
CPU → issues draw calls
GPU → renders the frame
```

Slow **disk** → late pipeline start (long loads, pops).
Low **RAM** → paging makes everything feel like slow storage.
Weak **CPU** → GPU waits (low FPS, idle GPU).
Weak **GPU** → CPU finishes early, graphics suffer (GPU at 100 %).

## What to upgrade first?

Match your symptom:

| Symptom | Likely priority |
|---------|-----------------|
| Low FPS at 4K / ultra | GPU |
| Unstable FPS at competitive 1080p | CPU (and RAM if <16 GB) |
| Endless loads, late textures | SSD / NVMe |
| Hitches, slow alt-tab, crashes | RAM (more GB or free memory) |
| Everything bad on old PC | Full platform refresh |

Typical **new** balanced build: GPU ≥ CPU ≥ 32 GB RAM ≥ NVMe. On existing hardware, **measure** first (Task Manager, Afterburner, Optimus).

## Free software tweaks

Before buying parts:

1. **Update GPU drivers**
2. **High performance** power plan (laptop plugged in)
3. Close unused overlays and recorders
4. **Optimus game mode** + purge standby RAM
5. Game on SSD, not 5400 rpm HDD
6. Realistic resolution and presets

## FAQ

**Does 32 GB beat 16 GB for FPS?** Only if 16 GB was exhausted. If a game uses 10 GB, 32 GB won't magically add FPS.

**NVMe vs SATA for Fortnite?** Nearly same FPS; NVMe wins on install and lobby loads.

**RAM overclock worth it?** Marginal; stable XMP/EXPO is usually enough.

**Does Optimus raise FPS?** It doesn't overclock GPU. It cuts system noise, frees RAM and prepares the PC — helpful when RAM is tight or background apps abound.

**Integrated GPU only?** iGPU limits everything; shared RAM and CPU hurt more. Serious gaming needs a dedicated card.

## Conclusion

- **GPU** → visuals and average FPS in most AAA
- **CPU** → minimum FPS and logic-heavy games
- **RAM** → smoothness when capacity is tight
- **Disk** → loads and streaming; rarely steady-scene FPS

Find your bottleneck, upgrade wisely and keep Windows clean. **Optimus** helps with RAM, startup, disk and game mode — free and local on Windows 10/11.
