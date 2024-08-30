var TimeLimitedCache = function() {
    this.cache = {}
    this.timers = {}
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    
    if (key in this.cache){
        clearTimeout(this.timers[key]);

        this.cache[key] = value;
        timer = setTimeout(() => {delete this.cache[key]}, duration);
        this.timers[key] = timer;

        return true
    }else{
        this.cache[key] = value;
        timer = setTimeout(() => {delete this.cache[key]}, duration);
        this.timers[key] = timer;
        
        return false;
    }   
     
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (key in this.cache){
        return this.cache[key];
    }else{
        return -1
    }
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return Object.keys(this.cache).length
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */