// Binary Problems : Reverse Bits
//Given a 32-bit unsigned integer, reverse its bits and return the resulting integer
// Example 1: Input: n = 00000010100101000001111010011100 Output:    964176192
// Example 2: Input: n = 11111111111111111111111111111101 Output:    3221225471
// Example 3: Input: n = 43261596 Output:    964176192
// Example 4: Input: n = 4294967293 Output:    3221225471

function reverseBits(n) {
    let result=0;
    for (let i=0;i<32;i++){
        let bit=n&1;
        result = result << 1 |bit;
        n=n >> 1;
    }
    return result >>>0;
}
console.log(reverseBits(0b00000010100101000001111010011100)); //964176192
console.log(reverseBits(0b11111111111111111111111111111101)); //3221225471
console.log(reverseBits(43261596));  //964176192
console.log(reverseBits(4294967293)); //3221225471