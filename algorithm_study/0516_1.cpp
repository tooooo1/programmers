#include <iostream>

using namespace std;

int n,a,b;

int solution(int n, int a, int b) {
    int answer=0;

    while(n!=1) {
        if(a==b) {
            return answer;
        } else {
            if(a%2==1) {
                a=a/2;
                a++;
            } else {
                a=a/2;
            } 
            if(b%2==1) {
                b=b/2;
                b++;
            } else {
                b=b/2;
            } 
            answer++;
            n=n/2;
        }
    }
}

int main() {
    cout<<solution(8,4,7);

}