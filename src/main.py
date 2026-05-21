from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

# คลังคำคมมีมแมวสุดกาว
CAT_QUOTES = [
    "มนุษย์... ไปตักอึให้เราเดี๋ยวนี้",
    "มองหน้าทำไม อยากมีเรื่อง (หรืออยากโดนตบแก้วน้ำตกโต๊ะ)?",
    "นอนวันละ 22 ชั่วโมง แต่อ่อนเพลียตลอดเวลา",
    "อุตส่าห์ซื้อที่นอนราคา 3,000 บาทเพื่อมานอนบนกล่องกระดาษราคา 0 บาท",
    "ตื่นมาตอนตี 3 เพื่อวิ่งรอบบ้านโดยไม่มีเหตุผล",
    "อ้วนไม่ได้เรียกอ้วน เค้าเรียก 'สมบูรณ์แบบในรูปทรงวงกลม'",
    "พยายามทำตัวพริ้วไหว... แต่ติดพุง"
]

# สุ่มรูปแมวตลกๆ จากอินเทอร์เน็ต (Cataas & Unsplash)
CAT_IMAGES = [
    "https://cataas.com/cat/meme",
    "https://cataas.com/cat/funny",
    "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?q=80&w=500",
    "https://images.unsplash.com/photo-1573865526739-10659fec78a5?q=80&w=500",
    "https://images.unsplash.com/photo-1533738363-b7f9aef128ce?q=80&w=500"
]

@app.get("/", tags=["home"])
async def home() -> dict:
    return {"message": "Hello world", "status": True}

# 📌 หน้าเว็บมีมแมวสุดรั่ว
@app.get("/meme", response_class=HTMLResponse)
async def cat_meme_page():
    html_content = """
    <!DOCTYPE html>
    <html lang="th">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>สมาคมแมวส้มแห่งประเทศไทย 🐱</title>
        <link href="https://fonts.googleapis.com/css2?family=Mitr:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Mitr', sans-serif;
                background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                margin: 0;
                padding: 20px;
                text-align: center;
            }
            .card {
                background: white;
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.15);
                max-width: 450px;
                width: 100%;
                border: 4px solid #ff6b6b;
                transition: transform 0.3s;
            }
            .card:hover {
                transform: scale(1.02) rotate(-1deg);
            }
            h1 {
                color: #ff6b6b;
                margin-top: 0;
                font-size: 28px;
                text-shadow: 2px 2px #ffe3e3;
            }
            .meme-img-container {
                width: 100%;
                height: 300px;
                border-radius: 12px;
                overflow: hidden;
                background-color: #f0f0f0;
                border: 3px solid #48dbfb;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .meme-img {
                width: 100%;
                height: 100%;
                object-fit: cover;
            }
            .quote-box {
                margin: 20px 0;
                padding: 15px;
                background: #f7f1e3;
                border-left: 5px solid #ffb142;
                font-weight: bold;
                color: #2c3e50;
                font-size: 18px;
                min-height: 54px;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            button {
                background: #ff6b6b;
                color: white;
                border: none;
                padding: 12px 25px;
                font-size: 18px;
                font-family: 'Mitr', sans-serif;
                border-radius: 50px;
                cursor: pointer;
                box-shadow: 0 5px 15px rgba(255, 107, 107, 0.4);
                transition: 0.2s;
                width: 100%;
            }
            button:hover {
                background: #ee5253;
                transform: translateY(-2px);
            }
            button:active {
                transform: translateY(1px);
            }
            .footer {
                margin-top: 20px;
                font-size: 12px;
                color: #666;
            }
        </style>
    </head>
    <body>

        <div class="card">
            <h1>ศาลากลางแมวเหมียว 🐱✨</h1>
            
            <div class="meme-img-container">
                <img id="catMeme" class="meme-img" src="https://cataas.com/cat/meme" alt="มีมแมว">
            </div>

            <div id="quote" class="quote-box">"มนุษย์... ไปตักอึให้เราเดี๋ยวนี้"</div>

            <button onclick="changeMeme()">เสพมีมเพิ่ม (กราบอ้อนวอนน้อน)</button>
        </div>

        <div class="footer">สร้างด้วยความเคารพรักในอุ้งเท้าแมว 🐾</div>

        <script>
            const quotes = """ + str(CAT_QUOTES) + """;
            
            function changeMeme() {
                const img = document.getElementById('catMeme');
                const quoteText = document.getElementById('quote');
                
                // สุ่มคำคม
                const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
                quoteText.innerText = `"${randomQuote}"`;
                
                // รีโหลดรูปภาพใหม่จาก API แมว (ใส่ตูดแคชต่อท้ายกันมันจำรูปเดิม)
                img.src = "https://cataas.com/cat/meme?time=" + new Date().getTime();
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)