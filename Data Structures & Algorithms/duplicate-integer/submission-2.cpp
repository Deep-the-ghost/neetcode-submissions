auto init = []() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    return 0;
}();
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n = nums.size();
        unordered_set<int> seen;

        for(int i = 0 ; i < n; i++){
        
           if( seen.count(nums[i])) {
            return true;
           }

           else{
            seen.insert(nums[i]);
           }
        }
        return false;
    }
};