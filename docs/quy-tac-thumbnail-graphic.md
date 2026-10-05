# Quy tắc thumbnail graphic — Second Nature
> Cách tạo thumbnail dạng **đồ hoạ dữ liệu** cùng phong cách với video motion graphics.
> Phiên bản 1.0 · 05/10/2026 · Mẫu gốc: `2_Discipline_Mindset/p08_…/02_thumbnail/thumbnail_graphic.html`

---

## 1. Ý tưởng cốt lõi

Thumbnail **chỉ chọn một phát hiện gây sốc nhất** trong kịch bản, có số liệu thật và nguồn thật. Biến nó thành **một con số khổng lồ + hai chữ đắt giá + một hình biểu diễn số liệu**.

```
┌──────────────────────────────────────────────┐
│  ┌──────────────┐   67%                      │
│  │ HÌNH DỮ LIỆU │   CHOSE PAIN   ← punch     │
│  │  (waffle,    │   over 15 minutes alone    │
│  │   cột, …)    │   with their thoughts      │
│  └──────────────┘                ← ngữ cảnh  │
│                                    [trống]   │
└──────────────────────────────────────────────┘
```

Vì sao hiệu quả với kênh này:
- **Đúng "Biến 1 — chiều sâu bằng chứng":** người xem thấy số liệu thật ngay từ thumbnail.
- **Khớp với video:** cùng font, màu và kiểu hình, nên bấm vào là thấy đúng thứ được hứa (giữ AVD).
- **Đọc được ở 168×94:** số lớn và một khối màu đọc nhanh hơn ảnh nhân vật nhỏ.

---

## 2. Bốn bước chọn ý tưởng từ kịch bản

### Bước 1 — Tìm "con số gây sốc"
Đọc các câu `mechanism`/nghiên cứu trong `script.json`, chấm điểm theo 3 tiêu chí, chọn câu cao điểm nhất:

| Tiêu chí | Câu hỏi |
|---|---|
| **Gây sốc** | Con số có trái với điều người xem nghĩ không? (67% chọn sốc điện > "người ta ghét đau") |
| **Đơn giản** | Diễn đạt được bằng **1 con số** (67%, 1/4, 56 DAYS, 2×) không? |
| **Có nguồn** | Có nghiên cứu cụ thể (tác giả, năm) trong `youtube_metadata.txt` không? |

Không có câu nào có số? → dùng **phương án B** ở mục 4 (hình cơ chế + 2–3 chữ).

### Bước 2 — Viết "punch" (2–3 chữ, VIẾT HOA)
Punch là **ý nghĩa cảm xúc** của con số, không phải mô tả nghiên cứu.

| Con số | ❌ Mô tả | ✅ Punch |
|---|---|---|
| 67% chọn sốc điện | CHOSE ELECTRIC SHOCKS | **CHOSE PAIN** |
| ~1/4 để ý (spotlight effect) | NOTICED THE SHIRT | **ACTUALLY NOTICED** |
| dự kiến 34 ngày, thực tế 56 | TOOK 56 DAYS | **NOT LAZY** |

### Bước 3 — Viết dòng ngữ cảnh (≤ 7 từ, chữ nghiêng, 2 dòng)
Nói **đối tượng so sánh** để con số có nghĩa: *"over 15 minutes alone / with their thoughts"*. Dòng này được phép nhỏ, vì nó dành cho người xem trên máy tính và để tăng độ tin cậy.

### Bước 4 — Chọn hình biểu diễn số liệu

| Dạng số liệu | Hình | Ví dụ |
|---|---|---|
| Tỉ lệ phần trăm / "x trên 100" | **Waffle 10×10**, tô màu nhấn đúng số ô | 67% → 67 ô |
| Phân số đơn giản (1/4, 2/3) | **Hình người** hoặc waffle | 1 trong 4 người tô màu |
| So sánh 2 giá trị | **2 cột ngang**: cột cũ màu xám, cột mới màu nhấn | 34 vs 56 ngày |
| Thay đổi theo thời gian | **Đường cong** tự vẽ, đoạn quan trọng màu nhấn | cortisol, tâm trạng |
| Không có số (phương án B) | **Biểu tượng cơ chế lớn** (tia sét, đồng hồ, tim, não) | — |

Thêm **một biểu tượng trắng** đè lên khối màu (tia sét, đồng hồ…) để hình có tâm điểm. Tối đa 1 biểu tượng.

---

## 3. Quy chuẩn bố cục (1280×720)

