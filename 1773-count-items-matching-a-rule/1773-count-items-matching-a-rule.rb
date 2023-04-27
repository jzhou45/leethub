# @param {String[][]} items
# @param {String} rule_key
# @param {String} rule_value
# @return {Integer}
def count_matches(items, rule_key, rule_value)
    count = 0
    items.each do |value|
        if value[0] == rule_value and rule_key == "type"
            count += 1
        end
        if value[1] == rule_value and rule_key == "color"
            count += 1
        end
        if value[2] == rule_value and rule_key == "name"
            count += 1
        end
    end
    return count
end
        