class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        unordered_map<char, int> s_hm;
        unordered_map<char, int> t_hm;
        for(int i = 0; i < s.length(); i++) {
            s_hm[s[i]]++;
            t_hm[t[i]]++;
        }
        return t_hm == s_hm;
    }
};
