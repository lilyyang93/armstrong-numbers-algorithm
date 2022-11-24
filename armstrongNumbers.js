// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function(array) {
    let armstrongs = []
    for (let num of array) {
        if (calculateArmstrong(num) == num) {
            armstrongs.push(num)
        }
    }
    return armstrongs 
};

function calculateArmstrong(num) {
    product = 0
    digits = num.toString().split('').map(Number)
    
    for (let d of digits) {
        product += d ** digits.length
    }
    return product
}