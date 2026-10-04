# Cúspide Silenciosa — Kênh mới Tiếng Tây Ban Nha

Dự án kênh YouTube **Cúspide Silenciosa (El Camino Disciplinado)**: nội dung về kỷ luật và phát triển bản thân bằng tiếng Tây Ban Nha (Mỹ Latinh), phong cách hoạt hình người que.

> *"La disciplina no hace ruido."*

Kênh giúp người xem hiểu cơ chế tâm lý đằng sau kỷ luật, thói quen và động lực, rồi áp dụng được ngay. Kênh còn mới, chưa có video nào.

## Nội dung repo

| Đường dẫn | Mô tả |
|---|---|
| `docs/flujo-produccion-el-camino-disciplinado.md` | Quy trình tự động hóa sản xuất kênh (v1.0) |
| `docs/README_SUBTITLES.md` | Hướng dẫn công cụ tạo và gắn phụ đề |
| `add_subtitles.py` | Script tạo phụ đề (Whisper, ASS/SRT/VTT, hardsub) |
| `demo/demo_jorge_raw.mp3` | Giọng đọc demo "Jorge" (bản thô) |
| `demo/demo_jorge_pro_studio_30s.mp3` | Giọng đọc demo "Jorge" (bản studio, 30 giây) |
| `tools/align_frames.py` | Căn thời gian từng Frame theo audio (dò khoảng lặng, không cần Whisper) |
| `tools/sticklib.py`, `tools/draw_frames.py` | Vẽ ảnh người que từng Frame bằng code (SVG → PNG) |
| `tools/render_video.py` | Ghép ảnh tĩnh (zoom nhẹ) + giọng đọc + phụ đề karaoke (Anton) → MP4 1080p30 |
| `tools/animate_video.py` | Bản motion graphics: từng lớp bật ra lần lượt, vật nhấn đập nhịp, nhân vật "thở", camera trôi → MP4 |
| `tools/make_thumbnails.py` | Thumbnail Mẫu B (triptych) và Mẫu C (lưới 6 khung) |
| `tools/make_chapters.py` | Chapters với timestamp thật theo audio |
| `fonts/Anton-Regular.ttf` | Font Anton (SIL OFL, xem `fonts/OFL-Anton.txt`) |
| `05_Autoconocimiento/project_28_7_senales_autosabotaje/` | Video "7 Señales de Autosabotaje": script, visuals, metadata, giọng Gonzalo, ảnh, phụ đề, thumbnail, video |

## Workflow dựng video graphic (mọi project)

Mỗi project nằm trong `<playlist>/project_<NN>_<slug>/` với `script.txt`, `transcript_and_visuals.txt`,
`youtube_metadata.txt` (chứa *Màu nhấn* và *Headline dùng chung*), `voz_gonzalo.mp3` và **`scenes.py`**:
kịch bản hình bằng code, gồm `build_layers(n, shot)` cho từng Frame và `thumb_b()` / `thumb_c()` cho thumbnail.
Phần dùng chung nằm trong `tools/` (`sticklib.py`, `scenekit.py`, `thumbkit.py`, `projectkit.py`).

```bash
pip install cairosvg pillow
P="01_Disciplina y Habitos/project_14_5_habitos_cambian_todo"
python3 tools/align_frames.py    --project "$P" --audio voz_gonzalo.mp3   # căn thời gian Frame theo giọng đọc
python3 tools/draw_frames.py     --project "$P"                           # ảnh tĩnh images/img_NNN.png
python3 tools/make_thumbnails.py --project "$P"                           # thumbnail Mẫu B + C
python3 tools/make_chapters.py   --project "$P"                           # chapters.txt (timestamp thật)
python3 tools/animate_video.py   --project "$P" --audio voz_gonzalo.mp3 --title <ten_video>_motion  # video motion graphics
```

| Project | Playlist | Video |
|---|---|---|
| 28 — 7 Señales de Autosabotaje | 05_Autoconocimiento (`#8B6CFF`) | `7_senales_autosabotaje_motion.mp4` |
| 14 — 5 Hábitos Que Cambian Todo | 01_Disciplina y Habitos (`#FF5A36`) | `5_habitos_cambian_todo_motion.mp4` |
| 15 — El Efecto Dominó | 01_Disciplina y Habitos (`#FF5A36`) | `efecto_domino_motion.mp4` |
| 16 — Tu Entorno Decide | 01_Disciplina y Habitos (`#FF5A36`) | `tu_entorno_decide_motion.mp4` |
| 17 — La Regla de las 2 Horas | 01_Disciplina y Habitos (`#FF5A36`) | `regla_2_horas_motion.mp4` |
| 18 — Por Qué la Ducha Fría Cambia Tu Disciplina | 01_Disciplina y Habitos (`#FF5A36`) | `ducha_fria_motion.mp4` |
| 19 — No Es Talento, Es GRIT | 02_Mentalidad y Exito (`#E8A23C`) | `no_es_talento_grit_motion.mp4` |
| 20 — 7 Habilidades Que Toda Persona Debe Dominar | 02_Mentalidad y Exito (`#E8A23C`) | `7_habilidades_clave_motion.mp4` |
| 21 — 5 Lecciones de Vida Que Aprendí Demasiado Tarde | 03_Motivacion y Superacion (`#FF3B78`) | `aprendi_demasiado_tarde_motion.mp4` |
| 22 — 5 Retos Que Muy Pocas Personas Se Atreven a Completar | 03_Motivacion y Superacion (`#FF3B78`) | `5_retos_extremos_motion.mp4` |
| 23 — ¿Buscas Motivación? Deja De Buscarla y Haz Esto | 03_Motivacion y Superacion (`#FF3B78`) | `deja_de_buscar_motivacion_motion.mp4` |
| 25 — Detox Digital de 7 Días: Recupera Tu Cerebro del Scroll | 04_Productividad Practica (`#3BA7C9`) | `detox_digital_7_dias_motion.mp4` |
| 26 — La Técnica Pomodoro Real (No la Versión de tu App) | 04_Productividad Practica (`#3BA7C9`) | `pomodoro_real_motion.mp4` |
| 27 — Por Qué el Multitasking Te Hace Más Lento (Ciencia) | 04_Productividad Practica (`#3BA7C9`) | `multitasking_falso_motion.mp4` |

## Lưu ý

`add_subtitles.py` import package `tools/` (`config`, `transcriber`, `ass_generator`, `srt_generator`, `video_renderer`, `video_assembler`, `xoa_watermark`). Package này chưa có trong repo, nên script chưa chạy được cho đến khi bổ sung.
