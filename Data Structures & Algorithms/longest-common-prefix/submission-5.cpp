class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty()) {
            return "";
        }
        string base = strs[0];
        for (int i =0;i<base.length();i++){
            char ch = base[i];
            for( int j= 1; j<strs.size();j++){
                if(i==strs[j].length() || strs[j][i] != ch){
                    return base.substr(0,i);
                }
            }
        }
        return base;
        
    }
};