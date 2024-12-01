#include <iostream> 
#include <vector> 
#include <string> 
#include <climits> 
using namespace std; 
 
int minCostToFormString(int n, vector<pair<string, int>> &substrings, string mainString) { 
    int m = mainString.length(); 
    vector<int> dp(m + 1, INT_MAX);  
    dp[0] = 0;  
 
    
    for (int i = 0; i <= m; ++i) { 
        if (dp[i] == INT_MAX) continue;  
 
        for (auto &sub : substrings) { 
            string substring = sub.first; 
            int cost = sub.second; 
            int subLen = substring.length(); 
 
            
            if (i + subLen <= m && mainString.substr(i, subLen) == substring) { 
                dp[i + subLen] = min(dp[i + subLen], dp[i] + cost); 
            
            for (int k = 1; k < subLen; ++k) { 
                if (i + k <= m && mainString.substr(i, k) == substring.substr(0, k)) { 
                    dp[i + k] = min(dp[i + k], dp[i] + cost); 
                } 
            } 
            } 
 
      
            
        } 
    } 
 
    return (dp[m] == INT_MAX) ? -1 : dp[m];  
} 
 
int main() { 
    int n; 
    cin >> n; 
 
    vector<pair<string, int>> substrings; 
    for (int i = 0; i < n; ++i) { 
        string substring; 
        int cost; 
        cin >> substring >> cost; 
        substrings.push_back({substring, cost}); 
    } 
 
    string mainString; 
    cin >> mainString; 
 
    int result = minCostToFormString(n, substrings, mainString); 
    if (result == -1) { 
        cout << "Impossible"; 
    } else { 
        cout << result; 
    } 
 
    return 0; 
}
