"""PlatformIO pre-build hook for optional custom KNOMI GIFs."""

Import("env")

from pathlib import Path
import sys

project_dir = Path(env.subst("$PROJECT_DIR"))
sys.path.insert(0, str(project_dir / "tools"))
from gif_to_c import convert_directory


convert_directory(project_dir / "assets" / "gifs", project_dir / "src" / "gif")
