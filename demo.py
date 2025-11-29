import gradio as gr
from google import genai
from google.genai import types
from PIL import Image

def generate_goods_image(input_image):
    """입력 이미지를 기반으로 캐릭터 인형 굿즈 이미지 생성"""
    if input_image is None:
        return None
    
    client = genai.Client(
        api_key="AIzaSyAdAFGr2fm9BZAlBCAM9FCaKyjFle06q1s",
    )

    # PIL Image를 바이트로 변환
    import io
    buffer = io.BytesIO()
    input_image.save(buffer, format="PNG")
    image_data = buffer.getvalue()

    model = "gemini-3-pro-image-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_bytes(data=image_data, mime_type="image/png"),
                types.Part.from_text(text="make a character goods based off of this photo"),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_modalities=["IMAGE", "TEXT"],
        image_config=types.ImageConfig(image_size="1K"),
    )

    # 이미지 생성
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if (
            chunk.candidates is None
            or chunk.candidates[0].content is None
            or chunk.candidates[0].content.parts is None
        ):
            continue
        
        part = chunk.candidates[0].content.parts[0]
        if part.inline_data and part.inline_data.data:
            # 바이트 데이터를 PIL Image로 변환

            output_buffer = io.BytesIO(part.inline_data.data)
            return Image.open(output_buffer)
    
    return None


# Gradio 인터페이스
demo = gr.Interface(
    fn=generate_goods_image,
    inputs=gr.Image(type="pil", label="Original", sources=["upload", "webcam"]),
    outputs=gr.Image(label="Generated"),
    title="Goods Character Image Generator",
    description="Upload an image and turn it into a character goods image.",
)

if __name__ == "__main__":
    demo.launch()

