// done in first trail both private and public
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


Form The String
Problem Description
Sara, a school-aged child with a keen interest in playing with strings, decided to challenge herself on a boring day. She collected N substrings and a main string with the goal of constructing the main string using these substrings. Each substring incurs a specific cost every time it is used. Sara decided to use only those substrings that are part of the given main string. In cases where characters repeat upon concatenation of the substrings, she can remove the unnecessary characters, though the cost remains the same.

For example, main string = "adkmu"

sub strings -

adkm 1

ad 3

dk 4

kmu 2

Optimised solution will be using the strings {adkm, kmu}, which will become adkmkmu. Sara will remove the characters km, and the total cost incurred will be 1 + 2 = 3.

Please help her achieve this with the minimum cost.

Constraints
1 <= length of main string <= 50

1 <= number of sub strings <= 100

1 <= cost of each sub string <= 100

length of each sub string <= length of main string

The main string, substrings will be having only lower-case alphabets.

Input
First line consists of an integer N, denoting the number of sub strings.

Next N lines consist of the substrings.

Last line consists of main string.

Output
Print an integer denoting the minimum cost within which we can form the main string. Print "Impossible" if it is impossible to form main string with the given set of sub strings.

Time Limit (secs)
1

Examples
Example 1

Input

10

evi 8

vta 9

co 1

dev 5

vit 6

odv 2

d 3

de 4

itaa 1

a 7

codevita

Output

18

Explanation

For forming the given main string, concatenate the sub strings {co, de, vit, a} which will incur a cost of 1 + 4 + 6 + 7 = 18, which is the minimum possible.

Example 2

Input

8

lo 2

wor 3

hel 3

orld 4

lowor 3

ello 4

orl 3

orld 2

helloworld

Output

8

Explanation

For forming the given main string, concatenate the sub strings {hel, lowor, orld} which will form the string hellowororld. From this string, we can remove the extra letters "or" to form the string helloworld. The cost incurred will be 3 + 3 + 2 = 8, which is the minimum possible.

Example 3

Input

4

hyd 10

eraa 20

bad 30

pqrs 40

hyderabad

Output

Impossible

Explanation

As the substring eraa is not present in the main string, hence we can't use it. Thus, we cannot form the main string hyderabad with the given substrings. Hence, print "Impossible".