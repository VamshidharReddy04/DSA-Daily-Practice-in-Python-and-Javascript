// Array problem given an array of integers, find if the array contains any duplicates.

function containsDuplicate(nums) {
    const seen = new Set();
    for (let num of nums) { 
        if (seen.has(num)) {
            return true; // Duplicate found
        }
        seen.add(num); // Add the value to the set
    }
    return false; // No duplicates found
}

console.log(containsDuplicate([1, 2, 3, 1])); // true
console.log(containsDuplicate([1, 2, 3, 4])); // false

// Time Complexity: O(n) - We traverse the array once
// Space Complexity: O(n) - In the worst case, we may store all elements in the set
