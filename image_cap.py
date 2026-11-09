import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

model_id = "Salesforce/blip-image-captioning-base"
processor = AutoProcessor.from_pretrained(model_id)
model = BlipForConditionalGeneration.from_pretrained(model_id)


def caption_image(input_image: np.ndarray):
    if input_image is None:
        return "Please upload an image."

    raw_image = Image.fromarray(input_image).convert("RGB")
    inputs = processor(images=raw_image, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100)
    return processor.decode(outputs[0], skip_special_tokens=True)


iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(type="numpy"),
    outputs="text",
    title="Image Captioning",
    description="Upload an image to generate a caption.",
)

if __name__ == "__main__":
    iface.launch()

