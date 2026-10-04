# Custom GIFs

Put replacement GIFs in this directory. PlatformIO converts them to the C
arrays used by KNOMI before each build.

Supported filenames map to the existing firmware slots:

| File | Replaces |
| --- | --- |
| `welcome.gif` | Wi-Fi/welcome animation |
| `voron.gif` | Idle animation 1 |
| `standby.gif` | Idle animation 2 |
| `homing.gif` | Homing animation |
| `probing.gif` | Probing animation |
| `qgling.gif` | QGL animation |
| `heated.gif` | Heating animation |
| `print.gif` | Printing animation |
| `print_ok.gif` | Print-complete animation |
| `printed.gif` | Printed/standby animation |

The display is `174x51` pixels. Keep GIFs small enough for the ESP32-S3
flash budget. A custom file changes only the matching slot; omitted files keep
the upstream animation.

For a manual conversion without a PlatformIO build:

```powershell
python tools/gif_to_c.py
```