| Thành phần | Quy cách |
|---|---|
| Nền | `#0A0908` + quầng sáng mờ màu nhấn (opacity ~10%) sau khối hình |
| Hình dữ liệu | Nửa trái: x 64–620, y 58–612 (waffle: ô 50px, khe 6px, bo góc 6px) |
| Con số lớn | Anton, **~300–330px** (≈ 45% chiều cao), trắng `#F4EFE7`, đặt từ x = 668, tự co cho vừa lề phải 64px |
| Punch | Anton **~130px**, màu nhấn `#E2553A`, ngay dưới con số |
| Ngữ cảnh | EB Garamond Italic **44px**, trắng 88%, 2 dòng |
| Màu nhấn | **Một màu duy nhất** `#E2553A`, chỉ dùng cho khối dữ liệu + punch |
| Chữ | Tối đa **1 con số + 3 chữ punch + 7 chữ ngữ cảnh** |
| Vùng cấm | Góc dưới-phải (x > 960, y > 612): trống · Dải đáy y > 634: trống · Lề 5% (64px) mọi cạnh |
| Logo | Không có |

**Đảo bố cục** (hình bên phải, chữ bên trái) khi muốn đổi nhịp giữa các video liền nhau, giữ nguyên mọi quy cách khác.

---

## 4. Quy tắc nội dung

1. **1 + 1 = 3:** đọc to tiêu đề + chữ trên thumbnail. Hai phần phải bổ sung nhau, **không lặp từ**. Tiêu đề nói lời hứa, thumbnail nói con số gây tò mò.
2. **Trung thực tuyệt đối:** con số phải có trong kịch bản **và** trong mục "Nguồn khoa học" của `youtube_metadata.txt`. Punch được phép nói gọn ("CHOSE PAIN") nhưng không được đổi nghĩa. Nếu nghiên cứu chỉ đúng với một nhóm (ví dụ "nam giới"), dòng ngữ cảnh hoặc tiêu đề phải không gây hiểu sai.
3. **Video phải trả lời sớm:** con số trên thumbnail phải xuất hiện trong video trước phút 0:30 (teaser) hoặc ở một mục rõ ràng.
4. **Phương án B (không có số):** dùng hình cơ chế lớn + punch 2–3 chữ ở vị trí con số (ví dụ "IT'S A FEELING").

---

## 5. Mẫu prompt

### 5.1 Prompt cho Claude (Opus 5.5) — **khuyên dùng**
Claude viết HTML/canvas rồi xuất JPG, nên chữ và số **chính xác 100%**, đồng nhất với video. Chạy trong Claude Code tại thư mục kênh, hoặc dán vào claude.ai.

```text
You are the thumbnail designer for Second Nature, a faceless science-backed self-improvement channel.
Build a YouTube thumbnail as ONE self-contained HTML file with a 1280x720 canvas, then render it to 02_thumbnail/thumbnail_graphic.jpg (Playwright screenshot, JPEG quality 95). Fonts: Anton and EB Garamond Italic from 00_Tools/motion/fonts/ (wait for document.fonts.ready before drawing).

CONTENT
- Big number: [SỐ, ví dụ 67%]
- Punch (accent color): [2–3 CHỮ VIẾT HOA, ví dụ CHOSE PAIN]
- Context, 2 lines, italic: [≤ 7 chữ, ví dụ over 15 minutes alone / with their thoughts]
- Data graphic on the left: [waffle 10x10 with N filled cells | two horizontal bars A vs B | hand-drawn curve | large icon]
- One white icon over the graphic: [lightning bolt | clock | heart | none]

LAYOUT
- Background #0A0908 with a faint accent glow (about 10% opacity) behind the graphic.
- Graphic in the left half: x 64–620, y 58–612. Waffle cells 50px, gap 6px, radius 6px; filled cells #E2553A, empty cells #F4EFE7 at 10%.
- Text column from x = 668: number in Anton about 330px #F4EFE7 (shrink to fit a 64px right margin), punch in Anton about 130px #E2553A directly below, context in EB Garamond Italic 44px #F4EFE7 at 88%.
- Keep empty: bottom-right corner (x > 960, y > 612), bottom strip (y > 634), 64px margin on every edge.
- Only one accent color. No logo, no watermark, no other text.

CHECK
- Render, then also export a 168x94 copy and confirm the number and punch are readable.
- Confirm nothing touches the forbidden zones. Fix and re-render if needed.
```

### 5.2 Prompt cho AI tạo ảnh (Nano Banana Pro / Ideogram / GPT Image)
Dùng khi không có Claude Code. **Phải kiểm tra lại từng chữ và con số**, vì AI tạo ảnh vẫn có thể viết sai chữ hoặc tô sai số ô.

