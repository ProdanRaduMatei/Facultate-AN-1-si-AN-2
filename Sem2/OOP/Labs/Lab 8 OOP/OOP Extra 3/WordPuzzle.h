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

using namespace std;

class Graph;

std::unordered_map<std::string, std::vector<std::string>> buildMap(std::vector<std::string>& words, char wildcard);

void buildGraph(Graph& g, vector<string>& words, char wildcard);

std::vector<std::string> bfs (Graph& g, string start, string end);

void startmenu();

void play();

void automatic();

void instructions();