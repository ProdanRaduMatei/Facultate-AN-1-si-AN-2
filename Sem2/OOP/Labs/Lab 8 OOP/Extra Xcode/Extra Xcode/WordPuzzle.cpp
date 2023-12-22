#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <algorithm>
#include <chrono>
#include <ctime>
#include <cstdlib>
#include <string>
#include <random>
#include <limits>
#include <unordered_set>
#include <utility>
#include <set>
#include <string>
#include <sstream>

using namespace std;
using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::ifstream;
using std::vector;
using std::unordered_map;
using std::queue;
using std::unordered_set;
using std::pair;
using std::set;



// Define the dictionary file path
const std::string DICT_PATH = "words_alpha.txt";
const std::string GAME_PATH = "username.csv";

// Define the colors for console output
#ifdef _WIN32
const std::string RESET = "\033[0m";
const std::string RED = "\033[31m";
#else
const std::string RESET = "\033[0m";
const std::string RED = "\033[1m\033[31m";
#endif

template<typename T>
class Graph {
private:
    std::unordered_map<T, std::vector<T>> adjList;
    //stores the adjacency list for each node
public:
    void addEdge(T src, T dest) {
        adjList[src].push_back(dest);
        adjList[dest].push_back(src); //for undirected graphs
    }
    std::vector<T> getNeighbours(T node) {
        return adjList[node];
    }
};

std::unordered_map<std::string, std::vector<std::string>> buildMap(std::vector<std::string>& words, char wildcard) {
    std::unordered_map<std::string, std::vector<std::string>> patterns;
    for (auto word : words) {
        for (int i = 0; i < word.size(); i++) {
            std::string pattern = word;
            pattern[i] = wildcard;
            patterns[pattern].push_back(word);
        }
    }
    return patterns;
}

void buildGraph(Graph<std::string>& g, std::vector<std::string>& words, char wildcard) {
    std::unordered_map<std::string, std::vector<std::string>> patterns = buildMap(words, wildcard);
    for (auto pattern : patterns) {
        std::vector<std::string> words = pattern.second;
        for (int i = 0; i < words.size(); i++)
            for (int j = i + 1; j < words.size(); j++)
                if (words[i] < words[j])
                    g.addEdge(words[i], words[j]);
    }
}

std::vector<std::string> bfs(Graph<std::string>& g, std::string start, std::string end) {
    std::unordered_map<std::string, bool> visited;
    std::unordered_map<std::string, std::string> parent;
    std::queue<std::string> q;
    q.push(start);
    visited[start] = true;
    while (!q.empty()) {
        std::string node = q.front();
        q.pop();
        for (auto neighbour : g.getNeighbours(node)) {
            if (!visited[neighbour]) {
                visited[neighbour] = true;
                parent[neighbour] = node;
                q.push(neighbour);
                if (neighbour == end) {
                    std::vector<std::string> path;
                    path.push_back(end);
                    std::string curr = end;
                    while (curr != start) {
                        path.push_back(parent[curr]);
                        curr = parent[curr];
                    }
                    path.push_back(start);
                    std::reverse(path.begin(), path.end());
                    return path;
                }
            }
        }
    }
    return {}; // empty vector if no path found
}

void startmenu();

