## What is standby memory

The **standby list** is RAM Windows uses as in-memory disk cache. It holds data from closed files and apps that might be needed again. Task Manager may show high "available" memory while new apps struggle because RAM is in standby, not truly free.

## Standby vs free vs modified

| Type | Meaning |
|------|---------|
| Free | Ready for new apps |
| Standby | Reusable cache, can be purged |
| Modified | Dirty pages pending write |

Purging standby is safe: Windows reloads from disk if needed.

## How to free standby

1. Reboot ( drastic but works )
2. Use **Optimus** → purge standby list with before/after metrics
3. Avoid tools that only show pretty charts

Optimus shows standby, modified, compression and totals in one view.

## When to purge

- Before heavy gaming or rendering
- When the system feels slow after hours of use
- After closing RAM-heavy apps

You don't need to purge hourly: Windows handles normal use well.

## Conclusion

Understanding standby helps you avoid fake optimizers. Optimus frees real memory with native operations, free and offline.
