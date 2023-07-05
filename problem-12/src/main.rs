use std::time::Instant;

fn main() {
    const DIVISOR_TARGET: u32 = 500;
    let start = Instant::now();
    for n in 1.. {
        let triangle = get_triangle(n);
        let divisors = get_divisors(triangle);
        if divisors > DIVISOR_TARGET {
            println!(
                "The triangle number of {} is {}, which has {} divisors.",
                n, triangle, divisors
            );
            break;
        }
    }
    let duration = start.elapsed();
    println!(
        "Looping Up to the Square Root of `n` took: {:?}\n",
        duration
    );

    let start = Instant::now();
    for n in 1.. {
        let triangle = get_triangle(n);
        let divisors = counter_divisors_in_pairs(triangle);
        if divisors > DIVISOR_TARGET {
            println!(
                "The triangle number of {} is {}, which has {} divisors.",
                n, triangle, divisors
            );
            break;
        }
    }
    let duration = start.elapsed();
    println!("Counting divisors in pairs took: {:?}", duration);
}

fn get_triangle(n: u32) -> u32 {
    let x: u32 = (1..=n).sum();
    x
}

fn get_divisors(n: u32) -> u32 {
    let mut divisors = 0;
    let sqrt_n = (n as f64).sqrt() as u32;
    for i in 1..=sqrt_n {
        if n % i == 0 {
            divisors += 2; // Accounting for both divisors
        }
    }
    if sqrt_n * sqrt_n == n {
        divisors -= 1; // If n is a perfect square, subtract one divisor
    }
    divisors
}

fn counter_divisors_in_pairs(n: u32) -> u32 {
    let mut divisors = 0;
    let sqrt_n = (n as f64).sqrt() as u32;
    for i in 1..=sqrt_n {
        if n % i == 0 {
            divisors += 2; // Accounting for both divisors
        }
    }
    if sqrt_n * sqrt_n == n {
        divisors -= 1; // If n is a perfect square, subtract one divisor
    }
    divisors
}
