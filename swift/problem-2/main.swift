var numA = 1
var numB = 1
var answer = 0// starting with zero because both starting values are odd

while numB < 4000000 {
    answer += numB % 2 == 0 ? numB : 0
    let tempA = numB
    numB = numA + numB
    numA = tempA
}

print("The answer is: \(answer)")
