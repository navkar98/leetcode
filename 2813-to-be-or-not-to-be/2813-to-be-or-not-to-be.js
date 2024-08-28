/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    toBe = function(x){
        if (val === x){
            return true
        }else{
            throw "Not Equal"
        };
    }

    notToBe = function(x){
        if (val !== x){
            return true
        }else{
            throw "Equal"
        };
    }

    return {toBe, notToBe}
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */