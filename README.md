<p align="center">
  <img src="assets/banner.png" alt="persiterm banner" width="100%">
</p>

<p align="center">
  <img src="assets/profile.png" alt="persiterm logo" width="120">
</p>

<h1 align="center">persiterm</h1>

<p align="center">
  <b>Readable Persian in every terminal · فارسی خوانا در همه ترمینال‌ها</b><br>
  Termux · Linux · macOS · Windows
</p>

<p align="center">
  <a href="#-english">English</a> · <a href="#-فارسی">فارسی</a> · <a href="https://t.me/rv8dev">Telegram: @rv8dev</a>
</p>

---

## 🇬🇧 English

Most terminals can't join Persian letters or display right-to-left text, so you get isolated, reversed letters. **persiterm** fixes that in two ways:

1. **Text filter**: reshapes Persian letters and reorders them visually, so any output becomes readable.
2. **Font installer**: downloads and installs the [Vazirmatn](https://github.com/rastikerdar/vazirmatn) font and, where possible, sets it in your terminal.

### Install

Requires Python 3.8+.

```bash
unzip persiterm.zip
cd persiterm
pip install .
```

**Termux:** run `pkg install python unzip` first.

### Use

```bash
# 1) fix a piece of text
persiterm print "سلام دنیا"

# 2) fix anything piped into it
echo "سلام دنیا" | persiterm fix
cat notes.txt | persiterm fix

# 3) run a command and fix its output
persiterm run ls -la

# 4) install the Persian font
persiterm font
```

If your terminal already supports RTL (e.g. mlterm), use `persiterm fix --no-bidi`, otherwise the text will be reversed twice.

If the `persiterm` command is not found (common on Windows), use:

```bash
python -m persiterm.cli print "سلام"
```

### Terminal support

| Terminal | Text filter | Font install | Font auto-set |
|---|:---:|:---:|:---:|
| Termux | ✅ | ✅ | ✅ |
| GNOME Terminal | ✅ | ✅ | ✅ |
| Other Linux terminals (kitty, Alacritty, Konsole, xterm…) | ✅ | ✅ | ❌ set manually |
| macOS Terminal / iTerm | ✅ | ✅ | ❌ set manually |
| Windows Terminal | ✅ | ✅ | ❌ set manually |
| Legacy cmd / PowerShell window | ✅ | ✅ | ❌ not possible |

> On Windows, use **Windows Terminal** instead of the old console window. Open *Settings → Defaults → Appearance* and set Font face to `Vazirmatn`.

### Limitations

- Output is in *visual order*. Don't copy it back into code or files.
- Very long lines that wrap in the terminal may break.
- Vazirmatn is not strictly monospace, so columns may look slightly uneven.

---

<div dir="rtl" align="right">

## 🇮🇷 فارسی

اکثر ترمینال‌ها حروف فارسی را بهم نمی‌چسبانند و راست‌چین هم نمی‌کنند، برای همین حروف جدا و برعکس نمایش داده می‌شوند. **persiterm** این مشکل را به دو روش حل می‌کند:

1. **فیلتر متن:** حروف فارسی را بهم می‌چسباند و ترتیب نمایش را درست می‌کند تا هر خروجی خوانا شود.
2. **نصب فونت:** فونت [وزیرمتن](https://github.com/rastikerdar/vazirmatn) را دانلود و نصب می‌کند و اگر ترمینال اجازه بدهد، خودش تنظیمش می‌کند.

### نصب

پایتون ۳.۸ یا بالاتر لازم است.

```bash
unzip persiterm.zip
cd persiterm
pip install .
```

**ترموکس:** اول `pkg install python unzip` را بزنید.

### استفاده

```bash
# ۱) درست کردن یک متن
persiterm print "سلام دنیا"

# ۲) درست کردن هر چیزی که با pipe بهش بدهید
echo "سلام دنیا" | persiterm fix
cat notes.txt | persiterm fix

# ۳) اجرای یک دستور و درست کردن خروجی‌اش
persiterm run ls -la

# ۴) نصب فونت فارسی
persiterm font
```

اگر ترمینال شما خودش RTL دارد (مثل mlterm)، از `persiterm fix --no-bidi` استفاده کنید، وگرنه متن دوبار برعکس می‌شود.

اگر دستور `persiterm` شناخته نشد (در ویندوز زیاد پیش می‌آید)، این را بزنید:

```bash
python -m persiterm.cli print "سلام"
```

### ترمینال‌های پشتیبانی‌شده

| ترمینال | فیلتر متن | نصب فونت | تنظیم خودکار فونت |
|---|:---:|:---:|:---:|
| Termux | ✅ | ✅ | ✅ |
| GNOME Terminal | ✅ | ✅ | ✅ |
| بقیه ترمینال‌های لینوکس (kitty، Alacritty، Konsole، xterm…) | ✅ | ✅ | ❌ دستی |
| ترمینال مک / iTerm | ✅ | ✅ | ❌ دستی |
| Windows Terminal | ✅ | ✅ | ❌ دستی |
| cmd / PowerShell قدیمی | ✅ | ✅ | ❌ ممکن نیست |

> در ویندوز به‌جای پنجره‌ی قدیمی cmd از **Windows Terminal** استفاده کنید. از *Settings ← Defaults ← Appearance* فونت را روی `Vazirmatn` بگذارید.

### محدودیت‌ها

- خروجی به ترتیب نمایشی است. آن را داخل کد یا فایل کپی نکنید.
- خطوط خیلی طولانی که در ترمینال wrap می‌شوند ممکن است خراب شوند.
- وزیرمتن کاملاً monospace نیست و ستون‌ها ممکن است کمی ناهم‌تراز دیده شوند.

</div>

---

<p align="center">
  Made by <b>rV8Dev</b> · <a href="https://t.me/rv8dev">@rv8dev</a>
</p>
