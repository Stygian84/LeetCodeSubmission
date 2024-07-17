/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let a = 0, b = 1;
    yield a;
    yield b;
    while (true) {
        let next = a + b;
        yield next;
        a = b;
        b = next;
    }
    
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */