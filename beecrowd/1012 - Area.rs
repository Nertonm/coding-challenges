use std::io;

fn main() {

    // Read a line from standard input
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let values: Vec<f64> = input
         .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();
    let (a, b, c) = (values[0], values[1], values[2]);

    // Calculate the areas of different shapes
    let pi = 3.14159;
    let area_triangulo = a * c / 2.0;
    let area_circulo = pi * c * c;
    let area_trapezio = (a + b) * c / 2.0;
    let area_quadrado = b * b;
    let area_retangulo = a * b;

    // Print the results
    println!("TRIANGULO: {:.3}", area_triangulo);
    println!("CIRCULO: {:.3}", area_circulo);
    println!("TRAPEZIO: {:.3}", area_trapezio);
    println!("QUADRADO: {:.3}", area_quadrado);
    println!("RETANGULO: {:.3}", area_retangulo);
}