fn main() {
    let answer = smallest_multiple(20);
    println!("The smallest multiple is: {answer}");
}

fn smallest_multiple(num: u32) -> u32 {
    for i in 1.. {
        let remainders: u32 = (1..=num).map(|x| i % x).sum();
        if remainders == 0 {
            return i;
        }
    }
    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(smallest_multiple(10), 2520);
    }
}
