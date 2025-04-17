use std::io::{self, BufRead};

fn main(){
    let stdin = io::stdin();    // Lê a entrada
    
    for line in stdin.lock().lines(){   // Leitura de linha a linha
        let n: u32 = match line {
            Ok(l) => l.trim().parse().unwrap(),
            Err(_) => continue,
        };
        
        // Inicializa o contador
        let mut count = 1;
        let mut rest = 1 % n;
        
        // Loop até que o primeiro numero 11... divisivel por n apareça
        while rest != 0 {
            rest =  (rest * 10 + 1) % n;
            count += 1;
        }
        
        println!("{}", count);
    }
}

//OBS: NA LINHA 7 o U NÃO PODE SER 16 pois utrapassara 65 mil em alguns casos
