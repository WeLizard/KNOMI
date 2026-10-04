"""Convert KNOMI GIF assets into LVGL-compatible C sources."""

from __future__ import annotations

import argparse
from pathlib import Path


SLOTS = {
    "welcome": ("gif_wifi.c", "gif_welcome", "GIF_WELCOME"),
    "voron": ("gif_voron.c", "gif_voron", "GIF_VORON"),
    "standby": ("gif_standby.c", "gif_standby", "GIF_STANDBY"),
    "homing": ("gif_homing.c", "gif_homing", "GIF_HOMING"),
    "probing": ("gif_probing.c", "gif_probing", "GIF_PROBING"),
    "qgling": ("gif_qgling.c", "gif_qgling", "GIF_QGLING"),
    "heated": ("gif_heated.c", "gif_heated", "GIF_HEATED"),
    "print": ("gif_print.c", "gif_print", "GIF_PRINT"),
    "print_ok": ("gif_print_ok.c", "gif_print_ok", "GIF_PRINT_OK"),
    "printed": ("gif_printed.c", "gif_printed", "GIF_PRINTED"),
}


def gif_dimensions(data: bytes) -> tuple[int, int]:
    if len(data) < 10 or data[:6] not in (b"GIF87a", b"GIF89a"):
        raise ValueError("input is not a GIF87a/GIF89a file")
    return int.from_bytes(data[6:8], "little"), int.from_bytes(data[8:10], "little")


def render_c(data: bytes, symbol: str, attribute: str, width: int, height: int) -> str:
    values = []
    for offset in range(0, len(data), 12):
        chunk = data[offset : offset + 12]
        values.append("    " + ", ".join(f"0x{byte:02x}" for byte in chunk) + ",")
    return """#ifdef __has_include
    #if __has_include("lvgl.h")
        #ifndef LV_LVGL_H_INCLUDE_SIMPLE
            #define LV_LVGL_H_INCLUDE_SIMPLE
        #endif
    #endif
#endif

#if defined(LV_LVGL_H_INCLUDE_SIMPLE)
    #include "lvgl.h"
#else
    #include "lvgl/lvgl.h"
#endif

#ifndef LV_ATTRIBUTE_MEM_ALIGN
#define LV_ATTRIBUTE_MEM_ALIGN
#endif

#ifndef LV_ATTRIBUTE_IMG_{attribute}
#define LV_ATTRIBUTE_IMG_{attribute}
#endif

const LV_ATTRIBUTE_MEM_ALIGN LV_ATTRIBUTE_LARGE_CONST LV_ATTRIBUTE_IMG_{attribute} uint8_t {symbol}_map[] = {{
{payload}
}};

const lv_img_dsc_t {symbol} = {{
  .header.cf = LV_IMG_CF_RAW_CHROMA_KEYED,
  .header.always_zero = 0,
  .header.reserved = 0,
  .header.w = {width},
  .header.h = {height},
  .data_size = {size},
  .data = {symbol}_map,
}};
""".format(
        attribute=attribute,
        symbol=symbol,
        payload="\n".join(values),
        width=width,
        height=height,
        size=len(data),
    )


def convert_gif(source: Path, destination: Path, symbol: str, attribute: str) -> None:
    data = source.read_bytes()
    width, height = gif_dimensions(data)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(render_c(data, symbol, attribute, width, height), encoding="ascii", newline="\n")
    print(f"GIF {source.name}: {width}x{height}, {len(data)} bytes -> {destination}")


def convert_directory(source_dir: Path, destination_dir: Path) -> None:
    for slot, (filename, symbol, attribute) in SLOTS.items():
        source = source_dir / f"{slot}.gif"
        if source.is_file():
            convert_gif(source, destination_dir / filename, symbol, attribute)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("assets/gifs"))
    parser.add_argument("--output", type=Path, default=Path("src/gif"))
    args = parser.parse_args()
    convert_directory(args.input, args.output)


if __name__ == "__main__":
    main()
