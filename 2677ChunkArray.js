/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let finalarray = [] ;
    while(arr.length > 0){
      finalarray.push(arr.splice(0,size));

    }
    return finalarray;
};
