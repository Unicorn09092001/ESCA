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
