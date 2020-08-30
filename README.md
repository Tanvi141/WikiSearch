# WikiSearch
Search engine on English Wikipedia

## Indexer
To run:
`index.sh <path_to_wiki_dump> <path_to_invertedindex_output> <invertedindex_stat.txt>`
invertedindex_stat.txt contains two numbers:
1. Total number of tokens (​ after converting to lowercase​ ) encountered in the dump
2. Total number of tokens in the inverted index

Related code files are in the directory **indexer**

## Searcher
To run:
`search.sh <path to directory containing the index> "<query string>"`

Related code files are in the directory **searcher**