/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    const initial_value=init
    var modified_value=init

    function increment(){
        modified_value+=1
        return modified_value
    }
    function decrement(){
        modified_value-=1
        return modified_value
    }
    function reset(){
        modified_value=initial_value
        return initial_value
    }
    return {
        increment: increment,
        decrement: decrement,
        reset: reset
    };
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */