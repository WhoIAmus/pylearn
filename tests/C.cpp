#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>
 
using namespace std;
 
long long getSum(int l,int r,vector<long long>& pref){
    if(l > r)
        return 0ll;
    long long l_sum = (l > 0 ? pref[l-1] : 0ll);
    if(r >= pref.size()){
        r -= pref.size();
        r++;
        return pref.back() - l_sum + pref[r];
    } else {
        return pref[r] - l_sum;
    }
}
 
int main(){
    ios::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
    int n,k;
    cin >> n >> k;
    int p[n+1];
    for(int i = 1; i <= n; i++){
        cin >> p[i];
    }
    long long ans[n+1];
    memset(ans,0,sizeof ans);
    int id[n+1];
    for(int i = 1; i <= n; i++){
        id[i] = -1;
    }
    vector<long long> cycle[n+1];
    int pos[n+1];
    for(int i = 1; i <= n; i++){
        if(id[i] == -1){
            int j = i;
            while(id[j] == -1){
                id[j] = i;
                cycle[i].push_back(j);
                j = p[j];
            }
            cycle[i].push_back(0);
            reverse(cycle[i].begin(),cycle[i].end());
            for(int p = 1; p < cycle[i].size(); p++){
                pos[cycle[i][p]] = p;
                cycle[i][p] += cycle[i][p-1];
            }
        }
        // cerr << "cycle: ";
        // for(auto& x : cycle[id[i]])
        //     cerr << x << " ";
        // cerr << "\n";
        long long full_cycles = k / (cycle[id[i]].size() - 1);
 
        long long rem = 0;
        if(k % cycle[id[i]].size() != 0)
            rem = getSum(pos[i],(pos[i]+k%(cycle[id[i]].size()-1))-1,cycle[id[i]]);
        // cerr << "full: " << full_cycles << ", rem: " << rem << "\n";
        // cerr << "l,r: " << pos[i] << " " << (pos[i] + k%(cycle[id[i]].size()-1))-1 << "\n";
        ans[p[i]] = full_cycles * cycle[id[i]].back() + rem;
    }
    
    for(int i = 1; i <= n; i++){
        cout << ans[i] << " ";
    }        
    cout << "\n";
    
    return 0;
}
