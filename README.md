# Video_Quality_Rating
A simple app to watch and rate given videos based on the quality.

## Requirements:

+ ffmpeg needs to be installed (Download here: https://www.ffmpeg.org/download.html).
  + Extract the folder.
  + Rename the folder to: FFmpeg
  + Copy/Cut folder to **C Drive** (C:\)
  + Open **Environment variables control panel**:
    + Open search bar
    + Type: *system variables*, open: **Edit the system environment variables**
    + Click **Environment variables**
    + In **System variables**, select *Path*, select *Edit*
    + Add the path of FFmpeg folder above to the list by click *New*
    + Click *OK* to save changes
    
+ The program requires **Pillow Image Library**
  > python -m pip install Pillow
  
## Testing:

The program is given to the two group to test. 
+ Group 1: Will be shown vary videos with different quality. (Select **Group 1** when entering **ID**)
+ Group 2: Will be the same video but with different quality. (Select **Group 2** when entering **ID**)

After each video, observer will be asked to rate the quality of the watched video. 
The result of the test will be saved to *result.csv* file.
