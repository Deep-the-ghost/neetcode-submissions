auto init = [](){
ios_base::sync_with_stdio(false);
cin.tie(NULL);
return 0;
}();
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
       if(strs.empty()){
        return "";
       } 
       sort(strs.begin(),strs.end());

       string first = strs[0];
       string last = strs[strs.size()-1];
       string result = "";

       for(int i =0;i<first.length();i++){
        if(first[i] == last[i]){
            result = result + first[i];
        }
        else{
            break;
        }
       }
       return result;
    }
};