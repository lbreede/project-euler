fn main() {
    const INPUT: u64 = 600851475143;
    let prime_factors = get_prime_factor(INPUT);
    println!(
        "The largest prime factor of {} is {}",
        INPUT,
        prime_factors.last().unwrap()
    );
}

fn get_prime_factor(n: u64) -> Vec<u64> {
    let mut prime_factors = Vec::new();
    let mut num = n;
    while num % 2 == 0 {
        prime_factors.push(2);
        num /= 2;
    }

    let sqrt_n = (num as f64).sqrt() as u64;
    let mut i = 3;
    while i <= sqrt_n {
        if num % i == 0 {
            prime_factors.push(i);
            num /= i;
        } else {
            i += 2; // Skip even numbers
        }
    }

    if num > 2 {
        prime_factors.push(num);
    }

    prime_factors
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(get_prime_factor(13195), vec![5, 7, 13, 29]);
    }
}
