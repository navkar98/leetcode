/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    curr_size = 0;
    new_arr = [];
    tmp = []

    arr.forEach((item)=> {
        if (curr_size >= size){
            curr_size = 0;
            new_arr.push(tmp);
            tmp = [];
        }
        tmp.push(item);
        curr_size++;
    })
    
    if (tmp.length >= 1){
        new_arr.push(tmp);
    }

    return new_arr;
};
