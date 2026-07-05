## Video to subtitles without upload

Courses and podcasts need SRT/VTT. Cloud services have minute limits and retention policies.

**Dicto** transcribes video locally and exports ready subtitles.

## Process

1. Import MP4/MKV in Dicto
2. FFmpeg extracts audio
3. Whisper generates timed segments
4. Export **SRT** or **VTT**

## Quality tips

Clear audio = better sync. Use medium model if hardware allows.

## vs cloud

| | Cloud | Dicto |
|---|-------|-------|
| Minute limits | Yes | No |
| Privacy | Low | Full |
| Cost | Subscription | Free |

Download Dicto for Windows.