```text
A YouTube thumbnail, 16:9, flat minimal data-graphic poster, dark editorial style.
Background: near-black warm #0A0908 with a faint red-orange glow on the left.
Left half: [a 10 by 10 grid of rounded squares where exactly N squares are filled solid red-orange #E2553A in reading order and the rest are dark grey | two horizontal bars without labels, a short grey one above a longer red-orange one], with one large white [lightning bolt] icon on top of the filled area.
Right half, left-aligned text in this exact order:
1) the number "[67%]" in a huge tall condensed bold sans-serif font (like Anton), warm white, about half the image height;
2) directly below, "[CHOSE PAIN]" in the same condensed font, red-orange #E2553A, about one fifth of the image height;
3) below that, two short lines in small italic serif (like EB Garamond): "[over 15 minutes alone]" / "[with their thoughts]".
The bottom-right corner and the bottom strip of the image stay empty and dark.
Only one accent color. Flat vector look, crisp edges, no gradients on text, no 3D, no photo, no people, no logo, no watermark, no extra words.
```

### 5.3 Prompt "đóng gói": để Claude tự chọn ý tưởng từ kịch bản
Dán kèm `script.json` + mục "Nguồn khoa học" trong `youtube_metadata.txt`. Claude áp dụng toàn bộ quy tắc ở mục 2–4 và trả về nội dung để điền vào prompt 5.1 hoặc 5.2.

```text
You are the thumbnail strategist for Second Nature. Using the script and the source list below, design ONE graphic data thumbnail.

1. List every statistic in the script that also appears in the source list. Score each 1–5 on: surprise (contradicts what viewers believe), simplicity (fits in one number like 67%, 1/4, 2x, 56 DAYS), source strength. Pick the highest total.
2. Write the punch: 2–3 words, ALL CAPS, the emotional meaning of the number, not a description of the study. Must not change the meaning of the finding.
3. Write the context: max 7 words over 2 short lines, italic, naming what the number is compared with.
4. Choose the data graphic: percentage → 10x10 waffle; simple fraction → people icons or waffle; two values → two bars; change over time → curve; no number → large mechanism icon. Add at most one white icon.
5. Check the 1+1=3 rule against the title "[TIÊU ĐỀ VIDEO]": thumbnail words must not repeat title words and together they must create a question the video answers before 0:30 or in a clearly marked step.
6. If no statistic qualifies, use plan B: a large mechanism icon + a 2–3 word punch in place of the number.

Output: the scoring table, your choice with one sentence of reasoning, then the filled CONTENT block for the HTML prompt and the filled prompt for an image model.

TITLE: [TIÊU ĐỀ]
SCRIPT: [dán script.json]
SOURCES: [dán mục Nguồn khoa học]
```

---

## 6. Ví dụ đã điền

| Video | Tiêu đề | Con số | Punch | Ngữ cảnh | Hình | Biểu tượng |
|---|---|---|---|---|---|---|
| **p08** ✅ đã làm | 7 Mental Toughness Habits Most People Never Build | **67%** | CHOSE PAIN | over 15 minutes alone / with their thoughts | Waffle 67/100 | Tia sét |
| p09 | Procrastination Isn't Laziness | **56 DAYS** | NOT LAZY | they planned 34. / it took 56. | 2 cột: 34 (xám) vs 56 (đỏ-cam) | Đồng hồ |
| p10 | The Perfect Confidence System | **1 IN 4** | ACTUALLY NOTICED | you guessed half / the room was watching | 4 hình người, 1 người tô màu | — |

**Giải thích nhanh:**
- **p08:** Wilson et al. (2014), *Science*: 67% nam giới chọn tự sốc điện. Video nói câu này ở giây 20 và ở thói quen số 4.
- **p09:** Buehler et al. (1994): dự kiến 33,9 ngày, thực tế 55,5 ngày (làm tròn 34/56 như trong kịch bản). Tiêu đề nói "không phải lười", thumbnail cho thấy nguyên nhân là lập kế hoạch sai.
- **p10:** Gilovich et al. (2000): đoán ~50% để ý, thực tế ~23% ("about a quarter" trong kịch bản). Tiêu đề nói "hệ thống tự tin", thumbnail gợi câu hỏi "chỉ 1/4 để ý đến mình?".

---

## 7. Checklist trước khi xuất

- [ ] Con số có trong kịch bản **và** trong nguồn khoa học, đúng số liệu.
- [ ] Punch 2–3 chữ, không đổi nghĩa phát hiện.
- [ ] Không lặp từ của tiêu đề. Đọc to tiêu đề + thumbnail: có tạo ra một câu hỏi không?
- [ ] Chỉ 1 màu nhấn `#E2553A`. Không logo.
- [ ] Vùng cấm trống: góc dưới-phải, dải đáy, lề 64px.
- [ ] Thu về 168×94: đọc được con số + punch trong 1 giây.
- [ ] Video trả lời con số trước 0:30 hoặc ở một mục rõ ràng.
- [ ] Xuất `02_thumbnail/thumbnail_graphic.jpg` (1280×720) và giữ file `.html` nguồn để sửa nhanh.
