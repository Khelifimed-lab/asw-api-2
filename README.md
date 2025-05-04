# PENCIL SHADOW 2 (asw-api-2)

A simple API that converts images to pencil sketch style using OpenCV.

- Endpoint: `/sketch` (POST)
- Content-Type: binary image (e.g. PNG, JPG)
- Response: pencil sketch version of the image.

## Tech stack
- Python + Flask
- OpenCV (with fixed max blur value = 20)
- Deployable on Render.com

This version is a fixed high-quality sketch API with max effect, designed to behave like: [https://pencilsketch.imageonline.co](https://pencilsketch.imageonline.co)