## Why Windows runs out of RAM

Windows manages memory aggressively: it keeps recent files and apps in the **standby list** to speed up re-launching. That's not a bug, but when you open games or heavy apps you may run short on available RAM.

Many "optimizers" show fake percentages or free memory Windows instantly reclaims. What works is targeting **working sets**, **standby** and **modified** with native APIs.

## Methods that actually work

### 1. Close unused apps
Task Manager (Ctrl+Shift+Esc) shows top RAM consumers. Close browser tabs and background apps before any tool.

### 2. Review startup programs
Fewer apps at boot = more free RAM from minute one. Optimus includes startup management.

### 3. Real freeing with Optimus
**Optimus** runs documented Windows operations:

- Empty process working sets
- Purge standby list (most effective)
- Flush modified pages
- Clear system file cache (optional, requires admin)

Measure before/after with memory breakdown. No telemetry or subscription.

## What to avoid

- Tools promising "50% more RAM" with fake animations
- Online services asking for remote PC access
- Disabling paging without knowing the impact

## Recommended steps

1. Download Optimus (installer or portable)
2. Run as administrator for advanced features
3. Open the RAM module and review standby/modified
4. Select operations and confirm
5. Compare results in the live monitor

## FAQ

**Does freeing RAM harm Windows?** Not with reversible operations like Optimus uses.

**How much RAM should I free?** It depends. Focus on real standby recovery, not a fixed number.

**Is it free?** Yes. Optimus is free and local.
