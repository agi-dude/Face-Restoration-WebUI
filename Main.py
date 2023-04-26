import subprocess
import gradio as gr
from PIL import Image
import time
from numpy import asarray
import os
import glob

CodeFormerLoc = "AIs\\CodeFormer"
GFPGANLoc = "GFPGAN"


def prepare_file(inputIMG, model):
    """Prepares the input images"""

    files = glob.glob(CodeFormerLoc + '\\inimgs\\*.*')
    for f in files:
        os.remove(f)
    files = glob.glob(GFPGANLoc + '\\inputs\\whole_imgs\\*.*')
    for f in files:
        os.remove(f)

    if model == "Code_Former":
        os.replace(inputIMG, CodeFormerLoc + "\\inimgs\\" + os.path.basename(inputIMG))
    elif model == "GFPGAN":
        os.replace(inputIMG, GFPGANLoc + "\\inputs\\whole_imgs\\" + os.path.basename(inputIMG))


def modelExecuterCodeForemer(input_img, weight):
    """Executer for CodeFormer"""

    print(input_img)  # For Debugging Purposes

    prepare_file(input_img, "Code_Former")
    time.sleep(3)
    if weight == 0: weight = "0.0"

    cmd = 'python ' + CodeFormerLoc + '\\inference_codeformer.py -w ' + str(weight) + ' --has_aligned --input_path "' + CodeFormerLoc + '\\inimgs"'
    print(cmd)
    os.system(cmd)

    outputfilename = os.path.basename(input_img)
    img = Image.open("results\\inimgs_" + str(weight) + "\\restored_faces\\" + outputfilename)

    return asarray(img)


def modelExecuterGFPGAN(input_img, Version):
    """Model Executer GFPGAN"""

    print(input_img)  # For Debugging Purposes

    prepare_file(input_img, "GFPGAN")
    time.sleep(3)

    cmd = "python " + GFPGANLoc +"\\inference_gfpgan.py -i inputs/whole_imgs -o results -v " + Version +" -s 2"
    print(cmd)
    os.system(cmd)

    outputfilename = os.path.basename(input_img)
    img = Image.open(GFPGANLoc + "\\results\\restored_imgs\\" + outputfilename)

    return asarray(img)


demo = gr.Interface(modelExecuterCodeForemer, [gr.Image(type="filepath"), gr.Slider(0, 1)], "image")
demo1 = gr.Interface(modelExecuterCodeForemer, [gr.Image(type="filepath"),
                                                gr.Dropdown(["1", "1.2", "1.3"], label="Model")], "image")
gr.TabbedInterface([demo, demo1], ["CodeFormer", "GFPGAN"]).launch()
