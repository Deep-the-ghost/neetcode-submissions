class Solution {
public:
    // Helper function to check if two strings are anagrams
    bool isAnagram(string s1, string s2) {
        sort(s1.begin(), s1.end());
        sort(s2.begin(), s2.end());
        return s1 == s2;
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        int n = strs.size();
        
        // Keeps track of words we have already put into a group
        vector<bool> visited(n, false); 

        // Loop through every word
        for (int i = 0; i < n; i++) {
            // If this word is already grouped, skip it
            if (visited[i] == true) {
                continue; 
            }

            // Create a new group starting with the current word
            vector<string> currentGroup;
            currentGroup.push_back(strs[i]);
            visited[i] = true; // Mark it as used

            // Look ahead at all remaining words to find its anagrams
            for (int j = i + 1; j < n; j++) {
                if (visited[j] == false && isAnagram(strs[i], strs[j])) {
                    currentGroup.push_back(strs[j]); // Add to group
                    visited[j] = true;               // Mark it as used
                }
            }

            // Add the completed group to our final results
            result.push_back(currentGroup);
        }

        return result;
    }
};