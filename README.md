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
| `fonts/Anton-Regular.ttf` | Font Anton (SIL OFL, xem `fonts/OFL-Anton.txt`) |
| `05_Autoconocimiento/project_28_7_senales_autosabotaje/` | Video "7 Señales de Autosabotaje": script, visuals, metadata, giọng Gonzalo, ảnh, phụ đề, thumbnail, video |

## Dựng video graphic (project 28)

```bash
pip install cairosvg pillow
P="05_Autoconocimiento/project_28_7_senales_autosabotaje"
python3 tools/align_frames.py   --project "$P" --audio voz_gonzalo.mp3
python3 tools/draw_frames.py    --project "$P"
python3 tools/make_thumbnails.py --project "$P"
python3 tools/render_video.py   --project "$P" --audio voz_gonzalo.mp3 --title 7_senales_autosabotaje
# Bản chuyển động (khuyên dùng), thêm --preview 20 để xem thử 20 giây đầu:
python3 tools/animate_video.py  --project "$P" --audio voz_gonzalo.mp3 --title 7_senales_autosabotaje_motion
```

## Playlist

| Playlist | Màu nhấn |
|---|---|
| 01_Disciplina y Habitos | `#FF5A36` |
| 02_Mentalidad y Exito | `#E8A23C` |
| 03_Motivacion y Superacion | `#FF3B78` |
| 04_Productividad Practica | `#3BA7C9` |
| 05_Autoconocimiento | `#8B6CFF` |

## Lưu ý

`add_subtitles.py` import package `tools/` (`config`, `transcriber`, `ass_generator`, `srt_generator`, `video_renderer`, `video_assembler`, `xoa_watermark`). Package này chưa có trong repo, nên script chưa chạy được cho đến khi bổ sung.
