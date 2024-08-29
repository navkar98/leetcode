/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    arr = {}
    this.forEach((item) => {
        key = fn(item);
        if (key in arr){
            arr[key].push(item)
        }else{
            arr[key] = [item];
        }
    });
    return arr
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */