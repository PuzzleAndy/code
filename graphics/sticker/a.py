from PIL import Image, ImageFilter

stroke_radius = 9
img = Image.open('lil_sho.png') # RGBA image
stroke_image = Image.new("RGBA", img.size, (255, 255, 255, 255))
img_alpha = img.getchannel(3).point(lambda x: 255 if x>0 else 0)
stroke_alpha = img_alpha.filter(ImageFilter.MaxFilter(stroke_radius))
# optionally, smooth the result
stroke_alpha = stroke_alpha.filter(ImageFilter.SMOOTH_MORE)
stroke_image.putalpha(stroke_alpha)
output = Image.alpha_composite(stroke_image, img)
output.save("output.png")