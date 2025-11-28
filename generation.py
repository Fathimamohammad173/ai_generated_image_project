from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(prompt, negative, num, steps, guidance):
    prompt = "highly detailed, 4k, professional lighting, " + prompt
    images = pipe(
        prompt,
        negative_prompt=negative,
        num_inference_steps=steps,
        guidance_scale=guidance,
        num_images_per_prompt=num
    ).images
    return images