void play() {
    int firsttime = 0;
    // Promt user for name
    string name;
    cout << "Please enter your name: ";
    cin >> name;
    // Prompt user for number of letters
    int numLetters;
    cout << "Please enter the number of letters: ";
    cin >> numLetters;

    // Select start word and target word
    string startWord, targetWord, line;
    vector<string> wordList;

    ifstream dictFile(DICT_PATH);
    if (dictFile.is_open()) {
        while (getline(dictFile, line)) {
            if (line.length() == numLetters) {
                wordList.push_back(line);
            }
        }
        dictFile.close();
    }
    else {
        cout << "Unable to open file" << endl;
        return;
    }

    if (wordList.empty()) {
        cout << "No words of length " << numLetters << " found in dictionary." << endl;
        return;
    }

    srand(time(NULL));
    startWord = wordList[rand() % wordList.size()];
    targetWord = wordList[rand() % wordList.size()];

    // Play game
    cout << "Start word: " << startWord << endl;
    cout << "Target word: " << targetWord << endl;

    int numMoves = 0;
    vector<string> usedWords;
    vector<int> hintIndices;

    string word = startWord;
    while (word != targetWord) {
        // Check if word is in dictionary
        bool inDict = find(wordList.begin(), wordList.end(), word) != wordList.end();

        if (!inDict) {
            cout << "Word not in dictionary. Please try again." << endl;
            cout << "Please enter a word: ";
            cin >> word;
            continue;
        }

        // Check if word is valid
        bool valid = true;
        if (word.length() != numLetters) {
            valid = false;
        }
        else {
            if (firsttime != 0) {
                int numDiff = 0;
                int diffIndex = -1;
                for (int i = 0; i < numLetters; i++) {
                    if (word[i] != startWord[i]) {
                        numDiff++;
                        diffIndex = i;
                    }
                }
                if (numDiff != 1) {
                    valid = false;
                }
                else {
                    hintIndices.push_back(diffIndex);
                }
            }
            else {
                firsttime++;
            }
        }
        if (!valid) {
            cout << "Invalid word. Please try again." << endl;
            cout << "Starting word: " << startWord << endl;
            cout << "Target word: " << targetWord << endl;
            cin >> word;
            cout << "Please enter a word: ";
            continue;
        }

        usedWords.push_back(word);
        numMoves++;
        startWord = word;

        // Display hint if requested
        char hint;
        cout << "Do you want a hint? (y/n): ";
        cin >> hint;
        if (hint == 'y' || hint == 'Y') {
            if (!hintIndices.empty()) {
                int hintIndex = hintIndices.back();
                hintIndices.pop_back();
                string hintWord = word;
                hintWord[hintIndex] = toupper(hintWord[hintIndex]);
                cout << "Change " << hintWord[hintIndex] << " to reach the target word." << endl;
            }
            else {
                cout << "No more hints available." << endl;
            }
        }

        // Get new word
        cout << "Starting word: " << startWord << endl;
        cout << "Target word: " << targetWord << endl;
        cout << "Please enter a word: ";
        cin >> word;
    }

    // Compute game data
    int numHintsUsed = usedWords.size() - 1;
    int optimalMoves = abs(targetWord[0] - startWord[0]);
    for (int i = 1; i < numLetters; i++) {
        optimalMoves += abs(targetWord[i] - startWord[i]);
    }

    // Display game data
    cout << "Congratulations! You reached the target word in " << numMoves << " moves." << endl;
    cout << "You used " << numHintsUsed << " hints." << endl;
    cout << "The optimal number of moves is " << optimalMoves << "." << endl;

    // Save game data
    ofstream gameFile(GAME_PATH, ios::app);
    if (gameFile.is_open()) {
        gameFile << name << "," << numLetters << "," << numMoves << "," << numHintsUsed << "," << optimalMoves << endl;
        gameFile.close();
    }
    else {
        cout << "Unable to open file" << endl;
    }

    // Display leaderboard
    cout << "Leaderboard:" << endl;
    ifstream gameFile2(GAME_PATH);
    if (gameFile2.is_open()) {
        string line;
        while (getline(gameFile2, line)) {
            stringstream ss(line);
            string name, numLetters, numMoves, numHintsUsed, optimalMoves;
            getline(ss, name, ',');
            getline(ss, numLetters, ',');
            getline(ss, numMoves, ',');
            getline(ss, numHintsUsed, ',');
            getline(ss, optimalMoves, ',');
            cout << name << ": " << numMoves << " moves, " << numHintsUsed << " hints, " << optimalMoves << " optimal moves" << endl;
        }
        gameFile2.close();
    }
    else {
        cout << "Unable to open file" << endl;
    }

    // Prompt user to play again
    char playAgain;
    cout << "Do you want to play again? (y/n): ";
    cin >> playAgain;
    if (playAgain == 'y' || playAgain == 'Y') {
        startmenu();
    }
}

void automatic() {
    // Prompt user for name
    string name;
    cout << "Please enter your name: ";
    cin >> name;

    // Prompt user for number of letters
    int numLetters;
    cout << "Please enter the number of letters: ";
    cin >> numLetters;

    // Select start word and target word
    string startWord;
    string targetWord;
    string line;
    ifstream dictFile(DICT_PATH);
    vector<string> words;
    if (dictFile.is_open()) {
        while (getline(dictFile, line)) {
            if (line.length() == numLetters) {
                words.push_back(line);
            }
        }
        dictFile.close();

        // Prompt user for start word and target word
        cout << "Please enter the start word: ";
        cin >> startWord;
        cout << "Please enter the target word: ";
        cin >> targetWord;

        // Check if start word and target word are valid
        if (find(words.begin(), words.end(), startWord) == words.end() ||
            find(words.begin(), words.end(), targetWord) == words.end()) {
            cout << "Invalid start or target word." << endl;
            return;
        }
    }
    else {
        cout << "Unable to open file" << endl;
        return;
    }

    // Play game
    cout << "Transformations needed to get from " << startWord << " to " << targetWord << ":" << endl;

    // Build graph
    Graph<string> g;
    buildGraph(g, words, '*');

    // Find path
    vector<string> path = bfs(g, startWord, targetWord);
    for (int i = 0; i < path.size() - 1; i++) {
        cout << path[i] << " -> ";
    }
    cout << path.back() << endl;
    cout << "Congratulations " << name << "! You have won!" << endl;
    startmenu();
}

void instructions() {
    cout << "Instructions:" << endl;
    cout << "1. Select the number of letters in the word." << endl;
    cout << "2. Enter a word that is one letter different from the previous word." << endl;
    cout << "3. Repeat step 2 until you reach the target word." << endl;
    cout << "4. You win!" << endl;
    startmenu();
}

void startmenu() {
    cout << "Welcome to Word Puzzle!" << endl;
    cout << "Please select an option:" << endl;
    cout << "1. Play" << endl;
    cout << "2. Automatic mode" << endl;
    cout << "3. Instructions" << endl;
    cout << "4. Exit" << endl;
    int choice;
    cin >> choice;
    switch (choice) {
    case 1:
        play();
        break;
    case 2:
        automatic();
        break;
    case 3:
        instructions();
        break;
    case 4:
        exit(0);
        break;
    default:
        cout << "Invalid input. Please try again." << endl;
        startmenu();
    }
}

int main() {
    startmenu();
    system("pause");
    return 0;
}
