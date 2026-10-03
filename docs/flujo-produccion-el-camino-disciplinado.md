# Quy Trình Tự Động Hóa Kênh YouTube — Cúspide Silenciosa — v1.0

> **NGÁCH KÊNH: DISCIPLINA Y CRECIMIENTO PERSONAL (kỷ luật & phát triển bản thân), tiếng Tây Ban Nha, phong cách hoạt hình người que.**
> Kênh **Cúspide Silenciosa** giúp người xem nói tiếng Tây Ban Nha (Mỹ Latinh) **hiểu cơ chế tâm lý đằng sau kỷ luật, thói quen và động lực — và áp dụng được ngay**. Mọi nội dung phải trả lời được câu hỏi: *"¿Este video me ayuda a ser más disciplinado, entender mi propia mente, o actuar hoy mismo — y explica el mecanismo detrás?"*
> Slogan: *"La disciplina no hace ruido."* — câu này là hằng số thương hiệu, xuất hiện trên banner kênh và có thể lặp lại trong outro của video.

---

## 📌 Ghi chú chuyển thể (đọc trước khi dùng)

Tài liệu này được viết lại từ quy trình sản xuất của một kênh khác (Synapse Secrets — khoa học não bộ, tiếng Anh, đã có 40+ video và dữ liệu hiệu suất thật). **Cúspide Silenciosa là kênh MỚI, chưa có video nào, chưa có dữ liệu.** Vì vậy:

- **Những gì GIỮ LẠI:** toàn bộ *phương pháp luận* — nguyên tắc "đóng gói trước khi viết kịch bản", cấu trúc kịch bản Gancho + Módulo đánh số + Cierre (xem Bước 2.3 — cập nhật 2026-09-02 sau khi phân tích transcript thật của 4 kênh tham khảo, xem `phan-tich-phong-cach-viet-kich-ban-doi-thu.md`), kỹ thuật giữ chân (pattern interrupt/open loop), quy tắc chia Frame hình ảnh theo câu/mệnh đề, kỷ luật đo lường & viết log hiệu suất, các "escape hatch" thử nghiệm có kiểm chứng. Đây là phần đã được chứng minh có giá trị bất kể ngách hay ngôn ngữ.
- **Những gì THAY ĐỔI HẲN:** ngách nội dung, ngôn ngữ (Tây Ban Nha thay vì tiếng Anh), hệ thống màu/thiết kế thumbnail (kênh này đã có bộ nhận diện riêng — nền đen, không dùng khối chữ vàng), độ dài video mục tiêu (dựa trên dữ liệu THẬT của 3 kênh đối thủ cùng ngách mà mình đã khảo sát, không phải số liệu của kênh khoa học não bộ), bộ công cụ sản xuất (kênh mới chưa có script Python riêng, dùng bộ công cụ đã đề xuất trong `kenh-youtube-tbn-strategy.md`).
- **Vì chưa có dữ liệu nội bộ:** mọi con số ở đây (độ dài, tốc độ đọc, CTR mục tiêu) là **ước tính ban đầu dựa trên nghiên cứu đối thủ**, không phải kết luận đã kiểm chứng. Tài liệu đánh dấu rõ chỗ nào cần đo lại bằng dữ liệu thật sau 5-10 video đầu, giống đúng kỷ luật mà bản gốc đã áp dụng.

---

## Bước 0: Nghiên Cứu & Đánh Giá Chủ Đề (Topic Greenlight)

TRƯỚC KHI làm bất kỳ nội dung nào, chủ đề phải vượt qua bài kiểm tra "Topic Greenlight":

- **Câu hỏi cổng (Gate Question):** *"Chủ đề này có giúp người xem KỶ LUẬT hơn / XÂY THÓI QUEN tốt hơn / HÀNH ĐỘNG ngay hôm nay (và giải thích được bằng cơ chế tâm lý), HOẶC giúp người xem tự nhận diện một nét tính cách/thói quen phổ biến của chính mình (Trụ cột 5)?"* Nếu KHÔNG với cả hai → từ chối.

- **Kiểm tra ngách (Niche Check):** Chủ đề BẮT BUỘC thuộc 1 trong 5 trụ cột sau (đúng theo tỉ trọng đã chốt ở `kenh-youtube-tbn-strategy.md`):

  1. ⭐ **Disciplina y Hábitos (40%):** rutinas matutinas/nocturnas, consistencia, "disciplina silenciosa", cómo mantener un hábito, romper malos hábitos. → *Trụ cột mạnh nhất — khớp trực tiếp với nội dung ăn khách nhất của cả 3 kênh đối thủ (Night Habits, 20 Tiny Habits, habits create success).*
  2. ⭐ **Mentalidad y Psicología del Éxito (25%):** tư duy thành công, tự kiểm soát, kỷ luật tinh thần, cơ chế tâm lý đằng sau ý chí. → *(8 Rare Discipline Habits, No Excuse.)*
  3. **Motivación y Superación (bổ sung vào 25% trên):** thử thách cá nhân, câu chuyện chuyển hóa, vượt qua giới hạn bản thân. → *(10 Rare Solo Challenges, 13 Life Lessons.)*
  4. **Productividad Práctica (20%):** tập trung, quản lý thời gian, ngừng trì hoãn, cai nghiện xao nhãng số (điện thoại/mạng xã hội). → *(fix your focus, quit p*rn addiction — góc dopamine/xao nhãng.)*
  5. 🆕 **Autoconocimiento — Rasgos y Hábitos que te Definen (15%):** mô tả/tự-nhận-diện một nét tính cách hoặc thói quen tâm lý-xã hội phổ biến ("¿Esto te pasa a ti?"). CHỈ dạng mô tả/tự-nhận-diện, KHÔNG dạy kỹ thuật thao túng người khác. Viết theo đúng cấu trúc mặc định ở Bước 2.3 (Gancho + Módulo đánh số + Cierre). → *Trụ cột thử nghiệm: kênh tham khảo gần ngách nhất (kênh khoa học não bộ) ghi nhận nội dung tự-chẩn-đoán đạt hiệu suất cao gấp 2 lần trung bình kênh — đáng thử nhưng CHƯA có bằng chứng nội bộ của Cúspide Silenciosa, theo dõi riêng ở Bước 6.4.*

  Nếu chủ đề KHÔNG thuộc 5 trụ cột trên → **TỪ CHỐI** và đề xuất chủ đề thay thế.

- **NGOÀI NGÁCH (từ chối thẳng):** dark psychology / kỹ thuật thao túng người khác *(khác với "autoconocimiento" mô tả/tự-nhận-diện ở Trụ cột 5)*; sức khỏe tâm thần lâm sàng thuần túy không gắn kỷ luật/thói quen (trầm cảm, rối loạn lo âu nặng — luôn khuyến nghị tìm chuyên gia, không tự biến thành nội dung "chữa trị"); làm giàu nhanh / manifesting / luật hấp dẫn không có cơ sở; nội dung chính trị hoặc tôn giáo; "motivación vacía" không có cơ chế hay hành động cụ thể đi kèm (đây chính là thứ Productividad-Real — kênh tham khảo — cố tình tránh: *"Sin motivación vacía. Solo lo que funciona."*).

- **Kiểm tra trùng lặp (Duplicate Check):** Liệt kê tên TẤT CẢ thư mục `project_*` trong 5 Playlist Folder dưới `OMMANI/Kênh mới Tiếng Tây Ban Nha/` (xem Bước 3.1) và so sánh chủ đề mới. *Kênh hiện chưa có project nào — bước này bắt đầu có tác dụng từ video thứ 2 trở đi.* Nếu liên quan video cũ, BẮT BUỘC tiếp cận từ góc khác và ghi chú rõ khác biệt.

- **Outlier Check (2 lớp):**
  - *Lớp ngoài:* Ưu tiên chủ đề mà 3 kênh cùng ngách đã khảo sát (**@007Method** 2,29K subs/30 video, **@SilentApex07** 1,48K subs/9 video, **@TheInspirePath7** 164K subs/64 video) đang có video views vượt trội so với trung bình kênh của họ, hoặc chủ đề lặp lại ở cả 3 kênh (dấu hiệu ngách đang "ăn"). Bổ sung tìm kiếm outlier tiếng Tây Ban Nha (WutNexLev/PsychToons-style content nếu có bản dịch/kênh tương đương ở thị trường LatAm).
  - *Lớp nội bộ:* Đối chiếu `channel_performance_log.md` (xem Bước 6.4). **Hiện đang trống — kênh mới.** Từ video thứ 5 trở đi, bắt đầu ưu tiên nhân bản/mở rộng chủ đề đã thắng trên chính kênh thay vì chỉ dựa vào đối thủ.

- **Điểm neo cảm xúc (Emotional Trigger):** Chủ đề phải đánh vào 1 trong 4: Tò mò (Curiosidad), Sợ hãi/Cấp bách (Miedo — *"estás saboteando tu propia disciplina sin darte cuenta"*), Phản trực giác (Contraintuitivo), hoặc Nhận diện bản thân (Autoidentificación — *"esto es exactamente lo que me pasa"*).

## Bước 0.5: Reverse Engineer Outlier (Tiền xử lý)

TRƯỚC KHI viết tiêu đề và prompt thumbnail cho mỗi dự án mới:
1. Tìm 3-5 video outlier từ 3 kênh tham khảo (hoặc kênh tiếng Tây Ban Nha cùng ngách nếu tìm được) — ưu tiên video có views/subscriber ratio cao.
2. Ghi lại thumbnail + tiêu đề của từng video outlier.
3. Phân tích điểm chung: công thức tiêu đề? bố cục ảnh? biểu cảm nhân vật?
4. Áp dụng vào packaging của video mới. Lưu phân tích vào `youtube_metadata.txt`.

## Bước 1: Thiết Kế Tiêu Đề & Thumbnail (Packaging-First Principle)

