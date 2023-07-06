function sumMultiples(limit)
    sum = 0
    for i in 1:limit-1
        if i % 3 == 0 || i % 5 == 0
            sum += i
        end
    end
    return sum
end

sum = sumMultiples(1000)
println("The sum is: ", sum)
