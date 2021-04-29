#include <iostream>
#include <string>

using namespace std;


int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    for(int &elem : arr) {
        elem = 10;
    }
    
    for(int &elem : arr) {
        cout << elem << " ";
    }
}