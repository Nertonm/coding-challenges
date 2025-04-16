use std::io::{self, BufRead};   // Importa o trait BufRead para usar o lines()

fn main() {
    let stdin = io::stdin();    // Obtem a entrada padrão

    for line in stdin.lock().lines() {  // Retorna uma linha por vez
        let input = line.unwrap();      // Atribui a linha a input
        if input.trim() == "0 0" {      // Caso de Saida
            break;
        }

        // Separa os digitos
        let mut parts = input.split_whitespace();   
        let x = parts.next().unwrap().chars().rev();            
        let y = parts.next().unwrap().chars().rev();    

        // Inicializa os contadores
        let mut count = 0;
        let mut carry = 0;

        // Converte para Numeros
        let mut digits_x = x.map(|c| c.to_digit(10).unwrap());
        let mut digits_y = y.map(|c| c.to_digit(10).unwrap());

        loop {
            // Pega o próximo digito de cada numero
            let num_x = digits_x.next();
            let num_y = digits_y.next();

            // Condição de Saida (Acabaram os numeros)
            if num_x.is_none() && num_y.is_none() && carry == 0 {
                break;
            }
            
            // Soma os numeros
            let sum = num_x.unwrap_or(0) + num_y.unwrap_or(0) + carry;

            // Verifica se tem um carry
            if sum >= 10 {
                carry = 1;
                count += 1;
            } else {
                carry = 0;
            }
        }

        // Exibe o resultado
        match count {
            0 => println!("No carry operation."),
            1 => println!("1 carry operation."),
            _ => println!("{} carry operations.", count),
        }
    }
}

