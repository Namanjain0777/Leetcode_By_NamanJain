class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int len = nums.length;
        int sum =0;
        int closestSum = nums[0] + nums[1] + nums[2]; 
        for(int i=0; i<len-2; i++){
            for(int j=i+1; j<len-1; j++){
                for(int k=j+1; k<len;  k++){
                    sum = (nums[i]+nums[j]+nums[k]);
                    //System.out.println(nums[i]+" : "+nums[j]+" : "+nums[k]+" : "+sum);
                     if (Math.abs(sum - target) < Math.abs(closestSum - target)) {
                        closestSum = sum;
                    }
                }
            }
        }
        return closestSum;
    }
}
