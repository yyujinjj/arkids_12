import qrcode
from PIL import Image, ImageDraw, ImageFont

season = 45  
num_sessions = 15
base_url = f"https://yyujinjj.github.io/arkids_12/season{season}/"

font_path = "C:/Windows/Fonts/malgun.ttf"
font = ImageFont.truetype(font_path, 20)

for i in range(1, num_sessions + 1):
    session = f"{i}st" if i == 1 else f"{i}nd" if i == 2 else f"{i}rd" if i == 3 else f"{i}th"
    label = f"매말매기 시즌45 유년부 - {i}일차"
    
    url = f"{base_url}{session}/"
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    
    w, h = img.size
    
    new_h = h + 40
    new_img = Image.new("RGB", (w, new_h), "white")
    new_img.paste(img, (0, 0))
    
    draw = ImageDraw.Draw(new_img)
    
    bbox = draw.textbbox((0, 0), label, font=font)
    text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    
    draw.text(((w - text_w) / 2, h + (40 - text_h) / 2),
              label, font=font, fill="black")
    
    filename = f"season{season}_{session}_qr.png"
    new_img.save(filename)
    print(f"QR 코드 저장 완료: {filename} → {url}")
