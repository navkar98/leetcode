/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    new_arr = [];
    n = arr.length;

    for (i = 0; i < n; i++){
        item = arr[i]
        if (fn(item, i)){
            new_arr.push(item);
        }
    }
    
    return new_arr;
};