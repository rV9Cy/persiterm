import os, platform, shutil, subprocess, sys, urllib.request

FONT_URL = ("https://github.com/rastikerdar/vazirmatn/raw/master/"
            "fonts/ttf/Vazirmatn-Regular.ttf")
FONT_NAME = "Vazirmatn"


def _download(dest, url):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    print(f"downloading {url}")
    urllib.request.urlretrieve(url, dest)


def _is_termux():
    return "com.termux" in os.environ.get("PREFIX", "") or os.path.isdir("/data/data/com.termux")


def install_font(url=FONT_URL):
    system = platform.system()
    fname = os.path.basename(url)
    if _is_termux():
        dest = os.path.expanduser("~/.termux/font.ttf")
        _download(dest, url)
        if shutil.which("termux-reload-settings"):
            subprocess.call(["termux-reload-settings"])
        print("Termux font installed. Swipe/restart the session if it did not change.")
    elif system == "Linux":
        dest = os.path.expanduser(f"~/.local/share/fonts/{fname}")
        _download(dest, url)
        subprocess.call(["fc-cache", "-f"])
        _linux_set_terminal_font()
    elif system == "Windows":
        _windows_install(url, fname)
    elif system == "Darwin":
        dest = os.path.expanduser(f"~/Library/Fonts/{fname}")
        _download(dest, url)
        print(f"Installed. Select '{FONT_NAME}' in your terminal's font settings.")
    else:
        sys.exit(f"Unsupported platform: {system}")


def _linux_set_terminal_font():
    if shutil.which("gsettings"):
        try:
            profile = subprocess.check_output(
                ["gsettings", "get", "org.gnome.Terminal.ProfilesList", "default"],
                text=True).strip().strip("'")
            base = f"org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles-:{profile}/"
            subprocess.check_call(["gsettings", "set", base, "use-system-font", "false"])
            subprocess.check_call(["gsettings", "set", base, "font", f"{FONT_NAME} 12"])
            print("GNOME Terminal font set.")
            return
        except Exception:
            pass
    print(f"Font installed. Select '{FONT_NAME}' manually in your terminal "
          "(kitty/alacritty: set font family in the config file).")


def _windows_install(url, fname):
    import winreg  # noqa
    local = os.environ["LOCALAPPDATA"]
    dest = os.path.join(local, "Microsoft", "Windows", "Fonts", fname)
    _download(dest, url)
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER,
                           r"Software\Microsoft\Windows NT\CurrentVersion\Fonts")
    winreg.SetValueEx(key, f"{FONT_NAME} (TrueType)", 0, winreg.REG_SZ, dest)
    print("Font installed for current user.")
    print(f'Windows Terminal: Settings > Defaults > Appearance > Font face = "{FONT_NAME}"')
    print("PowerShell/cmd (old console window): only raster/Consolas-like fonts are "
          "allowed there; use Windows Terminal instead.")
