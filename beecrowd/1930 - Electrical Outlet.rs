use std::io;

fn main() {
    // Read a line from standard input
    let mut input = String::new();

    // Prompt for input
    io::stdin().read_line(&mut input).expect("Entry error");

    // Parse the input into a vector of integers
    let tomadas: Vec<i32> = input
        // Read the input line and trim whitespace
        .trim()
        .split_whitespace()
        // Parse each part into an integer
        .filter_map(|x| x.parse().ok())
        // Collect the integers into a vector
        .collect();
    
    // Check if the vector has exactly 4 elements
    if tomadas.len() == 4 {
        // Calculate the total number of outlets
        let t_tomadas = tomadas.iter().sum::<i32>() - 3;
        // Print the result
        println!("{}", t_tomadas);
    } else {
        // Print an error message if the input is invalid
        eprintln!("Invalid input: Expected 4 integers.");
    }
}