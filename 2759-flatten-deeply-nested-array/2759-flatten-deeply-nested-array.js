/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    if (n > 0){
        let subArr = [];
        arr.forEach((item) => {
            if (Array.isArray(item)){
                subArr.push(...flat(item, n-1));
            }else{
                subArr.push(item);
            }
        });

        return subArr;
    }else{
        return arr;
    }
    
    
};