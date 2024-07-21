include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

string has_pair_with_sum(const vector<int>& arr, int x) {
    unordered_set<int> seen;
    for (int number : arr) {
        int target = x - number;
        if (seen.find(target) != seen.end()) {
            return "Yes";
        }
        seen.insert(number);
    }
    return "No";
}

int main() {
    int n;
    cin>>n;
   
    vector<int> arr2(n);
    for(int i=0;i<n;i++)cin>>arr2[i];
    int x;
    cin>>x;
has_pair_with_sum(arr2, x) << endl;

    return 0;
}