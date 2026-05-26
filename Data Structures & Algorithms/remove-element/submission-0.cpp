class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        // sort the array
        sort(nums.begin(),nums.end());

        // first i have to find where the val starts
        int i=0;
        while(i < nums.size() && nums[i] != val){
            i++;
        }


         //in one case if val is not present then i == num.size() then I have to return i
         if (i == nums.size()){
            return i;
         }


        // if val present then I have to find how much copies of val's are present
        int j = i;
        while(j < nums.size() && nums[j] == val ){
            j++;
        }


        //if from i to the end all numbers are val then we have to return i
        if(j == nums.size()){
            return i;
        }

        // if after the val's there are other numbers
        // j = j+1;
        while(j < nums.size() ){
            nums[i]=nums[j];
            i++;
            j++;
        }

        return i;


    }
};