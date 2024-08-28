/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    first = 0; second = 1;

    while(true){
        yield first;

        tmp = second + first;
        first = second;
        second = tmp;
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */