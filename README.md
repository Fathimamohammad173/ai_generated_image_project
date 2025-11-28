🌟 AI Image Generator – Text-to-Image ML Project

Transform text prompts into high-quality AI-generated images using open-source diffusion models.
This project was built as part of an ML Internship task to demonstrate hands-on skills in deep learning, generative AI, prompt engineering, and full-stack development.

🚀 Project Overview

This application allows users to:

✨ Convert text descriptions into images
🎨 Choose image styles (artistic, realistic, cartoon, etc.)
🖼 Generate multiple images per prompt
🌐 Use a simple web interface (Flask/Streamlit)
💾 Save generated images with metadata
🔧 Run locally on CPU or GPU

🧠 Tech Stack

Python

PyTorch

Diffusers (HuggingFace)

Flask / Streamlit

CUDA (optional GPU)

HTML/CSS for basic UI

📦 Features
📝 Text-to-Image Generation

Enter any text prompt such as:

“A futuristic city at sunset, 4K, ultra realistic”

“Cute robot painted in Van Gogh style”

🎛 Adjustable Settings

Number of images

Image style

Negative prompts

Guidance scale

🖥 User Interface

Enter prompt

View generated images

Download images

See generation progress

💾 Storage System

All images are stored with:

Prompt

Timestamp

Parameters used

File format (PNG/JPG)

🛠 Installation & Setup

🔹 Step 1: Clone the Repository
git clone <your_repo_link>
cd ai-image-generator

🔹 Step 2: Install Dependencies
pip install -r requirements.txt

🔹 Step 3: Run the App
python app.py

🔹 Step 4: Open in Browser
http://localhost:5000

⚡ Hardware Requirements
GPU (Recommended)

NVIDIA GPU (4GB+ VRAM)

CUDA installed

CPU (Fallback)

Works, but slower

No GPU required

💡 Prompt Engineering Tips

✔ Add details like “highly detailed, 8K, dramatic lighting”
✔ Specify style “anime style, watercolor, cyberpunk”
✔ Use negative prompts to remove unwanted elements
✔ Mention camera types for realism
✔ Avoid too short prompts

🔐 Ethical AI Usage

No harmful or illegal prompt submissions

No generation of violent, hateful, or explicit content

Images are watermarked to indicate AI origin

Follows responsible AI guidelines

📁 Project Structure
ai_image_generator/

│── app.py

│── requirements.txt

│── static/

│── templates/

│── models/

└── README.md


🧩 Limitations

CPU mode is slow

Limited model sizes due to hardware

Cannot perfectly mimic copyrighted art styles

Not trained on custom datasets

🔮 Future Improvements

Fine-tuning on custom datasets

Add more style presets

Upload custom images for editing

Add queue for large batch generation

Deploy as a public web app
