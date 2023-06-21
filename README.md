# Astro-Pi-FermiPi2

This is the repository for additional analysis software written by the FermiPi2 group for the Astro Pi challenge 2022-2023.

For simplicity we decided not to build the scripts, leaving them in .py format for easier understanding. 

Before running the program make sure to download and unzip the _res_ folder. It should be placed in the same directory in which the programs will be executed.
To properly execute and test _percentage.py_ please use the photos taken by the Raspberry HQ Camera during the runtime of our experiment. If needed here's a link to a Google Drive folder with the .zip file containing all the photos (_north_queensland.jpg_ and _south_queensland.jpg_ too): 
https://drive.google.com/drive/folders/1cqgH13ueihHxoCxQc6N0rvUC-FA2rbyI?usp=sharing

**A few technical details**:

- Comparison photos credits:
    - _north_queensland.jpg_ was taken from ESA photo archive (https://www.esa.int/ESA_Multimedia/Search?SearchText=queensland&result_type=images)
    - _south_queensland.jpg_ was taken from NASA photo archive (http://visibleearth.nasa.gov/images/2433/land_shallow_topo_east.tif)
- These programs require some resources to be downloaded with them (res folder). The res folder needs to be placed in the same directory in which the programs will be executed.
- Each of these programs is fine-tuned to analyze a certain type of photo: _percentage.py_ works well with photos taken by the Raspberry HQ Camera, _percentage_comp.py_ is adjusted for photo _north_queensland.jpg_, while _percentage_comp_2.py_ is designed to analyze _south_queensland.jpg_. Such a level of specificity was required due to the much better quality of the photos that we used for comparison. Logically all the programs operate in the same way, they differ only in RGB color ranges used for analysis.
- As briefly explained in the final report, this code was written in second place after receiving our primary analysis data. We concluded that our results not only were insufficient in terms of data extent provided (we only had information about the predominant color in each photo without a percentage value) but also were not accurate enough to provide any value to our experiment. Hence, we decided to simplify the analysis algorithms by not implying the use of AI models.

**Program structure**:
    - the user chooses an image through a system file dialog  
    - each image is resized (x0.3) to optimize analysis time without sacrificing too much precision
    - the resized image is then put through masks derived from the initially set RGB color ranges
    - after printing the results, the program gives the choice to save the results and/or analyze another photo
- Analysis results are saved in the _analysis_data_ folder that the program creates in the res folder.
- When opening the program more than one time it is normal to see the _[Errno 17] File exists_ error in the console since the folder in which the analysis results can be saved already exists. Don't mind the error, it doesn't affect the functionality of the program.


**How to analyze a photo:**
- open and execute the .py file of your choice
- select and open the photo you want to analyze from the file dialog
- wait for a few seconds as the program runs the analysis and opens the original photo
- after you take a look at the results you can save them by clicking the "save" button
- you can also analyze another photo, just click the button "analyze another photo" and choose it from the file dialog, just keep in mind that when you analyze another photo without saving the results they will be lost
