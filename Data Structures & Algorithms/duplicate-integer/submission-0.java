class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> numsmap = new HashMap<Integer,Integer>();
        for (int i= 0; i<nums.length; i++) {
            if (numsmap.containsKey(nums[i])) {
                return true;
            } else {
                numsmap.put(nums[i], 1);
            }
        }
        return false;
        
    }
}