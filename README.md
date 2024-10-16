# Welcome to the matrix

## setup
- fork and clone this repository
- setup a virtual environment `python -m venv venv`
- activate the environment `.\venv\Scripts\Activate`
- install deps `pip install -r requirements.txt`
- run the code `python saver.py`

## port this application to Java
1. Create a Main Application Window:

  - Use JFrame to create the main window.
  - Set up the frame to hold a custom Canvas where the falling characters will be drawn.
2. Custom Canvas for Drawing:

  - Extend Canvas or JPanel to create a custom drawing surface.
  - Use the paintComponent() method for rendering the falling characters.
3. Character Falling Logic:

  - Create a FallingText class to represent individual characters, including their position (x, y), speed, and color opacity (alpha).
  - Each FallingText instance will change its position based on the speed and occasionally update the character (like in the Python version).
4. Repaint Loop:

  - Use a Timer to update the position of characters and repaint the canvas periodically (similar to the game loop in Pygame).
5. Handle Opacity and Character Change:

  - Use Java’s AlphaComposite to manage the transparency of each character as it falls.
  - Randomly change characters at intervals to simulate the matrix "flickering" effect.
6. Randomization:

  - Randomize the speed, size, opacity, and characters in the stream.
