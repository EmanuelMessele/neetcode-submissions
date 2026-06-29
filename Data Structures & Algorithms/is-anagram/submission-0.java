class Solution {
    public boolean isAnagram(String s, String t) {

            if(s.length() != t.length()){  // we check first if they are the same size 
                return false; 
            }
            
            // from here we create a array that carry all the counts of each possible character, 26 letters in the alphabet
            int[] char_counts = new int[26];
            
            // the point is everytime we a value in the first string add its occurrence, if we see that same value in the second string, remove the occurence
            for(int i = 0; i < s.length(); i++){
                char_counts[s.charAt(i) - 'a'] ++; // doing - a will get us the index, so a - a = 0 , and b - a = 1
                char_counts[t.charAt(i) - 'a'] --;
            }

            // in the end, we want to see all counts = 0, to continue and return true
            for(int count : char_counts){
                if(count != 0){
                    return false; 
                }
            }



                return true; 
        }



        
}


