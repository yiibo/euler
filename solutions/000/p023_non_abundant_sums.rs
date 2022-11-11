
// Euler Project
// Problem 23: https://projecteuler.net/problem=23

// Notes:
//  First stab at Rust, code is slow as I haven't implemented too many heuristics in here
//  Didn't find elegant way of doing without using Vec functions

fn main() {
    // Print text to the console
    println!("12 is an abundant sum as 12 < {}", is_abundant(12));

    println!("10 is a deficient sum as 10 > {}", is_abundant(10));

    println!("{}", find_non_abun_sum(28124));
}

fn find_non_abun_sum(ul: usize) -> usize {
    let abun_nums = find_abun_nums(ul);

    let mut abun_sums = Vec::new();
    let mut sum = 0;

    for i in 0..abun_nums.len() {
        for j in i..abun_nums.len() {
            if abun_nums[i] + abun_nums[j] <= ul {
                abun_sums.push(abun_nums[i] + abun_nums[j]);
            }
        }
    }

    // Easiest way to do this using a rust Vec is to sort then dedup
    abun_sums.sort();
    abun_sums.dedup();

    for i in abun_sums {
        sum += i;
    }

    let total = (ul + 1) * ul / 2;

    println!("{}", total);
    println!("{}", sum);

    return total - sum;
}

fn find_abun_nums(ul: usize) -> Vec<usize> {
    let mut abun_nums = Vec::new();

    for i in 1 as usize..ul {
        if is_abundant(i as u32) {
            abun_nums.push(i);
        }
    }

    return abun_nums;
}


fn is_abundant(num: u32) -> bool {
    return sum_divisors(num) > num;
}

fn sum_divisors(n: u32) -> u32 {
    let mut sum = 1;

    for i in 2..(n as f64).sqrt() as u32 + 1 {
        if n % i == 0 {
            sum += i + n/i;
            if i == n/i {
                sum -= i
            }
        }
    }

    return sum;
}