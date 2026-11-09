# Image Captioning

A small Gradio app that generates captions for uploaded images using
[Salesforce BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base).

## Setup

Use Python 3.12. From the project folder, run:

```bash
python3.12 -m venv my_env
source my_env/bin/activate
pip install -r requirements.txt
python image_cap.py
```

Open the local URL printed in the terminal and upload an image to generate a caption.
The first run requires internet access to download the pretrained model.
