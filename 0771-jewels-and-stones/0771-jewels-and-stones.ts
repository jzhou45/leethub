function numJewelsInStones(jewels: string, stones: string): number {
    let count = new Map<string, number>();
    
    for (let jewel of jewels){
        count[jewel] = 0
    }
    
    for (let stone of stones){
        if (stone in count){
            count[stone] ++;
        }
    }
    
    // let arr:number[] = Object.values(count);
    // return arr.reduce((currSum:number, num:number) => currSum + num, 0);
    return Object.values(count).reduce((currSum:number, num:number) => currSum + num, 0);
};