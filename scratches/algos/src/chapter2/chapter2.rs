use rand;
use std::time::SystemTime;

#[derive(Debug)]
pub struct SortingStatistics {
    input_length: usize,
    n_assignments: usize,
    n_comparisons: usize,
    n_indexings: usize,
    n_swaps: usize,
    time_elapsed: u128,
}

impl SortingStatistics {
    fn new(length: usize) -> SortingStatistics {
        return SortingStatistics {
            input_length: length,
            n_comparisons: 0,
            n_swaps: 0,
            n_indexings: 0,
            n_assignments: 0,
            time_elapsed: 0,
        };
    }
}

pub fn random_vector(size: usize) -> Vec<usize> {
    let mut size: usize = rand::random();
    size = size % 100;
    let range = 0..size;
    return range.map(|_| rand::random()).collect();
}

pub fn insertion_sort<T: Ord>(array: &mut Vec<T>) -> SortingStatistics {

    let length = array.len();
    let mut result = SortingStatistics::new(length);
    let time_start = SystemTime::now();

    for position in 1..length {
        let mut i = position;
        result.n_assignments += 2;

        while i > 0 && array[i] < array[i - 1] {
            array.swap(i, i - 1);
            i = i - 1;

            result.n_swaps += 1;
            result.n_assignments += 1;
            result.n_comparisons += 2;
            result.n_indexings += 2;
        }
    }
    result.time_elapsed = time_start.elapsed().unwrap().as_nanos();
    return result;
}

#[test]
fn insertion() {
    for _ in 1..100000 {
        let mut vector = random_vector(100);
        let stats = insertion_sort(&mut vector);
        println!("{:?}", stats);
        for i in 1..vector.len() {
            let current = vector[i];
            let previous = vector[i - 1];
            assert!(current >= previous);
        }
    }
}
