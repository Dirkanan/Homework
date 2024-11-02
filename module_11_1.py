from PIL import Image, ImageDraw, ImageFont

def create_mem(image_path, text, output_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", 100)
    except IOError:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]  
    text_height = bbox[3] - bbox[1]  
    text_x = (image.width - text_width) / 2
    text_y = image.height - text_height - 10 


    draw.text((text_x, text_y), text, font=font, fill="white")

    image.save(output_path)


image_path = r"C:\Users\Юрий\PycharmProjects\home_works\Home-work\module11\библ.jpg" 
text = "чебоксары"  
output_path = r"C:\Users\Юрий\PycharmProjects\home_works\Home-work\module11\мемы\чебоксары.jpg" 

create_mem(image_path, text, output_path)
