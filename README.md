# KNOMI firmware fork

This repository tracks the official `firmware` branch from
`bigtreetech/KNOMI` and keeps custom firmware work on top of it.

## Build

```powershell
pio run -e knomiv2
```

Use `-e knomiv1` for KNOMI V1.

## Custom GIFs

Put replacement GIFs in `assets/gifs`. The PlatformIO pre-build hook converts
only the slots that are present into the LVGL C sources under `src/gif`.
See `assets/gifs/README.md` for the supported names and dimensions.

## Moonraker

Configure the printer IP and port in the KNOMI web interface. The firmware
polls Moonraker once per second for Klipper readiness, `_KNOMI_STATUS`,
`virtual_sdcard`, `display_status`, and `idle_timeout`, then reads printer
temperatures and job flags from `/api/printer`. The optional `screen_on` field
on `_KNOMI_STATUS` is exposed in the firmware data structure without requiring
it on printers that do not define it.

## Remotes

- `upstream`: `bigtreetech/KNOMI`
- `origin`: `WeLizard/KNOMI`

## Official documentation

- [KNOMI V1 manual](https://bigtreetech.github.io/docs/KNOMI.html)
- [KNOMI V2 manual](https://bigtreetech.github.io/docs/KNOMI2.html)
- [Upstream repository](https://github.com/bigtreetech/KNOMI)
