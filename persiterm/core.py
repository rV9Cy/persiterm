import re
import arabic_reshaper
try:
    from bidi import get_display          # python-bidi >= 0.5
except ImportError:
    from bidi.algorithm import get_display  # python-bidi 0.4.x

_ANSI = re.compile(r"(\x1b\[[0-9;?]*[ -/]*[@-~])")
_PERSIAN = re.compile(r"[\u0600-\u06FF\uFB50-\uFDFF\uFE70-\uFEFF]")
_reshaper = arabic_reshaper.ArabicReshaper(
    configuration={"delete_harakat": False, "support_ligatures": True})


def fix_line(line: str, bidi: bool = True) -> str:
    """Reshape Persian letters and reorder visually. ANSI colors are kept."""
    if not _PERSIAN.search(line):
        return line
    parts = _ANSI.split(line)
    if len(parts) == 1:
        text = _reshaper.reshape(line)
        return get_display(text) if bidi else text
    # Has ANSI codes: fix each text chunk separately, keep the codes.
    return "".join(p if _ANSI.fullmatch(p) else fix_line(p, bidi) for p in parts)
