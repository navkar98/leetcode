/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    len = functions.length
    if (len === 0){
        return function(x){ return x }; 
    }
    
    return function(x) {
        curr_res = x
        for (i = len - 1; i>= 0;i--){
            curr_res = functions[i](curr_res);
        }

        return curr_res
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */