#include <iostream>
using namespace std;

int main() {
    double num1, num2;

    // Solicitar al usuario que ingrese dos números
    cout << "Introduce el primer número: ";
    cin >> num1;
    cout << "Introduce el segundo número: ";
    cin >> num2;

    // Operaciones
    cout << "Suma: " << num1 + num2 << endl;
    cout << "Resta: " << num1 - num2 << endl;
    cout << "Multiplicación: " << num1 * num2 << endl;
     return 0;
}


#include <iostream>
using namespace std;

int main() {
    double precio, descuento, precioFinal;

    // Solicitar al usuario el precio del artículo
    cout << "Introduce el precio del artículo: ";
    cin >> precio;

    // Calcular el descuento (15%)
    descuento = precio * 0.15;

    // Calcular el precio final después de aplicar el descuento
    precioFinal = precio - descuento;

    // Mostrar el resultado
    cout << "El descuento aplicado es: " << descuento << endl;
    cout << "El precio final después del descuento es: " << precioFinal << endl;

    return 0;
}

