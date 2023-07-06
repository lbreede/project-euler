var sum = 0

for index in 1..<1000 {
    if index % 3 == 0 || index % 5 == 0 {
        sum += index
    }
}

print("The sum is: \(sum)")