Tuyệt đối KHÔNG viết kịch bản khi chưa chốt Tiêu đề và ý tưởng Thumbnail. Kịch bản sinh ra để phục vụ lời hứa của Tiêu đề.

### Tiêu đề (Title)

- Đề xuất **chính xác 3 tiêu đề** bằng **tiếng Tây Ban Nha (Mỹ Latinh trung lập)**, độ dài **≤ 60 ký tự** (lý tưởng 40-55 để không bị cắt trên mobile).
- **Front-load:** đặt từ khóa chính và hook vào 40% đầu tiên của tiêu đề.
- **Từ khóa tìm kiếm:** mỗi tiêu đề PHẢI chứa ≥ 1 cụm từ khóa người xem thật sự gõ (`hábitos`, `disciplina`, `cómo dejar de procrastinar`, `cómo enfocarte`, `rutina matutina`, `fuerza de voluntad`).
- **5 khuôn tiêu đề** (rút từ tiêu đề thật của 3 kênh tiếng Anh tham khảo — ưu tiên từ trên xuống):

  | Khuôn | Cách làm | Ví dụ (đã dịch/phỏng theo tiêu đề thật của đối thủ) |
  |---|---|---|
  | **A. Đếm danh sách** ⭐ mạnh nhất | Số lượng thói quen/dấu hiệu/bước. **Ưu tiên số LẺ/cụ thể (5, 7, 9, 3) hơn số tròn (10, 20)** khi hợp lý — khớp pattern thật quan sát ở Productividad Real (kênh tiếng Tây Ban Nha, xem cập nhật 2026-09-02 dưới đây). | `7 Hábitos Que Te Harán Irreconocible` *(gốc: "20 Tiny Habits That Will Make You Unrecognizable")* |
  | **B. Khung thời gian + biến đổi** | Mốc thời gian cụ thể + kết quả | `30 Días. 4 Reglas. Otra Persona.` *(gốc: "30 Days. 4 Rules. Become a Completely Different Person")* |
  | **C. Phủ định/tương phản** | Bác bỏ điều người xem đang tin | `No Es Pereza — Es Otra Cosa` |
  | **D. Mệnh lệnh + chú thích ngoặc đơn** | Hành động cụ thể + làm rõ cách | `Haz Esto Para Resetear Tu Mente (En 5 Minutos)` *(gốc: "Do This to Completely Reset Your Mind")* |
  | **E. So sánh ưu việt** | So với đa số | `Estos Hábitos Te Harán Más Disciplinado Que el 99%` *(gốc: "More Disciplined Than 99% of Men")* |

- **Mệnh đề phụ trong ngoặc đơn (cập nhật 2026-09-02) — áp dụng cho CẢ 5 khuôn, không riêng Khuôn D:** thêm 1 cụm ngắn trong ngoặc đơn nêu cơ chế/thời hạn/tương phản để tăng tính cụ thể, VD `(Sin Fuerza de Voluntad)`, `(Respaldado por la Ciencia)`, `(No Es lo que Piensas)` — mẫu này xuất hiện rất nhất quán ở Productividad Real (kênh tiếng Tây Ban Nha thật): *"...que Occidente IGNORA"*, *"...Sin Dieta ni Gimnasio"*, *"...No Es Falta de Voluntad"*.
- **Viết HOA 1-3 từ khoá cảm xúc/lợi ích giữa câu — BẮT BUỘC, không còn là tuỳ chọn** (cập nhật 2026-09-02, sửa từ hướng dẫn "có thể viết hoa" cũ): đây là kỹ thuật chủ đạo và nhất quán quan sát được ở Productividad Real (VD *"FRENAN el ENVEJECIMIENTO"*, *"5 Hábitos que ELIMINAN la Grasa"*) — không phải Title Case thông thường, mà là CAPS TOÀN BỘ cho đúng 1-3 từ mang cảm xúc/lợi ích chính, phần còn lại giữ nguyên chữ thường.
- **Emoji dẫn đầu tiêu đề — khuyến nghị ưu tiên** (cập nhật 2026-09-02, thay cho "không bắt buộc" cũ): quy tắc cũ dựa trên 2/3 kênh TIẾNG ANH không dùng emoji. Productividad Real — dữ liệu tiếng Tây Ban Nha thật, kênh gần thị trường mục tiêu nhất — dùng emoji dẫn đầu ở gần như MỌI tiêu đề (🇯🇵🍚🌙🤫🧠), thường gắn với chủ đề video (không chỉ trang trí). Nên đưa emoji dẫn đầu thành lựa chọn ưu tiên khi đặt tiêu đề, không còn xem là tuỳ chọn phụ.

### Câu lệnh tạo ảnh Thumbnail — THUMBNAIL SYSTEM v1.0

> **NGUYÊN TẮC CỐT LÕI 1:** Thumbnail là POSTER quảng cáo, KHÔNG phải khung hình trong video.
>
> **NGUYÊN TẮC CỐT LÕI 2:** Thumbnail cạnh tranh với các ô ảnh khác trong feed. Tương phản nội bộ ảnh chỉ là điều kiện cần — điều kiện đủ là tương phản với NỀN GIAO DIỆN và các ô ảnh hàng xóm.

#### 🔬 Căn cứ — soi 27 thumbnail thật của 3 kênh cùng ngách (29/08/2026)

| Kênh | Quy mô | Công thức lặp lại |
|---|---|---|
| **@007Method** | 2,29K subs · 30 video | Nền **tối/ảnh chụp lọc màu tối**, ảnh ghép 3 khung (triptych) kể chuyện trước-trong-sau, chữ trắng đậm khổng lồ, 1 badge tròn góc trái nhận diện kênh |
| **@SilentApex07** | 1,48K subs · 9 video | Nền tối, nhân vật minh họa phong cách manga, chữ trắng + đỏ nhấn, thanh tiến trình đỏ dưới cùng |
| **@TheInspirePath7** | 164K subs · 64 video | Nền tối, nhân vật minh họa 3 khung kể chuyện chuyển hóa, chữ trắng + đỏ nhấn, icon toggle switch lặp lại |

**Kết luận — khác hẳn hướng "nền sáng" của kênh khoa học não bộ tham khảo:** ngách *disciplina/motivation* tiếng Anh mà 3 kênh này đang khai thác dùng **nền TỐI gần như tuyệt đối** (0/27 ảnh dùng nền sáng).

> ⚠️ **Cập nhật 2026-09-02 — làm rõ lại kết luận trên, không phải hủy bỏ:** kết luận "nền tối là chuẩn ngách" ở trên CHỈ dựa trên 3 kênh TIẾNG ANH. Khi soi thêm **Productividad Real** (kênh tiếng Tây Ban Nha, 83,3K sub — kênh gần thị trường mục tiêu của Cúspide Silenciosa nhất trong 4 kênh tham khảo), thumbnail của họ dùng **nền ẤM/kem/be**, không tối, và vẫn hiệu quả ở quy mô lớn. Vậy "nền tối = chuẩn mực toàn ngách" là kết luận quá tự tin — thực ra đây là **một lựa chọn khác biệt hoá có chủ đích** (giúp Cúspide Silenciosa nổi bật khác Productividad Real trong feed), không phải quy luật bắt buộc của cả thị trường tiếng Tây Ban Nha. **Không đổi màu nền thật** — bộ nhận diện (avatar/banner/thumbnail template) đã publish dựa trên nền tối, giữ nguyên vì đây vẫn là lựa chọn hợp lý, chỉ sửa lại cách diễn đạt để không đánh giá sai tín hiệu thị trường.

Cúspide Silenciosa **giữ nguyên nền tối**, khớp với bộ nhận diện đã dựng (avatar/banner/thumbnail template đã publish) — như một lựa chọn khác biệt hoá có chủ đích, không phải vì "cả ngách đều làm vậy".

#### 🎨 BẢNG MÀU v1.0 — khớp với bộ nhận diện đã publish, không đổi

| Vai trò | Mã màu | Ghi chú |
|---|---|---|
| **Nền** | Đen ấm `#0B0B0C` | Hằng số thương hiệu — giống avatar/banner đã dựng |
| **Nhân vật/chữ chính** | Trắng ấm `#F5F5F0` | Không dùng trắng tinh `#FFFFFF` |
| **Màu nhấn chính (01_Disciplina y Hábitos)** | Cam-đỏ `#FF5A36` | Hằng số brand — dùng cho từ khóa nhấn trong chữ, thanh dưới cùng, badge |
| Màu nhấn 02_Mentalidad y Éxito | Vàng-hổ phách `#E8A23C` | |
| Màu nhấn 03_Motivación y Superación | Đỏ-hồng `#FF3B78` | |
| Màu nhấn 04_Productividad Práctica | Xanh lam nhạt `#3BA7C9` | Liên tưởng "tập trung, bình tĩnh" |
| Màu nhấn 05_Autoconocimiento | Tím `#8B6CFF` | Liên tưởng "nội tâm" |

> Ba yếu tố **nền đen · nhân vật/chữ trắng ấm · badge góc trái hình núi** là **hằng số thương hiệu**, không đổi theo playlist. Chỉ **một** màu nhấn (theo bảng trên) thay đổi theo playlist — dùng cho TỪ KHÓA được nhấn mạnh trong headline và cho panel/vật thể ẩn dụ trong ảnh.

#### QUY TẮC 1 — Nền TỐI, nhân vật/chữ SÁNG (giữ nguyên chuẩn ngách)

