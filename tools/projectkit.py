# -*- coding: utf-8 -*-
"""
projectkit.py — Nạp cấu hình một project: màu nhấn playlist + headline thumbnail (từ youtube_metadata.txt)
và module scenes.py (kịch bản hình) của chính project đó.
"""
import hashlib
import importlib.util
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sticklib  # noqa: E402

DEFAULT_ACCENT = "#FF5A36"


def read_meta(project):
    path = os.path.join(project, "youtube_metadata.txt")
    txt = open(path, encoding="utf-8").read() if os.path.isfile(path) else ""
    m = re.search(r"Màu nhấn:\s*(#[0-9A-Fa-f]{6})", txt)
    accent = m.group(1).upper() if m else DEFAULT_ACCENT
    m = re.search(r'Headline dùng chung:\s*"([^"]+)"(?:[^"]*"([^"]+)")?', txt)
    headline = m.group(1) if m else ""
    accent_word = m.group(2) if m and m.group(2) else (headline.split()[-1] if headline else "")
    # Quy tắc ký tự an toàn 1.3: headline thumbnail bỏ dấu (PERFECCIÓN → PERFECCION)
    strip = lambda t: "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")  # noqa: E731
    return {"accent": accent, "headline": strip(headline), "accent_word": strip(accent_word)}


def load_scenes(project):
    """Đặt màu nhấn rồi nạp <project>/scenes.py (phải định nghĩa build_layers(n, shot))."""
    project = os.path.abspath(project)
    meta = read_meta(project)
    sticklib.set_accent(meta["accent"])
    path = os.path.join(project, "scenes.py")
    name = "scenes_" + hashlib.md5(path.encode()).hexdigest()[:8]
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.META = meta
    return mod
