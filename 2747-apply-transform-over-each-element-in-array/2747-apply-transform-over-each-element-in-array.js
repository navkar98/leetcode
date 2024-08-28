/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    new_arr = [];
    n = arr.length;

    for (i = 0; i < n; i++){
        item = arr[i]
        new_arr.push(fn(item, i));
    }
    
    return new_arr;
};