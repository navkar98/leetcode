/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    
    return new Promise((resolve, reject) => {
        if(functions.length === 0) {
            resolve([]);
            return;
        }
        
        resArr = new Array(functions.length).fill(null);
        let counter = 0

        functions.forEach(async (item, idx) => {
            try{
                resArr[idx] = await item();
                counter++;

                if (counter === functions.length) {resolve(resArr)}
            }catch(err){
                reject(err)
            }
        });
    });

    
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */