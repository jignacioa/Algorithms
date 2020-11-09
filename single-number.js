var singleNumber = function(nums) {

    let countsObj = {};
    for(var i = 0; i < nums.length; i++) {
      let number = nums[i];
      if(countsObj[number] === undefined) {
        countsObj[number] = 1;
      }
      else (
        countsObj[number]++
      )
    }
    let output = []
    for(number in countsObj) {
      if (countsObj[number] === 1) {
      output.push(number)
      }
    }
     return output;
  }
  
  var nums = [1,2,1,3,2,5]
  console.log(singleNumber(nums))