# préambule import the different package
import time
import subprocess
import sys
import re

# define the most important variable
f_1er = ""
f_total = ""
sequencage = ""
time_  = ""
path = ""


verification = False
while verification != True:
    # ask the user to enter the information of the render
    f_1er = input("enter the first frame : ")
    f_total = input("enter the last frame : ")
    sequencage = input("enter the number of frame per session : ")
    time_  = input("enter the time that the program wait per session (minutes) : ")
    path = input("enter the path of your Blender project : ")
    #clear the terminal for more visibilty
    subprocess.run("clear", shell = True)

    #ask the user if the information are right
    print(f"first frame : {f_1er} \ntotal number of frame : {f_total} \nnumber of rendering session : {sequencage} \ntime between each section : {time_} \npath of blender project : {path}")
    test = input("is this right ? Y or N or STOP : ")
    
    #verify the input of the user for continue, redo or quit the program
    if test.upper() == "Y":
        verification = True
        subprocess.run("clear")
            
    elif test.upper() == "N":
        verification = False
   
    elif test.upper() == "STOP":
        print("stoping the program")
        sys.exit(0)
    else:
        print("Not a response closing the program")
        sys.exit(0)


# create the range, divide the total number of frame with the sequençage
q = int(f_total) // int(sequencage)
r = int(f_total) % int(sequencage)
# new variable for more comprehension
last_frame = int(sequencage)
first_frame = int(f_1er)
frame = int(f_1er)
# begin the rendering with for range the diision on line 46

output = ""

for i in range(int(q)):
    if i == 0:
        output = subprocess.run(["blender", "-b", path, "-s", str(first_frame), "-e", str(last_frame), "-a"], capture_output=True, text=True)
        first_frame += int(sequencage)
        last_frame += int(sequencage)
        print(output.stdout)
        pass
    else:
        # render the frame with the terminal
        subprocess.run(["blender", "-b", path, "-s", str(first_frame), "-e", str(last_frame), "-a"])
        #print(f"rendering frames {first_frame} to {last_frame}")
        # add the sequençage to the variable to continue
        first_frame += int(sequencage)
        last_frame += int(sequencage)
        if i == q - 1:
            break
        #waiting time before the next rendering
        print(f"waiting {time_} minute(s) before the next session")
        time.sleep(float(time_) * 60)

last_frame_2 = int(first_frame) + int(r) - 1
if r != 0:
    subprocess.run(["blender", "-b", path, "-s", str(first_frame), "-e", str(last_frame_2), "-a"])
#print(f"rendering frames {first_frame} to {first_frame + int(r) - 1}")

#ffmpeg initilisation
save_path = ""
for line in output.stdout.splitlines():
    if line.startswith("Saved:"):
       save_path = line[len("Saved:"):].strip().strip("'\"")

save_path_split = re.split(r"(/)", save_path)
taille = len(save_path_split)
save_path_split.pop(taille - 1)
save_path_split.pop(taille - 2)
save_path_str = "".join(save_path_split)

subprocess.run(["ffmpeg", "-r", "24", "-i", "%04d.png", "-c:v", "libx264", "-pix_fmt", "yuv420p", "otuput.mp4"], cwd = save_path_str)