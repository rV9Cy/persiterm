import argparse, subprocess, sys
from .core import fix_line


def _stream(bidi):
    out = sys.stdout
    for line in sys.stdin:
        out.write(fix_line(line.rstrip("\n"), bidi) + "\n")
        out.flush()


def main():
    p = argparse.ArgumentParser(prog="persiterm",
        description="Readable Persian in terminals without RTL support.")
    sub = p.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fix", help="filter: echo 'سلام' | persiterm fix")
    f.add_argument("--no-bidi", action="store_true",
                   help="reshape only (for terminals that already do RTL)")

    pr = sub.add_parser("print", help="print arguments fixed")
    pr.add_argument("text", nargs="+")

    r = sub.add_parser("run", help="run a command and fix its output")
    r.add_argument("command", nargs=argparse.REMAINDER)

    fo = sub.add_parser("font", help="install Persian font")
    fo.add_argument("--url", help="custom .ttf URL (default: Vazirmatn)")

    a = p.parse_args()
    if a.cmd == "fix":
        _stream(not a.no_bidi)
    elif a.cmd == "print":
        print(fix_line(" ".join(a.text)))
    elif a.cmd == "run":
        proc = subprocess.Popen(a.command, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True)
        for line in proc.stdout:
            print(fix_line(line.rstrip("\n")))
        sys.exit(proc.wait())
    elif a.cmd == "font":
        from .fonts import install_font, FONT_URL
        install_font(a.url or FONT_URL)
