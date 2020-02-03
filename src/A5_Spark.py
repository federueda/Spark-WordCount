from pyspark import SparkConf, SparkContext
import pyspark
import random

if __name__ == "__main__":
    # create context with necessary configuration
    conf = SparkConf().setAppName("PySpark Word Count").setMaster("local[2]")
    sc = SparkContext(conf=conf)

    # read text from file and split each line into words, and count by words
    lines = sc.textFile("t8shakespeare.txt")
    words = lines.flatMap(lambda line: line.split(" "))
    wordCounts = words.countByValue()

    # get the dictionary sorted from high to low counts and select position 25th (the first one is blank space)
    print(sorted(wordCounts.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)[24])

    sc.stop()
