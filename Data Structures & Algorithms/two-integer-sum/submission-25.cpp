class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hm;
        for (int i = 0; i < nums.size(); i++){
            if (hm.count(target - nums[i])){
                return {hm[target - nums[i]], i};
            }
            hm[nums[i]] = i;

        }
    }
};
