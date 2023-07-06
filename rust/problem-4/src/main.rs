fn main() {
    let largest_palindrome = largest_palindrome_product(3);
    println!(
        "The largest palindrome made from the product of two 3-digit numbers is {}",
        largest_palindrome
    );
}

fn largest_palindrome_product(digits: u32) -> u32 {
    let a = 10_u32.pow(digits);
    let b = 10_u32.pow(digits);
    let mut palindromes = Vec::new();

    for i in (1..a).rev() {
        for j in (1..b).rev() {
            if is_palindrome(i * j) {
                palindromes.push(i * j);
            }
        }
    }
    *palindromes.iter().max().unwrap()
}

fn is_palindrome(n: u32) -> bool {
    let s = n.to_string();
    let rev_s = s.chars().rev().collect::<String>();
    s == rev_s
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn is_palindrome_works() {
        assert_eq!(is_palindrome(9009), true);
        assert_eq!(is_palindrome(9019), false);
    }

    #[test]
    fn it_works() {
        assert_eq!(largest_palindrome_product(2), 9009);
        assert_eq!(largest_palindrome_product(3), 906609);
    }
}
