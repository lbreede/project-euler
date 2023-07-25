fn main() {
    let target_sum = 1000;

    for a in 1..(target_sum / 3) {
        for b in (a + 1)..((target_sum - a) / 2) {
            let c = target_sum - a - b;
            if c > b && a * a + b * b == c * c {
                println!(
                    "{} + {} + {} = {}\nSolution: {}",
                    a,
                    b,
                    c,
                    target_sum,
                    a * b * c
                );
            }
        }
    }
}