- Nền: độ sáng ≤ 20% — đen ấm `#0B0B0C`, KHÔNG gradient sáng, KHÔNG texture giấy.
- Nhân vật **người que** (DNA hình ảnh của kênh — xem `el-camino-disciplinado-branding.html`): nét trắng ấm `#F5F5F0`, tô đặc hoặc nét dày ≥ 8px, KHÔNG phải nét mảnh kiểu sketch.
- Có thể dùng gradient màu ẤM TỐI (nâu cháy → màu nhấn) ở phần dưới khung hình để tạo chiều sâu — đây là kỹ thuật cả 3 kênh tham khảo đều dùng (không phải nền phẳng tuyệt đối).
- **CẤM tầng xám giữa chiếm > 20% diện tích ảnh.**
- ✅ **Test bóng đen:** chuyển ảnh sang trắng đen → làm mờ 8px → thu về 160×90. Vẫn phải thấy rõ MỘT hình khối chính (nhân vật người que).
- ✅ **Test hàng xóm:** dán ảnh vào feed YouTube cạnh 5-6 thumbnail khác, lùi 1 mét — mắt phải rơi vào ảnh mình trước.

#### QUY TẮC 2 — Giữ đúng DNA "người que", không lẫn sang phong cách khác

- Nhân vật LUÔN là stick figure: đầu tròn, thân/tay/chân là nét thẳng hoặc SVG đơn giản — đây là điểm khác biệt cố ý so với phong cách nhân vật manga/ảnh chụp của 3 kênh tham khảo (nhanh sản xuất hơn, chi phí thấp hơn, và là lựa chọn thương hiệu đã chốt).
- **CẤM** chuyển sang minh họa chi tiết kiểu manga/anime hay ảnh người thật trong bộ thumbnail chính — nếu muốn thử nghiệm phong cách nhân vật thật, làm theo escape hatch riêng (xem Bước 6.4), không trộn vào bộ mặc định.
- Prompt bắt buộc chứa: `minimalist stick figure character, thick rounded white/cream strokes (#F5F5F0), solid dark background (#0B0B0C), bold flat illustration, NO detailed anime/manga rendering, NO photorealistic face`

#### QUY TẮC 3 — Cận cảnh một nhân vật (MẶC ĐỊNH) hoặc triptych (thử nghiệm phụ)

> ✏️ **Cập nhật 2026-09-02 — đảo thứ tự ưu tiên so với bản gốc:** bản gốc coi triptych là bố cục CTR cao nhất vì 007 Method/Inspire Path dùng chủ yếu — nhưng cả hai đều dựng triptych từ ẢNH CHỤP THẬT hoặc minh họa anime CHI TIẾT, nơi 3 khung đủ khác biệt để mắt phân biệt nhanh. DNA "người que" tối giản (đầu tròn, nét thẳng, không chi tiết mặt) khi đặt 3 khung cạnh nhau ở kích thước nhỏ (160×90, ảnh đại diện trong feed) rất dễ trông LẶP/MỜ vì thiếu chi tiết phân biệt giữa các khung. Bằng chứng ủng hộ: **Productividad Real** — kênh DUY NHẤT trong 4 kênh tham khảo cũng dùng nhân vật người que/vector tối giản — KHÔNG dùng triptych, luôn luôn 1 cảnh/1 nhân vật. Đây là kênh gần thị trường mục tiêu nhất, nên ưu tiên theo cách làm của họ hơn 2 kênh ảnh chụp/anime.

1. **Cận cảnh một nhân vật (MẶC ĐỊNH)** — nhân vật người que chiếm 50-70% khung, một vật thể ẩn dụ màu nhấn bên cạnh (Silent Apex và Productividad Real đều dùng chủ yếu cách này, dù khác phong cách nhân vật).
2. **Triptych 3 khung (thử nghiệm phụ, không mặc định)** — kể chuyện trước → giữa → sau. Chỉ dùng khi có lý do rõ ràng (VD chủ đề "trước/trong/sau" mạnh) và PHẢI kiểm tra kỹ bằng Test bóng đen (Quy tắc 1) ở đúng kích thước 160×90 trước khi chốt — nếu 3 khung người que trông lẫn vào nhau, quay lại phương án 1.

**CẤM** bố cục 2 nhân vật ngang hàng không rõ vai trò — nếu cần ý "so sánh", dùng escape hatch tương tự Quy tắc 3 của bản gốc: mỗi nửa phải có nhãn chữ riêng và lệch độ sáng rõ rệt, nếu không sẽ nhòe ở 160×90.

#### QUY TẮC 4 — Đếm yếu tố: tối đa 3 yếu tố, tối đa 2 nhóm thị giác

- Yếu tố: 1 = nhân vật · 2 = vật thể ẩn dụ/màu nhấn · 3 = chữ headline. Hết.
- Không yếu tố nào nhỏ hơn 8% chiều cao ảnh.
- CẤM chùm icon nhỏ, nhiều mũi tên, hạt sáng lấm tấm.

#### QUY TẮC 5 — Chữ TRẮNG thả trực tiếp trên ảnh (KHÔNG dùng khối màu nền như kênh khoa học não bộ)

Khác với hệ thống "khối chữ vàng" của kênh tham khảo kia — **cả 3 kênh cùng ngách disciplina/motivation đều thả chữ trực tiếp lên ảnh, có đổ bóng/viền tối để đọc được, KHÔNG có khối nền màu**. Cúspide Silenciosa theo đúng chuẩn này (khớp với `ThumbnailA/B.dc.html` đã dựng):

- Chữ **trắng ấm `#F5F5F0`** cho phần chính, **MỘT từ/cụm từ khóa** trong màu nhấn playlist (xem bảng màu) để tạo điểm nhấn thị giác — kỹ thuật "highlight 1 từ" mà cả 3 kênh tham khảo đều dùng (`success` màu đỏ, `DISCIPLINE` màu đỏ).
- Font: **hiển thị cực đậm, chữ hoa toàn bộ**, kiểu condensed sans (Bebas Neue hoặc tương đương) — khớp font đã dùng ở banner.
- Luôn có **dải gradient tối** phía sau vùng chữ (không phải khối màu đặc) để đảm bảo đọc được trên mọi nền ảnh — xem code mẫu trong `ThumbnailA.dc.html`.
- **Tối đa 5-6 từ** cho headline (dài hơn khối chữ vàng của kênh kia vì không bị giới hạn bởi kích thước khối — nhưng vẫn phải đọc được trong 1 giây).
- ⚠️ **Ký tự tiếng Tây Ban Nha rủi ro khi AI sinh ảnh:** `á é í ó ú ñ ¿ ¡` thường bị vẽ sai/méo bởi các công cụ tạo ảnh AI. Ưu tiên viết headline KHÔNG dấu khi có thể diễn đạt tương đương (`MAS` thay vì `MÁS` nếu không đổi nghĩa, hoặc chấp nhận và kiểm tra chính tả kỹ ở bước duyệt ảnh) — không dùng `¿`/`¡` mở đầu trong chữ thumbnail (chỉ dùng trong tiêu đề văn bản, không phải chữ render trong ảnh).

**Quy tắc 1+1=3 (giữ nguyên, bắt buộc):** đọc to Title + chữ thumbnail. Nếu bỏ chữ thumbnail đi mà không mất thông tin nào → chữ thumbnail SAI, viết lại. Title nói VẤN ĐỀ, chữ thumbnail nói KHOẢNH KHẮC/CON SỐ cụ thể.

#### QUY TẮC 6 — Vùng cấm đặt chữ

- 🚫 Góc dưới-phải, 25% × 15% (badge thời lượng YouTube đè lên).
- 🚫 Viền 5% mỗi cạnh.
- 🚫 Dải dưới cùng 12% (thanh tiến trình xem dở che) — đây cũng là nơi đặt **thanh màu nhấn mỏng** (khớp thiết kế đã publish), nên chữ headline phải nằm CAO HƠN dải này.
- ✅ Vùng an toàn: nửa dưới-giữa (trên dải cấm 12%) — khác với ngách kia (họ đặt ở nửa trên); 3 kênh tham khảo ở ngách này đều đặt chữ ở **nửa dưới** khung hình.
- Badge góc trái (logo núi) LUÔN cố định, không đổi vị trí giữa các video — đây là yếu tố nhận diện kênh trong feed.

#### QUY TẮC 7 — Biểu cảm/tư thế nhân vật người que đọc được ở kích thước nhỏ

- Vì người que không có khuôn mặt chi tiết, biểu cảm phải truyền tải qua **TƯ THẾ (pose)**: cúi gập vai (mệt mỏi/thất bại), đứng thẳng tay giơ cao (chiến thắng), ngồi khoanh chân (tĩnh tâm), sải chân chạy (hành động) — xem 3 pose mẫu đã dựng trong `ThumbnailA.dc.html`.
- Không yêu cầu mắt/miệng khoét trắng như kênh kia (người que của Cúspide Silenciosa không có mặt chi tiết — đây là lựa chọn phong cách, giữ nguyên).

#### QUY TẮC 8 — Một vật thể mang màu nhấn, còn lại trung tính

- **CHỈ MỘT** vật thể/panel được mang màu nhấn playlist. Mọi thứ còn lại là đen/trắng ấm.
- Ba hằng số thương hiệu không đổi theo playlist: nền đen · nhân vật người que trắng ấm · badge hình núi góc trái.

- Khung hình `--ar 16:9`. Lưu 3 Titles + 3 Thumbnail Prompts vào `youtube_metadata.txt`.

### 1.1 Viết chữ thẳng vào prompt tạo ảnh

```
A YouTube thumbnail, 16:9. Solid dark background (#0B0B0C), warm dark
gradient toward the bottom in {MÀU_NHẤN}.

A minimalist stick figure character (thick rounded warm-white strokes,
#F5F5F0), in a {TƯ_THẾ} pose, positioned in the {VỊ_TRÍ} of the frame,
filling about 55-65% of the frame height. Bold flat illustration style,
NO detailed anime rendering, NO photorealistic face, NO cross-hatching.

One accent object/panel in solid flat {MÀU_NHẤN}, thick dark outline.

Below the character, bold ultra-condensed sans-serif headline text in
warm white, reading exactly "{CHỮ_CHÍNH}", all capital letters, with the
word "{CHỮ_NHẤN}" in {MÀU_NHẤN}, sitting on a soft dark gradient scrim
for legibility, positioned in the lower-middle area, text height about
18-22% of the image height, perfectly legible when shrunk to 160x90 px.
A small circular badge in the top-left corner containing a simple white
mountain-peak icon on a dark circle.

--ar 16:9 --no bright background, light background, cream background,
yellow banner, gradient glow, extra text, additional words, captions,
subtitles, watermark, small lettering, gibberish text, cross-hatching,
sketch texture, second character with equal weight, photorealistic face,
anime face detail
```

