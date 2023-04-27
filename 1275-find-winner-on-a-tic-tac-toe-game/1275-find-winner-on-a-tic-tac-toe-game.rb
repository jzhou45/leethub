# @param {Integer[][]} moves
# @return {String}
def tictactoe(moves)
    grid = Array.new(3) { Array.new (3)}
    $player_A = "x"
    $player_B = "o"
    $current_player = $player_A
    moves.each do |idx1, idx2|
        grid[idx1][idx2] = $current_player
        switch_player
    end
    p grid
    if winner(grid, $player_A)
        return "A"
    elsif winner(grid, $player_B)
        return "B"
    elsif moves_left(grid)
        return "Pending"
    else
        return "Draw"
    end
end
    
def switch_player
    if $current_player == $player_A
        $current_player = $player_B
    else
        $current_player = $player_A
    end
end

def check_horizontal(grid, player)
    grid.each do |subarr|
        if subarr.all?(player)
            return true
        end
    end
    return false
end

def check_vertical(grid, player)
    grid = grid.transpose
    grid.each do |subarr|
        if subarr.all?(player)
            return true
        end
    end
    return false
end

def check_diagonal(grid, player)
    arr1 = []
    arr2 = []
    (0...grid.length).each do |idx|
        arr1 << grid[idx][idx]
        arr2 << grid[idx][grid.length - 1 - idx]
    end
    if arr1.all?(player) || arr2.all?(player)
        return true
    else
        return false
    end
end

def winner(grid, player)
    if check_vertical(grid, player) || check_horizontal(grid, player) || check_diagonal(grid, player)
        return true
    else
        return false
    end
end

def moves_left(grid)
    grid.each do |subarr|
        subarr.each do |ele|
            if ele == nil
                return true
            end
        end
    end
    return false
end