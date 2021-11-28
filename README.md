# Video Quality Rating
A simple app to watch and rate given videos based on the quality.

## Requirements:

+ **ffmpeg**: A collection of libraries and tools to process multimedia content such as audio, video, subtitles and related metadata.
  + To check if **ffmpeg** is installed, open **Command Prompt**, type: `ffmpeg`
  + To install: Go to [**FFmpeg** download page](https://www.ffmpeg.org/download.html). Download the campatible version for your OS, extract the folder.
     
   On **WINDOWS:**
    1. Rename the folder to: FFmpeg
    2. Copy/Cut folder to **C Drive** (C:\)
    3. Open **Environment variables control panel**:
        + Open search bar
        + Type: *system variables*, open: **Edit the system environment variables**
        + Click **Environment variables**
        + In **System variables**, select *Path*, select *Edit*
        + In new **Edit environment variable** window, select *New*
        + Copy and paste the path of the FFmpeg above here 
        + Click *OK* to save changes <br />
        
  More detail [here](https://windowsloop.com/install-ffmpeg-windows-10/)

    On **MacOS:**
    1. Press `Command+Space`, and type Terminal.
    2. Run the command below: 
   
      ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 2> /dev/null  
    3. Enter your Mac's user password if needed and wait for the command to finish.
    4. Run: `brew install ffmpeg`
    
  More detail [here](http://trac.ffmpeg.org/wiki/CompilationGuide/macOS)
    
    On **Linux:**
    1. Open Terminal.
    2. Run the command below: 
   
      sudo apt update
      sudo apt install ffmpeg  
    It might ask for additional disk space, type **Y**, and press **Enter**
    
  More detail [here](https://linuxhint.com/install-ffmpeg-ubuntu/)
  
+ **pip Library**, **Pillow Image Library** and **PyMySQL package** for **Python**:
        
   To install the libraries, packages (On both **Windows** and **MacOS**), open **Command Prompt**:   
    + For **pip Library**: `python -m ensurepip --upgrade`, more detail can be found on [pip documentation](https://pip.pypa.io/en/stable/installation/) 
    + For **Pillow Image Library**: `python -m pip install Pillow` 
    + For **PyMySQL package**: `python -m pip install PyMySQL`, more detail can be found on [PyMySQL](https://pypi.org/project/PyMySQL/)
    
   To install on **Linux**, open **Terminal**:
    + For **pip Library**: `sudo apt install python3-pip`
    + For **Pillow Image Library**: `sudo apt install python3-Pillow` 
    + For **PyMySQL package**: `sudo apt install python3-pymysql` 
    
+ **Videos for experiment**: 
  + Download the videos for testing:
    +  [Monday_Group.zip](https://drive.google.com/file/d/1qTmiInYrBu5rGkOU-U6WCG969eW_mpIK/view?usp=sharing)
    +  [Thursday_Group.zip](https://drive.google.com/file/d/1YMnzW6_iQvR777wGWbddLs7P6DrofgpI/view?usp=sharing)
  + Unzip the folder and relocate the unzipped one to where the **Video_Quality_Rating** is located (the folder should be named with the tittle `Monday_Group` or `Thursday_Group`). 
  
  For example: The directory to `Monday_Group` should be: `...\Video_Quality_Rating\Monday_Group\[videos_here]`
  
## Testing:

The program is given to the two group to test. 
+ **Monday_Group**: Select **Monday Group** when entering **Student ID**.
+ **Thursday_Group**: Select **Thursday Group** when entering **Student ID**.

To run the application, open **Command Prompt** where the application located, type: `python app.py`

After each video, observer will be asked to rate the quality of the watched video. 
The result of the test will be saved to *result.csv* file.
