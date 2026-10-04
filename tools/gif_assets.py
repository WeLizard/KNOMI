"""PlatformIO pre-build hook for optional custom KNOMI GIFs."""

Import("env")

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gif_to_c import convert_directory


project_dir = Path(env.subst("$PROJECT_DIR"))
convert_directory(project_dir / "assets" / "gifs", project_dir / "src" / "gif")