- `{TƯ_THẾ}`: `slumped shoulders looking down` · `standing tall with both arms raised` · `sitting cross-legged, calm` · `mid-stride running`.
- `{VỊ_TRÍ}`: `left third` · `right third` · `center`.
- `{CHỮ_CHÍNH}` / `{CHỮ_NHẤN}`: theo 1 trong 5 khuôn tiêu đề (Bước 1), tối đa 5-6 từ, không dấu khi có thể.
- `{MÀU_NHẤN}`: theo playlist (bảng màu v1.0).

### 1.2 Bộ ký tự an toàn cho chữ trong ảnh

| | Ký tự | Ví dụ |
|---|---|---|
| ✅ An toàn | A-Z không dấu, 0-9, khoảng trắng | `8 HABITOS` · `30 DIAS` · `NO ES PEREZA` |
| ⚠️ Rủi ro, kiểm tra kỹ | á é í ó ú ñ | `MAS FUERTE` an toàn hơn `MÁS FUERTE` |
| ❌ Tránh hẳn | ¿ ¡ % → ≠ & / | Diễn đạt lại bằng chữ thường: `POR QUE FALLAS` thay vì `¿POR QUÉ FALLAS?` |

### 1.3 Gán Playlist (bắt buộc ở khâu packaging)

Gán video vào 1 trong 5 Playlist Folder (xem đầy đủ ở Bước 3.1), ghi vào `youtube_metadata.txt` kèm màu nhấn tương ứng.

---

## Bước 2: Viết & Tối Ưu Hóa Kịch Bản (Script Writing)

### 2.1 Đầu vào

- **Dạng A — Kịch bản thô:** người dùng cung cấp bản thảo ngắn/thiếu cấu trúc. AI mở rộng, viết lại theo cấu trúc Gancho + Módulo đánh số + Cierre.
- **Dạng B — Chỉ có chủ đề:** AI nghiên cứu và viết kịch bản hoàn chỉnh bằng tiếng Tây Ban Nha.

### 2.2 Yêu cầu độ dài — dựa trên dữ liệu THẬT của 3 kênh đối thủ, không phải kênh khoa học não bộ

> 🎯 **ĐỘ DÀI KHỞI ĐIỂM: 4-7 PHÚT ≈ 650-1.100 TỪ tiếng Tây Ban Nha.** Mục tiêu ngắm: ~850 từ (≈ 5,5 phút).
> Căn cứ: thời lượng video thật đã quan sát ở 3 kênh tham khảo dao động **2:41 - 6:11 phút**, phần lớn 3-6 phút — KHÁC HẲN khoảng "10-15 phút" của kênh khoa học não bộ (con số đó được đo cho MỘT kênh khác, ngách khác, khán giả khác — không nên bê nguyên sang đây).

**Cách quy đổi từ → phút (ƯỚC TÍNH, PHẢI ĐO LẠI sau khi chọn giọng đọc thật):**
- Tốc độ đọc tự nhiên tiếng Tây Ban Nha ước tính **~150 từ/phút (~2,5 từ/giây)** — con số tham khảo ngành, CHƯA đo trên giọng đọc thật của kênh.
- 650 từ ÷ 150 ≈ **4,3 phút** · 850 từ ÷ 150 ≈ **5,7 phút** · 1.100 từ ÷ 150 ≈ **7,3 phút**.
- ⚠️ **Bắt buộc đo lại** ngay sau khi xuất audio đầu tiên (xem Bước 4): dùng file `.srt` xuất kèm (hoặc `ffprobe`) lấy thời lượng file, chia cho số từ trong đoạn tương ứng, tính lại từ/giây thật, cập nhật ngưỡng ở mục 2.2 và 5.2. Đừng tin số ước tính này quá 1 video.
- 📏 **Đã đo trên giọng thương hiệu Gonzalo (2026-09-29):** script project_14 — 783 từ → 5:21 phút = **~2,4 từ/giây (~146 từ/phút)**, sát ước tính 150 từ/phút. Quy đổi thật: 650 từ ≈ **4,4 phút** · 850 từ ≈ **5,8 phút** · 1.100 từ ≈ **7,5 phút**.

**Vì sao khởi điểm ngắn hơn kênh kia:** kênh khoa học não bộ TĂNG độ dài dựa trên dữ liệu 40+ video sẵn có (biết chắc video ngắn của họ trước đây đang thắng). Cúspide Silenciosa **chưa có dữ liệu gì** — bắt đầu ở đúng khoảng độ dài đã được validate bởi đối thủ cùng ngách là lựa chọn an toàn hơn suy đoán. Sau 5-10 video, nếu AVD% cho thấy khán giả xem hết mà vẫn còn muốn thêm (AVD% cao, xem hết > 70%), thử tăng dần lên 7-9 phút.

**Mật độ nội dung (áp dụng ngay từ đầu, không đợi có bằng chứng để "phình" như kênh kia):**

| Chỉ số mật độ | Mục tiêu |
|---|---|
| Số Módulo (kỹ thuật/thói quen đánh số, xem 2.3) | 4-6 |
| Trích dẫn/nguồn tham khảo có tên | ≥ 2 |
| Pattern interrupt hoặc antithesis mỗi Módulo | ~1 (≈ 5-8 lần/video — xem 2.5.A, cập nhật theo tần suất thật quan sát ở 4 kênh tham khảo) |
| Open loops | ≥ 2 |

🚫 **CẤM kéo dài bằng cách:** lặp ý đã nói, tóm tắt giữa chừng quá 2 câu, mở bài lan man. Không đủ chất liệu → quay lại Bước 0 chọn chủ đề khác.

### 2.3 Cấu trúc kịch bản: Gancho + Módulo Đánh Số + Cierre (Mạch 1 — mặc định)

> ✏️ **Cập nhật 2026-09-02:** cấu trúc dưới đây thay thế bản "7 phần tiểu luận liên tục" trước đó, sau khi đối chiếu với transcript/caption/mô tả THẬT của 4 kênh tham khảo (007 Method, Silent Apex, The Inspire Path, Productividad Real — xem `phan-tich-phong-cach-viet-kich-ban-doi-thu.md`). Phát hiện cốt lõi: cả 4 kênh không viết theo mạch tiểu luận, mà dùng khung **danh sách đánh số xuyên suốt toàn video** — mỗi mục tự chứa đủ cơ chế + cách sửa, không tách "phần giải thích" và "phần áp dụng" ra hai khối cách xa nhau như bản cũ (La Inmersión vs La Acción).

| Phần | Tên (ES) | Mục đích | Độ dài |
|:--:|---|---|:--:|
| **1** | **EL GANCHO** (Hook) | Câu đầu tạo sốc/tò mò, đánh vào nỗi đau về KỶ LUẬT — TẬP TRUNG — ĐỘNG LỰC. Vào thẳng vấn đề trong 5-10 giây, **KHÔNG có lời chào/giới thiệu** ("Hola, bienvenidos a…" bị cấm hoàn toàn — cả 4 kênh tham khảo đều vào thẳng hook ở câu đầu tiên). Chọn 1 trong 3 biến thể (đã xác nhận là 3 dạng chủ đạo ở thị trường này): <br>(a) *Tình huống quen thuộc:* *"Pones la alarma a las 5 a.m. y a las 5:01 ya la apagaste…"* <br>(b) *Câu hỏi phản biện "¿Y si…?":* *"¿Y si el problema no es tu falta de motivación, sino la forma en que tu cerebro fue condicionado?"* <br>(c) *Vào thẳng mục số 1, không rào đón:* *"Número uno: gánate la primera hora de tu mañana."* | 40-70 từ |
| **2** | **LA PROMESA** (Promise) | Nói rõ viewer được gì VÀ nêu rõ SỐ LƯỢNG módulo sắp tới (khớp với con số đã dùng ở tiêu đề/thumbnail): *"Estos son los 5 hábitos que van a cambiar tu disciplina — y te explico POR QUÉ funcionan, no solo qué hacer."* | 30-50 từ |
| **3…N+2** | **MÓDULO 1 … MÓDULO N** (mỗi módulo = 1 kỹ thuật/thói quen/mecanismo, đánh số rõ ràng: *"Hábito uno…" / "Número dos…"*) | Mỗi módulo là MỘT đơn vị tự chứa đủ 4 lớp, KHÔNG dồn phần "cách sửa" về cuối video: <br>**(a) Tên cơ chế/quy tắc** — gọi tên chính thức nếu có (dopamina, efecto Zeigarnik, ego depletion…). <br>**(b) Ví dụ đời thường/lý do tâm lý** — vì sao điều này xảy ra, ví dụ cực relatable. <br>**(c) Cách sửa/áp dụng CỤ THỂ** — làm gì, mất bao lâu, ngay trong módulo này (không hẹn "sẽ nói ở phần sau"). <br>**(d) Kết quả/lợi ích ngắn** — điều gì thay đổi nếu áp dụng. <br>Dùng 1 câu chuyển tiếp lặp lại xuyên các módulo làm nhịp neo (VD: *"Aquí está la clave…"*, *"La solución es simple…"*, *"Esto es lo que cambia todo…"*) — chọn 1 câu cho cả video, lặp trước phần (c) của mỗi módulo. Nếu chủ đề có 1 sự thật phản trực giác mạnh, đặt nó làm PUNCHLINE của módulo áp dụng antithesis: *"La disciplina no se trata de fuerza de voluntad — se trata de eliminar la fricción."* (thay cho việc tách "El Giro" thành phần riêng như bản cũ). Chọn **N = 4-6 módulo** tuỳ độ dài mục tiêu (xem 2.2). | 90-220 từ/módulo (tổng médulos: **550-910 từ**) |
| **Cuối** | **EL CIERRE** (CTA) | Ưu tiên CTA dạng **cam kết công khai** (đã quan sát hiệu quả cao ở 007 Method — 300+ phản hồi thật): dẫn vào comment ghim, VD *"Escribe 'Estoy listo' aquí abajo — voy a fijar este comentario, y en 30 días quiero que vuelvas a decirme qué cambió."* (phối hợp với bước ghim comment sau khi đăng, xem Bước công đoạn đăng tải). Có thể thay bằng câu hỏi tương tác gắn trải nghiệm cá nhân nếu chủ đề không hợp cam kết 30 ngày: *"Cuéntame en los comentarios — ¿cuál de estos vas a probar primero?"* → Like → Suscríbete. | 30-70 từ |
| | **TỔNG** | | **650-1.100 từ** ≈ 4-7 phút |

