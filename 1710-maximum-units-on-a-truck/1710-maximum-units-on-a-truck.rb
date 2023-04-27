# @param {Integer[][]} box_types
# @param {Integer} truck_size
# @return {Integer}
def maximum_units(box_types, truck_size)
    box_types = box_types.sort_by { |a, b| b } .reverse
    counter = 0
    truck_size.times do
        num_box, units = box_types[0]
        counter += units
        box_types[0][0] -= 1
        box_types.shift if box_types[0][0].zero?
        break if box_types.empty?
    end
    counter
end