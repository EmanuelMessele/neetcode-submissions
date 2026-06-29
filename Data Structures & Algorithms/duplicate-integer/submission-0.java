class Solution {
    public boolean hasDuplicate(int[] nums) {
        /** my thought process here is to just iterate through the array with 2 different
        for loops and change the boolean to false if necessary
    */
        boolean hasDup = false; // set our boolean value to false 

        // iterate through the 
        for(int i = 0; i < nums.length; i++){
            int number = nums[i]; 
            for(int j = 0; j < nums.length; j++){
                if(number == nums[j] && i != j){ // checking if i is not equal to j makes sure we arent reading that same number
                    hasDup = true; 
                }
            }
        }

        return hasDup; 
    }
}