**Nhịp module tham khảo (không bắt buộc, chỉ để định hướng khi outline):** N=4 módulo/mỗi módulo dài hơn (~140-220 từ) phù hợp chủ đề cần giải thích cơ chế sâu; N=6 módulo/mỗi módulo ngắn hơn (~90-150 từ) phù hợp dạng liệt kê nhanh kiểu "X hábitos en X minutos" — cả hai đều đã quan sát được ở các kênh tham khảo.

### 2.4 Quy tắc nội dung

#### A. Trích dẫn/nguồn tham khảo
- Mỗi kịch bản ≥ 2 nghiên cứu/tác giả có tên cụ thể. **BẮT BUỘC verify bằng WebSearch trước khi đưa vào `script.txt`** — không được "nhớ mang máng".
- Nguồn phù hợp ngách (đã quen thuộc với khán giả self-improvement, dễ kiểm chứng): James Clear (*Atomic Habits*), Cal Newport (*Deep Work*), BJ Fogg (*Tiny Habits*, Stanford), Kelly McGonigal (*The Willpower Instinct*), Angela Duckworth (*Grit*), Roy Baumeister (nghiên cứu về ego depletion/ý chí), David Goggins, và các triết gia khắc kỷ (Marco Aurelio, Séneca, Epicteto) khi phù hợp góc "disciplina mental".
- Đúng: *"James Clear explica en Atomic Habits que…"* Sai: *"Los estudios dicen que…"* (quá chung chung).

#### B. Khung khái niệm (dùng ít nhất 1 làm xương sống)
- **Hình thành thói quen:** vòng lặp cue-rutina-recompensa, apilamiento de hábitos (habit stacking), regla del 2%/1% diario.
- **Tâm lý ý chí:** ego depletion, dicotomía de control (khắc kỷ), regla del 40% (Goggins).
- **Dopamina/motivación:** dopamine loop, procrastinación como protección emocional, fricción vs. facilidad.
- **Hiệu ứng nhận thức:** efecto Zeigarnik (open loop tâm lý), sobrecarga cognitiva.

#### C. Quy tắc "Giải quyết nỗi vật lộn"
Mỗi video trả lời: **"¿Por qué no puedo [X]?"** — X là vật lộn phổ biến về kỷ luật/thói quen/tập trung. Ví dụ: *"¿Por qué empiezo con toda la motivación y a los 3 días ya lo dejé?"*, *"¿Por qué sé lo que tengo que hacer y aun así no lo hago?"*

#### D. Disclaimer
Khi chạm chủ đề sức khỏe tâm thần ở mức lâm sàng, chèn 1 câu trước CTA: *"Este video es solo con fines educativos y no sustituye consejo profesional. Si sientes que necesitas ayuda, por favor busca un profesional de salud mental."*

### 2.5 Kỹ thuật giữ chân bắt buộc

#### A. Pattern Interrupts (~1 sau mỗi Módulo, tức ~5-8 lần/video — tăng từ ngưỡng ≥4 cũ sau khi đo tần suất thật ở 4 kênh tham khảo: nhạc hiệu/chuyển ý xuất hiện gần như mỗi 30-70 giây, tương ứng mỗi módulo. Không lặp câu)
- `"Pero aquí es donde se pone interesante de verdad…"`
- `"Presta mucha atención a esto…"`
- `"Y esto es lo que cambió todo…"`
- `"Espera — todavía hay más."`
- `"Esto es lo que nadie te dice…"`

#### B. Open Loops (≥ 2, PHẢI đóng lại trước khi hết video)
- `"…y en un momento te muestro la técnica exacta para arreglar esto."`
- `"Llegaremos al giro contraintuitivo al final — pero primero…"`

#### C. Emotional Anchors
Mỗi phần có ≥ 1: tình huống relatable, số liệu gây sốc, trích dẫn tác giả quen thuộc, ẩn dụ sống động.

#### D. First 5 Seconds Visual Hook
5 giây đầu (hình + hook) PHẢI khớp/mở rộng trực tiếp từ cảnh thumbnail.

### 2.6 Giọng văn

- **Trò chuyện, nghiêm túc, không hô khẩu hiệu:** khớp tông đã chốt ("La disciplina no hace ruido") — tránh ngôn ngữ motivational rỗng kiểu *"¡Tú puedes lograrlo!"*.
- **Đồng cảm & xác nhận trước khi thách thức:** *"Si no puedes mantener un hábito, no es que te falte voluntad. Tu cerebro está haciendo exactamente lo que fue diseñado para hacer."*
- **Mỗi thuật ngữ kèm ẩn dụ ngay:** *"La corteza prefrontal — piénsalo como el gerente de tu cerebro, el que dice 'no' cuando el resto de ti quiere decir 'sí' a la pereza."*
- **Nhịp đọc (cập nhật 2026-09-02 — đo từ transcript/caption thật):** câu **ngắn 6-10 từ là MẶC ĐỊNH**, không phải "xen đều" long/short như trước. Chỉ cho câu dài hơn (~15-20 từ) khi đang giải thích cơ chế, rồi cắt ngắn lại NGAY cho câu chốt/punchline ngay sau đó — đúng nhịp "giải thích dài → chốt ngắn" quan sát được ở cả 4 kênh tham khảo.
- **Thừa nhận cá nhân (tuỳ chọn, không bắt buộc mọi video):** cho phép 1 câu ngắn kiểu *"Yo también estuve ahí…"* / *"A mí también me pasó…"* ở đầu Módulo 1 hoặc ngay sau Gancho, khi chủ đề hợp giọng gần gũi hơn coach thuần túy (mẫu quan sát ở Productividad Real — kênh tiếng Tây Ban Nha gần nhất với thị trường mục tiêu). Không dùng nếu làm loãng tông "trò chuyện, nghiêm túc" đã chốt.

### 2.7 Quy trình xử lý theo dạng đầu vào

**Dạng A (kịch bản thô):** phân tích luận điểm chính → chia thành N=4-6 Módulo → bổ sung 4 lớp cho mỗi Módulo (cơ chế/ví dụ/cách sửa cụ thể/kết quả — cách sửa nằm NGAY trong Módulo, không dồn về cuối) → kiểm tra đạt 650-1.100 từ → chèn pattern interrupt mỗi Módulo/open loop → verify trích dẫn → đọc lại flow.

**Dạng B (chỉ có chủ đề):** nghiên cứu web tìm 3-4 góc hấp dẫn nhất → **cổng chất liệu**: nếu < 3 kỹ thuật/góc riêng biệt và < 2 nguồn verify được → chủ đề quá mỏng, quay lại Bước 0 → xác định Emotional Trigger + câu "Giải quyết nỗi vật lộn" → outline Gancho + N Módulo + Cierre với ngân sách từ → viết 650-1.100 từ → chèn kỹ thuật giữ chân → review.

### 2.8 Checklist kiểm tra script

- [ ] Đạt **650-1.100 từ** (đếm bằng `wc -w script.txt`)
- [ ] Đủ Gancho + N Módulo (4-6) + Cierre, số từ từng phần trong ngân sách (2.3)
- [ ] Hook không bắt đầu bằng "En este video…" VÀ không có lời chào/giới thiệu ("Hola, bienvenidos…")
- [ ] Mỗi Módulo có đủ 4 lớp (cơ chế/ví dụ/cách sửa cụ thể/kết quả) — cách sửa nằm ngay trong Módulo, KHÔNG dồn về cuối video
- [ ] ~1 pattern interrupt hoặc antithesis mỗi Módulo (tổng ~5-8), ≥ 2 open loops (đều được đóng)
- [ ] Câu chuyển tiếp lặp lại xuyên các Módulo đã chọn và dùng nhất quán (2.3)
- [ ] ≥ 2 trích dẫn có tên, đã verify bằng WebSearch
- [ ] ≥ 1 khung khái niệm làm xương sống
- [ ] Không đoạn nào lặp ý đã nói
- [ ] Có disclaimer nếu chạm sức khỏe tâm thần
- [ ] Cierre dùng CTA cam kết công khai (comment 1 câu ngắn) khi chủ đề hợp, không chỉ câu hỏi mở đơn thuần

Lưu vào `script.txt`.

### 2.9 Mô tả video (Description) — sau khi script xong

- **120-200 từ tiếng Tây Ban Nha:** Hook (1-2 dòng đầu chứa từ khóa chính), tóm tắt 3-4 ý chính, CTA.
- **10-15 hashtags**, lowercase: `#disciplina`, `#habitos`, `#motivacion`, `#productividad`, `#desarrollopersonal`, `#autodisciplina`.
- **YouTube Chapters (bổ sung 2026-09-02)** — đặt tên chương khớp từng Módulo trong script (xem cấu trúc mới ở Bước 2.3), dán trực tiếp vào phần Description theo định dạng YouTube yêu cầu (dòng đầu `0:00` bắt buộc, mỗi dòng sau `mm:ss Tên chương`, ≥ 3 chương, chương đầu tại `0:00`):
  ```
  0:00 El Gancho
  0:12 Módulo 1: {tên ngắn theo nội dung}
  1:05 Módulo 2: {tên ngắn theo nội dung}
  ...
  X:XX Cierre
  ```
  Lấy timestamp thật từ file `.srt` đã xuất ở Bước 4 (khớp thời điểm bắt đầu mỗi Módulo trong `script.txt`), không ước lượng. Mẫu này quan sát trực tiếp ở Productividad Real (kênh tiếng Tây Ban Nha tham khảo — thanh scrub của họ có chương đặt tên rõ như "Práctica 1: Respiración Tanden") và khớp tự nhiên với cấu trúc Módulo đánh số vừa cập nhật.
