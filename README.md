# Blender rendering helper for macOS and Linux

This script written in Python allows you to render Blender animation in multiple times. The script renders each frame one by one, saves them in Blender’s default output folder, and creates a 24fps video from the PNG files.. You can choose how many frames will render and choose the time between each session. This script is **only for Linux and macOS**, but I will try to update it soon for Windows users. This project is made for people who have an old PC or a PC with small capacity.

## How to install

To install this script you only have to download the *main.py* file and put it in whatever folder on your PC.  
To work properly you will need to add Blender to your [PATH](https://docs.blender.org/manual/en/latest/advanced/command_line/index.html) and you will also need to install [FFmpeg](https://ffmpeg.org/download.html).

## How to use it

1. Launch the terminal from the folder of the script  
2. Run the script with:
    ```bash
    python3 main.py
    ```
3. Enter the first frame of your animation (often frame number 1)  
4. Enter the last frame of your animation  
5. Enter the number of frames you want to render in each session (the script allows odd numbers)  
6. Enter the time you want the script to wait between each session (allowing your PC to cooldown)  
7. Enter the PATH of your Blender project  
   (on Mac: go to the .blend file, right click, press Alt and select “Copy .blend as path”)  
8. Verify your answers because the script doesn't check if you put the right information  
9. The script will then begin.  
   In the terminal, the first session will take longer to start because of a code error,  
   but it's not a big deal — just wait.

## The project

This project was made by me, a 16-year-old beginner in Python, so it certainly has a lot of bugs.  
If the script doesn't work or if you encounter a bug, don't hesitate to contact me on GitHub.
If this project helps many people, I will keep improving it. Please don’t hesitate to give your feedback.
