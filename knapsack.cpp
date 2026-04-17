#include <iostream>
#include <vector>

using namespace std;

int knapsack_with_repetition(const vector<int>& weights, const vector<int>& values, const int W)
{
    const int N = weights.size();
 
    vector<int> K(W + 1, 0);
    for (int w = 1; w <= W; w++) {
        for (int i = 0; i < N; i++) {
            if (weights[i] <= w) {
                K[w] = max(K[w - weights[i]] + values[i], K[w]);
            }
        }
    }
 
    return K[W];
}
