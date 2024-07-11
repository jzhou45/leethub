/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, color) {
    const isInScope = (r, c) => r >= 0 && r < image.length && c >= 0 && c < image[0].length
    const originalColor = image[sr][sc]
    const isOriginalColor = (r, c) => originalColor === image?.[r]?.[c]
    
    const search = (r, c) => {
        if (!(isInScope(r, c) && isOriginalColor(r, c))) return
        image[r][c] = color
        search(r - 1, c)
        search(r + 1, c)
        search(r, c - 1)
        search(r, c + 1)
    }
    
    if (!(originalColor === color)) search(sr, sc)
    return image
};