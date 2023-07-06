fn main() {
    const INPUT: u32 = 100;
    let answer = sum_square_difference(INPUT);
    println!("The sum square difference of {} is {}", INPUT, answer);
}

fn sum_square_difference(num: u32) -> u32 {
    square_of_sums(num) - sum_of_squares(num)
}

fn sum_of_squares(num: u32) -> u32 {
    (1..=num).map(|x| x * x).sum()
}

fn square_of_sums(num: u32) -> u32 {
    (1..=num).sum::<u32>().pow(2)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(sum_square_difference(10), 2640);
        assert_eq!(sum_square_difference(100), 25164150);
    }
}
