#include <iostream> //  Permite entrada e saida
#include <iomanip>  //  Permite manipular a entrada e saida

int main(){
    int  n;
    //  Entrada
    std::cin >> n;

    double x = 0.0;
    //  Loop padrão
    for (short i = 0; i < n; ++i)
        x = 1.0/(2.0 + x);

    x = 1.0 + x;
    //  Saida normal do C, fixed para usar um ponto fixo inves de notação cientifica,
    //  endl para forçar saida
    std::cout << std::fixed << std::setprecision(10) << x << std::endl;
    
    return 0;
}
