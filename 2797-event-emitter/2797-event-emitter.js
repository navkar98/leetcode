class EventEmitter {
    constructor() {
        this.events = {}
    }
    
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        
        if (eventName in this.events){
            this.events[eventName].push(callback)
        }else{
            this.events[eventName] = []
            this.events[eventName].push(callback)
        }
        
        return {
            unsubscribe: () => {
                let index = this.events[eventName].indexOf(callback)
                if (index > -1) {
                    this.events[eventName].splice(index, 1);
                }
                return undefined
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        let result = []

        if (!(eventName in this.events)){return result}

        this.events[eventName].forEach((item) => {
            result.push(item(...args))
        })

        return result
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */