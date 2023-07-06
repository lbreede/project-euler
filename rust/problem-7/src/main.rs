fn main() {
    const INPUT: u32 = 10001;
    let answer = nth_prime(INPUT);
    println!("The {}st prime is {}", INPUT, answer)
}

fn nth_prime(n: u32) -> u32 {
    let mut primes: Vec<u32> = Vec::new();

    for i in 2.. {
        if is_prime(i) {
            primes.push(i);
        }
        if primes.len() as u32 == n {
            return *primes.last().unwrap();
        }
    }
    0
}

fn is_prime(n: u32) -> bool {
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }
    for i in 3..n {
        if n % i == 0 {
            return false;
        }
    }
    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(nth_prime(6), 13);
    }
}
