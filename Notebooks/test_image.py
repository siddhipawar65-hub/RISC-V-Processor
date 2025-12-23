import cocotb
from cocotb.triggers import Timer
import numpy as np
from PIL import Image
import os

@cocotb.test()
async def test_image_proc(dut):
    # --- USE YOUR DIRECT PATH HERE ---
    image_path = r"C:\Users\rujut\OIP.jpg" 
    save_directory = os.path.dirname(image_path)
    
    gray_save_path = os.path.join(save_directory, "output_gray.png")
    seg_save_path = os.path.join(save_directory, "output_seg.png")

    # Load and resize
    img = Image.open(image_path).convert("RGB").resize((64, 64))
    pixels = np.array(img)
    h, w = pixels.shape[:2]

    dut.threshold.value = 127

    gray_img = np.zeros((h, w), dtype=np.uint8)
    seg_img = np.zeros((h, w), dtype=np.uint8)

    for y in range(h):
        for x in range(w):
            r, g, b = pixels[y, x]
            dut.r.value = int(r)
            dut.g.value = int(g)
            dut.b.value = int(b)
            await Timer(1, units="ns")
            
            # Capture the hardware output
            gray_img[y, x] = int(dut.gray.value)
            seg_img[y, x] = int(dut.segmented.value)
    
    # --- FORCE SAVE TO ABSOLUTE PATH ---
    Image.fromarray(gray_img).save(gray_save_path)
    Image.fromarray(seg_img).save(seg_save_path)
    
    cocotb.log.info(f"SUCCESS: Saved images to {save_directory}")
