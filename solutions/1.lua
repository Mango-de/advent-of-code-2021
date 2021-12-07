Lines = {}

for line in io.lines('inputs\\1') do
    Lines[#Lines + 1] = tonumber(line)
end

function Part1()
    local i = -1
    local last = 0
    for _, n in pairs(Lines) do
        if n > last then
            i = i + 1
        end
        last = n
    end
    print(i)
end

Part1()

function Part2()
    local i = -1
    local last = 0
    for c, _ in pairs(Lines) do
        local size = 0
        for _ in pairs(Lines) do size = size + 1 end
        if c <= size - 2 then
            local sum = Lines[c] + Lines[c + 1] + Lines[c + 2]
            if sum > last then
                i = i + 1
            end
            last = sum
        end
    end
    print(i)
end

Part2()