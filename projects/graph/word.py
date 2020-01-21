"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
1. Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return None if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""

"""
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

"""
3 Steps to Solve Any Graph Problem:

1. Translate the problem into Graphs teminology
2. Build your graph
3. Traverse or search your graph
"""

# 1. words are nodes, if only one letter difference is our edge
# 2. build graph
# 3. do a bfs from start word to end word

from util import Stack, Queue  # These may come in handy
import string

f = open('words.txt', 'r')
words = f.read().split('\n')
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

# build graph

def get_neighbors(word):
    """
    return all words from word_list that are 1 letter different
    """
    neighbors = []
    alphabet = list(string.ascii_lowercase)
    # for each letter in the word,
    for i in range(len(word)):
        # for each letter in the alphabed
        for letter in alphabet:
            # change the word letter to the alphabet letter
            list_word = list(word)
            list_word[i] = letter
            w = "".join(list_word)
            # if the new word is in the word_set:
            if w != word and w in word_set:
                # add it to neighbors
                neighbors.append(w)
    return neighbors
    # change one letter to another letter in the alphabet incrementally
    # search the graph for that
    # then repeat for each letter in the world

# bfs from start to end
def find_ladders(begin_word, end_word):
    # create a queue
    q = Queue()
    # enqueue a path to starting word
    q.enqueue([begin_word])
    # create a visited set
    visited = set()
    # wile the queue is not empty:
    while q.size() > 0:
        # dequeue the next path
        path = q.dequeue()
        # grab the last word from the path
        v = path[-1]
        # if it's not been visited
        if v not in visited:
            # check if the word is our end word, if so return path
            if v == end_word:
                return path
            # mark it as visited
            visited.add(v)
            # enqueue a path to each neighbor
            for neighbor in get_neighbors(v):
                # copy the path, note: reference vs. value, in python, lists have references to original last so will keep adding to same list instead of copying that list and adding to different lists
                path_copy = path.copy()
                # append the neighbor to the back
                path_copy.append(neighbor)
                q.enqueue(path_copy)


print(get_neighbors('cat'))
print(find_ladders('sail', 'boat'))
print(find_ladders('happy', 'hungry'))
