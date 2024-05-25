function sortSentence(s: string): string {
    const arr = s.split(' ');
    let res: string[] = Array(arr.length + 1).fill('');
    
    for (const word of arr) {
        const lastChar = word[word.length - 1];
        res[parseInt(lastChar)] = word.slice(0, word.length - 1);
    }
    
    return res.slice(1).join(' ');
};