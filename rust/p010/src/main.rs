// fn is_prime(n: u64) -> bool {
//     if n == 1 {
//         return false;
//     }
//     if n == 2 {
//         return true;
//     }
//     for x in 2..n {
//         if n % x == 0 {
//             return false;
//         }
//     }
//     true
// }

// fn summation_of_primes(n: u64) -> u64 {
//     (2..=n).filter(|x| is_prime(*x)).sum()
// }

// GitHub Copilot Chat implementation using the Sieve of Eratosthenes
fn sieve_of_eratosthenes(n: u64) -> Vec<bool> {
    let mut primes = vec![true; (n + 1) as usize];
    primes[0] = false;
    primes[1] = false;
    for i in 2..=((n as f64).sqrt() as u64) {
        if primes[i as usize] {
            let mut j = i * i;
            while j <= n {
                primes[j as usize] = false;
                j += i;
            }
        }
    }
    primes
}

fn summation_of_primes(n: u64) -> u64 {
    let primes = sieve_of_eratosthenes(n);
    (2..=n).filter(|x| primes[*x as usize]).sum()
}

fn main() {
    println!("{}", summation_of_primes(2000000));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_summation_of_primes() {
        assert_eq!(summation_of_primes(10), 17);
    }
}
