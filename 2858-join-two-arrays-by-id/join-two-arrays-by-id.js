/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    let map = new Map();

    arr1.forEach(obj => {
        map.set(obj.id, { ...obj });
    });

    arr2.forEach(obj => {
        if (map.has(obj.id)) {
            let existingObj = map.get(obj.id);
            Object.assign(existingObj, obj);
        } else {
            map.set(obj.id, { ...obj });
        }
    });

    let mergedArray = Array.from(map.values());
    mergedArray.sort((a, b) => a.id - b.id);

    return mergedArray;
};