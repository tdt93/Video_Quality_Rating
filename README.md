# Video Quality Rating
A simple app to watch and rate given videos based on the quality.

## Requirements:

+ **ffmpeg**: A collection of libraries and tools to process multimedia content such as audio, video, subtitles and related metadata.
  + To check if **ffmpeg** is installed, open **Command Prompt**, type: `ffmpeg`
  + To install: Go to [**FFmpeg** download page](https://www.ffmpeg.org/download.html).
    1. Download the campatible version for your OS, extract the folder.
    2. Rename the folder to: FFmpeg
    3. Copy/Cut folder to **C Drive** (C:\)
    4. Open **Environment variables control panel**:
        + Open search bar
        + Type: *system variables*, open: **Edit the system environment variables**
        + Click **Environment variables**
        + In **System variables**, select *Path*, select *Edit*
        + Add the path of FFmpeg folder above to the list by click *New*
        + Click *OK* to save changes
    
+ **pip Library** and **Pillow Image Library** for **Python**:
  + To check if the libraries have been installed (On both **Windows** and **MacOS**), open **Command Prompt**:
    - To check for **pip Library**, type: `python -m pip --version` 
    - To check for **Pillow Image Library**, type: `python -m PIL --version`
        
  + To install the libraries (On both **Windows** and **MacOS**), open **Command Prompt**:   
    + For **pip Library**: `python -m ensurepip --upgrade`, more detail can be found on [pip documentation](https://pip.pypa.io/en/stable/installation/) 
    + For **Pillow Image Library**: `python -m pip install Pillow` 

+ **Sample videos**: 
  + Download the sample videos for testing [here](https://drive.google.com/file/d/1k450SHWLSetcTSNZAjt4L-QEAmXzGuu2/view?usp=sharing)
  + Extract the folder and copy the **videos** (not their folders) into their according folders where the application located (**Monday Group** and **Thursday Group**)
  
## Testing:

The program is given to the two group to test. 
+ **Monday Group**: Will be shown vary videos with different quality. (Select **Monday Group** when entering **ID**)
+ **Thursday Group**: Will be the same video but with different quality. (Select **Thursday Group** when entering **ID**)

To run the application, open **Command Prompt** where the application located, type: `python app.py`

After each video, observer will be asked to rate the quality of the watched video. 
The result of the test will be saved to *result.csv* file.
