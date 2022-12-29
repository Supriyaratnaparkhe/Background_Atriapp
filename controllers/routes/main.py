from .atri import Atri
from fastapi import Request, Response
from atri_utils import *

def creat_new_background(at: Atri, back_img):
    if at.Image2.custom.src != '/app-assets/pic11.jpeg':
        inp_img = Image.open('assets/' + at.Image2.custom.src.split('/')[-1]).resize((600,600))
        if type(back_img) == str:
            back = Image.open('assets/' + back_img.split('/')[-1]).resize((600,600))
        
        if type(back_img) == bytes:
            back = Image.fromarray(parse_uploaded_file(back_img)).resize((600,600))
            
        img_new = change_background(inp_img, back, return_as_np_array=True)
        at.Image2.custom.src = creat_media_response(img_new, mime_type='images/jpeg')

def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    at.Flex27.styles.display = "none"
    at.TextBox10.styles.color = "#9D9D9D"
    pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    if at.TextBox10.onClick:
        at.Flex27.styles.display = 'flex'
        at.Flex23.styles.display = 'none'
        at.TextBox10.styles.color = "#000000"
        at.TextBox11.styles.color = "#9D9D9D"
    if at.TextBox11.onClick:
        at.Flex23.styles.display = 'flex'
        at.Flex27.styles.display = 'none'
        at.TextBox11.styles.color = "#000000"
        at.TextBox10.styles.color = "#9D9D9D"
        
    if at.Image6.onClick:
        at.Image2.custom.src = at.Image6.custom.src
        at.Image3.custom.src = at.Image6.custom.src
    if at.Image4.onClick:
        at.Image2.custom.src = at.Image4.custom.src
        at.Image3.custom.src = at.Image4.custom.src
    if at.Image7.onClick:
        at.Image2.custom.src = at.Image7.custom.src
        at.Image3.custom.src = at.Image7.custom.src
    if at.Image8.onClick:
        at.Image2.custom.src = at.Image8.custom.src
        at.Image3.custom.src = at.Image8.custom.src
        
    if at.Upload1.onChange:
        if at.Upload1.io.files is not None:
            file = at.Upload1.io.files[0]
            files_bytes = file.file.read()
            at.Image2.custom.src = create_media_response(files_bytes, mime_type=file.content_type)
            at.Image3.custom.src = at.Image2.custom.src
            
    if at.Image10.onClick:
        at.Image14.custom.src = at.Image10.custom.src
        #creat_new_background(at, at.Image14.custom.src)
    if at.Image11.onClick:
        at.Image14.custom.src = at.Image11.custom.src
        #creat_new_background(at, at.Image11.custom.src)
    if at.Image12.onClick:
        at.Image14.custom.src = at.Image12.custom.src
        #creat_new_background(at, at.Image12.custom.src)
    if at.Image13.onClick:
        at.Image14.custom.src = at.Image13.custom.src
        #creat_new_background(at, at.Image13.custom.src)
        
    if at.Upload3.onChange:
        if at.Upload3.io.files is not None:
            file = at.Upload3.io.files[0]
            files_bytes = file.file.read()
            at.Image14.custom.src = create_media_response(files_bytes, mime_type=file.content_type)
            creat_new_background(at, files_bytes)
            creat_new_background(at, files_bytes)
            
         
    pass