#include <iostream>

using namespace std;

int main(){
    int k = 10;
    int c[k];
    for(int i = 0; i < k; i++){
        cin >> c[i];
    }
    for(int i = k-1; i >= 0; i--){
        while(c[i] > 0){
            cout << i << " ";
            c[i]--;
        }
    }
    return 0;
}
