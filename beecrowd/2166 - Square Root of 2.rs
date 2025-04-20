use std::io;

fn main(){
    let mut n = String::new();

    //  Entrada
    io::stdin().read_line(&mut n).unwrap();
    
    let n: u8 = n.trim().parse().unwrap();
    
    let mut x = 0.0;
    

    //  Loop padrão
    for _ in 0..n{
        x = 1.0 /(2.0 + x);
    }
    
    x = 1.0 + x;
    println!("{:.10}",x); 
}

