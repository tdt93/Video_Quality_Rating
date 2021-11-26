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
    
+ **pip Library** and **Pillow Image Library** for **Python**:
  + To check if the libraries have been installed (On both **Windows** and **MacOS**), open **Command Prompt**:
    - To check for **pip Library**, type: `python -m pip --version` 
    - To check for **Pillow Image Library**, type: `python -m PIL --version`
        
  + To install the libraries (On both **Windows** and **MacOS**), open **Command Prompt**:   
    + For **pip Library**: `python -m ensurepip --upgrade`, more detail can be found on [pip documentation](https://pip.pypa.io/en/stable/installation/) 
    + For **Pillow Image Library**: `python -m pip install Pillow` 

+ **Videos for experiment**: 
  + Download the videos for testing:
    +  [Monday Group](https://drive.google.com/file/d/1qTmiInYrBu5rGkOU-U6WCG969eW_mpIK/view?usp=sharing)
    +  [Thursday Group](https://drive.google.com/file/d/1YMnzW6_iQvR777wGWbddLs7P6DrofgpI/view?usp=sharing)
  + Extract the folder to the location where application is located (the folder should be named with the tittle `Monday_Group` or `Thursday_Group`). 
  
  For example: The directory to `Monday_Group` should be: `...\Video_Quality_Rating\Monday_Group\[videos_here]`
  
## Testing:

The program is given to the two group to test. 
+ **Monday_Group**: Select **Monday Group** when entering **Student ID**.
+ **Thursday_Group**: Select **Thursday Group** when entering **Student ID**.

To run the application, open **Command Prompt** where the application located, type: `python app.py`

After each video, observer will be asked to rate the quality of the watched video. 
The result of the test will be saved to *result.csv* file.
