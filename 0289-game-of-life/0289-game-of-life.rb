# @param {Integer[][]} board
# @return {Void} Do not return anything, modify board in-place instead.
def game_of_life(board)
    arr = []
    board.each do |subarr|
        temp = []
        subarr.each { |ele| temp << ele }
        arr << temp
    end
    (0...board.length).each do |row|
        (0...board[0].length).each do |col|
            count = horizontal(arr, row, col) + vertical(arr, row, col) + diagional(arr, row, col)
            cell = arr[row][col]
            if count == 2 && cell == 1
                board[row][col] = 1
            elsif count == 3
                board[row][col] = 1
            else
                board[row][col] = 0
            end
        end
    end
    board
end

def horizontal(matrix, row, col)
    count = 0
    count += 1 if matrix[row][col - 1] == 1 && col-1 >= 0
    count += 1 if matrix[row][col + 1] == 1 && col +1 < matrix[0].length
    count
end

def vertical(matrix, row, col)
    count = 0
    if row - 1 >= 0
        count += 1 if matrix[row - 1][col] == 1
    end
    if row + 1 < matrix.length
        count += 1 if matrix[row + 1][col] == 1
    end
    count
end

def diagional(matrix, row, col)
    count = 0
    if row - 1 >= 0 && col - 1 >= 0
        count += 1 if matrix[row - 1][col - 1] == 1 
    end
    if row - 1 >= 0 && col + 1 < matrix[0].length
        count += 1 if matrix[row - 1][col + 1] == 1
    end
    if row + 1 < matrix.length && col + 1 < matrix[0].length
        count += 1 if matrix[row + 1][col + 1] == 1
    end
    if row + 1 < matrix.length && col - 1 >= 0
        count += 1 if matrix[row + 1][col - 1] == 1
    end
    count
end