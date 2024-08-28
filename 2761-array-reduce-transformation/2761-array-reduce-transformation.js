/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    len = nums.length;

    if (len <= 0){
        return init;
    }

    ans = init;
    for(i = 0; i<len; i++){
        ans = fn(ans, nums[i])
    }

    return ans
};