- Bổ sung vào `youtube_metadata.txt`.

### 2.10 Checklist metadata

- [ ] Description ≥ 120 từ, từ khóa chính trong 2 dòng đầu
- [ ] ≥ 10 hashtags lowercase
- [ ] 3 titles ≤ 60 ký tự, mỗi title ≥ 1 từ khóa
- [ ] Đã gán Playlist Folder
- [ ] 3 thumbnail prompts đủ style + bố cục + chữ (≤ 6 từ) + `--ar 16:9`
- [ ] Chapters đủ ≥ 3 mốc, dòng đầu là `0:00`, tên khớp từng Módulo, timestamp lấy từ `.srt` thật

---

## Bước 3: Khởi Tạo Không Gian Làm Việc

### 3.1 Cấu trúc Playlist Folder

`OMMANI/Kênh mới Tiếng Tây Ban Nha/` có **5 Playlist Folder cấp 1**, khớp 5 trụ cột ở Bước 0:

| Playlist Folder | Chủ đề nhận | Màu nhấn |
|---|---|---|
| `01_Disciplina y Habitos` | Rutinas, consistencia, romper malos hábitos | Cam-đỏ `#FF5A36` |
| `02_Mentalidad y Exito` | Tư duy thành công, tự kiểm soát, kỷ luật tinh thần | Vàng-hổ phách `#E8A23C` |
| `03_Motivacion y Superacion` | Thử thách cá nhân, chuyển hóa, câu chuyện | Đỏ-hồng `#FF3B78` |
| `04_Productividad Practica` | Tập trung, quản lý thời gian, ngừng trì hoãn | Xanh lam `#3BA7C9` |
| `05_Autoconocimiento` | Tự-chẩn-đoán tính cách/thói quen (thử nghiệm) | Tím `#8B6CFF` |

**Quy tắc chọn Playlist Folder cho project mới:** đối chiếu chủ đề với 5 trụ cột ở Bước 0 → tạo project TRỰC TIẾP bên trong đúng folder, không tạo ở root.

### 3.2 Tạo thư mục dự án

- Tên thư mục: `project_XX_ten_chu_de_YYYYMMDD`. Kênh mới bắt đầu từ `project_01`.
- Đường dẫn ví dụ: `OMMANI/Kênh mới Tiếng Tây Ban Nha/01_Disciplina y Habitos/project_01_rutina_matutina_20260901/`.
- Thư mục con: `audio/`, `images/`, `thumbnail/`.
- **Naming MP4:** đúng tiêu đề đã chọn, Title Case, thay `"`, `'`, `:` bằng `-`.

### 3.3 Bộ công cụ sản xuất (chưa có script Python riêng — dùng bộ đã đề xuất)

Vì đây là kênh mới, chưa có `build_scenes.py`/`render_video.py` tuỳ biến như kênh kia. Dùng đúng bộ công cụ đã chốt trong `kenh-youtube-tbn-strategy.md`:

| Công đoạn | Công cụ |
|---|---|
| Giọng đọc tiếng Tây Ban Nha | **edge-tts, giọng `es-CO-GonzaloNeural` (rate -16%, pitch -20Hz)** qua script `tools/voz_canal.py` — miễn phí, không cần API key, xuất kèm phụ đề `.srt` có timestamp — xem chi tiết ở Bước 4 |
| Hoạt hình người que | StickReel hoặc FlexClip |
| Dựng, phụ đề, nhạc nền | CapCut |
| Thumbnail | Prompt ở Bước 1.1 qua công cụ tạo ảnh AI có sẵn (Midjourney/tương đương), hoặc chỉnh trực tiếp trên canvas `el-camino-disciplinado-branding.html` đã publish |

> Nếu về sau kênh phát triển script tự động hoá riêng (tương tự `build_scenes.py`), áp dụng lại nguyên vẹn kỷ luật đo tốc độ đọc thật ở Bước 2.2 và 5.2 — chỉ thay công cụ, không thay phương pháp.

---

## Bước 4: Chuyển Thể Kịch Bản Thành Giọng Đọc (TTS) — dùng `edge-tts` giọng Gonzalo (`tools/voz_canal.py`)

> Công cụ đã chốt (2026-09-29): **`edge-tts`** (thư viện Python mã nguồn mở, dùng dịch vụ Microsoft Edge Neural TTS qua mạng — miễn phí, không cần API key), giọng **`es-CO-GonzaloNeural`** (nam, Colombia — giọng rõ, trung lập Mỹ Latinh), chỉnh chậm và trầm để gần chất giọng ElevenLabs "Ludovico" mà kênh dùng ở các video đầu.
>
> **Phạm vi:** các project ĐÃ có file audio (giọng ElevenLabs Ludovico) giữ nguyên, KHÔNG làm lại. Mọi project mới từ nay dùng giọng Gonzalo.
>
> Mẫu nghe chuẩn: `demo_voices/07_Gonzalo_GIONG_CHINH_KENH.mp3`.
>
> Lưu ý: `edge-tts` dùng dịch vụ đọc của trình duyệt Edge, không phải gói Azure TTS có giấy phép thương mại chính thức — cần mạng Internet khi xuất audio.

### 4.1 Cài đặt (đã làm sẵn — chỉ cần khi cài lại máy)

```
.venv/bin/pip install edge-tts
```

### 4.2 Thông số giọng thương hiệu — CỐ ĐỊNH, không đổi giữa các video

| Thông số | Giá trị |
|---|---|
| Giọng | `es-CO-GonzaloNeural` |
| Tốc độ | `--rate=-16%` |
| Cao độ | `--pitch=-20Hz` |
| Xử lý thêm | Không (không hạ giọng/EQ bằng ffmpeg) |

Các thông số nằm ở đầu file `tools/voz_canal.py`. Chỉ sửa ở đó nếu cố ý đổi chất giọng cho TOÀN kênh.

### 4.3 Lệnh xuất audio + phụ đề

```
# Một project:
.venv/bin/python tools/voz_canal.py "01_Disciplina y Habitos/project_14_5_habitos_cambian_todo_20260907"

# Mọi project chưa có audio (tự bỏ qua project đã có audio):
.venv/bin/python tools/voz_canal.py --all

# Nghe thử một câu:
.venv/bin/python tools/voz_canal.py --text "Hoy empieza tu disciplina." --out prueba.mp3
```

- Đầu vào: `script.txt` của project (chỉ chứa lời đọc).
- Đầu ra: `audio/voz_gonzalo.mp3` + `audio/voz_gonzalo.srt` — file `.srt` có **timestamp theo từng câu**, dùng TRỰC TIẾP làm căn cứ chia Frame ở Bước 5.3 (canh mỗi Frame ≤ 6 giây theo timestamp thật).
- Project nào đã có bất kỳ file `.mp3/.wav/.m4a` sẽ bị bỏ qua để không ghi đè audio cũ. Muốn làm lại thì xoá `audio/voz_gonzalo.*` trước.
- Kiểm tra phát âm: nghe lại các số, tên riêng, từ tiếng Anh. Nếu đọc sai, viết lại trong `script.txt` theo cách đọc (vd. "25%" → "veinticinco por ciento") rồi xuất lại.

### 4.4 Đo lại tốc độ đọc thật

- Đã đo lần đầu: **~2,4 từ/giây (~146 từ/phút)** — xem Bước 2.2. Sau mỗi vài video, đối chiếu lại: timestamp dòng cuối của `audio/voz_gonzalo.srt` (≈ tổng thời lượng) chia cho số từ của `script.txt`.

---

## Bước 5: File `transcript_and_visuals.txt` (Kịch Bản Hình Ảnh & Song Ngữ)

> Từ video này trở đi, **kịch bản hình ảnh + bản song ngữ hợp nhất vào ĐÚNG MỘT file duy nhất**: `transcript_and_visuals.txt` (đặt ở thư mục gốc project) — không tách riêng `transcript_bilingual.txt` như trước nữa. Định dạng theo đúng khuôn frame-by-frame bên dưới, để mỗi Frame là một khối tự-đủ (self-contained) copy thẳng được vào công cụ tạo ảnh AI mà không cần kéo lên xem STYLE RULES ở nơi khác.

### 5.1 Khối tiêu đề file (Header) — luôn đặt ở đầu `transcript_and_visuals.txt`

```
################################################################################
# TRANSCRIPT & VISUALS - Project {SO}: {Tên chủ đề video, tiếng Anh ngắn gọn}
# Playlist Folder: {01-05_Ten_Playlist}  |  Video frame style: dark stick-figure line-art
# Cach dung: Copy khoi [VISUAL DESCRIPTION] + [STYLE RULES] vao cong cu tao anh AI cho tung Frame.
# Chia Frame theo phuong phap Buoc 5.3 (cau/menh de hoan chinh, khong cat giua cau theo so tu).
# Tong: {N} Scenes / {M} Frames  |  Script: {X} tu ~ {Y} phut  |  Nguong 15 tu/Frame (2.5 tu/giay x 6s)
# Anh xa file anh: Frame N  ->  images/img_{N:03d}.png  (kiem bang: ls images | wc -l  =  {M})
# Frame 001 BAT BUOC tai hien canh thumbnail (xem Buoc 2.5.D — First 5 Seconds Visual Hook).
################################################################################
```

