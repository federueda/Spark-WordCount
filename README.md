# Apache Spark - WordCount

A5 SPARK EXERCISE

Load the complete Shakespeare writings, strip the header and search for the #24 most used word in his writings. 

Additionally, do the following:

- 1. What installation did you worked with? Where there any obstacles?
- 2. What is the resulting word?

Reference to Shakespeare’s work: https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt

## 1. Installation Apache Spark

I used Homebrew to install all the tools. The main obstacle was configuring the correct enviromental variables and paths.

### 1st Step: Install Java using Brew

$ brew cask install java

### 2nd Step: Install Scala using Brew

$ brew install scala

### 3rd Step: Install Apache Spark using Brew

brew install apache-spark

### 4th Step: Install PySpark

$ pip3 install pyspark

### 5th Step: Define environmental variables/paths in .bash_profile for Java, Spark and PySpark

$ sudo nano .bash_profile

## 2. Resulting Words

In this example we will find the 24th most used word in the text file. In this case we erase all the headers directly from the text file. You can check the [A5_Spark.py file](https://github.com/federueda/Spark_WordCount/blob/master/src/A5_Spark.py) from the src folder.

### 6th Step: use pyspark to code word count functionality using Spark

I used a Jupyter Notebook to run the code. The first thing is to create a context with necessary configuration, then read text from file and split each line into words, and count by words. Finally, get the dictionary sorted from high to low counts and select position 25th (the first one is blank space). Also, I need to upload the text file in the correct path to be read and at the end of the code stop the used Spark Context.

<p align="center">
<img src="https://github.com/federueda/Spark_WordCount/blob/master/docs/JupyterSpark.png" width="700" height="300" title="Spark">
</p>

The resulting word is "AS" used 4267 times in the text file.
