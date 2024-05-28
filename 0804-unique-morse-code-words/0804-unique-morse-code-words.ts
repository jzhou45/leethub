function uniqueMorseRepresentations(words: string[]): number {
    const alphaToMorse = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--.."
    }
    
    let res = 0;
    const seen = new Set<string>();
    
    for (const word of words) {
        let newWord = ''
        for (const char of word) {
            newWord += alphaToMorse[char];
        }
        if (!seen.has(newWord)) {
            seen.add(newWord);
            res++;
        }
    }
    
    return res;
};