- Điền số liệu THẬT sau khi chia Frame xong (không để trống/ước lượng sai — đây là bảng tra cứu nhanh cho người dựng video, không phải trang trí).
- Ghi bằng ASCII không dấu ở dòng comment (tránh lỗi encoding khi mở bằng một số công cụ dòng lệnh) — riêng nội dung `[ES]`/`[VI]` bên dưới vẫn viết đầy đủ dấu tiếng Tây Ban Nha/Việt như bình thường.
- Dòng cuối "Frame 001 BẮT BUỘC..." là NGUYÊN TẮC, không phải số liệu đo được — kênh mới chưa có `channel_performance_log.md` để trích dẫn "bài học đã học", nên neo thẳng vào quy tắc First 5 Seconds Visual Hook đã chốt ở Bước 2.5.D thay vì bịa một con số hiệu suất chưa có thật.

### 5.2 Phân chia cảnh (Scene)

Chia kịch bản thành các "Cảnh" logic theo cấu trúc Gancho + Módulo + Cierre (2.3) — mỗi Módulo thường là 1 Cảnh riêng, chèn tiêu đề cảnh:
```
================================================================================
## ESCENA 1: EL GANCHO (La Rutina de las 5 A.M.)
================================================================================
```
```
================================================================================
## ESCENA 2: MÓDULO 1 — Gánate la Primera Hora
================================================================================
```

### 5.3 Chia Frame (Visual Script)

> ⚠️ **Mỗi Frame ≤ 6 giây audio** — ảnh phải đổi ít nhất mỗi 6 giây để giữ nhịp.
> **Ngưỡng từ/Frame (ƯỚC TÍNH ban đầu, đo lại theo Bước 4):** 2,5 từ/giây × 6 ≈ 15 từ tiếng Tây Ban Nha/Frame. Với kịch bản 650-1.100 từ → khoảng **45-75 Frame/video** (thấp hơn nhiều so với kênh kia vì video ngắn hơn — hợp lý với năng lực sản xuất của kênh mới).

**Quy trình chia (ưu tiên theo thứ tự, giữ nguyên phương pháp gốc — đây là phần transferable tốt nhất của tài liệu):**
1. Tách câu trước. Câu hoàn chỉnh ≤ ~15-18 từ → 1 Frame.
2. Câu dài hơn → chỉ cắt tại ranh giới ý/mệnh đề thật: dấu gạch ngang, hai chấm, chấm phẩy, liên từ (`y`, `pero`, `así que`, `o`) khi phần sau có chủ ngữ+động từ riêng, mệnh đề phụ (`porque`, `que`, `cuando`).
3. Không bao giờ để Frame là mảnh câu lửng lơ chỉ vì đã gần mốc 15 từ — ưu tiên giữ trọn ý.
4. Mỗi Frame gắn với đúng 1 khối 6 trường ở mục 5.4 (`[FRAME ID]`, `[SHOT TYPE]`, `[ES]`, `[VI]`, `[VISUAL DESCRIPTION]`, `[STYLE RULES - DO NOT MODIFY]`).
5. Đánh số Frame **liên tục xuyên suốt cả video** (không reset về F001 ở mỗi Scene mới) — VD Scene 1 kết thúc ở F007 thì Scene 2 bắt đầu từ F008, đúng như `S02_F008` trong ví dụ ở 5.4.
6. Sau khi chia xong, xác minh nối toàn bộ `[ES]` theo thứ tự Frame khớp nguyên văn `script.txt`, và đếm lại tổng số Frame để điền vào Header (5.1).

**Nội dung `[VISUAL DESCRIPTION]`** — 3 yếu tố, theo đúng DNA người que đã chốt:
1. **Bối cảnh & ánh sáng:** không gian tối, nguồn sáng ấm/lạnh theo cảm xúc cảnh.
2. **Tư thế nhân vật:** vì người que không có mặt chi tiết, biểu cảm truyền qua dáng đứng/ngồi/chạy (xem Quy tắc 7, Bước 1).
3. **Ẩn dụ thị giác:** chuyển khái niệm tâm lý trừu tượng thành hình ảnh vật lý (ý chí như một cơ bắp mỏi, thói quen như một con đường mòn trên núi, procrastinación như một hố sâu dưới chân).

> ✏️ **Motif hình ảnh cụ thể (bổ sung 2026-09-02, rút từ Productividad Real — kênh tiếng Tây Ban Nha dùng nhân vật vector tối giản gần nhất với DNA người que)** — có thể dùng làm lựa chọn cụ thể cho yếu tố 3 (Ẩn dụ thị giác) thay vì luôn phải nghĩ ẩn dụ mới: **vòng tròn khoanh vùng** (circular highlight ring) quanh 1 vật thể/chi tiết cần nhấn; **dấu X đỏ** gạch chéo lên vật thể tượng trưng cho thói quen xấu; **dấu check** xác nhận hành động đúng; **mũi tên lên/xuống** thể hiện tiến bộ/suy giảm. Giữ đúng nguyên tắc "1 vật thể mang màu nhấn" (Quy tắc 8, Bước 1) khi dùng các motif này — không lạm dụng quá 1 motif/Frame.

**`[SHOT TYPE]`** — chọn 1 trong: `WIDE SHOT` · `MEDIUM SHOT` · `CLOSE-UP` · `EXTREME CLOSE-UP` (giữ nguyên tiếng Anh — đây là thuật ngữ kỹ thuật dựng phim, không phải lời thoại). Đổi loại shot mỗi 2-3 Frame liên tiếp để tránh nhịp hình đơn điệu.

### 5.4 Khối Frame đầy đủ (Frame Block Format)

Mỗi Frame là MỘT khối gồm đúng 6 trường theo thứ tự sau, cách nhau 1 dòng trống với Frame kế tiếp — **`[STYLE RULES - DO NOT MODIFY]` lặp lại ở CUỐI MỖI FRAME** (không viết 1 lần rồi tham chiếu ngược, để mỗi khối copy-paste được ngay vào công cụ tạo ảnh mà không cần cuộn lên tìm):

```
[FRAME ID]: S01_F001   ->  images/img_001.png
[SHOT TYPE]: WIDE SHOT
[ES]: {Câu/mệnh đề tiếng Tây Ban Nha của đúng Frame này, khớp nguyên văn script.txt}
[VI]: {Dịch tiếng Việt tương ứng, để bạn — người sản xuất — đối chiếu nghĩa}
[VISUAL DESCRIPTION]:
{Mô tả hình ảnh bằng tiếng Anh, viết văn xuôi 1 đoạn theo 3 yếu tố ở 5.3 — bối cảnh/ánh sáng, tư thế nhân vật, ẩn dụ thị giác. KHÔNG lặp lại nguyên văn câu thoại, mô tả CẢNH chứ không diễn giải lại lời.}
[STYLE RULES - DO NOT MODIFY]:
- Aspect ratio: strictly 16:9 (widescreen, suitable for YouTube).
- Art style: Minimalist stick figure illustration, bold flat shapes, thick rounded strokes. NO detailed anime/manga rendering, NO photorealistic face, NO cross-hatching.
- Color: Solid dark background (#0B0B0C). Character and linework in warm white (#F5F5F0). The ONLY accent color allowed is {MÀU_NHẤN_PLAYLIST theo Bước 1 — VD #FF5A36 cho 01_Disciplina y Hábitos} for one metaphorical object/highlight per frame — everything else stays black/warm-white ink tones.
- Character Design: The main character is a minimalist stick figure — round head, thick rounded warm-white strokes (stroke width ≥ 8px), simple straight limbs, NO detailed face (no eyes/mouth unless the pose itself needs to convey emotion). This character must look IDENTICAL in every frame.
- Background: Clean, mostly empty dark space. NO complex scenery backgrounds. If context is needed, use MINIMAL flat shapes only, keeping the background sparse and uncluttered.
- Composition: Centered or slightly off-center. The main subject occupies 50-70% of the frame height.
- Text: NO text inside the frame — this is a body-content frame, not the thumbnail. (Exception: Frame 001 khi tái hiện cảnh thumbnail theo Bước 2.5.D thì áp dụng nguyên Quy tắc 5-6 ở Bước 1 thay vì dòng này.)
- FORBIDDEN: Absolutely NO watermarks, NO signatures, NO dates, NO borders, and NO extra text/captions anywhere in the image.

[FRAME ID]: S01_F002   ->  images/img_002.png
[SHOT TYPE]: MEDIUM SHOT
[ES]: ...
[VI]: ...
[VISUAL DESCRIPTION]:
...
[STYLE RULES - DO NOT MODIFY]:
... (lặp lại y hệt khối trên)
```

- Ánh xạ file ảnh **cố định**: Frame `S0X_F0YY` → `images/img_0YY.png` (số Frame 3 chữ số, đệm 0 — `img_001.png`, `img_012.png`, `img_203.png`...). Số trong tên file LUÔN khớp số `F` trong `[FRAME ID]`, không khớp theo Scene.
- Đổi Scene mới → chèn lại khối `====...====` / `## ESCENA N: ...` (5.2) rồi tiếp tục đánh số Frame liên tục, KHÔNG reset lại header/không lặp lại khối tiêu đề file (5.1) — khối đó chỉ xuất hiện đúng 1 lần ở đầu file.

### 5.5 Xoá watermark Gemini TRƯỚC khi ghép video — BẮT BUỘC từ project_14 trở đi

Mọi ảnh tạo bằng Gemini (ảnh Frame trong `images/` và thumbnail trong `thumbnail/`) có logo ngôi sao ở góc dưới phải. Phải xoá trước khi ghép video và trước khi đăng thumbnail. Công cụ: `tools/xoa_watermark.py` (chỉ xoá logo nhìn thấy; watermark ẩn SynthID vẫn còn).

