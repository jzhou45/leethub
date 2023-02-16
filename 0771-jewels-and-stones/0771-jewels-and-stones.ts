function numJewelsInStones(jewels: string, stones: string): number {
    let count = {};
    
    for (let jewel of jewels){
        count[jewel] = 0
    }
    
    for (let stone of stones){
        if (stone in count){
            count[stone] ++;
        }
    }
    
    let arr:number[] = Object.values(count);
    return arr.reduce((currSum:number, num:number) => currSum + num, 0);
};