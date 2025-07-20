# Mr.Chess

## Description
Mr.Chess is a desktop chess application designed for two human players to enjoy a 1v1 chess match on a single Windows PC. Developed using Python and Pygame in PyCharm, the game features a clean, intuitive interface where players use the mouse to move pieces and the keyboard for additional controls. Key features include:
- **Mouse-based Movement**: Click and place pieces to make moves, with highlighted valid moves for the selected piece.
- **Keyboard Controls**: Undo/redo moves, start a new game, and switch between six board color schemes.
- **Game Mechanics**: Supports pawn promotion, checkmate, and stalemate detection. No AI opponent is included, focusing on human vs. human gameplay.
- **Visuals**: A customizable 8x8 chessboard with piece images stored in the `Chess_project` folder.

The game is packaged as an executable (`MRChess.exe`) for easy installation and play, requiring no additional dependencies for end users.

## Installation Instructions
1. **Download the Game**:
   - Download the MrChess.rar file from the following Google Drive link: [[Download the game](https://drive.google.com/file/d/1weATcSm_miZMtWtURMLUJC3vu15MoTt7/view?usp=drive_link)].
   - Extract the .rar file using a tool like WinRAR or 7-Zip to obtain Chess_project.exe and MRChess.exe.

2. **Chess_project Setup**:
   - Place the `Chess_project` folder in the `C:\` directory (i.e., `C:\Chess_project`). This folder contains the piece images (`images/` directory) required for the game.
   - Ensure the folder structure remains intact, as the game references images from `C:\Chess_project\Chess\images\`.

3. **MRChess Setup**:
   - Place the `MRChess.exe` executable in any preferred directory.
   - Double-click `MRChess.exe` to install and launch the game. The game opens directly to the chessboard, ready for play.
   - Ensure approximately 250 MB of free disk space is available.

No additional software or dependencies are required to run the executable.

## Controls
- **Mouse**: Click to select a piece and click on a valid square to move it. Valid moves are highlighted in green, with the selected square in blue.
- **Keyboard**:
  - `R`: Start a new game.
  - `Z`: Undo the last move (limited to one undo unless reset).
  - `X`: Redo the last undone move (available only after an undo and before a new game).
  - `1, 2, 3, 4, 5, 6`: Change the board color scheme (e.g., grayscale, purple, blue, etc.).

## Screenshots
Below are placeholders for screenshots of the game. These will be updated manually with images showcasing gameplay.

- **Gameplay Screenshot 1**: 
![Gameplay1](Images/Gameplay.png)
- **Gameplay Screenshot 2**: 
![Gameplay2](Images/Gameplay2.png)
- **Gameplay Screenshot 3**: 
![Gameplay3](Images/Gameplay3.png)

## Installation and Gameplay Video
A video demonstrating the installation process and gameplay will be added manually. It will cover:
- Setting up the `Chess_project` folder and `MRChess.exe`.
- Launching the game and playing a sample match, including move highlights and color changes.

https://github.com/user-attachments/assets/b76902a8-8910-4e0e-9948-f2c6025be6b6

## System Requirements
- **Operating System**: Windows PC
- **Free Disk Space**: Approximately 250 MB
- **For End Users**: No additional software or dependencies required to run `MRChess.exe`.
- **For Developers**: To modify or run the source code, Python 3.x and Pygame must be installed. Use `pip install pygame` to install Pygame.

## Contributing
Mr.Chess was developed by a team led by LAP207, who maintains the GitHub repository and handles all uploads. Team members are added as collaborators with read access to the repository. To contribute:
- **Suggestions or Code Contributions**: Contact LAP207 to share changes locally (e.g., via email or shared drive). Alternatively, fork the repository, make changes, and submit a pull request for review.
- **Issues**: Report bugs or suggest features by creating an issue in the GitHub repository.


## Developed By
LAP207
