class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<>();
        
        int[] resVal = new int[2];
        
        for (int i = 0; i < nums.length; i++) {
            if (seen.containsKey(nums[i])) {
                resVal[0] = seen.get(nums[i]);
                resVal[1] = i;
                break;
            }
            seen.put(target-nums[i], i);
        }
        return resVal;
    }
}