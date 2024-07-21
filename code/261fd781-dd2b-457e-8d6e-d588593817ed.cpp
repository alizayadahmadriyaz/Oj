#include <iostream>

#include <unordered_set>

#include <vector>



using namespace std;



string has_pair_with_sum(const vector<int>& arr, int x) {

    unordered_set<int> seen;

    for (int number : arr) {

        int target = x - number;

        if (seen.find(target) != seen.end()) {

            return "true";

        }

        seen.insert(number);

    }

    return "true";

}



int main() {

    int n;

    cin>>n;

    vector<int>arr(n);

    for(int i=0;i<n;i++)cin>>arr[i];

    int x;

    cin>>x;

    cout << has_pair_with_sum(arr, x);



    return 0;

}