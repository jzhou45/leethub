function twoSum(nums: number[], target: number): number[] {
    let hash = new Map<number, number>();
    
    for (let i = 0; i < nums.length; i++){
        const diff = target - nums[i];
        if (diff in hash){
            return [hash[diff], i];
        }
        hash[nums[i]] = i;
    }
};