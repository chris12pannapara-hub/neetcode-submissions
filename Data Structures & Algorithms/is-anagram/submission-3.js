class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length){
            return false
        }

        // let topS = s.split('').sort().join();
        // let topT = t.split('').sort().join();

        // return topS == topT;


        const cartS = {};
        const cartT = {};

        for(let i=0; i<s.length; i++){
            cartS[s[i]] = 1 + (cartS[s[i]] || 0);
            cartT[t[i]] = 1 + (cartT[t[i]] || 0);
        }
        for (const n in cartS ){
            if(cartS[n] !== cartT[n]){
                return false;
            }
        }
        return true;
    }
}
