# Video Quality Rating
A simple app to watch and rate given videos based on the quality.  
An **AGH** experiment. This experiment uses the *AGH/NTIA* dataset, which is provided from Consumer Digital Video Library ([CDVL](https://www.cdvl.org/)).

## Requirements: (preferably to be performed on Windows)

+ From this repository: Download as ZIP, extract and rename the folder back to *Video_Quality_Rating*.

+ **ffmpeg**: A collection of libraries and tools to process multimedia content such as audio, video, subtitles and related metadata.
  + To check if **ffmpeg** is installed, open **Command Prompt**, type: `ffmpeg`
  + To install: Go to [**FFmpeg** download page](https://www.ffmpeg.org/download.html). Download the campatible version for Windows: 
    + Current version: [*builds from gyan.dev*](https://www.gyan.dev/ffmpeg/builds/).
    + Download: *ffmpeg-git-essentials.7z*
     
   On **WINDOWS:**
    1. Extract and rename the folder to: **ffmpeg**
    2. Copy/Cut folder to **C Drive** (the path should be: `C:\ffmpeg`)
    3. Open the **ffmpeg** folder, get the Path to the sub folder as: `C:\ffmpeg\...\bin`, copy the Path
    4. Open **Environment variables control panel**:
        + Open search bar
        + Type: *system variables*, open: **Edit the system environment variables**
        + Click **Environment variables**
        + In **System variables**, select *Path*, select *Edit*
        + In new **Edit environment variable** window, select *New*
        + Paste the Path from above here (`C:\ffmpeg\...\bin`)
        + Click *OK* to save changes <br />
        
    5. Open **Command Prompt**, type: `ffmpeg` and check if the command works properly.
 
  More detail [in English](https://windowsloop.com/install-ffmpeg-windows-10/) | [in Polish](https://soundartifacts.com/pl/how-to/186-how-to-install-ffmpeg-on-windows-10-amp-add-ffmpeg-to-windows-path.html)

<!--    On **MacOS:**
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
    
  More detail [here](https://linuxhint.com/install-ffmpeg-ubuntu/) -->
  
+ **pip Library**, **Pillow Image Library** and **PyMySQL package** for **Python**:
        
   To install the libraries, packages (On both **Windows** and **MacOS**), open **Command Prompt** and run:   
    + For **pip Library**: `python -m ensurepip --upgrade`, more detail can be found on [pip documentation](https://pip.pypa.io/en/stable/installation/) 
    + For **Pillow Image Library**: `python -m pip install Pillow` 
    + For **PyMySQL package**: `python -m pip install PyMySQL`, more detail can be found on [PyMySQL](https://pypi.org/project/PyMySQL/)
    
  <!-- To install on **Linux**, open **Terminal** and run:
    + For **pip Library**: `sudo apt install python3-pip`
    + For **Pillow Image Library**: `sudo apt install python3-Pillow` 
    + For **PyMySQL package**: `sudo apt install python3-pymysql` -->
    
+ **Videos for experiment**: 
  + Download the videos for testing according to the group of the participant:
    +  [Monday_Group.zip](https://drive.google.com/file/d/1jjoDG5JyC5KLv2ekNddikpnHEQRAaQdk/view?usp=sharing)
    +  [Thursday_Group.zip](https://drive.google.com/file/d/1ALyRvkUoc8jlqPG1eSH4PBJUmxOUcaJS/view?usp=sharing)
  + Unzip the folder and relocate the unzipped one to where the **Video_Quality_Rating** is located (the folder should be named with the tittle `Monday_Group` or `Thursday_Group`). 
  
  For example: The directory to `Monday_Group` should be: `...\Video_Quality_Rating\Monday_Group\[videos_here]`
  
## Testing:

To run the application, open **Command Prompt** where the *application folder* located, type: `python app.py`

The program is given to the two group to test. 
+ **Monday_Group**: Select **Monday Group** when entering **Student ID**.
+ **Thursday_Group**: Select **Thursday Group** when entering **Student ID**.

After each video, observer will be asked to rate the quality of the watched video. 
At the end, observer will be redirected to the [**Questionnaire page**](https://psychocracow.fra1.qualtrics.com/jfe/form/SV_5o4u1gnnML5umQC) to finish the test.

**NOTE:** After the test, please rename the *result.csv* in the *Video_Quality_Rating* folder to *result_[student ID].csv* and attach to the report in **Moodle**.

## Calculate Video Quality Indicators 

+ Go to [AGH Video Quality of Experiance](https://qoe.agh.edu.pl/indicators/) 
+ Download the executable file suited to your operating systems. 
+ Follow the instructions on the page and calculate Video Quality Indicators (VQI)  
