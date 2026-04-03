class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> hm;
        for (int num : nums) {
            if (hm.count(num)){
                return true;
            }
            hm.insert(num);
        }
        return false;
    }
};