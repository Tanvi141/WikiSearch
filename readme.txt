METHOD OF INDEXING:
Posting list stores term frequency. 
I did not store tf-idf since 1: I might have had to compromise on floating point precision and 2: I can easily change my formula for calculating tfidf without rewriting the whole index.
I combine all the indices into one file, and then split it into sub chunks of a particular size. log.txt stored first line of every file.
Similarly title files are also split into multiple files.
the directory created has two sub dirs. One for all the index files and one for all the title files.

METHOD OF SEARCHING:
First I store the log files of index split and titles split in a list. This helps me to access them easily.
I search which file a word is in by using binary search.
In order to rank them I calculate tfidf score.
tf idf needs to know total number of documents in the inverted index. For that there is a single line file in the index called count.txt

FILES IN MY CODE:
All the files related to searching are in searcher/
All the files related to indexing are in indexer/
─ indexer
│   ├── indexer.py
│   ├── main.py
│   ├── merge.py
│   ├── parse.py
│   ├── preprocess.py
│   ├── process.py

├── searcher
│   ├── binsrch.py
│   ├── main.py
│   ├── match.py


the code in each file is described by the filename.

