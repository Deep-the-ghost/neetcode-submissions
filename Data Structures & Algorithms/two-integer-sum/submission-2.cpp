auto init = [](){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    return 0;
}();
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> seen_numbers;
        for(int i = 0 ; i < nums.size() ; i++){
            int complement = target - nums[i];
            if(seen_numbers.find(complement) != seen_numbers.end()){
                return {seen_numbers[complement],i};
            }
            seen_numbers[nums[i]]=i;
        }
        return{};
    }
};
