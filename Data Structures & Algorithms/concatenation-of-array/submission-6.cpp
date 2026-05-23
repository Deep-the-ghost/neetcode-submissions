class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans;
        
        // OPTIMIZATION: Tell C++ to allocate the exact memory needed upfront
        ans.reserve(2 * n);

        // Your original loops (which are perfectly fine!)
        for(int i = 0; i < n; i++){
            ans.push_back(nums[i]);
        }
        for(int j = 0; j < n; j++){
            ans.push_back(nums[j]);
        }
        
        return ans;
    }
};