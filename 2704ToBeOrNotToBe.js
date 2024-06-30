/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return obj= {
        toBe:(num)=>{
            if (val === num){
                return true
            }
            else{
                throw new Error ("Not Equal")
            }
        },
        notToBe:(num)=>{
            if (val !== num){
                return true
            }
            else if (val === num){
                throw new Error ('Equal')
            }
        }

    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */