class Solution {
    public int[] twoSum(int[] nums, int target) {

        // we will return an array of the 2 indexes that add up to the target
        int[] indexs = new int[2];

        // iterate thru the array 
        for(int i = 0; i < nums.length; i++){
            for(int j = 0; j < nums.length; j++){
                // if nums i and nums j = target and i and j are not the same
               if(nums[i] + nums[j] == target && i != j) {
                if(i < j){
                    indexs[0] = i;
                    indexs[1] = j; 
                } else {
                    indexs[1] = i;
                    indexs[0] = j; 
                }
            }
        }
     }

            

        return indexs; 
    }
}
