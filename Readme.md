# DALL-E Image Generator with Flask and Bootstrap

## Overview

This project is a web application that allows users to generate images using OpenAI's DALL-E model. It is built using Flask for the backend and Bootstrap for the frontend.

![screenshot](https://raw.githubusercontent.com/shaheryaryousaf/ai-image-generator/main/Capture.JPG)

## Features

- User-friendly interface for generating images
- Real-time image generation based on user input
- Built with Flask and Bootstrap for easy customization

## Prerequisites

- Python 3.x
- Flask
- OpenAI API key

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/shaheryaryousaf/ai-image-generator.git
   ```

2. **Navigate to the project directory**

   ```bash
   cd ai-image-generator

   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

#### Make sure to setup a virtual envoirnment and install all packages

## Usage

1. Open your web browser and go to `http://localhost:81/`.
2. Enter your prompt in the input field.
3. Click the "Submit" button to generate the image.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
