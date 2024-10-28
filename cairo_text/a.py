import cairo 

wnd_w = 700
wnd_h = 700

with cairo.ImageSurface(cairo.FORMAT_RGB24, wnd_w, wnd_h) as sfc: 
	ctx = cairo.Context(sfc)
	ctx.set_source_rgb(255, 255, 255) 
	ctx.select_font_face( 
		'Arial', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
	ctx.set_font_size(80)
	_, _, txt_w, txt_h, _, _ = ctx.text_extents('Hello, World!')
	ctx.move_to(wnd_w / 2 - txt_w / 2, wnd_h / 2 + txt_h / 2)
	ctx.show_text('Hello, World!')
	ctx.stroke()
	sfc.write_to_png('text.png')