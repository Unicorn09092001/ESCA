# 🎬 Subtitle Master — Tool Tạo & Gắn Phụ Đề Kênh Cúspide Silenciosa

Bộ công cụ tự động hóa khâu tạo và gắn phụ đề (Captions / Subtitles) chuyên biệt cho kênh **Cúspide Silenciosa (El Camino Disciplinado)**.

---

## 🌟 Tính Năng Nổi Bật

1. **Nhận diện giọng nói tiếng Tây Ban Nha cực chuẩn:** Tích hợp mô hình `faster-whisper` tối ưu cho chip Apple Silicon, trích xuất timestamp chính xác tới từng từ.
2. **Khớp kịch bản (Script Alignment) 100%:** Tự động đối chiếu với `script.txt` gốc để sửa lỗi chính tả của AI, giữ nguyên dấu câu Tây Ban Nha (`¿`, `¡`, `ñ`, `á`, `é`, `í`, `ó`, `ú`) và chuẩn hóa viết hoa.
3. **Cụm từ giật nhịp High-Retention (3–5 từ):** Giữ nhịp đọc nhanh, cuốn hút, tối ưu thời gian giữ chân người xem (AVD) trên YouTube.
4. **Màu sắc thương hiệu tự động:** Tự động nhận diện Playlist và đổi màu từ khóa highlight theo đúng quy chuẩn nhận diện:
   - `01_Disciplina y Habitos`: Cam-đỏ `#FF5A36`
   - `02_Mentalidad y Exito`: Vàng-hổ phách `#E8A23C`
   - `03_Motivacion y Superacion`: Đỏ-hồng `#FF3B78`
   - `04_Productividad Practica`: Xanh lam nhạt `#3BA7C9`
   - `05_Autoconocimiento`: Tím `#8B6CFF`
5. **Render siêu tốc (Apple VideoToolbox):** Tận dụng phần cứng đồ họa Apple M2 để render video 1080p60 ở tốc độ **~200-300 FPS** (video 6 phút chỉ mất ~20 giây).
6. **Đa dạng đầu ra:** Xuất video hardsub sẵn sàng đăng, đồng thời xuất cả `.srt` (chuẩn YouTube CC), `.vtt` và `.ass`.
7. **Hỗ trợ cả Web UI trực quan và Dòng lệnh CLI.**

---

## 🚀 Hướng Dẫn Sử Dụng Nhanh

Mở Terminal tại thư mục kênh:
```bash
cd "/Users/pvchien/OMMANI/Kênh mới Tiếng Tây Ban Nha"
```

### Cách 1: Sử dụng Giao Diện Web Trực Quan (Web UI)
Chạy lệnh sau để bật giao diện trên trình duyệt:
```bash
.venv/bin/python run_web_ui.py
```
👉 Mở trình duyệt vào địa chỉ: **`http://localhost:8501`**
- Chọn Playlist và Project bạn muốn làm sub.
- Bấm **"📸 Xem Trước 1 Frame"** để kiểm tra vị trí, màu sắc, font chữ.
- Bấm **"⚡ Render Thử Nghiệm 10 Giây"** để xem video chạy thử ngay trên web.
- Bấm **"🚀 Render Video Đầy Đủ"** để xuất video hoàn chỉnh.

---

### Cách 2: Sử dụng Dòng Lệnh (CLI)

#### 1. Xử lý theo thư mục Project (Khuyên dùng):
Chỉ cần truyền đường dẫn thư mục project, tool sẽ tự tìm file video, audio, script và màu playlist:
```bash
# Render video đầy đủ:
.venv/bin/python add_subtitles.py --project "01_Disciplina y Habitos/project_03_rutina_matutina_perfecta_20260904"

# Render thử nghiệm 10 giây đầu (chỉ mất ~2 giây):
.venv/bin/python add_subtitles.py --project "01_Disciplina y Habitos/project_03_rutina_matutina_perfecta_20260904" --preview 10

# Xuất 1 frame ảnh xem trước bố cục tại giây thứ 4:
.venv/bin/python add_subtitles.py --project "01_Disciplina y Habitos/project_03_rutina_matutina_perfecta_20260904" --preview-frame 4.0
```

#### 2. Xử lý một file video bất kỳ:
```bash
.venv/bin/python add_subtitles.py --video "duong/dan/video.mp4" --script "duong/dan/script.txt"
```

#### 3. Chạy hàng loạt cho cả một Playlist:
Tự động duyệt qua toàn bộ các project trong playlist và gắn sub:
```bash
.venv/bin/python add_subtitles.py --playlist "01_Disciplina y Habitos"
```

---

## 🎨 Các Tùy Chọn Kiểu Dáng (Styles)

| Tham số | Giá trị | Mô tả |
|---|---|---|
| `--style` | `karaoke` *(Mặc định)* | Từ đang đọc phát sáng bằng màu nhấn của playlist, các từ còn lại màu trắng ấm. Giữ chân người xem tốt nhất. |
| | `minimalist_dark` | Chữ trắng ấm `#F5F5F0` viền đen sắc nét, không đổi màu từng từ. |
| | `box_pill` | Khung nền đen mờ bo tròn thanh lịch phía sau chữ. |
| `--font` | `Anton` *(Mặc định)* | Font chữ cực đậm, phong cách YouTube hiện đại. (Hỗ trợ `Inter`, `Arial`). |
| `--size` | `64` *(Mặc định)* | Cỡ chữ phụ đề. |
| `--uppercase` | Cờ bật | Viết HOA toàn bộ phụ đề (vd: `TE DESPIERTAS. AGARRAS EL TELÉFONO.`). |
| `--accent` | `#RRGGBB` | Ghi đè màu nhấn thủ công (vd: `--accent "#FF5A36"`). |
| `--only-subs` | Cờ bật | Chỉ tạo file phụ đề `.srt`, `.ass`, `.vtt` mà không render video. |
| `--soft` | Cờ bật | Nhúng track softsub vào file MP4 mà không re-encode (xong ngay lập tức). |

---

## 📁 Cấu Trúc File Xuất Ra

Trong thư mục của mỗi project:
```
project_folder/
├── subtitles/
│   ├── <video_name>.ass           <- File định dạng phụ đề cao cấp (màu sắc, karaoke)
│   ├── <video_name>.srt           <- File chuẩn tải lên YouTube Studio (Closed Captions)
│   ├── <video_name>.vtt           <- File WebVTT
│   └── <video_name>_frame_4.0s.jpg <- Ảnh xem trước (nếu có)
├── <video_name>_subtitled.mp4     <- Video hoàn chỉnh ĐÃ GẮN SUBTITLE
└── <video_name>_preview_10s.mp4   <- Video 10 giây xem trước (nếu chạy --preview 10)
```
