Name: Charles Shin

Date: 5/24/2021

Course: IT FDN 110 A Sp21: Foundations of Programming: Python

Assignment 07

GitHub URL: https://github.com/shin900215/IntroToProg-Python-Mod07

## Assignment 07: Pickling and Structured Error Handling

### Introduction

In this assignment, pickling and structured error handling are described. The pickling example described in the textbook will be used to describe the pickling, and the structured error handling are shown at the end of this assignment. 

Using the pickling, the variety, the shape, and the brand of the pickles will be separately stored then combined. Once the pickling is done, a data file will be created that contains all the data in it. When the pickling example is done, the script used in this assignment will ask the user if the user would like to see any of the variety, shape, or the brand of the pickle. When the user input is not valid, the prompt will show up and tell the user that the input is not correct. 

### Discussion

Figure 1 shows the header of the script. IT shows the description of the script as well as who made changes to the script. 

![image](https://user-images.githubusercontent.com/83855330/119437596-54b1ec80-bcd3-11eb-9377-77727c2641a9.png)

Figure 1. Header of the script.

Figure 2 shows the pickling process. First, it imports the pickle from the Python. Then, it defines the variety, shape, and the brand of the pickle. Note that ‘wb’ was used to write to a binary file. It opens, creates one if there is no file created already, the file, storing the data, then close the file.
![image](https://user-images.githubusercontent.com/83855330/119437714-8d51c600-bcd3-11eb-8e47-fb0250cc7dad.png)

Figure 2. Pickling and creating the data file.

Figure 3 shows the process of reading data from the file. As shown in the figure, the script opens the data file created, reads the data in the file, and print the contents for the user. The result will print out three lines that will contain the variety, shape, and the brand of the pickle. 

![image](https://user-images.githubusercontent.com/83855330/119437731-9478d400-bcd3-11eb-940e-f01800bdf0e3.png)

Figure 3. Reading the pickled data from the data file.

Figure 4 describes the shelving of the data. As shown in the figure, the shelved data will be stored in the data file called pickles2.dat. The process will be to first import the shelve from the Python, open the data file, and shelve the data. To show that they are properly shelved, four print were used to print out the shelved data in the data file. The last print of 2 blank lines are just to separate this section from the next one.  

![image](https://user-images.githubusercontent.com/83855330/119437772-abb7c180-bcd3-11eb-83d3-60c5ee36f50c.png)

Figure 4. Shelving the data.

Figure 5 shows the description of the structured error handling. As shown, the script asks for the user input among variety, shape, or brand. If the user do not type one of the correct selections, the script notifies the user that the user input is wrong.

![image](https://user-images.githubusercontent.com/83855330/119437790-b2463900-bcd3-11eb-8d28-4cd5cf2580a9.png)

Figure 5. Structured Error Handling

### Conclusion

Figure 6 shows the result of running the script in the Python environment. The first section shows the printed results of the pickled data, and the second portion shows the shelved data. The last portion shows the result of when the correct input was typed in.

![image](https://user-images.githubusercontent.com/83855330/119437814-c0945500-bcd3-11eb-9847-58c7d366fac8.png)

Figure 6. The result showing the pickled and shelved data. It shows at the end the result of having a correct input.

Figure 7 shows a similar result to figure 6, except the end portion. The user input is wrong this time, and the script tells the user that the input is wrong. 

![image](https://user-images.githubusercontent.com/83855330/119437856-d0ac3480-bcd3-11eb-9840-fe385d5b83bb.png)

Figure 7. The result showing the pickled and shelved data. It shows at the end the result of having an incorrect input.

Figure 8 and 9 shows similar results, except they were run in the OS environment. The identical results were obtained when run in the OS environment. 

![image](https://user-images.githubusercontent.com/83855330/119437891-df92e700-bcd3-11eb-80b3-61f9da12ce1b.png)

Figure 8. The result showing the pickled and shelved data run in the OS. It shows at the end the result of having a correct input.

![image](https://user-images.githubusercontent.com/83855330/119437913-e883b880-bcd3-11eb-8a64-2979ce7c23ac.png)

Figure 9. The result showing the pickled and shelved data run in the OS. It shows at the end the result of having an incorrect input.

Figure 10 shows the active folder after running the script. As shown in the figure, the data files define and used in the script were created after running the script.

![image](https://user-images.githubusercontent.com/83855330/119437942-f6d1d480-bcd3-11eb-9082-3f8479d94558.png)

Figure 10. Data files created after running the script.

### Summary
This assignment described the pickling process as well as the structured error handling process. The original script created for this assignment as well as this assignment document will be submitted via Canvas. Also, the contents will be available in the GitHub repository as well as the website that will be created. 
