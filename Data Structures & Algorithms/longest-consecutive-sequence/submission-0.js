class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let sortNums = new Set(nums);
        let seqLength = 0;

        for(let num of sortNums){
            if(!sortNums.has(num-1)){
                let length = 1;
                while(sortNums.has(num+length)){
                    length++;
                }
                seqLength = Math.max(seqLength , length);
            }
        }
        return seqLength;


    }
}
