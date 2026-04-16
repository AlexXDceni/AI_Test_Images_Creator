# AI Image Creator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Pygame-2.0+-green.svg" alt="Pygame">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

> A simple and intuitive pixel art drawing tool designed for creating training images for AI models, particularly neural networks that work with image classification or generation.

---

## Features

### Drawing Tools
- **Left Click** - Draw pixels
- **Right Click** - Erase pixels (sets to white)
- Adjustable canvas size (custom width and height)
- Square ratio lock option (1:1) for square images

### File Management
- **Save drawings** as PNG files with custom names
- Auto-generated timestamp for saved files
- Dedicated save directory for all your creations

### Customization
- Setup screen to configure canvas dimensions before starting
- Flexible grid size
- Clean, minimalist interface

---

## Screenshots

```
┌─────────────────────────────────────────────┐
│  [Clear]  [Save]                            │  ← Menu Bar
├─────────────────────────────────────────────┤
│                                             │
│                                             │
│           ┌───────────────────┐             │
│           │ ■ ■ □ □ □ □ □ □   │             │
│           │ ■ □ □ □ □ □ □ □   │             │
│           │ □ □ ■ ■ ■ □ □ □   │             │  ← Drawing Grid
│           │ □ □ □ □ □ ■ □ □   │             │
│           │ □ □ □ □ □ □ □ ■   │             │
│           │ □ □ ■ ■ ■ □ □ □   │             │
│           └───────────────────┘             │
│                                             │
│              Saved: drawing.png             │  ← Status Message
└─────────────────────────────────────────────┘
```

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/AI-Image-Creator.git
cd AI-Image-Creator
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python main.py
```

---

## Usage

### Setup Screen
When you launch the application, you'll see a setup screen:

1. **Width** - Enter the desired canvas width in pixels
2. **Height** - Enter the desired canvas height in pixels
3. **1:1 Button** - Click to lock the aspect ratio to square (1:1)
   - When active, changing either width or height will automatically update the other
4. **Start** - Click to begin drawing with the specified dimensions

### Drawing Controls

| Action | Input | Description |
|--------|-------|-------------|
| Draw | Left Mouse Button | Fill a pixel with the current color |
| Erase | Right Mouse Button | Reset a pixel to white |
| Clear Canvas | Click "Clear" button | Remove all drawn pixels |
| Save Drawing | Click "Save" button | Open save dialog to name and save your drawing |

### Save Dialog
When you click "Save":
1. A dialog appears
2. Enter your desired filename (without extension)
3. Click "Save" to save or "Cancel" to abort
4. Files are saved to the `saved_drawings/` folder

---

## Project Structure

```
AI-Image-Creator/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── .gitignore          # Git ignore rules
└── saved_drawings/     # Directory for saved images (created automatically)
```

---

## Dependencies

| Package | Version | Description |
|---------|---------|-------------|
| pygame | 2.0+ | Cross-platform game development library |
| pygame_gui | 0.6+ | GUI library for pygame |

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## Use Cases

### AI Training Data
This tool is particularly useful for creating simple image datasets for AI training:

- **Digit Recognition** - Create handwritten digit images
- **Simple Classification** - Draw simple shapes or symbols
- **Character Recognition** - Design custom characters or letters
- **Sketch Training** - Generate simple sketch-style images

### Example Configurations

| Purpose | Width | Height |
|---------|-------|--------|
| MNIST-style digits | 28 | 28 |
| Small icons | 16 | 16 |
| Medium icons | 32 | 32 |
| Large images | 64 | 64 |

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Built with [Pygame](https://www.pygame.org/) and [pygame_gui](https://pygame-gui.readthedocs.io/)
- Inspired by the need for simple pixel art tools for AI training data

---

<p align="center">
  Made with ❤️ for AI enthusiasts and pixel art lovers
</p>
