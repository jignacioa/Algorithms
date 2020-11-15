var findDuplicates = function(nums) {
    let counts = {};
    for(var i =  0; i < nums.length; i++) {
        let key = nums[i];
        if (counts[key] === undefined) {
            counts[key] = 1;
        }
        else (counts[key]++)
    }
    let output = [];
    for(number in counts) {
        if(counts[number] > 1) {
           output.push(number);
        }
    }
    return output;
};

var nums = [4,3,2,7,8,2,3,1]
findDuplicates(nums);