class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans;
        ans.reserve(2*n);

        for(int i=0 ; i < nums.size(); i++){
            ans.push_back(nums[i]);
        }
        for(int j=0 ; j < nums.size(); j++){
            ans.push_back(nums[j]);
        }
       return ans;
    }
    
};