- **Tự động:** bước ghép video (`add_subtitles.py` / web UI, hàm `process_project`) tự chạy xoá watermark rồi ghép từ `images_clean/`. Không cần làm tay.
- **Chạy riêng một project** (vd. để lấy thumbnail sạch trước khi ghép):
  ```
  .venv/bin/python tools/xoa_watermark.py --project "01_Disciplina y Habitos/project_14_5_habitos_cambian_todo_20260907"
  ```
- Kết quả: `images_clean/` (cùng tên file với `images/`, dùng để ghép video) và `thumbnail/<tên>_clean.png` (**file này mới là thumbnail để đăng lên YouTube**). Ảnh gốc không bị sửa. Ảnh đã xử lý được bỏ qua ở lần chạy sau, trừ khi ảnh gốc thay đổi.
- Thumbnail còn giữ tên tải về `Gemini_Generated_Image_...` luôn được xoá tại vị trí logo, kể cả khi logo nằm trên nền quá sáng để phát hiện. Nếu đổi tên thumbnail, kiểm tra lại bằng mắt file `_clean`.
- Kiểm tra nhanh: mở vài ảnh trong `images_clean/` và file thumbnail `_clean`, phóng to góc dưới phải. Nếu còn vết rõ (hiếm, thường do logo đè lên nét vẽ trắng), sửa tay bằng Photopea (Spot Healing Brush).

---

## Bước 6: Chiến Lược Đăng Bài & Đánh Giá Sau Đăng

### 6.1 Chiến lược đăng bài

- **Tần suất:** 1 video dài/tuần (khởi điểm, theo `kenh-youtube-tbn-strategy.md`). Tăng dần lên 2 video/tuần khi quy trình sản xuất đã ổn định.
- **Sau khi đăng:** thêm video vào đúng playlist YouTube tương ứng Playlist Folder ngay.

### 6.2 End Screen & Cards

- End Screen 20s cuối: 1 video "Xem tiếp" (cùng Playlist Folder) + nút Suscribirse.
- ≥ 1 Info Card giữa video, trỏ về video cùng playlist.

### 6.3 Phân tích sau đăng & A/B Testing

- **Chỉ số chính:** Average View Duration % và CTR thumbnail — KHÔNG phải số subscriber.
- **CTR đọc theo nguồn traffic**, không đọc số tổng (benchmark chung: Trang chủ 3-8% · Đề xuất 2-6% · Tìm kiếm 3-9% · Feed người đăng ký 8-15%).
- **A/B Test:** dùng Test & Compare của YouTube Studio khi kênh đủ điều kiện (thường cần một lượng subscriber/video tối thiểu — kiểm tra trong Studio).
- Sau 48h: kiểm tra AVD sơ bộ. Sau 28 ngày: cập nhật `channel_performance_log.md`.

### 6.4 Vòng lặp đo CTR — bắt buộc thiết lập TỪ VIDEO ĐẦU TIÊN

> 🚨 Kênh khoa học não bộ tham khảo đã học một bài học đắt giá: đăng 40+ video mà không ghi log nào, không rút được bài học packaging nào. **Cúspide Silenciosa thiết lập vòng lặp này NGAY TỪ ĐẦU, không đợi đến khi có vấn đề.**

**Bảng log bắt buộc** trong `channel_performance_log.md`:

| Project | Title đã dùng | Chữ thumbnail | Khuôn tiêu đề (A-E) | Bố cục (Triptych/Cận cảnh) | Playlist | Ngày đăng | Impressions | CTR tổng % | CTR Browse % | CTR Search % | AVD % | AVD phút | Views 28d | Bài học |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

- Điền sau 48h (sơ bộ) → sau 14 ngày (A/B nếu có) → sau 28 ngày (số cuối + bài học).
- Sau mỗi 5 video: sắp theo CTR Browse giảm dần, so 2 video cao nhất với 2 video thấp nhất — khác nhau ở khuôn tiêu đề nào? bố cục nào? màu nhấn nào? Ghi kết luận 1 dòng.

**🎯 Các giả thuyết đang chờ kiểm chứng (đặt trước, không đổi tiêu chí sau khi thấy số):**

1. **Nền tối thắng nền sáng ở ngách này** (dựa trên 100% thumbnail đối thủ dùng nền tối). Nếu sau 8-10 video, CTR Browse trung bình < 2% và một thử nghiệm nền sáng (1 video) cho kết quả tốt hơn rõ rệt → xem lại giả thuyết, ghi vào đây, đừng âm thầm giữ nguyên.
2. **Độ dài 4-7 phút phù hợp cho khán giả kênh mới.** Sau 5-10 video, nếu AVD% cao (>60%) và ổn định → thử tăng dần lên 7-9 phút cho 2-3 video, so sánh AVD% tuyệt đối (phút).
3. **Trụ cột 5 (Autoconocimiento)** — theo dõi riêng, xem có lặp lại hiệu suất cao như quan sát được ở kênh tham khảo hay không.

**🔬 Escape hatch — nhân vật người que vs. minh họa manga/ảnh thật:**
Dữ liệu ngành cho thấy khuôn mặt người/nhân vật chi tiết thường có CTR cao hơn stick figure trần trụi. Cúspide Silenciosa giữ người que theo lựa chọn thương hiệu + tốc độ sản xuất, nhưng: **cứ mỗi 6 video thì làm 1 biến thể thumbnail dùng minh họa nhân vật chi tiết hơn** (cùng chữ, cùng title), chạy Test & Compare. Sau 12 video (2 lần test), nếu biến thể chi tiết thắng rõ rệt cả 2 lần → cân nhắc chuyển hướng phong cách và ghi vào tài liệu này.

### 6.5 Đồng bộ thương hiệu kênh

- Đã đồng bộ: avatar, banner, thumbnail template (xem `el-camino-disciplinado-branding.html`, đã publish và lưu vào thư mục `Branding/`).

**Mô tả kênh (About) — dán vào YouTube Studio → Tùy chỉnh kênh → Cơ bản → Mô tả:**

```
La disciplina no hace ruido — pero cambia todo.

En Cúspide Silenciosa encontrarás videos sobre disciplina, hábitos y psicología del éxito, explicados con el mecanismo real detrás de cada consejo (no solo motivación vacía).

Aquí hablamos de:
🧠 Disciplina y hábitos — cómo construirlos y no abandonarlos a la primera semana.
💭 Mentalidad y psicología del éxito — por qué tu cerebro te sabotea y cómo recuperar el control.
🔥 Motivación y superación personal — historias y retos que te empujan a actuar hoy.
⏱️ Productividad práctica — más enfoque, menos distracciones, resultados reales.
🪞 Autoconocimiento — para entender los hábitos y patrones que te definen.

Subimos un video nuevo cada semana. Si estás listo para dejar de esperar motivación y empezar a construir disciplina real, este es tu lugar.

Suscríbete y activa la campana 🔔 — la disciplina no hace ruido, pero se nota.
```

(881/1.000 ký tự — 2 dòng đầu là phần hiện trước nút "Mostrar más", đã chèn slogan + từ khóa chính `disciplina`, `hábitos`, `psicología del éxito` ngay từ câu đầu.)

**Từ khóa kênh — dán vào YouTube Studio → Tùy chỉnh kênh → Cơ bản → Từ khóa:**

```
disciplina, hábitos, motivación, desarrollo personal, autodisciplina, crecimiento personal, productividad, mentalidad de éxito, rutina matutina, cómo dejar de procrastinar, fuerza de voluntad, superación personal, autoconocimiento, psicología del éxito, cómo ser disciplinado, disciplina silenciosa, hábitos saludables, control mental, mentalidad ganadora, cúspide silenciosa, motivación diaria, kaizen, hábitos atómicos, cómo tener disciplina, cómo ser más productivo
```

(468/500 ký tự — mỗi mục là 1 từ khóa kênh sẽ liên kết đúng với YouTube search cho ngách + tên thương hiệu; không nhồi từ khóa trùng lặp/không liên quan để tránh bị YouTube coi là spam từ khóa.)

---

## Kết Quả Đầu Ra (Output Checklist)

Mỗi project hoàn chỉnh PHẢI có đủ, nằm trong đúng Playlist Folder:

### Thư mục gốc project:
- [ ] `script.txt` — 650-1.100 từ tiếng Tây Ban Nha
- [ ] `youtube_metadata.txt` — 3 Titles (≤60 ký tự) + Playlist + Description (≥120 từ) + Hashtags (≥10) + 3 Thumbnail Prompts
- [ ] `transcript_and_visuals.txt` — Header (Bước 5.1) + Scene/Frame đầy đủ theo khuôn `[FRAME ID]/[SHOT TYPE]/[ES]/[VI]/[VISUAL DESCRIPTION]/[STYLE RULES - DO NOT MODIFY]` (Bước 5.4), số Frame trong Header khớp số ảnh thật trong `images/`
- [ ] `audio/voz_gonzalo.mp3` + `audio/voz_gonzalo.srt` (xuất cùng lúc bằng `tools/voz_canal.py`, Bước 4)
- [ ] `<Tiêu đề đã chọn>.mp4`

### Thư mục `thumbnail/`:
- [ ] 3 ảnh thumbnail (16:9), đạt chuẩn THUMBNAIL SYSTEM v1.0
- [ ] Bản `_clean` của thumbnail sẽ đăng (đã xoá watermark Gemini — Bước 5.5)

### Thư mục `images/`:
- [ ] Ảnh minh họa từng Frame, đặt tên `img_001.png`, `img_002.png`... (đệm 0, 3 chữ số) khớp đúng số `F` trong `[FRAME ID]` — kiểm bằng `ls images | wc -l` phải bằng đúng số Frame ghi trong Header của `transcript_and_visuals.txt`

### Thư mục `images_clean/` (tự tạo khi ghép video — Bước 5.5):
- [ ] Đủ số ảnh như `images/`, đã xoá watermark Gemini

### Sau khi đăng:
- [ ] Đã thêm vào đúng Playlist YouTube
- [ ] Đã ghi dòng đầu tiên vào `channel_performance_log.md` (sau 48h)
