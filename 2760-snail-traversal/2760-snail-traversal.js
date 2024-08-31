/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    n = this.length;
    if (rowsCount * colsCount != n){
        return []
    }

    flag = false;
    let newArr = Array.from({ length: rowsCount }).map(() =>
                Array.from({ length: colsCount }).fill(null)
            );
    let pointer = 0;

    for (j = 0; j < colsCount; j++){
        for (i = 0; i < rowsCount; i++){
            let newI = i;
            if (flag){
                newI = rowsCount - i -1;
            }
            newArr[newI][j] = this[pointer++];
        }
        
        flag = !flag;
    }

    return newArr;
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */